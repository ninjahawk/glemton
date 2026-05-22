# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 18:16:14 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 976M / 3000M (32.5%) |
| Step | 59590 |
| Latest loss | 2.0617 |
| Avg loss (last 30 logged) | 2.2917 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 21:01:30 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.34 -> 2.17 -> 2.56 -> 2.11 -> 2.22 -> 2.53 -> 2.16 -> 1.95 -> 2.32 -> 2.30 -> 2.12 -> 2.59

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=59480 tokens=974.5M loss=2.5677 lr=2.38e-04 tok/s=12485
[train] step=59490 tokens=974.7M loss=1.9598 lr=2.38e-04 tok/s=12485
[train] step=59500 tokens=974.8M loss=2.3844 lr=2.38e-04 tok/s=12485
[train] step=59510 tokens=975.0M loss=1.9911 lr=2.38e-04 tok/s=12485
[train] step=59520 tokens=975.2M loss=2.3323 lr=2.38e-04 tok/s=12485
[train] step=59530 tokens=975.3M loss=2.2860 lr=2.38e-04 tok/s=12485
[train] step=59540 tokens=975.5M loss=2.6437 lr=2.38e-04 tok/s=12485
[train] step=59550 tokens=975.7M loss=2.2520 lr=2.37e-04 tok/s=12485
[train] step=59560 tokens=975.8M loss=2.5915 lr=2.37e-04 tok/s=12485
[train] step=59570 tokens=976.0M loss=2.6105 lr=2.37e-04 tok/s=12485
[train] step=59580 tokens=976.2M loss=2.4050 lr=2.37e-04 tok/s=12485
[train] step=59590 tokens=976.3M loss=2.0617 lr=2.37e-04 tok/s=12485
```
