# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 23:57:07 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1232M / 3000M (41.1%) |
| Step | 75180 |
| Latest loss | 2.1320 |
| Avg loss (last 30 logged) | 2.2303 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 15:20:22 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.77 -> 2.13 -> 2.31 -> 2.26 -> 2.08 -> 2.25 -> 2.05 -> 2.17 -> 2.19 -> 2.22 -> 2.39 -> 2.17

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] step=75070 tokens=1229.9M loss=2.2487 lr=2.05e-04 tok/s=12486
[train] step=75080 tokens=1230.1M loss=1.9940 lr=2.05e-04 tok/s=12486
[train] step=75090 tokens=1230.3M loss=2.6098 lr=2.05e-04 tok/s=12486
[train] step=75100 tokens=1230.4M loss=2.6209 lr=2.05e-04 tok/s=12486
[train] step=75110 tokens=1230.6M loss=2.1439 lr=2.05e-04 tok/s=12486
[train] step=75120 tokens=1230.8M loss=2.2893 lr=2.05e-04 tok/s=12486
[train] step=75130 tokens=1230.9M loss=2.3349 lr=2.05e-04 tok/s=12486
[train] step=75140 tokens=1231.1M loss=2.1112 lr=2.05e-04 tok/s=12486
[train] step=75150 tokens=1231.3M loss=2.2294 lr=2.05e-04 tok/s=12486
[train] step=75160 tokens=1231.4M loss=2.1694 lr=2.04e-04 tok/s=12486
[train] step=75170 tokens=1231.6M loss=2.1496 lr=2.04e-04 tok/s=12486
[train] step=75180 tokens=1231.7M loss=2.1320 lr=2.04e-04 tok/s=12486
```
