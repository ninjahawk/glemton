# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 06:14:17 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 436M / 3000M (14.5%) |
| Step | 26580 |
| Latest loss | 2.2965 |
| Avg loss (last 30 logged) | 2.4381 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 2 days, 9:03:26 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.28 -> 2.42 -> 2.20 -> 2.39 -> 2.56 -> 2.38 -> 2.22 -> 2.10 -> 2.62 -> 2.49 -> 2.52 -> 2.53

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=26470 tokens=433.7M loss=2.4403 lr=2.88e-04 tok/s=12485
[train] step=26480 tokens=433.8M loss=2.3048 lr=2.88e-04 tok/s=12485
[train] step=26490 tokens=434.0M loss=2.6518 lr=2.88e-04 tok/s=12485
[train] step=26500 tokens=434.2M loss=2.6972 lr=2.88e-04 tok/s=12485
[train] step=26510 tokens=434.3M loss=2.3419 lr=2.88e-04 tok/s=12485
[train] step=26520 tokens=434.5M loss=2.1697 lr=2.88e-04 tok/s=12485
[train] step=26530 tokens=434.7M loss=2.5007 lr=2.88e-04 tok/s=12485
[train] step=26540 tokens=434.8M loss=2.7699 lr=2.88e-04 tok/s=12485
[train] step=26550 tokens=435.0M loss=2.4801 lr=2.88e-04 tok/s=12485
[train] step=26560 tokens=435.2M loss=2.5322 lr=2.88e-04 tok/s=12485
[train] step=26570 tokens=435.3M loss=2.3107 lr=2.88e-04 tok/s=12485
[train] step=26580 tokens=435.5M loss=2.2965 lr=2.88e-04 tok/s=12485
```
