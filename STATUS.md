# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 16:15:55 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 886M / 3000M (29.5%) |
| Step | 54090 |
| Latest loss | 2.0065 |
| Avg loss (last 30 logged) | 2.3569 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1 day, 23:02:00 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.41 -> 2.34 -> 2.21 -> 2.78 -> 2.70 -> 2.47 -> 2.43 -> 2.27 -> 2.59 -> 2.17 -> 2.46 -> 2.42

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`

## Recent log tail
```
[train] step=53980 tokens=884.4M loss=2.5556 lr=2.48e-04 tok/s=12484
[train] step=53990 tokens=884.6M loss=2.4869 lr=2.48e-04 tok/s=12484
[train] step=54000 tokens=884.7M loss=2.3068 lr=2.48e-04 tok/s=12484
[train] step=54010 tokens=884.9M loss=2.7228 lr=2.48e-04 tok/s=12484
[train] step=54020 tokens=885.1M loss=2.2852 lr=2.48e-04 tok/s=12484
[train] step=54030 tokens=885.2M loss=2.4327 lr=2.48e-04 tok/s=12484
[train] step=54040 tokens=885.4M loss=2.1416 lr=2.48e-04 tok/s=12484
[train] step=54050 tokens=885.6M loss=2.0925 lr=2.48e-04 tok/s=12485
[train] step=54060 tokens=885.7M loss=2.4208 lr=2.48e-04 tok/s=12484
[train] step=54070 tokens=885.9M loss=2.2679 lr=2.48e-04 tok/s=12484
[train] step=54080 tokens=886.0M loss=2.8607 lr=2.48e-04 tok/s=12484
[train] step=54090 tokens=886.2M loss=2.0065 lr=2.48e-04 tok/s=12484
```
