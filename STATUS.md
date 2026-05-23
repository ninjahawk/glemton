# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 20:36:36 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1082M / 3000M (36.0%) |
| Step | 66010 |
| Latest loss | 2.1468 |
| Avg loss (last 30 logged) | 2.3149 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 18:40:52 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.05 -> 2.21 -> 2.14 -> 2.22 -> 2.51 -> 2.18 -> 2.03 -> 2.09 -> 2.03 -> 2.08 -> 2.17 -> 2.25

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`

## Recent log tail
```
[train] step=65900 tokens=1079.7M loss=2.4093 lr=2.25e-04 tok/s=12486
[train] step=65910 tokens=1079.9M loss=2.0952 lr=2.25e-04 tok/s=12486
[train] step=65920 tokens=1080.0M loss=2.1040 lr=2.25e-04 tok/s=12486
[train] step=65930 tokens=1080.2M loss=2.1033 lr=2.25e-04 tok/s=12486
[train] step=65940 tokens=1080.4M loss=2.7114 lr=2.24e-04 tok/s=12486
[train] step=65950 tokens=1080.5M loss=2.4811 lr=2.24e-04 tok/s=12486
[train] step=65960 tokens=1080.7M loss=2.5594 lr=2.24e-04 tok/s=12486
[train] step=65970 tokens=1080.9M loss=2.2645 lr=2.24e-04 tok/s=12486
[train] step=65980 tokens=1081.0M loss=2.2473 lr=2.24e-04 tok/s=12486
[train] step=65990 tokens=1081.2M loss=2.2097 lr=2.24e-04 tok/s=12486
[train] step=66000 tokens=1081.3M loss=2.0637 lr=2.24e-04 tok/s=12486
[train] step=66010 tokens=1081.5M loss=2.1468 lr=2.24e-04 tok/s=12486
```
