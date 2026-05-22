# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-21 23:43:12 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 143M / 3000M (4.8%) |
| Step | 8710 |
| Latest loss | 2.6750 |
| Avg loss (last 30 logged) | 2.6369 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 2 days, 15:33:05 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.89 -> 2.65 -> 2.88 -> 2.36 -> 2.81 -> 2.84 -> 2.56 -> 2.63 -> 2.36 -> 2.76 -> 2.70 -> 2.55

## Checkpoints on disk
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=8600 tokens=140.9M loss=2.7637 lr=2.99e-04 tok/s=12489
[train] step=8610 tokens=141.1M loss=2.5127 lr=2.99e-04 tok/s=12489
[train] step=8620 tokens=141.2M loss=2.3755 lr=2.99e-04 tok/s=12489
[train] step=8630 tokens=141.4M loss=2.7664 lr=2.99e-04 tok/s=12489
[train] step=8640 tokens=141.6M loss=2.4939 lr=2.99e-04 tok/s=12489
[train] step=8650 tokens=141.7M loss=2.8849 lr=2.99e-04 tok/s=12489
[train] step=8660 tokens=141.9M loss=2.6348 lr=2.99e-04 tok/s=12489
[train] step=8670 tokens=142.0M loss=2.7080 lr=2.99e-04 tok/s=12489
[train] step=8680 tokens=142.2M loss=2.7803 lr=2.99e-04 tok/s=12489
[train] step=8690 tokens=142.4M loss=2.5506 lr=2.99e-04 tok/s=12489
[train] step=8700 tokens=142.5M loss=2.9510 lr=2.99e-04 tok/s=12489
[train] step=8710 tokens=142.7M loss=2.6750 lr=2.99e-04 tok/s=12489
```
