# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 14:19:18 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1878M / 3000M (62.6%) |
| Step | 114630 |
| Latest loss | 1.8872 |
| Avg loss (last 30 logged) | 2.0447 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 1 day, 0:57:11 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.03 -> 1.84 -> 2.49 -> 2.23 -> 2.05 -> 2.29 -> 1.92 -> 2.29 -> 2.18 -> 2.31 -> 2.03 -> 2.33

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=114520 tokens=1876.3M loss=2.5457 lr=1.14e-04 tok/s=12489
[train] step=114530 tokens=1876.5M loss=2.0914 lr=1.14e-04 tok/s=12489
[train] step=114540 tokens=1876.6M loss=1.9689 lr=1.14e-04 tok/s=12489
[train] step=114550 tokens=1876.8M loss=1.9342 lr=1.14e-04 tok/s=12489
[train] step=114560 tokens=1877.0M loss=1.9997 lr=1.14e-04 tok/s=12489
[train] step=114570 tokens=1877.1M loss=1.8048 lr=1.14e-04 tok/s=12489
[train] step=114580 tokens=1877.3M loss=1.9028 lr=1.14e-04 tok/s=12489
[train] step=114590 tokens=1877.4M loss=2.0539 lr=1.14e-04 tok/s=12489
[train] step=114600 tokens=1877.6M loss=2.3306 lr=1.14e-04 tok/s=12489
[train] step=114610 tokens=1877.8M loss=1.7975 lr=1.14e-04 tok/s=12489
[train] step=114620 tokens=1877.9M loss=2.0402 lr=1.14e-04 tok/s=12489
[train] step=114630 tokens=1878.1M loss=1.8872 lr=1.14e-04 tok/s=12489
```
