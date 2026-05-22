# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 15:25:47 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 849M / 3000M (28.3%) |
| Step | 51800 |
| Latest loss | 2.3124 |
| Avg loss (last 30 logged) | 2.3201 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1 day, 23:52:04 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.55 -> 2.24 -> 2.23 -> 2.08 -> 2.08 -> 2.60 -> 2.46 -> 2.15 -> 2.52 -> 2.39 -> 2.22 -> 2.39

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`

## Recent log tail
```
[train] step=51690 tokens=846.9M loss=2.1837 lr=2.52e-04 tok/s=12484
[train] step=51700 tokens=847.1M loss=2.2995 lr=2.52e-04 tok/s=12484
[train] step=51710 tokens=847.2M loss=2.2441 lr=2.52e-04 tok/s=12484
[train] step=51720 tokens=847.4M loss=2.5488 lr=2.52e-04 tok/s=12484
[train] step=51730 tokens=847.5M loss=1.9454 lr=2.52e-04 tok/s=12484
[train] step=51740 tokens=847.7M loss=2.1899 lr=2.52e-04 tok/s=12484
[train] step=51750 tokens=847.9M loss=2.7005 lr=2.52e-04 tok/s=12484
[train] step=51760 tokens=848.0M loss=2.5902 lr=2.52e-04 tok/s=12484
[train] step=51770 tokens=848.2M loss=2.1880 lr=2.52e-04 tok/s=12484
[train] step=51780 tokens=848.4M loss=2.3942 lr=2.52e-04 tok/s=12484
[train] step=51790 tokens=848.5M loss=2.2705 lr=2.52e-04 tok/s=12484
[train] step=51800 tokens=848.7M loss=2.3124 lr=2.52e-04 tok/s=12484
```
