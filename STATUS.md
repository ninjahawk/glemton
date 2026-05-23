# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 07:48:18 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1585M / 3000M (52.8%) |
| Step | 96740 |
| Latest loss | 1.9787 |
| Avg loss (last 30 logged) | 2.1099 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 7:28:28 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.94 -> 2.16 -> 2.03 -> 1.71 -> 2.03 -> 1.92 -> 2.59 -> 1.69 -> 2.30 -> 1.75 -> 2.44 -> 1.93

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=96630 tokens=1583.2M loss=2.5750 lr=1.55e-04 tok/s=12488
[train] step=96640 tokens=1583.3M loss=2.0085 lr=1.55e-04 tok/s=12488
[train] step=96650 tokens=1583.5M loss=1.7892 lr=1.55e-04 tok/s=12488
[train] step=96660 tokens=1583.7M loss=1.9323 lr=1.55e-04 tok/s=12488
[train] step=96670 tokens=1583.8M loss=2.3675 lr=1.55e-04 tok/s=12488
[train] step=96680 tokens=1584.0M loss=2.2456 lr=1.55e-04 tok/s=12488
[train] step=96690 tokens=1584.2M loss=1.9935 lr=1.55e-04 tok/s=12488
[train] step=96700 tokens=1584.3M loss=2.0843 lr=1.55e-04 tok/s=12488
[train] step=96710 tokens=1584.5M loss=1.9308 lr=1.55e-04 tok/s=12488
[train] step=96720 tokens=1584.7M loss=2.3672 lr=1.55e-04 tok/s=12488
[train] step=96730 tokens=1584.8M loss=1.9419 lr=1.55e-04 tok/s=12488
[train] step=96740 tokens=1585.0M loss=1.9787 lr=1.55e-04 tok/s=12488
```
