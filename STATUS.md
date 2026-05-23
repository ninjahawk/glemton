# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 09:28:34 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1660M / 3000M (55.3%) |
| Step | 101330 |
| Latest loss | 1.8159 |
| Avg loss (last 30 logged) | 2.1184 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 5:48:06 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.97 -> 2.44 -> 1.86 -> 1.98 -> 2.43 -> 1.90 -> 2.24 -> 2.53 -> 2.22 -> 1.74 -> 2.25 -> 2.08

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=101220 tokens=1658.4M loss=2.1810 lr=1.44e-04 tok/s=12488
[train] step=101230 tokens=1658.6M loss=1.9696 lr=1.44e-04 tok/s=12488
[train] step=101240 tokens=1658.7M loss=2.3321 lr=1.44e-04 tok/s=12488
[train] step=101250 tokens=1658.9M loss=2.3442 lr=1.44e-04 tok/s=12488
[train] step=101260 tokens=1659.0M loss=2.3154 lr=1.44e-04 tok/s=12488
[train] step=101270 tokens=1659.2M loss=1.9228 lr=1.44e-04 tok/s=12488
[train] step=101280 tokens=1659.4M loss=1.7889 lr=1.44e-04 tok/s=12488
[train] step=101290 tokens=1659.5M loss=1.8601 lr=1.44e-04 tok/s=12488
[train] step=101300 tokens=1659.7M loss=1.8565 lr=1.44e-04 tok/s=12488
[train] step=101310 tokens=1659.9M loss=2.0782 lr=1.44e-04 tok/s=12488
[train] step=101320 tokens=1660.0M loss=2.3929 lr=1.44e-04 tok/s=12488
[train] step=101330 tokens=1660.2M loss=1.8159 lr=1.44e-04 tok/s=12488
```
