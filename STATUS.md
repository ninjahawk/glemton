# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 13:39:12 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1848M / 3000M (61.6%) |
| Step | 112800 |
| Latest loss | 2.2868 |
| Avg loss (last 30 logged) | 2.2025 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 1 day, 1:37:13 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.43 -> 2.06 -> 1.69 -> 2.25 -> 2.15 -> 2.20 -> 2.02 -> 2.14 -> 2.06 -> 1.88 -> 1.97 -> 2.18

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=112690 tokens=1846.3M loss=2.2771 lr=1.18e-04 tok/s=12489
[train] step=112700 tokens=1846.5M loss=2.1302 lr=1.18e-04 tok/s=12489
[train] step=112710 tokens=1846.6M loss=2.2875 lr=1.18e-04 tok/s=12489
[train] step=112720 tokens=1846.8M loss=2.1315 lr=1.18e-04 tok/s=12489
[train] step=112730 tokens=1847.0M loss=2.2658 lr=1.18e-04 tok/s=12489
[train] step=112740 tokens=1847.1M loss=2.6409 lr=1.18e-04 tok/s=12489
[train] step=112750 tokens=1847.3M loss=1.5029 lr=1.18e-04 tok/s=12489
[train] step=112760 tokens=1847.5M loss=2.4411 lr=1.18e-04 tok/s=12489
[train] step=112770 tokens=1847.6M loss=2.4319 lr=1.18e-04 tok/s=12489
[train] step=112780 tokens=1847.8M loss=2.1774 lr=1.18e-04 tok/s=12489
[train] step=112790 tokens=1848.0M loss=1.9078 lr=1.18e-04 tok/s=12489
[train] step=112800 tokens=1848.1M loss=2.2868 lr=1.18e-04 tok/s=12489
```
