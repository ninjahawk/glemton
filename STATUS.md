# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 01:43:33 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 233M / 3000M (7.8%) |
| Step | 14210 |
| Latest loss | 2.9350 |
| Avg loss (last 30 logged) | 2.5668 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 2 days, 13:32:33 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.57 -> 2.64 -> 2.56 -> 2.34 -> 2.43 -> 2.88 -> 2.90 -> 2.60 -> 2.49 -> 2.52 -> 2.58 -> 2.28

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=14100 tokens=231.0M loss=2.5258 lr=2.97e-04 tok/s=12490
[train] step=14110 tokens=231.2M loss=2.4128 lr=2.97e-04 tok/s=12490
[train] step=14120 tokens=231.3M loss=2.5039 lr=2.97e-04 tok/s=12490
[train] step=14130 tokens=231.5M loss=3.0063 lr=2.97e-04 tok/s=12490
[train] step=14140 tokens=231.7M loss=2.2381 lr=2.97e-04 tok/s=12490
[train] step=14150 tokens=231.8M loss=2.3907 lr=2.97e-04 tok/s=12490
[train] step=14160 tokens=232.0M loss=2.6433 lr=2.97e-04 tok/s=12490
[train] step=14170 tokens=232.2M loss=2.2847 lr=2.97e-04 tok/s=12490
[train] step=14180 tokens=232.3M loss=2.4606 lr=2.97e-04 tok/s=12490
[train] step=14190 tokens=232.5M loss=2.2799 lr=2.97e-04 tok/s=12490
[train] step=14200 tokens=232.7M loss=2.3602 lr=2.97e-04 tok/s=12490
[train] step=14210 tokens=232.8M loss=2.9350 lr=2.97e-04 tok/s=12490
```
