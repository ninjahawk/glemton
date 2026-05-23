# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 21:46:47 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1134M / 3000M (37.8%) |
| Step | 69220 |
| Latest loss | 2.1422 |
| Avg loss (last 30 logged) | 2.2084 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 17:30:39 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.97 -> 2.41 -> 2.39 -> 1.98 -> 2.07 -> 2.24 -> 2.18 -> 2.31 -> 2.10 -> 2.22 -> 2.43 -> 1.87

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`

## Recent log tail
```
[train] step=69110 tokens=1132.3M loss=2.2616 lr=2.18e-04 tok/s=12486
[train] step=69120 tokens=1132.5M loss=2.0227 lr=2.18e-04 tok/s=12486
[train] step=69130 tokens=1132.6M loss=2.3509 lr=2.18e-04 tok/s=12486
[train] step=69140 tokens=1132.8M loss=2.4365 lr=2.18e-04 tok/s=12486
[train] step=69150 tokens=1133.0M loss=1.9179 lr=2.18e-04 tok/s=12486
[train] step=69160 tokens=1133.1M loss=2.0676 lr=2.18e-04 tok/s=12486
[train] step=69170 tokens=1133.3M loss=1.9480 lr=2.18e-04 tok/s=12486
[train] step=69180 tokens=1133.4M loss=1.9369 lr=2.18e-04 tok/s=12486
[train] step=69190 tokens=1133.6M loss=2.4431 lr=2.18e-04 tok/s=12486
[train] step=69200 tokens=1133.8M loss=1.8681 lr=2.18e-04 tok/s=12486
[train] step=69210 tokens=1133.9M loss=2.1222 lr=2.18e-04 tok/s=12486
[train] step=69220 tokens=1134.1M loss=2.1422 lr=2.18e-04 tok/s=12486
```
