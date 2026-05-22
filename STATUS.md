# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 18:26:15 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 984M / 3000M (32.8%) |
| Step | 60050 |
| Latest loss | 2.4238 |
| Avg loss (last 30 logged) | 2.3239 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 20:51:21 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.99 -> 2.56 -> 1.92 -> 2.47 -> 2.09 -> 2.04 -> 2.19 -> 2.52 -> 2.28 -> 2.23 -> 2.46 -> 2.15

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=59940 tokens=982.1M loss=2.1724 lr=2.37e-04 tok/s=12485
[train] step=59950 tokens=982.2M loss=2.6204 lr=2.37e-04 tok/s=12485
[train] step=59960 tokens=982.4M loss=2.4336 lr=2.37e-04 tok/s=12485
[train] step=59970 tokens=982.5M loss=2.0027 lr=2.37e-04 tok/s=12485
[train] step=59980 tokens=982.7M loss=2.2111 lr=2.37e-04 tok/s=12485
[train] step=59990 tokens=982.9M loss=2.5350 lr=2.37e-04 tok/s=12485
[train] step=60000 tokens=983.0M loss=2.6332 lr=2.37e-04 tok/s=12485
[train] step=60010 tokens=983.2M loss=2.2540 lr=2.37e-04 tok/s=12485
[train] step=60020 tokens=983.4M loss=2.1535 lr=2.37e-04 tok/s=12485
[train] step=60030 tokens=983.5M loss=2.6539 lr=2.37e-04 tok/s=12485
[train] step=60040 tokens=983.7M loss=2.1637 lr=2.37e-04 tok/s=12485
[train] step=60050 tokens=983.9M loss=2.4238 lr=2.37e-04 tok/s=12485
```
