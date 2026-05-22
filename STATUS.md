# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 19:56:30 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1052M / 3000M (35.0%) |
| Step | 64180 |
| Latest loss | 2.4551 |
| Avg loss (last 30 logged) | 2.2634 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 19:20:54 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.53 -> 2.04 -> 2.14 -> 1.96 -> 2.15 -> 2.21 -> 2.33 -> 2.18 -> 2.12 -> 2.65 -> 2.41 -> 2.22

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`

## Recent log tail
```
[train] step=64070 tokens=1049.7M loss=2.1513 lr=2.28e-04 tok/s=12486
[train] step=64080 tokens=1049.9M loss=2.1897 lr=2.28e-04 tok/s=12486
[train] step=64090 tokens=1050.1M loss=2.2223 lr=2.28e-04 tok/s=12486
[train] step=64100 tokens=1050.2M loss=2.2458 lr=2.28e-04 tok/s=12486
[train] step=64110 tokens=1050.4M loss=2.0756 lr=2.28e-04 tok/s=12486
[train] step=64120 tokens=1050.5M loss=2.1643 lr=2.28e-04 tok/s=12486
[train] step=64130 tokens=1050.7M loss=2.2618 lr=2.28e-04 tok/s=12486
[train] step=64140 tokens=1050.9M loss=2.4008 lr=2.28e-04 tok/s=12486
[train] step=64150 tokens=1051.0M loss=1.8961 lr=2.28e-04 tok/s=12486
[train] step=64160 tokens=1051.2M loss=2.2219 lr=2.28e-04 tok/s=12486
[train] step=64170 tokens=1051.4M loss=2.1297 lr=2.28e-04 tok/s=12486
[train] step=64180 tokens=1051.5M loss=2.4551 lr=2.28e-04 tok/s=12486
```
