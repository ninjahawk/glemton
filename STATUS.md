# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 22:06:50 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1149M / 3000M (38.3%) |
| Step | 70140 |
| Latest loss | 2.1584 |
| Avg loss (last 30 logged) | 2.1823 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 17:10:30 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.66 -> 2.11 -> 2.19 -> 2.61 -> 2.24 -> 2.12 -> 2.79 -> 2.56 -> 2.35 -> 2.43 -> 2.48 -> 2.21

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`

## Recent log tail
```
[train] step=70030 tokens=1147.4M loss=1.8752 lr=2.16e-04 tok/s=12486
[train] step=70040 tokens=1147.5M loss=2.1691 lr=2.16e-04 tok/s=12486
[train] step=70050 tokens=1147.7M loss=2.2754 lr=2.16e-04 tok/s=12486
[train] step=70060 tokens=1147.9M loss=2.3409 lr=2.16e-04 tok/s=12486
[train] step=70070 tokens=1148.0M loss=2.0832 lr=2.16e-04 tok/s=12486
[train] step=70080 tokens=1148.2M loss=2.1432 lr=2.16e-04 tok/s=12486
[train] step=70090 tokens=1148.4M loss=2.2104 lr=2.16e-04 tok/s=12486
[train] step=70100 tokens=1148.5M loss=2.3148 lr=2.16e-04 tok/s=12486
[train] step=70110 tokens=1148.7M loss=2.2229 lr=2.16e-04 tok/s=12486
[train] step=70120 tokens=1148.8M loss=2.2093 lr=2.16e-04 tok/s=12486
[train] step=70130 tokens=1149.0M loss=2.6609 lr=2.16e-04 tok/s=12486
[train] step=70140 tokens=1149.2M loss=2.1584 lr=2.16e-04 tok/s=12486
```
