# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 10:38:44 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1713M / 3000M (57.1%) |
| Step | 104540 |
| Latest loss | 2.1813 |
| Avg loss (last 30 logged) | 2.0857 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 4:37:54 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.18 -> 2.18 -> 2.28 -> 1.63 -> 2.13 -> 2.05 -> 2.55 -> 2.11 -> 2.13 -> 1.79 -> 2.04 -> 2.14

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=104430 tokens=1711.0M loss=1.9605 lr=1.37e-04 tok/s=12488
[train] step=104440 tokens=1711.1M loss=2.0569 lr=1.37e-04 tok/s=12488
[train] step=104450 tokens=1711.3M loss=2.1121 lr=1.37e-04 tok/s=12488
[train] step=104460 tokens=1711.5M loss=2.0352 lr=1.37e-04 tok/s=12488
[train] step=104470 tokens=1711.6M loss=2.0574 lr=1.37e-04 tok/s=12488
[train] step=104480 tokens=1711.8M loss=2.3875 lr=1.37e-04 tok/s=12488
[train] step=104490 tokens=1712.0M loss=2.2323 lr=1.37e-04 tok/s=12488
[train] step=104500 tokens=1712.1M loss=1.8904 lr=1.37e-04 tok/s=12488
[train] step=104510 tokens=1712.3M loss=2.0947 lr=1.37e-04 tok/s=12488
[train] step=104520 tokens=1712.5M loss=2.1444 lr=1.37e-04 tok/s=12488
[train] step=104530 tokens=1712.6M loss=2.2266 lr=1.37e-04 tok/s=12488
[train] step=104540 tokens=1712.8M loss=2.1813 lr=1.37e-04 tok/s=12488
```
