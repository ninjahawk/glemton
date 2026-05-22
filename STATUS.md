# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 04:34:00 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 360M / 3000M (12.0%) |
| Step | 22000 |
| Latest loss | 2.2759 |
| Avg loss (last 30 logged) | 2.4155 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 2 days, 10:43:07 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.95 -> 2.70 -> 2.55 -> 2.47 -> 2.30 -> 2.34 -> 2.61 -> 2.37 -> 2.20 -> 2.67 -> 2.28 -> 2.59

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=21890 tokens=358.6M loss=2.4811 lr=2.92e-04 tok/s=12487
[train] step=21900 tokens=358.8M loss=2.4510 lr=2.92e-04 tok/s=12487
[train] step=21910 tokens=359.0M loss=2.2484 lr=2.92e-04 tok/s=12487
[train] step=21920 tokens=359.1M loss=2.6123 lr=2.92e-04 tok/s=12487
[train] step=21930 tokens=359.3M loss=2.5940 lr=2.92e-04 tok/s=12487
[train] step=21940 tokens=359.5M loss=2.0851 lr=2.92e-04 tok/s=12487
[train] step=21950 tokens=359.6M loss=2.3097 lr=2.92e-04 tok/s=12487
[train] step=21960 tokens=359.8M loss=2.4218 lr=2.92e-04 tok/s=12487
[train] step=21970 tokens=360.0M loss=2.3854 lr=2.92e-04 tok/s=12487
[train] step=21980 tokens=360.1M loss=2.5875 lr=2.92e-04 tok/s=12487
[train] step=21990 tokens=360.3M loss=2.3625 lr=2.92e-04 tok/s=12487
[train] step=22000 tokens=360.4M loss=2.2759 lr=2.92e-04 tok/s=12487
```
