# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 14:15:38 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 796M / 3000M (26.5%) |
| Step | 48590 |
| Latest loss | 2.2916 |
| Avg loss (last 30 logged) | 2.3319 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 1:02:17 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.22 -> 2.31 -> 2.35 -> 2.73 -> 2.68 -> 2.16 -> 2.20 -> 2.34 -> 2.06 -> 2.30 -> 2.48 -> 2.37

## Checkpoints on disk
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`

## Recent log tail
```
[train] step=48480 tokens=794.3M loss=2.2381 lr=2.58e-04 tok/s=12484
[train] step=48490 tokens=794.5M loss=2.2864 lr=2.58e-04 tok/s=12484
[train] step=48500 tokens=794.6M loss=2.0861 lr=2.58e-04 tok/s=12484
[train] step=48510 tokens=794.8M loss=2.3114 lr=2.58e-04 tok/s=12484
[train] step=48520 tokens=795.0M loss=2.2974 lr=2.58e-04 tok/s=12484
[train] step=48530 tokens=795.1M loss=2.5254 lr=2.58e-04 tok/s=12484
[train] step=48540 tokens=795.3M loss=2.3639 lr=2.58e-04 tok/s=12484
[train] step=48550 tokens=795.4M loss=2.4671 lr=2.58e-04 tok/s=12484
[train] step=48560 tokens=795.6M loss=2.3665 lr=2.58e-04 tok/s=12484
[train] step=48570 tokens=795.8M loss=2.3658 lr=2.58e-04 tok/s=12484
[train] step=48580 tokens=795.9M loss=2.2629 lr=2.58e-04 tok/s=12484
[train] step=48590 tokens=796.1M loss=2.2916 lr=2.58e-04 tok/s=12484
```
