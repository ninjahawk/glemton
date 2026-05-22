# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 02:23:39 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 263M / 3000M (8.8%) |
| Step | 16040 |
| Latest loss | 2.5222 |
| Avg loss (last 30 logged) | 2.5105 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 2 days, 12:52:31 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.46 -> 2.34 -> 2.76 -> 2.60 -> 2.89 -> 2.50 -> 2.44 -> 2.65 -> 2.44 -> 2.50 -> 2.34 -> 2.24

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=15930 tokens=261.0M loss=2.5484 lr=2.96e-04 tok/s=12490
[train] step=15940 tokens=261.2M loss=2.3965 lr=2.96e-04 tok/s=12490
[train] step=15950 tokens=261.3M loss=2.3880 lr=2.96e-04 tok/s=12490
[train] step=15960 tokens=261.5M loss=2.6454 lr=2.96e-04 tok/s=12490
[train] step=15970 tokens=261.7M loss=2.5816 lr=2.96e-04 tok/s=12490
[train] step=15980 tokens=261.8M loss=2.3443 lr=2.96e-04 tok/s=12490
[train] step=15990 tokens=262.0M loss=2.3723 lr=2.96e-04 tok/s=12490
[train] step=16000 tokens=262.1M loss=2.8082 lr=2.96e-04 tok/s=12490
[train] step=16010 tokens=262.3M loss=2.4181 lr=2.96e-04 tok/s=12490
[train] step=16020 tokens=262.5M loss=2.2416 lr=2.96e-04 tok/s=12490
[train] step=16030 tokens=262.6M loss=3.2123 lr=2.96e-04 tok/s=12490
[train] step=16040 tokens=262.8M loss=2.5222 lr=2.96e-04 tok/s=12490
```
