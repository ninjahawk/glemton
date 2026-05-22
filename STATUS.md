# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 14:25:40 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 804M / 3000M (26.8%) |
| Step | 49040 |
| Latest loss | 2.2748 |
| Avg loss (last 30 logged) | 2.3442 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 0:52:39 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.68 -> 2.54 -> 2.23 -> 2.33 -> 2.17 -> 2.19 -> 2.17 -> 2.29 -> 2.26 -> 2.37 -> 2.32 -> 2.15

## Checkpoints on disk
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`

## Recent log tail
```
[train] step=48930 tokens=801.7M loss=2.4363 lr=2.57e-04 tok/s=12483
[train] step=48940 tokens=801.8M loss=2.4868 lr=2.57e-04 tok/s=12483
[train] step=48950 tokens=802.0M loss=2.3551 lr=2.57e-04 tok/s=12483
[train] step=48960 tokens=802.2M loss=1.9981 lr=2.57e-04 tok/s=12483
[train] step=48970 tokens=802.3M loss=2.2207 lr=2.57e-04 tok/s=12483
[train] step=48980 tokens=802.5M loss=2.3367 lr=2.57e-04 tok/s=12483
[train] step=48990 tokens=802.7M loss=2.5711 lr=2.57e-04 tok/s=12483
[train] step=49000 tokens=802.8M loss=2.0478 lr=2.57e-04 tok/s=12483
[train] step=49010 tokens=803.0M loss=2.4383 lr=2.57e-04 tok/s=12483
[train] step=49020 tokens=803.1M loss=2.1518 lr=2.57e-04 tok/s=12483
[train] step=49030 tokens=803.3M loss=2.7473 lr=2.57e-04 tok/s=12483
[train] step=49040 tokens=803.5M loss=2.2748 lr=2.57e-04 tok/s=12483
```
