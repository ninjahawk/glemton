# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-21 23:13:07 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 120M / 3000M (4.0%) |
| Step | 7330 |
| Latest loss | 2.4929 |
| Avg loss (last 30 logged) | 2.6931 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 2 days, 16:03:51 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.55 -> 3.23 -> 2.68 -> 2.86 -> 2.56 -> 2.63 -> 2.90 -> 2.54 -> 2.90 -> 2.65 -> 2.69 -> 2.69

## Checkpoints on disk
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=7220 tokens=118.3M loss=2.9548 lr=2.99e-04 tok/s=12487
[train] step=7230 tokens=118.5M loss=2.5712 lr=2.99e-04 tok/s=12487
[train] step=7240 tokens=118.6M loss=2.5405 lr=2.99e-04 tok/s=12487
[train] step=7250 tokens=118.8M loss=2.7616 lr=2.99e-04 tok/s=12487
[train] step=7260 tokens=118.9M loss=2.9398 lr=2.99e-04 tok/s=12487
[train] step=7270 tokens=119.1M loss=2.3220 lr=2.99e-04 tok/s=12487
[train] step=7280 tokens=119.3M loss=2.8813 lr=2.99e-04 tok/s=12487
[train] step=7290 tokens=119.4M loss=2.7246 lr=2.99e-04 tok/s=12487
[train] step=7300 tokens=119.6M loss=2.4112 lr=2.99e-04 tok/s=12487
[train] step=7310 tokens=119.8M loss=2.6924 lr=2.99e-04 tok/s=12487
[train] step=7320 tokens=119.9M loss=2.5161 lr=2.99e-04 tok/s=12487
[train] step=7330 tokens=120.1M loss=2.4929 lr=2.99e-04 tok/s=12487
```
