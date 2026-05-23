# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 21:36:45 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1127M / 3000M (37.6%) |
| Step | 68760 |
| Latest loss | 2.0489 |
| Avg loss (last 30 logged) | 2.3108 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 17:40:40 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.69 -> 2.54 -> 2.46 -> 2.00 -> 2.10 -> 1.91 -> 2.19 -> 2.13 -> 2.49 -> 1.95 -> 1.99 -> 2.22

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`

## Recent log tail
```
[train] step=68650 tokens=1124.8M loss=2.3121 lr=2.19e-04 tok/s=12486
[train] step=68660 tokens=1124.9M loss=2.1110 lr=2.19e-04 tok/s=12486
[train] step=68670 tokens=1125.1M loss=2.2410 lr=2.19e-04 tok/s=12486
[train] step=68680 tokens=1125.3M loss=2.1982 lr=2.19e-04 tok/s=12486
[train] step=68690 tokens=1125.4M loss=2.0857 lr=2.19e-04 tok/s=12486
[train] step=68700 tokens=1125.6M loss=2.2581 lr=2.19e-04 tok/s=12486
[train] step=68710 tokens=1125.7M loss=2.6981 lr=2.19e-04 tok/s=12486
[train] step=68720 tokens=1125.9M loss=2.1080 lr=2.19e-04 tok/s=12486
[train] step=68730 tokens=1126.1M loss=2.7927 lr=2.19e-04 tok/s=12486
[train] step=68740 tokens=1126.2M loss=2.2230 lr=2.19e-04 tok/s=12486
[train] step=68750 tokens=1126.4M loss=2.5631 lr=2.19e-04 tok/s=12486
[train] step=68760 tokens=1126.6M loss=2.0489 lr=2.19e-04 tok/s=12486
```
