# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 05:04:05 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 383M / 3000M (12.8%) |
| Step | 23380 |
| Latest loss | 2.2285 |
| Avg loss (last 30 logged) | 2.4375 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 2 days, 10:12:49 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.27 -> 3.31 -> 2.25 -> 2.47 -> 2.19 -> 2.34 -> 2.50 -> 2.25 -> 2.66 -> 2.48 -> 2.38 -> 2.61

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=23270 tokens=381.3M loss=2.4829 lr=2.91e-04 tok/s=12487
[train] step=23280 tokens=381.4M loss=2.2851 lr=2.91e-04 tok/s=12487
[train] step=23290 tokens=381.6M loss=2.4227 lr=2.91e-04 tok/s=12487
[train] step=23300 tokens=381.7M loss=2.7972 lr=2.91e-04 tok/s=12487
[train] step=23310 tokens=381.9M loss=2.5212 lr=2.91e-04 tok/s=12487
[train] step=23320 tokens=382.1M loss=2.3312 lr=2.91e-04 tok/s=12487
[train] step=23330 tokens=382.2M loss=2.4340 lr=2.91e-04 tok/s=12487
[train] step=23340 tokens=382.4M loss=2.4359 lr=2.90e-04 tok/s=12487
[train] step=23350 tokens=382.6M loss=2.6112 lr=2.90e-04 tok/s=12487
[train] step=23360 tokens=382.7M loss=2.6728 lr=2.90e-04 tok/s=12487
[train] step=23370 tokens=382.9M loss=2.0776 lr=2.90e-04 tok/s=12487
[train] step=23380 tokens=383.1M loss=2.2285 lr=2.90e-04 tok/s=12487
```
