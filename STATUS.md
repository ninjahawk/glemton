# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 02:53:44 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 285M / 3000M (9.5%) |
| Step | 17420 |
| Latest loss | 2.5827 |
| Avg loss (last 30 logged) | 2.5302 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 2 days, 12:22:39 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.42 -> 2.71 -> 2.58 -> 2.18 -> 2.48 -> 2.24 -> 2.64 -> 2.85 -> 2.47 -> 2.60 -> 2.32 -> 2.65

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=17310 tokens=283.6M loss=2.7011 lr=2.95e-04 tok/s=12490
[train] step=17320 tokens=283.8M loss=2.3622 lr=2.95e-04 tok/s=12490
[train] step=17330 tokens=283.9M loss=2.6652 lr=2.95e-04 tok/s=12490
[train] step=17340 tokens=284.1M loss=2.5052 lr=2.95e-04 tok/s=12490
[train] step=17350 tokens=284.3M loss=2.4561 lr=2.95e-04 tok/s=12490
[train] step=17360 tokens=284.4M loss=2.6117 lr=2.95e-04 tok/s=12490
[train] step=17370 tokens=284.6M loss=2.3467 lr=2.95e-04 tok/s=12490
[train] step=17380 tokens=284.8M loss=2.3351 lr=2.95e-04 tok/s=12490
[train] step=17390 tokens=284.9M loss=2.6510 lr=2.95e-04 tok/s=12489
[train] step=17400 tokens=285.1M loss=2.9612 lr=2.95e-04 tok/s=12489
[train] step=17410 tokens=285.2M loss=2.5961 lr=2.95e-04 tok/s=12489
[train] step=17420 tokens=285.4M loss=2.5827 lr=2.95e-04 tok/s=12489
```
