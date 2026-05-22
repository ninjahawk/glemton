# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 01:53:34 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 240M / 3000M (8.0%) |
| Step | 14670 |
| Latest loss | 2.3644 |
| Avg loss (last 30 logged) | 2.5641 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 2 days, 13:22:24 |
| Projected finish | Sun 2026-05-24 15:15 |

## Loss trajectory (sampled)
2.46 -> 2.73 -> 2.38 -> 2.57 -> 2.88 -> 2.49 -> 2.40 -> 2.81 -> 2.37 -> 2.39 -> 2.22 -> 2.75

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=14560 tokens=238.6M loss=2.8470 lr=2.97e-04 tok/s=12490
[train] step=14570 tokens=238.7M loss=2.3588 lr=2.97e-04 tok/s=12490
[train] step=14580 tokens=238.9M loss=2.4711 lr=2.97e-04 tok/s=12490
[train] step=14590 tokens=239.0M loss=2.3549 lr=2.97e-04 tok/s=12490
[train] step=14600 tokens=239.2M loss=2.5816 lr=2.97e-04 tok/s=12490
[train] step=14610 tokens=239.4M loss=3.1405 lr=2.97e-04 tok/s=12490
[train] step=14620 tokens=239.5M loss=2.4844 lr=2.97e-04 tok/s=12490
[train] step=14630 tokens=239.7M loss=2.3585 lr=2.97e-04 tok/s=12490
[train] step=14640 tokens=239.9M loss=2.6621 lr=2.97e-04 tok/s=12490
[train] step=14650 tokens=240.0M loss=2.7468 lr=2.97e-04 tok/s=12490
[train] step=14660 tokens=240.2M loss=2.2859 lr=2.97e-04 tok/s=12490
[train] step=14670 tokens=240.4M loss=2.3644 lr=2.97e-04 tok/s=12490
```
