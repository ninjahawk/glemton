# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 06:48:09 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1540M / 3000M (51.3%) |
| Step | 93990 |
| Latest loss | 2.1482 |
| Avg loss (last 30 logged) | 2.1301 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 8:28:40 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.28 -> 2.14 -> 2.05 -> 1.72 -> 2.00 -> 2.25 -> 1.57 -> 1.48 -> 1.99 -> 1.72 -> 1.98 -> 2.14

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=93880 tokens=1538.1M loss=2.2476 lr=1.61e-04 tok/s=12488
[train] step=93890 tokens=1538.3M loss=2.1631 lr=1.61e-04 tok/s=12488
[train] step=93900 tokens=1538.5M loss=2.2064 lr=1.61e-04 tok/s=12488
[train] step=93910 tokens=1538.6M loss=1.7676 lr=1.61e-04 tok/s=12488
[train] step=93920 tokens=1538.8M loss=1.9966 lr=1.61e-04 tok/s=12488
[train] step=93930 tokens=1538.9M loss=2.1725 lr=1.61e-04 tok/s=12488
[train] step=93940 tokens=1539.1M loss=1.8775 lr=1.61e-04 tok/s=12488
[train] step=93950 tokens=1539.3M loss=1.8431 lr=1.61e-04 tok/s=12488
[train] step=93960 tokens=1539.4M loss=2.0532 lr=1.61e-04 tok/s=12488
[train] step=93970 tokens=1539.6M loss=2.1443 lr=1.61e-04 tok/s=12488
[train] step=93980 tokens=1539.8M loss=1.7324 lr=1.61e-04 tok/s=12488
[train] step=93990 tokens=1539.9M loss=2.1482 lr=1.61e-04 tok/s=12488
```
