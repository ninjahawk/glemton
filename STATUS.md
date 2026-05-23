# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 02:57:34 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1367M / 3000M (45.6%) |
| Step | 83440 |
| Latest loss | 2.1398 |
| Avg loss (last 30 logged) | 2.1723 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 12:19:27 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.82 -> 2.16 -> 2.17 -> 2.42 -> 2.38 -> 2.39 -> 2.54 -> 1.87 -> 2.18 -> 2.06 -> 2.34 -> 2.10

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`

## Recent log tail
```
[train] step=83330 tokens=1365.3M loss=2.4170 lr=1.86e-04 tok/s=12487
[train] step=83340 tokens=1365.4M loss=1.7681 lr=1.86e-04 tok/s=12487
[train] step=83350 tokens=1365.6M loss=2.2756 lr=1.86e-04 tok/s=12487
[train] step=83360 tokens=1365.8M loss=2.0507 lr=1.86e-04 tok/s=12487
[train] step=83370 tokens=1365.9M loss=2.1873 lr=1.86e-04 tok/s=12487
[train] step=83380 tokens=1366.1M loss=2.0230 lr=1.86e-04 tok/s=12487
[train] step=83390 tokens=1366.3M loss=2.3292 lr=1.86e-04 tok/s=12487
[train] step=83400 tokens=1366.4M loss=1.8784 lr=1.86e-04 tok/s=12487
[train] step=83410 tokens=1366.6M loss=2.1030 lr=1.86e-04 tok/s=12487
[train] step=83420 tokens=1366.8M loss=2.1767 lr=1.86e-04 tok/s=12487
[train] step=83430 tokens=1366.9M loss=2.6936 lr=1.86e-04 tok/s=12487
[train] step=83440 tokens=1367.1M loss=2.1398 lr=1.86e-04 tok/s=12487
```
