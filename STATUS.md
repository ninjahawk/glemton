# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 15:45:50 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 864M / 3000M (28.8%) |
| Step | 52710 |
| Latest loss | 2.2751 |
| Avg loss (last 30 logged) | 2.3194 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1 day, 23:32:11 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.10 -> 1.96 -> 2.28 -> 2.60 -> 2.69 -> 2.15 -> 2.55 -> 2.37 -> 2.30 -> 2.22 -> 2.82 -> 2.44

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`

## Recent log tail
```
[train] step=52600 tokens=861.8M loss=2.4499 lr=2.51e-04 tok/s=12484
[train] step=52610 tokens=862.0M loss=2.3656 lr=2.51e-04 tok/s=12484
[train] step=52620 tokens=862.1M loss=2.4148 lr=2.51e-04 tok/s=12484
[train] step=52630 tokens=862.3M loss=2.0726 lr=2.51e-04 tok/s=12484
[train] step=52640 tokens=862.5M loss=2.2336 lr=2.51e-04 tok/s=12484
[train] step=52650 tokens=862.6M loss=2.0163 lr=2.51e-04 tok/s=12484
[train] step=52660 tokens=862.8M loss=2.2043 lr=2.51e-04 tok/s=12484
[train] step=52670 tokens=862.9M loss=2.1778 lr=2.51e-04 tok/s=12484
[train] step=52680 tokens=863.1M loss=2.0574 lr=2.50e-04 tok/s=12484
[train] step=52690 tokens=863.3M loss=2.4376 lr=2.50e-04 tok/s=12484
[train] step=52700 tokens=863.4M loss=2.3337 lr=2.50e-04 tok/s=12484
[train] step=52710 tokens=863.6M loss=2.2751 lr=2.50e-04 tok/s=12484
```
