# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 15:55:52 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 871M / 3000M (29.0%) |
| Step | 53170 |
| Latest loss | 2.5630 |
| Avg loss (last 30 logged) | 2.3500 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1 day, 23:22:10 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.34 -> 2.32 -> 2.14 -> 2.08 -> 2.36 -> 2.15 -> 2.81 -> 2.54 -> 2.15 -> 2.27 -> 2.15 -> 2.06

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`

## Recent log tail
```
[train] step=53060 tokens=869.3M loss=2.9511 lr=2.50e-04 tok/s=12484
[train] step=53070 tokens=869.5M loss=2.5907 lr=2.50e-04 tok/s=12484
[train] step=53080 tokens=869.7M loss=2.1454 lr=2.50e-04 tok/s=12484
[train] step=53090 tokens=869.8M loss=2.0829 lr=2.50e-04 tok/s=12484
[train] step=53100 tokens=870.0M loss=2.1094 lr=2.50e-04 tok/s=12484
[train] step=53110 tokens=870.2M loss=2.3071 lr=2.50e-04 tok/s=12484
[train] step=53120 tokens=870.3M loss=2.1656 lr=2.50e-04 tok/s=12484
[train] step=53130 tokens=870.5M loss=2.6031 lr=2.50e-04 tok/s=12484
[train] step=53140 tokens=870.6M loss=2.0648 lr=2.50e-04 tok/s=12484
[train] step=53150 tokens=870.8M loss=2.1218 lr=2.50e-04 tok/s=12484
[train] step=53160 tokens=871.0M loss=2.3596 lr=2.50e-04 tok/s=12484
[train] step=53170 tokens=871.1M loss=2.5630 lr=2.50e-04 tok/s=12484
```
