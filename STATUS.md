# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 10:18:41 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1698M / 3000M (56.6%) |
| Step | 103620 |
| Latest loss | 2.4112 |
| Avg loss (last 30 logged) | 2.0685 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 4:58:04 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.72 -> 2.35 -> 1.93 -> 2.18 -> 1.79 -> 2.07 -> 2.17 -> 1.87 -> 2.08 -> 2.51 -> 2.09 -> 1.94

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=103510 tokens=1695.9M loss=1.9378 lr=1.39e-04 tok/s=12488
[train] step=103520 tokens=1696.1M loss=2.3460 lr=1.39e-04 tok/s=12488
[train] step=103530 tokens=1696.2M loss=2.1330 lr=1.39e-04 tok/s=12488
[train] step=103540 tokens=1696.4M loss=2.0886 lr=1.39e-04 tok/s=12488
[train] step=103550 tokens=1696.6M loss=2.0950 lr=1.39e-04 tok/s=12488
[train] step=103560 tokens=1696.7M loss=2.5675 lr=1.39e-04 tok/s=12488
[train] step=103570 tokens=1696.9M loss=2.0038 lr=1.39e-04 tok/s=12488
[train] step=103580 tokens=1697.1M loss=1.9233 lr=1.39e-04 tok/s=12488
[train] step=103590 tokens=1697.2M loss=1.9393 lr=1.39e-04 tok/s=12488
[train] step=103600 tokens=1697.4M loss=2.0958 lr=1.39e-04 tok/s=12488
[train] step=103610 tokens=1697.5M loss=1.8270 lr=1.39e-04 tok/s=12488
[train] step=103620 tokens=1697.7M loss=2.4112 lr=1.39e-04 tok/s=12488
```
