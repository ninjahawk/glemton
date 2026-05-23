# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 06:18:05 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1517M / 3000M (50.6%) |
| Step | 92610 |
| Latest loss | 1.9805 |
| Avg loss (last 30 logged) | 2.1074 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 8:58:49 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.04 -> 2.37 -> 2.28 -> 2.21 -> 1.69 -> 1.92 -> 2.29 -> 2.30 -> 1.95 -> 2.10 -> 2.14 -> 2.41

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=92500 tokens=1515.5M loss=1.8945 lr=1.65e-04 tok/s=12488
[train] step=92510 tokens=1515.7M loss=1.9584 lr=1.65e-04 tok/s=12488
[train] step=92520 tokens=1515.8M loss=2.0875 lr=1.65e-04 tok/s=12488
[train] step=92530 tokens=1516.0M loss=2.1191 lr=1.64e-04 tok/s=12488
[train] step=92540 tokens=1516.2M loss=2.1815 lr=1.64e-04 tok/s=12488
[train] step=92550 tokens=1516.3M loss=1.8084 lr=1.64e-04 tok/s=12488
[train] step=92560 tokens=1516.5M loss=2.1369 lr=1.64e-04 tok/s=12488
[train] step=92570 tokens=1516.7M loss=1.9855 lr=1.64e-04 tok/s=12488
[train] step=92580 tokens=1516.8M loss=1.7978 lr=1.64e-04 tok/s=12488
[train] step=92590 tokens=1517.0M loss=2.4077 lr=1.64e-04 tok/s=12488
[train] step=92600 tokens=1517.2M loss=2.3764 lr=1.64e-04 tok/s=12488
[train] step=92610 tokens=1517.3M loss=1.9805 lr=1.64e-04 tok/s=12488
```
