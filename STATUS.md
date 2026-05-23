# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 22:36:54 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1172M / 3000M (39.1%) |
| Step | 71520 |
| Latest loss | 2.3100 |
| Avg loss (last 30 logged) | 2.1714 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 16:40:19 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.64 -> 2.15 -> 2.00 -> 2.33 -> 1.94 -> 2.34 -> 2.20 -> 2.23 -> 2.60 -> 2.06 -> 2.29 -> 2.04

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`

## Recent log tail
```
[train] step=71410 tokens=1170.0M loss=1.9470 lr=2.13e-04 tok/s=12486
[train] step=71420 tokens=1170.1M loss=2.2415 lr=2.13e-04 tok/s=12486
[train] step=71430 tokens=1170.3M loss=2.1755 lr=2.13e-04 tok/s=12486
[train] step=71440 tokens=1170.5M loss=1.8160 lr=2.13e-04 tok/s=12486
[train] step=71450 tokens=1170.6M loss=2.3335 lr=2.13e-04 tok/s=12486
[train] step=71460 tokens=1170.8M loss=2.1113 lr=2.13e-04 tok/s=12486
[train] step=71470 tokens=1171.0M loss=2.3079 lr=2.13e-04 tok/s=12486
[train] step=71480 tokens=1171.1M loss=1.9054 lr=2.13e-04 tok/s=12486
[train] step=71490 tokens=1171.3M loss=2.0405 lr=2.13e-04 tok/s=12486
[train] step=71500 tokens=1171.5M loss=2.0548 lr=2.13e-04 tok/s=12486
[train] step=71510 tokens=1171.6M loss=2.5567 lr=2.13e-04 tok/s=12486
[train] step=71520 tokens=1171.8M loss=2.3100 lr=2.13e-04 tok/s=12486
```
