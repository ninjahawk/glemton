# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 16:56:01 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 916M / 3000M (30.5%) |
| Step | 55920 |
| Latest loss | 1.8552 |
| Avg loss (last 30 logged) | 2.2150 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1 day, 22:21:57 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.45 -> 2.45 -> 2.18 -> 2.11 -> 2.20 -> 2.27 -> 2.44 -> 2.67 -> 2.49 -> 2.54 -> 1.93 -> 2.25

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=55810 tokens=914.4M loss=2.5309 lr=2.45e-04 tok/s=12484
[train] step=55820 tokens=914.6M loss=1.8885 lr=2.45e-04 tok/s=12484
[train] step=55830 tokens=914.7M loss=2.2308 lr=2.45e-04 tok/s=12484
[train] step=55840 tokens=914.9M loss=2.0855 lr=2.45e-04 tok/s=12484
[train] step=55850 tokens=915.0M loss=2.2693 lr=2.45e-04 tok/s=12484
[train] step=55860 tokens=915.2M loss=2.1786 lr=2.45e-04 tok/s=12484
[train] step=55870 tokens=915.4M loss=2.3758 lr=2.45e-04 tok/s=12484
[train] step=55880 tokens=915.5M loss=2.0389 lr=2.45e-04 tok/s=12484
[train] step=55890 tokens=915.7M loss=2.2077 lr=2.45e-04 tok/s=12484
[train] step=55900 tokens=915.9M loss=2.2452 lr=2.45e-04 tok/s=12484
[train] step=55910 tokens=916.0M loss=2.0701 lr=2.45e-04 tok/s=12484
[train] step=55920 tokens=916.2M loss=1.8552 lr=2.45e-04 tok/s=12484
```
