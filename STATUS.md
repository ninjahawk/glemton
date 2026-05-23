# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 21:56:48 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1142M / 3000M (38.1%) |
| Step | 69680 |
| Latest loss | 2.2448 |
| Avg loss (last 30 logged) | 2.2847 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 17:20:38 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.05 -> 1.92 -> 2.45 -> 2.53 -> 2.17 -> 2.34 -> 2.34 -> 1.97 -> 2.24 -> 2.09 -> 2.26 -> 2.19

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`

## Recent log tail
```
[train] step=69570 tokens=1139.8M loss=2.0879 lr=2.17e-04 tok/s=12486
[train] step=69580 tokens=1140.0M loss=2.1980 lr=2.17e-04 tok/s=12486
[train] step=69590 tokens=1140.2M loss=2.2737 lr=2.17e-04 tok/s=12486
[train] step=69600 tokens=1140.3M loss=2.4433 lr=2.17e-04 tok/s=12486
[train] step=69610 tokens=1140.5M loss=2.2072 lr=2.17e-04 tok/s=12486
[train] step=69620 tokens=1140.7M loss=2.0132 lr=2.17e-04 tok/s=12486
[train] step=69630 tokens=1140.8M loss=2.4966 lr=2.17e-04 tok/s=12486
[train] step=69640 tokens=1141.0M loss=2.3532 lr=2.17e-04 tok/s=12486
[train] step=69650 tokens=1141.1M loss=2.2725 lr=2.17e-04 tok/s=12486
[train] step=69660 tokens=1141.3M loss=2.1877 lr=2.17e-04 tok/s=12486
[train] step=69670 tokens=1141.5M loss=2.3128 lr=2.17e-04 tok/s=12486
[train] step=69680 tokens=1141.6M loss=2.2448 lr=2.17e-04 tok/s=12486
```
