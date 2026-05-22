# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 16:25:56 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 894M / 3000M (29.8%) |
| Step | 54550 |
| Latest loss | 2.2562 |
| Avg loss (last 30 logged) | 2.3075 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 22:51:46 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.43 -> 2.44 -> 1.98 -> 2.10 -> 2.21 -> 2.68 -> 2.36 -> 2.20 -> 2.45 -> 2.52 -> 2.34 -> 2.02

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`

## Recent log tail
```
[train] step=54440 tokens=891.9M loss=2.3469 lr=2.47e-04 tok/s=12485
[train] step=54450 tokens=892.1M loss=2.5807 lr=2.47e-04 tok/s=12485
[train] step=54460 tokens=892.3M loss=2.2077 lr=2.47e-04 tok/s=12485
[train] step=54470 tokens=892.4M loss=2.0983 lr=2.47e-04 tok/s=12485
[train] step=54480 tokens=892.6M loss=2.0594 lr=2.47e-04 tok/s=12485
[train] step=54490 tokens=892.8M loss=2.0425 lr=2.47e-04 tok/s=12485
[train] step=54500 tokens=892.9M loss=2.0802 lr=2.47e-04 tok/s=12485
[train] step=54510 tokens=893.1M loss=2.3291 lr=2.47e-04 tok/s=12485
[train] step=54520 tokens=893.3M loss=2.0244 lr=2.47e-04 tok/s=12485
[train] step=54530 tokens=893.4M loss=2.1949 lr=2.47e-04 tok/s=12485
[train] step=54540 tokens=893.6M loss=2.4030 lr=2.47e-04 tok/s=12485
[train] step=54550 tokens=893.7M loss=2.2562 lr=2.47e-04 tok/s=12485
```
