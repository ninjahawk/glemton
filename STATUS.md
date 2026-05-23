# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 05:17:55 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1472M / 3000M (49.1%) |
| Step | 89860 |
| Latest loss | 2.3372 |
| Avg loss (last 30 logged) | 2.2446 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 9:58:53 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.20 -> 2.08 -> 2.01 -> 1.92 -> 2.10 -> 2.05 -> 2.11 -> 2.51 -> 2.44 -> 1.94 -> 2.57 -> 2.42

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`

## Recent log tail
```
[train] step=89750 tokens=1470.5M loss=2.2575 lr=1.71e-04 tok/s=12487
[train] step=89760 tokens=1470.6M loss=1.9668 lr=1.71e-04 tok/s=12487
[train] step=89770 tokens=1470.8M loss=1.8211 lr=1.71e-04 tok/s=12487
[train] step=89780 tokens=1471.0M loss=2.1231 lr=1.71e-04 tok/s=12488
[train] step=89790 tokens=1471.1M loss=2.0629 lr=1.71e-04 tok/s=12488
[train] step=89800 tokens=1471.3M loss=2.0138 lr=1.71e-04 tok/s=12488
[train] step=89810 tokens=1471.4M loss=2.2663 lr=1.71e-04 tok/s=12488
[train] step=89820 tokens=1471.6M loss=1.7651 lr=1.71e-04 tok/s=12488
[train] step=89830 tokens=1471.8M loss=2.4177 lr=1.71e-04 tok/s=12488
[train] step=89840 tokens=1471.9M loss=2.6240 lr=1.71e-04 tok/s=12488
[train] step=89850 tokens=1472.1M loss=2.4626 lr=1.71e-04 tok/s=12488
[train] step=89860 tokens=1472.3M loss=2.3372 lr=1.71e-04 tok/s=12488
```
