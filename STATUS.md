# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 08:58:29 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1638M / 3000M (54.6%) |
| Step | 99950 |
| Latest loss | 1.9596 |
| Avg loss (last 30 logged) | 2.1338 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 6:18:16 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.75 -> 2.58 -> 2.26 -> 1.91 -> 2.20 -> 1.88 -> 1.59 -> 1.73 -> 1.95 -> 2.60 -> 1.96 -> 2.38

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=99840 tokens=1635.8M loss=2.0753 lr=1.47e-04 tok/s=12488
[train] step=99850 tokens=1635.9M loss=2.3149 lr=1.47e-04 tok/s=12488
[train] step=99860 tokens=1636.1M loss=2.3550 lr=1.47e-04 tok/s=12488
[train] step=99870 tokens=1636.3M loss=2.2214 lr=1.47e-04 tok/s=12488
[train] step=99880 tokens=1636.4M loss=1.8925 lr=1.47e-04 tok/s=12488
[train] step=99890 tokens=1636.6M loss=1.9567 lr=1.47e-04 tok/s=12488
[train] step=99900 tokens=1636.8M loss=2.4549 lr=1.47e-04 tok/s=12488
[train] step=99910 tokens=1636.9M loss=2.1630 lr=1.47e-04 tok/s=12488
[train] step=99920 tokens=1637.1M loss=2.1165 lr=1.47e-04 tok/s=12488
[train] step=99930 tokens=1637.3M loss=2.3805 lr=1.47e-04 tok/s=12488
[train] step=99940 tokens=1637.4M loss=1.9572 lr=1.47e-04 tok/s=12488
[train] step=99950 tokens=1637.6M loss=1.9596 lr=1.47e-04 tok/s=12488
```
