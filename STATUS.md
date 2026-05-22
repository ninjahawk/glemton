# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 18:36:17 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 991M / 3000M (33.0%) |
| Step | 60510 |
| Latest loss | 2.3722 |
| Avg loss (last 30 logged) | 2.2305 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 20:41:21 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.25 -> 2.11 -> 2.28 -> 2.13 -> 2.15 -> 2.13 -> 2.16 -> 2.37 -> 1.96 -> 2.64 -> 1.98 -> 2.11

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=60400 tokens=989.6M loss=1.9904 lr=2.36e-04 tok/s=12485
[train] step=60410 tokens=989.8M loss=2.1663 lr=2.36e-04 tok/s=12485
[train] step=60420 tokens=989.9M loss=1.7563 lr=2.36e-04 tok/s=12485
[train] step=60430 tokens=990.1M loss=2.6308 lr=2.36e-04 tok/s=12485
[train] step=60440 tokens=990.2M loss=2.2128 lr=2.36e-04 tok/s=12485
[train] step=60450 tokens=990.4M loss=2.3911 lr=2.36e-04 tok/s=12485
[train] step=60460 tokens=990.6M loss=2.1487 lr=2.36e-04 tok/s=12485
[train] step=60470 tokens=990.7M loss=2.2877 lr=2.36e-04 tok/s=12485
[train] step=60480 tokens=990.9M loss=2.1082 lr=2.36e-04 tok/s=12485
[train] step=60490 tokens=991.1M loss=2.3192 lr=2.36e-04 tok/s=12485
[train] step=60500 tokens=991.2M loss=2.1274 lr=2.36e-04 tok/s=12485
[train] step=60510 tokens=991.4M loss=2.3722 lr=2.36e-04 tok/s=12485
```
