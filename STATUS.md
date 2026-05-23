# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 08:18:23 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1608M / 3000M (53.6%) |
| Step | 98120 |
| Latest loss | 2.1761 |
| Avg loss (last 30 logged) | 2.1560 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 6:58:19 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.04 -> 1.77 -> 1.75 -> 2.37 -> 2.19 -> 2.09 -> 2.26 -> 1.81 -> 2.08 -> 2.31 -> 2.64 -> 2.39

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=98010 tokens=1605.8M loss=2.4448 lr=1.52e-04 tok/s=12488
[train] step=98020 tokens=1606.0M loss=2.4102 lr=1.52e-04 tok/s=12488
[train] step=98030 tokens=1606.1M loss=2.0942 lr=1.52e-04 tok/s=12488
[train] step=98040 tokens=1606.3M loss=2.4917 lr=1.52e-04 tok/s=12488
[train] step=98050 tokens=1606.5M loss=2.4256 lr=1.52e-04 tok/s=12488
[train] step=98060 tokens=1606.6M loss=2.4250 lr=1.52e-04 tok/s=12488
[train] step=98070 tokens=1606.8M loss=2.1340 lr=1.52e-04 tok/s=12488
[train] step=98080 tokens=1606.9M loss=2.0544 lr=1.52e-04 tok/s=12488
[train] step=98090 tokens=1607.1M loss=2.0223 lr=1.52e-04 tok/s=12488
[train] step=98100 tokens=1607.3M loss=2.3877 lr=1.52e-04 tok/s=12488
[train] step=98110 tokens=1607.4M loss=2.2898 lr=1.51e-04 tok/s=12488
[train] step=98120 tokens=1607.6M loss=2.1761 lr=1.51e-04 tok/s=12488
```
