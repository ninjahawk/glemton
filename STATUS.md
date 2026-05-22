# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 01:03:25 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 203M / 3000M (6.8%) |
| Step | 12380 |
| Latest loss | 2.5436 |
| Avg loss (last 30 logged) | 2.5764 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 2 days, 14:12:35 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.74 -> 2.56 -> 2.44 -> 2.35 -> 2.31 -> 2.36 -> 2.99 -> 2.41 -> 2.42 -> 2.79 -> 2.60 -> 2.33

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=12270 tokens=201.0M loss=2.3150 lr=2.98e-04 tok/s=12490
[train] step=12280 tokens=201.2M loss=2.5075 lr=2.98e-04 tok/s=12490
[train] step=12290 tokens=201.4M loss=2.9320 lr=2.98e-04 tok/s=12490
[train] step=12300 tokens=201.5M loss=2.3800 lr=2.98e-04 tok/s=12490
[train] step=12310 tokens=201.7M loss=2.2880 lr=2.98e-04 tok/s=12490
[train] step=12320 tokens=201.9M loss=2.3388 lr=2.98e-04 tok/s=12490
[train] step=12330 tokens=202.0M loss=2.4939 lr=2.98e-04 tok/s=12490
[train] step=12340 tokens=202.2M loss=2.8824 lr=2.98e-04 tok/s=12490
[train] step=12350 tokens=202.3M loss=2.5021 lr=2.98e-04 tok/s=12490
[train] step=12360 tokens=202.5M loss=2.3342 lr=2.98e-04 tok/s=12490
[train] step=12370 tokens=202.7M loss=2.6282 lr=2.98e-04 tok/s=12490
[train] step=12380 tokens=202.8M loss=2.5436 lr=2.98e-04 tok/s=12490
```
