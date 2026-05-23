# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 21:16:42 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1112M / 3000M (37.1%) |
| Step | 67850 |
| Latest loss | 1.9150 |
| Avg loss (last 30 logged) | 2.2948 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 18:00:33 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.38 -> 1.86 -> 2.64 -> 2.14 -> 2.28 -> 2.57 -> 2.38 -> 1.91 -> 2.15 -> 2.15 -> 2.64 -> 2.00

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`

## Recent log tail
```
[train] step=67740 tokens=1109.9M loss=2.3601 lr=2.21e-04 tok/s=12486
[train] step=67750 tokens=1110.0M loss=2.4943 lr=2.21e-04 tok/s=12486
[train] step=67760 tokens=1110.2M loss=1.9960 lr=2.21e-04 tok/s=12486
[train] step=67770 tokens=1110.3M loss=2.7258 lr=2.21e-04 tok/s=12486
[train] step=67780 tokens=1110.5M loss=2.7475 lr=2.21e-04 tok/s=12486
[train] step=67790 tokens=1110.7M loss=2.3436 lr=2.21e-04 tok/s=12486
[train] step=67800 tokens=1110.8M loss=2.1535 lr=2.21e-04 tok/s=12486
[train] step=67810 tokens=1111.0M loss=2.2427 lr=2.21e-04 tok/s=12486
[train] step=67820 tokens=1111.2M loss=2.2286 lr=2.21e-04 tok/s=12486
[train] step=67830 tokens=1111.3M loss=2.0032 lr=2.20e-04 tok/s=12486
[train] step=67840 tokens=1111.5M loss=2.1624 lr=2.20e-04 tok/s=12486
[train] step=67850 tokens=1111.7M loss=1.9150 lr=2.20e-04 tok/s=12486
```
