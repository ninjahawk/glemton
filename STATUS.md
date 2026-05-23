# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 10:58:48 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1728M / 3000M (57.6%) |
| Step | 105460 |
| Latest loss | 1.9153 |
| Avg loss (last 30 logged) | 2.1454 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 4:17:45 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.15 -> 2.18 -> 1.89 -> 2.23 -> 1.79 -> 2.22 -> 2.21 -> 2.03 -> 2.11 -> 1.71 -> 1.99 -> 2.06

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=105350 tokens=1726.1M loss=2.0967 lr=1.35e-04 tok/s=12488
[train] step=105360 tokens=1726.2M loss=2.0310 lr=1.35e-04 tok/s=12488
[train] step=105370 tokens=1726.4M loss=2.0930 lr=1.35e-04 tok/s=12488
[train] step=105380 tokens=1726.5M loss=1.9130 lr=1.35e-04 tok/s=12488
[train] step=105390 tokens=1726.7M loss=2.2340 lr=1.35e-04 tok/s=12488
[train] step=105400 tokens=1726.9M loss=1.9696 lr=1.35e-04 tok/s=12488
[train] step=105410 tokens=1727.0M loss=2.4430 lr=1.35e-04 tok/s=12488
[train] step=105420 tokens=1727.2M loss=2.4322 lr=1.35e-04 tok/s=12488
[train] step=105430 tokens=1727.4M loss=1.8682 lr=1.35e-04 tok/s=12488
[train] step=105440 tokens=1727.5M loss=2.0579 lr=1.35e-04 tok/s=12488
[train] step=105450 tokens=1727.7M loss=2.0633 lr=1.35e-04 tok/s=12488
[train] step=105460 tokens=1727.9M loss=1.9153 lr=1.35e-04 tok/s=12488
```
