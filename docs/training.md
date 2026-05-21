# Training recipe

## What's wired

`src/glemton/train.py` is a single-GPU AdamW loop with:
- bf16 mixed precision via `torch.amp.autocast`
- 8-bit Adam via `bitsandbytes` when available, plain `AdamW` fallback (Windows + bitsandbytes is historically finicky)
- Gradient accumulation
- Cosine LR schedule with linear warmup measured in **tokens seen**, not steps
- Grad-norm clipping at 1.0
- Decoupled weight decay (no decay on norms or embeddings)
- Token-budget-based checkpoints (every 250 M tokens for the full run)

## Hyperparameters — v1.0 full pretrain (`configs/glemton-350m.yaml`)

| | |
|---|---|
| Total tokens | 7 B |
| Peak LR | 3 × 10⁻⁴ |
| Min LR | 3 × 10⁻⁵ (10% of peak) |
| Warmup | 100 M tokens (~1.4% of total) |
| Sequence length | 2048 (pretrain), RoPE θ=1e6 lets us extend to 32 k for eval |
| Micro batch | 1 |
| Grad accum | 8 |
| Effective batch | 8 sequences × 2048 = 16 384 tokens / step |
| Steps total | ~ 427 000 |
| Optimizer | AdamW 8-bit (bnb), fallback AdamW |
| β1, β2 | 0.9, 0.95 |
| Weight decay | 0.1 |
| Grad clip | 1.0 |

## Hyperparameters — debug (`configs/debug-10m.yaml`)

12 M params, 50 M tokens, sequence length 1024, batch 16, no 8-bit Adam. Should converge to a sane loss curve in <30 min on the 5070 if the toolchain is healthy. This is the **gate** before launching the full run.

## Schedule rationale

- **Cosine to 10% of peak.** Standard small-LM setup. Chinchilla used 0.1 to ~0.0; we keep some floor to leave room for late-training improvement.
- **Warmup in tokens not steps.** Survives batch-size and grad-accum changes without re-tuning.
- **β₂ = 0.95.** Less smoothing than the 0.999 default — better fit for short pretrains that don't accumulate huge optimizer state.
- **Grad checkpointing** wired in config but not yet plumbed into model.py forward — re-enable once we confirm memory headroom on the 5070 at 350 M with sequence-length 2048.

## Throughput expectations

TinyLlama (1.1 B) trained on 16× A100-40 G for 90 days at ~ 1 T tokens. RTX 5070 is roughly 0.3–0.4× A100 throughput for this workload at our size. Linear scaling estimate for Glemton (350 M, 7 B tokens):

```
TinyLlama: 1.1B × 1T = 1.1e18 param-token-ops on 16 A100 → reference
Glemton:    0.35B × 7e9 = 2.45e18 / scale  ≈ 0.22× of TinyLlama param-tokens
On 1 5070 ≈ 0.02× of 16 A100s → wall-time fraction ≈ 0.22 / 0.02 ≈ 11×
TinyLlama took 90 days → naive Glemton estimate: ~ 90/16 × 0.22 ≈ 1.2 days
```

That's a hand-wavy back-of-envelope and ignores fixed overhead, sliding-window vs full-attention scaling, and any toolchain inefficiencies. **The honest range is 1–4 weeks of GPU burn** on a single 5070 for the full 7 B pretrain. The 10 M debug run is hours, not days.

## What to measure during pretrain

- **Loss curve** — should drop fast in the first 100 M tokens, then flatten to a slow decline.
- **Throughput (tok/s)** — log every 10 steps. A drop usually means a memory thrash or a data-loader stall.
- **Grad norm** — pre-clip values. A spike is a divergence warning; a creeping rise can mean LR is too high.
- **Validation loss on a held-out shard** — every 250 M tokens, same time as checkpoint.

## What to NOT measure

Standard LM benchmarks (MMLU, HellaSwag, ARC) — Glemton is small and dialogue-trained; it will under-perform 7 B web-text models on these. That's expected and not the headline. The headline metrics live in `docs/evals.md`.
