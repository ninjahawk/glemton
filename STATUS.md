# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 14:55:41 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 826M / 3000M (27.5%) |
| Step | 50420 |
| Latest loss | 2.4282 |
| Avg loss (last 30 logged) | 2.3398 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 0:22:14 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.44 -> 2.21 -> 2.16 -> 2.35 -> 2.26 -> 2.39 -> 2.18 -> 2.52 -> 2.37 -> 2.14 -> 2.31 -> 2.23

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`

## Recent log tail
```
[train] step=50310 tokens=824.3M loss=2.5577 lr=2.55e-04 tok/s=12484
[train] step=50320 tokens=824.4M loss=2.2406 lr=2.55e-04 tok/s=12484
[train] step=50330 tokens=824.6M loss=2.4068 lr=2.55e-04 tok/s=12484
[train] step=50340 tokens=824.8M loss=2.0331 lr=2.55e-04 tok/s=12484
[train] step=50350 tokens=824.9M loss=2.1173 lr=2.55e-04 tok/s=12484
[train] step=50360 tokens=825.1M loss=2.3482 lr=2.55e-04 tok/s=12484
[train] step=50370 tokens=825.3M loss=2.4227 lr=2.55e-04 tok/s=12484
[train] step=50380 tokens=825.4M loss=2.6857 lr=2.55e-04 tok/s=12484
[train] step=50390 tokens=825.6M loss=2.2079 lr=2.55e-04 tok/s=12484
[train] step=50400 tokens=825.8M loss=2.2310 lr=2.55e-04 tok/s=12484
[train] step=50410 tokens=825.9M loss=2.2467 lr=2.55e-04 tok/s=12484
[train] step=50420 tokens=826.1M loss=2.4282 lr=2.55e-04 tok/s=12484
```
