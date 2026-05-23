# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 08:28:24 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1615M / 3000M (53.8%) |
| Step | 98580 |
| Latest loss | 2.0784 |
| Avg loss (last 30 logged) | 2.1227 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 6:48:18 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.10 -> 2.79 -> 2.26 -> 2.15 -> 2.03 -> 1.85 -> 2.26 -> 2.01 -> 1.86 -> 1.97 -> 2.20 -> 2.34

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=98470 tokens=1613.3M loss=1.8249 lr=1.51e-04 tok/s=12488
[train] step=98480 tokens=1613.5M loss=1.6270 lr=1.51e-04 tok/s=12488
[train] step=98490 tokens=1613.7M loss=2.7062 lr=1.51e-04 tok/s=12488
[train] step=98500 tokens=1613.8M loss=2.0341 lr=1.51e-04 tok/s=12488
[train] step=98510 tokens=1614.0M loss=2.2298 lr=1.51e-04 tok/s=12488
[train] step=98520 tokens=1614.2M loss=1.8598 lr=1.51e-04 tok/s=12488
[train] step=98530 tokens=1614.3M loss=2.4008 lr=1.51e-04 tok/s=12488
[train] step=98540 tokens=1614.5M loss=2.7195 lr=1.50e-04 tok/s=12488
[train] step=98550 tokens=1614.6M loss=2.0850 lr=1.50e-04 tok/s=12488
[train] step=98560 tokens=1614.8M loss=2.3419 lr=1.50e-04 tok/s=12488
[train] step=98570 tokens=1615.0M loss=2.1831 lr=1.50e-04 tok/s=12488
[train] step=98580 tokens=1615.1M loss=2.0784 lr=1.50e-04 tok/s=12488
```
