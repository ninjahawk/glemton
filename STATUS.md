# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 02:33:41 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 270M / 3000M (9.0%) |
| Step | 16500 |
| Latest loss | 2.3347 |
| Avg loss (last 30 logged) | 2.5526 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 2 days, 12:42:30 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.58 -> 2.22 -> 2.29 -> 2.55 -> 2.64 -> 2.70 -> 2.55 -> 2.47 -> 2.56 -> 2.66 -> 2.84 -> 2.59

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=16390 tokens=268.5M loss=2.9031 lr=2.96e-04 tok/s=12490
[train] step=16400 tokens=268.7M loss=2.4712 lr=2.96e-04 tok/s=12490
[train] step=16410 tokens=268.9M loss=2.5345 lr=2.96e-04 tok/s=12490
[train] step=16420 tokens=269.0M loss=2.7187 lr=2.96e-04 tok/s=12490
[train] step=16430 tokens=269.2M loss=2.7921 lr=2.96e-04 tok/s=12490
[train] step=16440 tokens=269.4M loss=3.0493 lr=2.96e-04 tok/s=12490
[train] step=16450 tokens=269.5M loss=2.3542 lr=2.96e-04 tok/s=12490
[train] step=16460 tokens=269.7M loss=2.5752 lr=2.96e-04 tok/s=12490
[train] step=16470 tokens=269.8M loss=2.5916 lr=2.96e-04 tok/s=12490
[train] step=16480 tokens=270.0M loss=2.5493 lr=2.96e-04 tok/s=12490
[train] step=16490 tokens=270.2M loss=2.5726 lr=2.96e-04 tok/s=12490
[train] step=16500 tokens=270.3M loss=2.3347 lr=2.95e-04 tok/s=12490
```
