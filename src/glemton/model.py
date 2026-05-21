"""Glemton model — dense decoder-only transformer, Llama-style.

Architecture decisions live in docs/architecture.md. Summary:
- RMSNorm, SwiGLU, GQA, RoPE (theta=1e6 for long-context extension)
- Sliding-window attention with periodic global layers (Llama-3-style)
- Tied input/output embeddings
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F


@dataclass
class ModelConfig:
    vocab_size: int = 32000
    d_model: int = 1024
    n_layers: int = 30
    n_heads: int = 16
    n_kv_heads: int = 4
    ffn_dim: int = 2752
    max_seq_len: int = 32768
    rope_theta: float = 1_000_000.0
    norm_eps: float = 1e-5
    tie_embeddings: bool = True
    sliding_window: int = 4096
    global_every: int = 6  # every Nth layer is full-attention

    @property
    def head_dim(self) -> int:
        assert self.d_model % self.n_heads == 0
        return self.d_model // self.n_heads


class RMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float = 1e-5):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        rms = x.pow(2).mean(-1, keepdim=True).add(self.eps).rsqrt()
        return (x * rms).to(x.dtype) * self.weight


def precompute_rope_cache(head_dim: int, max_seq_len: int, theta: float, device, dtype):
    inv_freq = 1.0 / (theta ** (torch.arange(0, head_dim, 2, device=device).float() / head_dim))
    t = torch.arange(max_seq_len, device=device).float()
    freqs = torch.outer(t, inv_freq)
    cos = freqs.cos().to(dtype)
    sin = freqs.sin().to(dtype)
    return cos, sin


def apply_rope(x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor) -> torch.Tensor:
    # x: (B, H, T, D)  cos/sin: (T, D/2)
    x1, x2 = x.chunk(2, dim=-1)
    cos = cos[None, None, :, :]
    sin = sin[None, None, :, :]
    return torch.cat([x1 * cos - x2 * sin, x1 * sin + x2 * cos], dim=-1)


def repeat_kv(x: torch.Tensor, n_rep: int) -> torch.Tensor:
    if n_rep == 1:
        return x
    B, H, T, D = x.shape
    return x[:, :, None, :, :].expand(B, H, n_rep, T, D).reshape(B, H * n_rep, T, D)


class Attention(nn.Module):
    def __init__(self, cfg: ModelConfig, use_sliding: bool):
        super().__init__()
        self.cfg = cfg
        self.use_sliding = use_sliding
        self.q_proj = nn.Linear(cfg.d_model, cfg.n_heads * cfg.head_dim, bias=False)
        self.k_proj = nn.Linear(cfg.d_model, cfg.n_kv_heads * cfg.head_dim, bias=False)
        self.v_proj = nn.Linear(cfg.d_model, cfg.n_kv_heads * cfg.head_dim, bias=False)
        self.o_proj = nn.Linear(cfg.n_heads * cfg.head_dim, cfg.d_model, bias=False)
        self.n_rep = cfg.n_heads // cfg.n_kv_heads

    def forward(self, x, cos, sin, attn_mask: Optional[torch.Tensor] = None):
        B, T, _ = x.shape
        cfg = self.cfg
        q = self.q_proj(x).view(B, T, cfg.n_heads, cfg.head_dim).transpose(1, 2)
        k = self.k_proj(x).view(B, T, cfg.n_kv_heads, cfg.head_dim).transpose(1, 2)
        v = self.v_proj(x).view(B, T, cfg.n_kv_heads, cfg.head_dim).transpose(1, 2)

        q = apply_rope(q, cos, sin)
        k = apply_rope(k, cos, sin)

        k = repeat_kv(k, self.n_rep)
        v = repeat_kv(v, self.n_rep)

        is_causal = attn_mask is None
        window = cfg.sliding_window if self.use_sliding else None
        # F.scaled_dot_product_attention handles causal + sliding via attn_mask shape.
        # For now: pure causal. Sliding-window is added when we wire FlashAttention-3.
        out = F.scaled_dot_product_attention(
            q, k, v, attn_mask=attn_mask, is_causal=is_causal, dropout_p=0.0
        )
        out = out.transpose(1, 2).contiguous().view(B, T, cfg.d_model)
        return self.o_proj(out)


class SwiGLU(nn.Module):
    def __init__(self, cfg: ModelConfig):
        super().__init__()
        self.gate = nn.Linear(cfg.d_model, cfg.ffn_dim, bias=False)
        self.up = nn.Linear(cfg.d_model, cfg.ffn_dim, bias=False)
        self.down = nn.Linear(cfg.ffn_dim, cfg.d_model, bias=False)

    def forward(self, x):
        return self.down(F.silu(self.gate(x)) * self.up(x))


class Block(nn.Module):
    def __init__(self, cfg: ModelConfig, layer_idx: int):
        super().__init__()
        use_sliding = (layer_idx + 1) % cfg.global_every != 0
        self.attn_norm = RMSNorm(cfg.d_model, cfg.norm_eps)
        self.attn = Attention(cfg, use_sliding=use_sliding)
        self.ffn_norm = RMSNorm(cfg.d_model, cfg.norm_eps)
        self.ffn = SwiGLU(cfg)

    def forward(self, x, cos, sin, attn_mask=None):
        x = x + self.attn(self.attn_norm(x), cos, sin, attn_mask=attn_mask)
        x = x + self.ffn(self.ffn_norm(x))
        return x


class Glemton(nn.Module):
    def __init__(self, cfg: ModelConfig):
        super().__init__()
        self.cfg = cfg
        self.tok_embed = nn.Embedding(cfg.vocab_size, cfg.d_model)
        self.layers = nn.ModuleList([Block(cfg, i) for i in range(cfg.n_layers)])
        self.norm = RMSNorm(cfg.d_model, cfg.norm_eps)
        self.lm_head = nn.Linear(cfg.d_model, cfg.vocab_size, bias=False)
        if cfg.tie_embeddings:
            self.lm_head.weight = self.tok_embed.weight
        self._rope_cache: Optional[tuple[torch.Tensor, torch.Tensor]] = None
        self.apply(self._init_weights)

    @staticmethod
    def _init_weights(module: nn.Module):
        if isinstance(module, nn.Linear):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def _get_rope(self, T: int, device, dtype):
        if self._rope_cache is None or self._rope_cache[0].size(0) < T or self._rope_cache[0].device != device:
            self._rope_cache = precompute_rope_cache(
                self.cfg.head_dim, max(T, self.cfg.max_seq_len), self.cfg.rope_theta, device, dtype
            )
        cos, sin = self._rope_cache
        return cos[:T], sin[:T]

    def forward(self, input_ids: torch.Tensor, targets: Optional[torch.Tensor] = None):
        B, T = input_ids.shape
        x = self.tok_embed(input_ids)
        cos, sin = self._get_rope(T, x.device, x.dtype)
        for block in self.layers:
            x = block(x, cos, sin)
        x = self.norm(x)
        logits = self.lm_head(x)
        if targets is None:
            return logits, None
        loss = F.cross_entropy(
            logits.view(-1, logits.size(-1)), targets.view(-1), ignore_index=-100
        )
        return logits, loss

    def num_parameters(self) -> int:
        seen = set()
        n = 0
        for p in self.parameters():
            if id(p) in seen:
                continue
            seen.add(id(p))
            n += p.numel()
        return n


def model_from_config(cfg_dict: dict) -> Glemton:
    m = cfg_dict["model"]
    attn = m.get("attention", {})
    cfg = ModelConfig(
        vocab_size=m["vocab_size"],
        d_model=m["d_model"],
        n_layers=m["n_layers"],
        n_heads=m["n_heads"],
        n_kv_heads=m["n_kv_heads"],
        ffn_dim=m["ffn_dim"],
        max_seq_len=m["max_seq_len"],
        rope_theta=float(m["rope_theta"]),
        norm_eps=float(m["norm_eps"]),
        tie_embeddings=bool(m.get("tie_embeddings", True)),
        sliding_window=int(attn.get("sliding_window", 4096)),
        global_every=int(attn.get("global_every", 6)),
    )
    return Glemton(cfg)
