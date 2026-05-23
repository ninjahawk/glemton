# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 04:37:49 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1442M / 3000M (48.1%) |
| Step | 88030 |
| Latest loss | 2.5918 |
| Avg loss (last 30 logged) | 2.1487 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 10:39:05 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.64 -> 2.51 -> 2.42 -> 1.90 -> 2.01 -> 1.87 -> 2.04 -> 2.11 -> 2.74 -> 2.24 -> 2.19 -> 1.94

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`

## Recent log tail
```
[train] step=87920 tokens=1440.5M loss=2.4515 lr=1.75e-04 tok/s=12487
[train] step=87930 tokens=1440.6M loss=2.1007 lr=1.75e-04 tok/s=12487
[train] step=87940 tokens=1440.8M loss=2.4569 lr=1.75e-04 tok/s=12487
[train] step=87950 tokens=1441.0M loss=2.1077 lr=1.75e-04 tok/s=12487
[train] step=87960 tokens=1441.1M loss=2.1694 lr=1.75e-04 tok/s=12487
[train] step=87970 tokens=1441.3M loss=2.5741 lr=1.75e-04 tok/s=12487
[train] step=87980 tokens=1441.5M loss=1.8414 lr=1.75e-04 tok/s=12487
[train] step=87990 tokens=1441.6M loss=2.1380 lr=1.75e-04 tok/s=12487
[train] step=88000 tokens=1441.8M loss=2.0997 lr=1.75e-04 tok/s=12487
[train] step=88010 tokens=1442.0M loss=1.9443 lr=1.75e-04 tok/s=12487
[train] step=88020 tokens=1442.1M loss=2.3054 lr=1.75e-04 tok/s=12487
[train] step=88030 tokens=1442.3M loss=2.5918 lr=1.75e-04 tok/s=12487
```
