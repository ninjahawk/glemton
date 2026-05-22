# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 17:56:10 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 961M / 3000M (32.0%) |
| Step | 58670 |
| Latest loss | 2.4009 |
| Avg loss (last 30 logged) | 2.2696 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 21:21:39 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.18 -> 2.30 -> 2.46 -> 2.41 -> 2.13 -> 2.29 -> 2.14 -> 2.57 -> 2.55 -> 2.19 -> 2.11 -> 2.52

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=58560 tokens=959.4M loss=2.0144 lr=2.39e-04 tok/s=12485
[train] step=58570 tokens=959.6M loss=2.3233 lr=2.39e-04 tok/s=12485
[train] step=58580 tokens=959.8M loss=2.2525 lr=2.39e-04 tok/s=12485
[train] step=58590 tokens=959.9M loss=2.2875 lr=2.39e-04 tok/s=12485
[train] step=58600 tokens=960.1M loss=2.7148 lr=2.39e-04 tok/s=12485
[train] step=58610 tokens=960.3M loss=1.9435 lr=2.39e-04 tok/s=12485
[train] step=58620 tokens=960.4M loss=2.3657 lr=2.39e-04 tok/s=12485
[train] step=58630 tokens=960.6M loss=2.0363 lr=2.39e-04 tok/s=12485
[train] step=58640 tokens=960.8M loss=2.0926 lr=2.39e-04 tok/s=12485
[train] step=58650 tokens=960.9M loss=2.5166 lr=2.39e-04 tok/s=12485
[train] step=58660 tokens=961.1M loss=2.4649 lr=2.39e-04 tok/s=12485
[train] step=58670 tokens=961.2M loss=2.4009 lr=2.39e-04 tok/s=12485
```
