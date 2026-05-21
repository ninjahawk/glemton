"""Sampling / inference for Glemton.

Standard temperature + top-k + top-p sampling. Loads a checkpoint, runs an
autoregressive decode against a prompt. Used by `scripts/chat.py` and by
the eval harness when it needs model outputs.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import torch
import torch.nn.functional as F
import yaml

from .model import Glemton, model_from_config
from .tokenizer import load as load_tokenizer


def load_checkpoint(ckpt_path: str, device: Optional[str] = None) -> tuple[Glemton, dict]:
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
    cfg = ckpt["cfg"]
    model = model_from_config(cfg).to(device)
    model.load_state_dict(ckpt["model"])
    model.eval()
    return model, cfg


@torch.no_grad()
def generate(
    model: Glemton,
    input_ids: torch.Tensor,
    max_new_tokens: int = 128,
    temperature: float = 0.8,
    top_k: int = 40,
    top_p: float = 0.95,
    eos_id: Optional[int] = None,
) -> torch.Tensor:
    """Greedy / sampled autoregressive decode. input_ids: (B, T) on model device."""
    device = next(model.parameters()).device
    input_ids = input_ids.to(device)
    out = input_ids.clone()
    for _ in range(max_new_tokens):
        # Crop context window if it would exceed the model's max_seq_len.
        ctx = out[:, -model.cfg.max_seq_len:]
        logits, _ = model(ctx)
        logits = logits[:, -1, :] / max(temperature, 1e-5)

        if top_k > 0:
            v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
            logits[logits < v[..., -1, None]] = -float("inf")
        if 0 < top_p < 1.0:
            sorted_logits, sorted_idx = torch.sort(logits, descending=True)
            probs = F.softmax(sorted_logits, dim=-1)
            cumprobs = probs.cumsum(dim=-1)
            keep = cumprobs - probs <= top_p
            keep[..., 0] = True  # always keep top-1
            mask = torch.zeros_like(logits, dtype=torch.bool)
            mask.scatter_(-1, sorted_idx, keep)
            logits[~mask] = -float("inf")

        probs = F.softmax(logits, dim=-1)
        next_tok = torch.multinomial(probs, num_samples=1)
        out = torch.cat([out, next_tok], dim=-1)
        if eos_id is not None and (next_tok == eos_id).all():
            break
    return out


def generate_text(
    model: Glemton,
    tokenizer,
    prompt: str,
    max_new_tokens: int = 128,
    temperature: float = 0.8,
    top_k: int = 40,
    top_p: float = 0.95,
) -> str:
    enc = tokenizer.encode(prompt)
    input_ids = torch.tensor(enc.ids, dtype=torch.long).unsqueeze(0)
    eos_id = tokenizer.token_to_id("<eos>")
    out = generate(
        model, input_ids,
        max_new_tokens=max_new_tokens,
        temperature=temperature, top_k=top_k, top_p=top_p,
        eos_id=eos_id,
    )
    new_ids = out[0, input_ids.size(1):].tolist()
    return tokenizer.decode(new_ids)


def main():
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--ckpt", required=True)
    p.add_argument("--tokenizer", default="data/tokenizer/glemton-bpe-32k.json")
    p.add_argument("--prompt", default="<user> Hello.\n<reply>")
    p.add_argument("--max-new-tokens", type=int, default=128)
    p.add_argument("--temperature", type=float, default=0.8)
    p.add_argument("--top-k", type=int, default=40)
    p.add_argument("--top-p", type=float, default=0.95)
    args = p.parse_args()

    model, cfg = load_checkpoint(args.ckpt)
    tok = load_tokenizer(args.tokenizer)
    text = generate_text(
        model, tok, args.prompt,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        top_k=args.top_k,
        top_p=args.top_p,
    )
    print(text)


if __name__ == "__main__":
    main()
