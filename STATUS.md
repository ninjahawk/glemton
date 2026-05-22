# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 07:14:27 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 480M / 3000M (16.0%) |
| Step | 29330 |
| Latest loss | 2.3857 |
| Avg loss (last 30 logged) | 2.4399 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 2 days, 8:03:22 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.45 -> 2.27 -> 2.61 -> 2.32 -> 2.27 -> 2.22 -> 2.40 -> 2.43 -> 2.17 -> 2.49 -> 2.29 -> 2.63

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=29220 tokens=478.7M loss=2.0347 lr=2.85e-04 tok/s=12485
[train] step=29230 tokens=478.9M loss=2.3854 lr=2.85e-04 tok/s=12485
[train] step=29240 tokens=479.1M loss=2.3145 lr=2.85e-04 tok/s=12485
[train] step=29250 tokens=479.2M loss=2.3787 lr=2.85e-04 tok/s=12485
[train] step=29260 tokens=479.4M loss=2.3475 lr=2.85e-04 tok/s=12485
[train] step=29270 tokens=479.6M loss=2.1999 lr=2.85e-04 tok/s=12485
[train] step=29280 tokens=479.7M loss=2.2876 lr=2.85e-04 tok/s=12485
[train] step=29290 tokens=479.9M loss=2.4366 lr=2.85e-04 tok/s=12485
[train] step=29300 tokens=480.1M loss=2.6261 lr=2.85e-04 tok/s=12485
[train] step=29310 tokens=480.2M loss=2.1011 lr=2.85e-04 tok/s=12485
[train] step=29320 tokens=480.4M loss=2.3314 lr=2.85e-04 tok/s=12485
[train] step=29330 tokens=480.5M loss=2.3857 lr=2.85e-04 tok/s=12485
```
