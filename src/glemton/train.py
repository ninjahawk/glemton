"""Training loop for Glemton.

Single-GPU. bf16 mixed precision. 8-bit Adam via bitsandbytes when available
(falls back to plain torch.optim.AdamW on Windows where bnb is finicky).
Gradient accumulation for batch-size scaling on a 12 GB card.
"""

from __future__ import annotations

import math
import os
import time
from contextlib import nullcontext
from pathlib import Path

import torch
import yaml

from .data import make_dataloader
from .model import Glemton, model_from_config


def _build_optimizer(model: torch.nn.Module, lr: float, weight_decay: float, beta1: float, beta2: float, prefer_8bit: bool):
    decay_params, no_decay_params = [], []
    for name, p in model.named_parameters():
        if not p.requires_grad:
            continue
        if p.dim() < 2 or name.endswith(".weight") and ("norm" in name.lower() or "embed" in name.lower()):
            no_decay_params.append(p)
        else:
            decay_params.append(p)
    groups = [
        {"params": decay_params, "weight_decay": weight_decay},
        {"params": no_decay_params, "weight_decay": 0.0},
    ]
    if prefer_8bit:
        try:
            import bitsandbytes as bnb
            return bnb.optim.AdamW8bit(groups, lr=lr, betas=(beta1, beta2))
        except Exception as e:
            print(f"[train] 8-bit Adam unavailable ({e}); falling back to AdamW")
    return torch.optim.AdamW(groups, lr=lr, betas=(beta1, beta2))


def _lr_schedule(step_tokens: int, warmup_tokens: int, total_tokens: int, lr: float, lr_min: float) -> float:
    if step_tokens < warmup_tokens:
        return lr * step_tokens / max(1, warmup_tokens)
    decay = (step_tokens - warmup_tokens) / max(1, total_tokens - warmup_tokens)
    decay = min(1.0, decay)
    coef = 0.5 * (1.0 + math.cos(math.pi * decay))
    return lr_min + (lr - lr_min) * coef


def train(config_path: str, resume_from: str | None = None):
    with open(config_path) as f:
        cfg = yaml.safe_load(f)
    tr = cfg["train"]
    name = cfg.get("name", "glemton")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dtype = torch.bfloat16 if tr.get("precision", "bf16") == "bf16" else torch.float32

    # Cast weights to the training dtype. With fp32 weights on 12 GB the 350M
    # model OOMs at the backward pass because gradients + optimizer state +
    # autocast activations exceed VRAM. bf16 weights halve that footprint.
    model = model_from_config(cfg).to(device=device, dtype=dtype)
    if tr.get("grad_checkpointing", False):
        # Custom checkpointing wired in model.py once we have a full forward to wrap.
        pass

    # Continual pretraining: load weights from a previous checkpoint and pick
    # up training from there. We restore model state always; optimizer state
    # restoration is best-effort (skipped if absent or shape-mismatched).
    resumed_tokens = 0
    resumed_step = 0
    resumed_ckpt = None
    if resume_from:
        print(f"[train] resuming from {resume_from}")
        resumed_ckpt = torch.load(resume_from, map_location=device, weights_only=False)
        model.load_state_dict(resumed_ckpt["model"])
        resumed_tokens = int(resumed_ckpt.get("tokens", 0))
        resumed_step = int(resumed_ckpt.get("step", 0))
        print(f"[train] resumed at step={resumed_step} tokens={resumed_tokens/1e6:.1f}M")

    n_params = model.num_parameters()
    print(f"[train] {name}: {n_params/1e6:.1f}M params on {device}")

    optimizer = _build_optimizer(
        model,
        lr=tr["lr"],
        weight_decay=tr["weight_decay"],
        beta1=tr["beta1"],
        beta2=tr["beta2"],
        prefer_8bit=(tr.get("optimizer", "adamw") == "adamw_8bit"),
    )

    if resumed_ckpt is not None and "optimizer" in resumed_ckpt:
        try:
            optimizer.load_state_dict(resumed_ckpt["optimizer"])
            print("[train] resumed optimizer state")
        except Exception as e:
            print(f"[train] optimizer state restore failed ({e}); starting optimizer fresh")

    loader = make_dataloader(
        cfg["data"]["shard_dir"],
        seq_len=tr["seq_len"],
        batch_size=tr["micro_batch_size"],
        num_workers=2,
        source_weights=cfg["data"].get("source_weights"),
    )

    micro_batches_per_step = tr["grad_accum_steps"]
    total_tokens = int(tr["total_tokens"])
    tokens_per_step = tr["seq_len"] * tr["micro_batch_size"] * micro_batches_per_step
    warmup_tokens = int(tr["warmup_tokens"])

    ckpt_dir = Path("checkpoints") / name
    ckpt_dir.mkdir(parents=True, exist_ok=True)
    ckpt_every_tokens = int(tr["checkpoint_every_tokens"])

    autocast_ctx = (
        torch.amp.autocast(device_type="cuda", dtype=dtype)
        if device.type == "cuda"
        else nullcontext()
    )

    tokens_seen = resumed_tokens
    step = resumed_step
    next_ckpt = ((tokens_seen // ckpt_every_tokens) + 1) * ckpt_every_tokens
    t0 = time.time()

    loader_iter = iter(loader)
    while tokens_seen < total_tokens:
        optimizer.zero_grad(set_to_none=True)
        accum_loss = 0.0
        for _ in range(micro_batches_per_step):
            x, y = next(loader_iter)
            x = x.to(device, non_blocking=True)
            y = y.to(device, non_blocking=True)
            with autocast_ctx:
                _, loss = model(x, targets=y)
                loss = loss / micro_batches_per_step
            loss.backward()
            accum_loss += loss.item()
            tokens_seen += x.numel()

        if tr.get("grad_clip", 0.0) > 0:
            torch.nn.utils.clip_grad_norm_(model.parameters(), tr["grad_clip"])

        lr_now = _lr_schedule(tokens_seen, warmup_tokens, total_tokens, tr["lr"], tr["lr_min"])
        for pg in optimizer.param_groups:
            pg["lr"] = lr_now

        optimizer.step()
        step += 1

        if step % 10 == 0:
            elapsed = time.time() - t0
            tok_per_s = tokens_seen / max(1, elapsed)
            print(
                f"[train] step={step} tokens={tokens_seen/1e6:.1f}M "
                f"loss={accum_loss:.4f} lr={lr_now:.2e} tok/s={tok_per_s:.0f}",
                flush=True,
            )

        if tokens_seen >= next_ckpt:
            path = ckpt_dir / f"step_{step}_tokens_{tokens_seen//1_000_000}M.pt"
            torch.save(
                {
                    "model": model.state_dict(),
                    "optimizer": optimizer.state_dict(),
                    "step": step,
                    "tokens": tokens_seen,
                    "cfg": cfg,
                },
                path,
            )
            print(f"[train] checkpoint -> {path}")
            next_ckpt += ckpt_every_tokens

    path = ckpt_dir / "final.pt"
    torch.save(
        {
            "model": model.state_dict(),
            "optimizer": optimizer.state_dict(),
            "step": step,
            "tokens": tokens_seen,
            "cfg": cfg,
        },
        path,
    )
    print(f"[train] final checkpoint -> {path}")


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("config")
    p.add_argument("--resume", default=None, help="path to a checkpoint to resume from")
    args = p.parse_args()
    train(args.config, resume_from=args.resume)
