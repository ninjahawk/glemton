# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-21 23:03:05 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 113M / 3000M (3.8%) |
| Step | 6870 |
| Latest loss | 2.4794 |
| Avg loss (last 30 logged) | 2.7067 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 2 days, 16:14:11 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.85 -> 3.06 -> 2.80 -> 2.91 -> 2.42 -> 2.63 -> 2.68 -> 2.84 -> 2.84 -> 2.70 -> 2.57 -> 2.58

## Checkpoints on disk
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=6760 tokens=110.8M loss=2.5434 lr=2.99e-04 tok/s=12486
[train] step=6770 tokens=110.9M loss=2.7377 lr=2.99e-04 tok/s=12486
[train] step=6780 tokens=111.1M loss=2.8094 lr=2.99e-04 tok/s=12486
[train] step=6790 tokens=111.2M loss=2.6128 lr=2.99e-04 tok/s=12486
[train] step=6800 tokens=111.4M loss=3.0887 lr=2.99e-04 tok/s=12486
[train] step=6810 tokens=111.6M loss=3.1034 lr=2.99e-04 tok/s=12486
[train] step=6820 tokens=111.7M loss=2.8006 lr=2.99e-04 tok/s=12486
[train] step=6830 tokens=111.9M loss=3.0021 lr=2.99e-04 tok/s=12486
[train] step=6840 tokens=112.1M loss=2.5358 lr=2.99e-04 tok/s=12486
[train] step=6850 tokens=112.2M loss=2.5765 lr=2.99e-04 tok/s=12486
[train] step=6860 tokens=112.4M loss=2.5908 lr=2.99e-04 tok/s=12486
[train] step=6870 tokens=112.6M loss=2.4794 lr=2.99e-04 tok/s=12486
```
