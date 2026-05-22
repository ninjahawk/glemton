# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 18:56:20 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1006M / 3000M (33.5%) |
| Step | 61430 |
| Latest loss | 1.8689 |
| Avg loss (last 30 logged) | 2.2888 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 20:21:11 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.60 -> 2.67 -> 2.53 -> 2.53 -> 2.02 -> 2.58 -> 2.44 -> 2.18 -> 1.76 -> 2.39 -> 2.10 -> 2.59

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`

## Recent log tail
```
[train] step=61320 tokens=1004.7M loss=2.9186 lr=2.34e-04 tok/s=12485
[train] step=61330 tokens=1004.8M loss=2.1336 lr=2.34e-04 tok/s=12485
[train] step=61340 tokens=1005.0M loss=2.5656 lr=2.34e-04 tok/s=12485
[train] step=61350 tokens=1005.2M loss=2.3066 lr=2.34e-04 tok/s=12485
[train] step=61360 tokens=1005.3M loss=2.0264 lr=2.34e-04 tok/s=12485
[train] step=61370 tokens=1005.5M loss=2.5210 lr=2.34e-04 tok/s=12485
[train] step=61380 tokens=1005.6M loss=1.9741 lr=2.34e-04 tok/s=12485
[train] step=61390 tokens=1005.8M loss=2.3349 lr=2.34e-04 tok/s=12485
[train] step=61400 tokens=1006.0M loss=2.1314 lr=2.34e-04 tok/s=12485
[train] step=61410 tokens=1006.1M loss=2.5928 lr=2.34e-04 tok/s=12485
[train] step=61420 tokens=1006.3M loss=2.3848 lr=2.34e-04 tok/s=12485
[train] step=61430 tokens=1006.5M loss=1.8689 lr=2.34e-04 tok/s=12485
```
