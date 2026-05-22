# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 14:05:36 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 789M / 3000M (26.3%) |
| Step | 48130 |
| Latest loss | 2.5471 |
| Avg loss (last 30 logged) | 2.3417 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 1:12:32 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.54 -> 2.15 -> 2.19 -> 2.43 -> 2.16 -> 2.11 -> 2.24 -> 2.21 -> 2.27 -> 2.38 -> 2.50 -> 2.16

## Checkpoints on disk
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`

## Recent log tail
```
[train] step=48020 tokens=786.8M loss=2.4488 lr=2.59e-04 tok/s=12483
[train] step=48030 tokens=786.9M loss=2.2553 lr=2.59e-04 tok/s=12483
[train] step=48040 tokens=787.1M loss=2.2971 lr=2.59e-04 tok/s=12483
[train] step=48050 tokens=787.3M loss=2.2953 lr=2.59e-04 tok/s=12483
[train] step=48060 tokens=787.4M loss=2.4457 lr=2.59e-04 tok/s=12483
[train] step=48070 tokens=787.6M loss=2.2084 lr=2.59e-04 tok/s=12483
[train] step=48080 tokens=787.7M loss=2.3886 lr=2.59e-04 tok/s=12483
[train] step=48090 tokens=787.9M loss=2.2557 lr=2.59e-04 tok/s=12483
[train] step=48100 tokens=788.1M loss=2.1568 lr=2.58e-04 tok/s=12483
[train] step=48110 tokens=788.2M loss=2.3652 lr=2.58e-04 tok/s=12483
[train] step=48120 tokens=788.4M loss=2.4569 lr=2.58e-04 tok/s=12483
[train] step=48130 tokens=788.6M loss=2.5471 lr=2.58e-04 tok/s=12483
```
