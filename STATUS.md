# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 10:04:55 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 608M / 3000M (20.3%) |
| Step | 37120 |
| Latest loss | 2.2144 |
| Avg loss (last 30 logged) | 2.4005 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 5:13:24 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.22 -> 2.83 -> 2.03 -> 2.19 -> 2.46 -> 2.38 -> 3.03 -> 2.28 -> 2.49 -> 2.31 -> 2.38 -> 2.26

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=37010 tokens=606.4M loss=2.7557 lr=2.75e-04 tok/s=12483
[train] step=37020 tokens=606.5M loss=2.0248 lr=2.75e-04 tok/s=12483
[train] step=37030 tokens=606.7M loss=2.2163 lr=2.75e-04 tok/s=12483
[train] step=37040 tokens=606.9M loss=2.7101 lr=2.75e-04 tok/s=12483
[train] step=37050 tokens=607.0M loss=2.3152 lr=2.75e-04 tok/s=12483
[train] step=37060 tokens=607.2M loss=2.6658 lr=2.75e-04 tok/s=12483
[train] step=37070 tokens=607.4M loss=2.2686 lr=2.75e-04 tok/s=12483
[train] step=37080 tokens=607.5M loss=2.5190 lr=2.75e-04 tok/s=12483
[train] step=37090 tokens=607.7M loss=2.1388 lr=2.75e-04 tok/s=12483
[train] step=37100 tokens=607.8M loss=2.2585 lr=2.75e-04 tok/s=12483
[train] step=37110 tokens=608.0M loss=2.3009 lr=2.75e-04 tok/s=12483
[train] step=37120 tokens=608.2M loss=2.2144 lr=2.75e-04 tok/s=12483
```
