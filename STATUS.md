# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 10:48:46 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1720M / 3000M (57.3%) |
| Step | 105000 |
| Latest loss | 2.0409 |
| Avg loss (last 30 logged) | 2.0696 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 4:27:54 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.03 -> 2.26 -> 2.03 -> 2.33 -> 2.23 -> 2.35 -> 2.11 -> 2.15 -> 2.22 -> 2.20 -> 2.43 -> 1.79

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=104890 tokens=1718.5M loss=1.9301 lr=1.36e-04 tok/s=12488
[train] step=104900 tokens=1718.7M loss=1.9214 lr=1.36e-04 tok/s=12488
[train] step=104910 tokens=1718.8M loss=1.9759 lr=1.36e-04 tok/s=12488
[train] step=104920 tokens=1719.0M loss=1.9930 lr=1.36e-04 tok/s=12488
[train] step=104930 tokens=1719.2M loss=1.8872 lr=1.36e-04 tok/s=12488
[train] step=104940 tokens=1719.3M loss=2.4651 lr=1.36e-04 tok/s=12488
[train] step=104950 tokens=1719.5M loss=1.7058 lr=1.36e-04 tok/s=12488
[train] step=104960 tokens=1719.7M loss=1.7072 lr=1.36e-04 tok/s=12488
[train] step=104970 tokens=1719.8M loss=2.0056 lr=1.36e-04 tok/s=12488
[train] step=104980 tokens=1720.0M loss=1.7904 lr=1.36e-04 tok/s=12488
[train] step=104990 tokens=1720.2M loss=2.0012 lr=1.36e-04 tok/s=12488
[train] step=105000 tokens=1720.3M loss=2.0409 lr=1.36e-04 tok/s=12488
```
