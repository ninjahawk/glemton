# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 05:34:10 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 406M / 3000M (13.5%) |
| Step | 24750 |
| Latest loss | 2.2251 |
| Avg loss (last 30 logged) | 2.3872 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 2 days, 9:43:12 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.47 -> 2.45 -> 2.19 -> 2.51 -> 2.95 -> 2.38 -> 2.43 -> 2.25 -> 2.40 -> 2.40 -> 2.48 -> 2.25

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=24640 tokens=403.7M loss=2.4487 lr=2.89e-04 tok/s=12486
[train] step=24650 tokens=403.9M loss=2.4357 lr=2.89e-04 tok/s=12486
[train] step=24660 tokens=404.0M loss=2.5267 lr=2.89e-04 tok/s=12486
[train] step=24670 tokens=404.2M loss=2.2156 lr=2.89e-04 tok/s=12486
[train] step=24680 tokens=404.4M loss=2.3853 lr=2.89e-04 tok/s=12486
[train] step=24690 tokens=404.5M loss=2.3061 lr=2.89e-04 tok/s=12486
[train] step=24700 tokens=404.7M loss=2.6384 lr=2.89e-04 tok/s=12486
[train] step=24710 tokens=404.8M loss=2.3488 lr=2.89e-04 tok/s=12486
[train] step=24720 tokens=405.0M loss=2.4836 lr=2.89e-04 tok/s=12486
[train] step=24730 tokens=405.2M loss=2.2463 lr=2.89e-04 tok/s=12486
[train] step=24740 tokens=405.3M loss=2.1750 lr=2.89e-04 tok/s=12486
[train] step=24750 tokens=405.5M loss=2.2251 lr=2.89e-04 tok/s=12486
```
