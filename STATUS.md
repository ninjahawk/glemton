# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 17:16:04 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 931M / 3000M (31.0%) |
| Step | 56840 |
| Latest loss | 2.2403 |
| Avg loss (last 30 logged) | 2.2838 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 22:01:34 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.36 -> 2.20 -> 2.38 -> 1.98 -> 2.33 -> 2.14 -> 2.33 -> 2.40 -> 2.23 -> 2.08 -> 2.61 -> 2.09

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=56730 tokens=929.5M loss=2.3064 lr=2.43e-04 tok/s=12485
[train] step=56740 tokens=929.6M loss=2.1900 lr=2.43e-04 tok/s=12485
[train] step=56750 tokens=929.8M loss=2.2799 lr=2.43e-04 tok/s=12485
[train] step=56760 tokens=930.0M loss=2.3546 lr=2.43e-04 tok/s=12485
[train] step=56770 tokens=930.1M loss=2.0485 lr=2.43e-04 tok/s=12485
[train] step=56780 tokens=930.3M loss=2.4992 lr=2.43e-04 tok/s=12485
[train] step=56790 tokens=930.4M loss=2.5252 lr=2.43e-04 tok/s=12485
[train] step=56800 tokens=930.6M loss=2.1451 lr=2.43e-04 tok/s=12485
[train] step=56810 tokens=930.8M loss=2.0983 lr=2.43e-04 tok/s=12485
[train] step=56820 tokens=930.9M loss=2.0911 lr=2.43e-04 tok/s=12485
[train] step=56830 tokens=931.1M loss=2.1338 lr=2.43e-04 tok/s=12485
[train] step=56840 tokens=931.3M loss=2.2403 lr=2.43e-04 tok/s=12485
```
