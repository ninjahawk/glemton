# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 20:46:37 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1089M / 3000M (36.3%) |
| Step | 66470 |
| Latest loss | 2.9233 |
| Avg loss (last 30 logged) | 2.1883 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 18:30:51 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.38 -> 2.37 -> 2.20 -> 2.23 -> 2.26 -> 2.18 -> 2.47 -> 2.31 -> 1.93 -> 2.55 -> 2.37 -> 2.10

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`

## Recent log tail
```
[train] step=66360 tokens=1087.2M loss=1.9155 lr=2.24e-04 tok/s=12486
[train] step=66370 tokens=1087.4M loss=2.1161 lr=2.24e-04 tok/s=12486
[train] step=66380 tokens=1087.6M loss=1.9333 lr=2.24e-04 tok/s=12486
[train] step=66390 tokens=1087.7M loss=2.2518 lr=2.24e-04 tok/s=12486
[train] step=66400 tokens=1087.9M loss=2.1238 lr=2.24e-04 tok/s=12486
[train] step=66410 tokens=1088.1M loss=2.0108 lr=2.24e-04 tok/s=12486
[train] step=66420 tokens=1088.2M loss=2.4030 lr=2.23e-04 tok/s=12486
[train] step=66430 tokens=1088.4M loss=2.1041 lr=2.23e-04 tok/s=12486
[train] step=66440 tokens=1088.6M loss=2.1019 lr=2.23e-04 tok/s=12486
[train] step=66450 tokens=1088.7M loss=2.0431 lr=2.23e-04 tok/s=12486
[train] step=66460 tokens=1088.9M loss=2.1898 lr=2.23e-04 tok/s=12486
[train] step=66470 tokens=1089.0M loss=2.9233 lr=2.23e-04 tok/s=12486
```
