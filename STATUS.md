# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 14:45:40 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 818M / 3000M (27.3%) |
| Step | 49960 |
| Latest loss | 2.3456 |
| Avg loss (last 30 logged) | 2.2820 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 0:32:23 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.25 -> 2.86 -> 2.30 -> 2.51 -> 2.58 -> 2.86 -> 2.35 -> 1.99 -> 2.36 -> 2.07 -> 2.79 -> 2.08

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`

## Recent log tail
```
[train] step=49850 tokens=816.7M loss=2.1868 lr=2.56e-04 tok/s=12484
[train] step=49860 tokens=816.9M loss=2.3785 lr=2.55e-04 tok/s=12484
[train] step=49870 tokens=817.1M loss=2.6321 lr=2.55e-04 tok/s=12484
[train] step=49880 tokens=817.2M loss=2.4128 lr=2.55e-04 tok/s=12484
[train] step=49890 tokens=817.4M loss=2.1519 lr=2.55e-04 tok/s=12484
[train] step=49900 tokens=817.6M loss=2.2556 lr=2.55e-04 tok/s=12484
[train] step=49910 tokens=817.7M loss=2.3070 lr=2.55e-04 tok/s=12484
[train] step=49920 tokens=817.9M loss=2.2955 lr=2.55e-04 tok/s=12484
[train] step=49930 tokens=818.1M loss=2.3102 lr=2.55e-04 tok/s=12484
[train] step=49940 tokens=818.2M loss=2.0750 lr=2.55e-04 tok/s=12484
[train] step=49950 tokens=818.4M loss=1.8962 lr=2.55e-04 tok/s=12484
[train] step=49960 tokens=818.5M loss=2.3456 lr=2.55e-04 tok/s=12484
```
