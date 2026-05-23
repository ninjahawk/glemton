# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 09:08:30 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1645M / 3000M (54.8%) |
| Step | 100410 |
| Latest loss | 2.4230 |
| Avg loss (last 30 logged) | 2.1734 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 6:08:16 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.00 -> 1.93 -> 2.16 -> 2.22 -> 2.05 -> 2.12 -> 2.29 -> 1.76 -> 2.17 -> 2.24 -> 2.05 -> 2.28

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=100300 tokens=1643.3M loss=2.4172 lr=1.46e-04 tok/s=12488
[train] step=100310 tokens=1643.5M loss=2.2064 lr=1.46e-04 tok/s=12488
[train] step=100320 tokens=1643.6M loss=2.2208 lr=1.46e-04 tok/s=12488
[train] step=100330 tokens=1643.8M loss=2.2360 lr=1.46e-04 tok/s=12488
[train] step=100340 tokens=1644.0M loss=2.2649 lr=1.46e-04 tok/s=12488
[train] step=100350 tokens=1644.1M loss=2.0670 lr=1.46e-04 tok/s=12488
[train] step=100360 tokens=1644.3M loss=1.9225 lr=1.46e-04 tok/s=12488
[train] step=100370 tokens=1644.5M loss=2.0036 lr=1.46e-04 tok/s=12488
[train] step=100380 tokens=1644.6M loss=2.0160 lr=1.46e-04 tok/s=12488
[train] step=100390 tokens=1644.8M loss=2.2755 lr=1.46e-04 tok/s=12488
[train] step=100400 tokens=1645.0M loss=2.1802 lr=1.46e-04 tok/s=12488
[train] step=100410 tokens=1645.1M loss=2.4230 lr=1.46e-04 tok/s=12488
```
