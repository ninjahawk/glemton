# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 23:47:05 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1224M / 3000M (40.8%) |
| Step | 74730 |
| Latest loss | 2.1916 |
| Avg loss (last 30 logged) | 2.1973 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 15:30:07 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.04 -> 1.95 -> 2.57 -> 2.10 -> 2.36 -> 1.91 -> 2.23 -> 2.27 -> 2.44 -> 2.46 -> 2.33 -> 2.17

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] step=74620 tokens=1222.6M loss=2.5089 lr=2.06e-04 tok/s=12486
[train] step=74630 tokens=1222.7M loss=2.2771 lr=2.06e-04 tok/s=12486
[train] step=74640 tokens=1222.9M loss=2.1373 lr=2.06e-04 tok/s=12486
[train] step=74650 tokens=1223.1M loss=1.7786 lr=2.06e-04 tok/s=12486
[train] step=74660 tokens=1223.2M loss=2.4347 lr=2.06e-04 tok/s=12486
[train] step=74670 tokens=1223.4M loss=1.9409 lr=2.06e-04 tok/s=12486
[train] step=74680 tokens=1223.6M loss=2.3945 lr=2.06e-04 tok/s=12486
[train] step=74690 tokens=1223.7M loss=2.2486 lr=2.06e-04 tok/s=12486
[train] step=74700 tokens=1223.9M loss=2.1956 lr=2.06e-04 tok/s=12486
[train] step=74710 tokens=1224.0M loss=2.1667 lr=2.05e-04 tok/s=12486
[train] step=74720 tokens=1224.2M loss=2.0554 lr=2.05e-04 tok/s=12486
[train] step=74730 tokens=1224.4M loss=2.1916 lr=2.05e-04 tok/s=12486
```
