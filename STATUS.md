# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 02:03:36 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 248M / 3000M (8.3%) |
| Step | 15130 |
| Latest loss | 2.3499 |
| Avg loss (last 30 logged) | 2.5400 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 2 days, 13:12:41 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.59 -> 2.38 -> 2.44 -> 2.31 -> 2.85 -> 2.57 -> 2.28 -> 3.00 -> 2.50 -> 2.91 -> 2.51 -> 2.27

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=15020 tokens=246.1M loss=2.6963 lr=2.96e-04 tok/s=12489
[train] step=15030 tokens=246.3M loss=2.4434 lr=2.96e-04 tok/s=12489
[train] step=15040 tokens=246.4M loss=2.5847 lr=2.96e-04 tok/s=12489
[train] step=15050 tokens=246.6M loss=3.0409 lr=2.96e-04 tok/s=12489
[train] step=15060 tokens=246.7M loss=2.2905 lr=2.96e-04 tok/s=12489
[train] step=15070 tokens=246.9M loss=2.4835 lr=2.96e-04 tok/s=12489
[train] step=15080 tokens=247.1M loss=2.4806 lr=2.96e-04 tok/s=12489
[train] step=15090 tokens=247.2M loss=2.5851 lr=2.96e-04 tok/s=12489
[train] step=15100 tokens=247.4M loss=2.4555 lr=2.96e-04 tok/s=12489
[train] step=15110 tokens=247.6M loss=2.2711 lr=2.96e-04 tok/s=12489
[train] step=15120 tokens=247.7M loss=2.9602 lr=2.96e-04 tok/s=12489
[train] step=15130 tokens=247.9M loss=2.3499 lr=2.96e-04 tok/s=12489
```
