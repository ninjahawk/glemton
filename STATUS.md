# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 15:35:48 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 856M / 3000M (28.5%) |
| Step | 52250 |
| Latest loss | 1.9073 |
| Avg loss (last 30 logged) | 2.3030 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1 day, 23:42:11 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.46 -> 2.44 -> 2.50 -> 2.45 -> 2.30 -> 2.67 -> 2.28 -> 2.66 -> 2.15 -> 2.30 -> 2.39 -> 2.02

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`

## Recent log tail
```
[train] step=52140 tokens=854.3M loss=1.9147 lr=2.51e-04 tok/s=12484
[train] step=52150 tokens=854.4M loss=2.1463 lr=2.51e-04 tok/s=12484
[train] step=52160 tokens=854.6M loss=2.0812 lr=2.51e-04 tok/s=12484
[train] step=52170 tokens=854.8M loss=2.5327 lr=2.51e-04 tok/s=12484
[train] step=52180 tokens=854.9M loss=1.9253 lr=2.51e-04 tok/s=12484
[train] step=52190 tokens=855.1M loss=2.9770 lr=2.51e-04 tok/s=12484
[train] step=52200 tokens=855.2M loss=2.5594 lr=2.51e-04 tok/s=12484
[train] step=52210 tokens=855.4M loss=2.2135 lr=2.51e-04 tok/s=12484
[train] step=52220 tokens=855.6M loss=2.0563 lr=2.51e-04 tok/s=12484
[train] step=52230 tokens=855.7M loss=2.0231 lr=2.51e-04 tok/s=12484
[train] step=52240 tokens=855.9M loss=2.6052 lr=2.51e-04 tok/s=12484
[train] step=52250 tokens=856.1M loss=1.9073 lr=2.51e-04 tok/s=12484
```
