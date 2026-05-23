# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 22:16:51 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1157M / 3000M (38.6%) |
| Step | 70600 |
| Latest loss | 2.0777 |
| Avg loss (last 30 logged) | 2.1629 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 17:00:29 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.39 -> 2.36 -> 2.19 -> 2.00 -> 2.37 -> 2.15 -> 2.50 -> 2.02 -> 2.27 -> 2.23 -> 2.28 -> 2.66

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`

## Recent log tail
```
[train] step=70490 tokens=1154.9M loss=2.1329 lr=2.15e-04 tok/s=12486
[train] step=70500 tokens=1155.1M loss=2.5973 lr=2.15e-04 tok/s=12486
[train] step=70510 tokens=1155.2M loss=1.8564 lr=2.15e-04 tok/s=12486
[train] step=70520 tokens=1155.4M loss=1.9730 lr=2.15e-04 tok/s=12486
[train] step=70530 tokens=1155.6M loss=2.1772 lr=2.15e-04 tok/s=12486
[train] step=70540 tokens=1155.7M loss=2.2613 lr=2.15e-04 tok/s=12486
[train] step=70550 tokens=1155.9M loss=2.2260 lr=2.15e-04 tok/s=12486
[train] step=70560 tokens=1156.1M loss=2.2350 lr=2.15e-04 tok/s=12486
[train] step=70570 tokens=1156.2M loss=2.1558 lr=2.15e-04 tok/s=12486
[train] step=70580 tokens=1156.4M loss=2.6568 lr=2.15e-04 tok/s=12486
[train] step=70590 tokens=1156.5M loss=2.4615 lr=2.15e-04 tok/s=12486
[train] step=70600 tokens=1156.7M loss=2.0777 lr=2.15e-04 tok/s=12486
```
