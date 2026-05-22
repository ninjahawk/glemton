# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 13:55:35 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 781M / 3000M (26.0%) |
| Step | 47670 |
| Latest loss | 2.2068 |
| Avg loss (last 30 logged) | 2.3173 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 1:22:41 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.34 -> 2.23 -> 2.14 -> 2.20 -> 2.00 -> 2.59 -> 2.57 -> 2.14 -> 2.40 -> 1.91 -> 2.40 -> 2.75

## Checkpoints on disk
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`

## Recent log tail
```
[train] step=47560 tokens=779.2M loss=2.2360 lr=2.59e-04 tok/s=12483
[train] step=47570 tokens=779.4M loss=2.0615 lr=2.59e-04 tok/s=12483
[train] step=47580 tokens=779.6M loss=2.2771 lr=2.59e-04 tok/s=12483
[train] step=47590 tokens=779.7M loss=2.2709 lr=2.59e-04 tok/s=12483
[train] step=47600 tokens=779.9M loss=2.4769 lr=2.59e-04 tok/s=12483
[train] step=47610 tokens=780.0M loss=2.2840 lr=2.59e-04 tok/s=12483
[train] step=47620 tokens=780.2M loss=2.3382 lr=2.59e-04 tok/s=12483
[train] step=47630 tokens=780.4M loss=2.5832 lr=2.59e-04 tok/s=12483
[train] step=47640 tokens=780.5M loss=2.7486 lr=2.59e-04 tok/s=12483
[train] step=47650 tokens=780.7M loss=2.0578 lr=2.59e-04 tok/s=12483
[train] step=47660 tokens=780.9M loss=2.3720 lr=2.59e-04 tok/s=12483
[train] step=47670 tokens=781.0M loss=2.2068 lr=2.59e-04 tok/s=12483
```
