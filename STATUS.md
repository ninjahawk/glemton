# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 00:07:08 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1239M / 3000M (41.3%) |
| Step | 75640 |
| Latest loss | 2.4213 |
| Avg loss (last 30 logged) | 2.2033 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 15:10:13 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.32 -> 2.10 -> 2.11 -> 2.06 -> 2.38 -> 2.08 -> 1.80 -> 2.39 -> 2.28 -> 2.30 -> 2.14 -> 2.58

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] step=75530 tokens=1237.5M loss=2.1106 lr=2.04e-04 tok/s=12486
[train] step=75540 tokens=1237.6M loss=1.9657 lr=2.04e-04 tok/s=12486
[train] step=75550 tokens=1237.8M loss=2.3277 lr=2.04e-04 tok/s=12486
[train] step=75560 tokens=1238.0M loss=2.4166 lr=2.04e-04 tok/s=12486
[train] step=75570 tokens=1238.1M loss=2.5391 lr=2.04e-04 tok/s=12486
[train] step=75580 tokens=1238.3M loss=2.2788 lr=2.04e-04 tok/s=12486
[train] step=75590 tokens=1238.5M loss=2.1746 lr=2.04e-04 tok/s=12486
[train] step=75600 tokens=1238.6M loss=2.3625 lr=2.04e-04 tok/s=12486
[train] step=75610 tokens=1238.8M loss=2.0486 lr=2.03e-04 tok/s=12486
[train] step=75620 tokens=1239.0M loss=2.5772 lr=2.03e-04 tok/s=12486
[train] step=75630 tokens=1239.1M loss=2.4522 lr=2.03e-04 tok/s=12486
[train] step=75640 tokens=1239.3M loss=2.4213 lr=2.03e-04 tok/s=12486
```
