# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 06:28:06 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1525M / 3000M (50.8%) |
| Step | 93070 |
| Latest loss | 2.1151 |
| Avg loss (last 30 logged) | 2.1203 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 8:48:41 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.69 -> 2.26 -> 2.13 -> 2.24 -> 2.28 -> 2.64 -> 2.09 -> 2.32 -> 1.86 -> 2.38 -> 1.90 -> 2.03

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=92960 tokens=1523.1M loss=2.3511 lr=1.63e-04 tok/s=12488
[train] step=92970 tokens=1523.2M loss=2.0637 lr=1.63e-04 tok/s=12488
[train] step=92980 tokens=1523.4M loss=1.9917 lr=1.63e-04 tok/s=12488
[train] step=92990 tokens=1523.5M loss=1.8568 lr=1.63e-04 tok/s=12488
[train] step=93000 tokens=1523.7M loss=1.8097 lr=1.63e-04 tok/s=12488
[train] step=93010 tokens=1523.9M loss=2.2006 lr=1.63e-04 tok/s=12488
[train] step=93020 tokens=1524.0M loss=1.8837 lr=1.63e-04 tok/s=12488
[train] step=93030 tokens=1524.2M loss=2.3383 lr=1.63e-04 tok/s=12488
[train] step=93040 tokens=1524.4M loss=2.3722 lr=1.63e-04 tok/s=12488
[train] step=93050 tokens=1524.5M loss=2.0266 lr=1.63e-04 tok/s=12488
[train] step=93060 tokens=1524.7M loss=2.4601 lr=1.63e-04 tok/s=12488
[train] step=93070 tokens=1524.9M loss=2.1151 lr=1.63e-04 tok/s=12488
```
