# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 04:03:55 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 338M / 3000M (11.3%) |
| Step | 20630 |
| Latest loss | 2.5254 |
| Avg loss (last 30 logged) | 2.4814 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 2 days, 11:12:44 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.72 -> 2.70 -> 2.40 -> 2.36 -> 2.30 -> 2.26 -> 2.43 -> 2.64 -> 2.55 -> 2.44 -> 2.44 -> 2.45

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=20520 tokens=336.2M loss=2.6875 lr=2.93e-04 tok/s=12488
[train] step=20530 tokens=336.4M loss=2.4375 lr=2.93e-04 tok/s=12488
[train] step=20540 tokens=336.5M loss=2.3518 lr=2.93e-04 tok/s=12488
[train] step=20550 tokens=336.7M loss=2.6459 lr=2.93e-04 tok/s=12488
[train] step=20560 tokens=336.9M loss=3.1487 lr=2.93e-04 tok/s=12488
[train] step=20570 tokens=337.0M loss=2.5918 lr=2.93e-04 tok/s=12488
[train] step=20580 tokens=337.2M loss=2.2730 lr=2.93e-04 tok/s=12488
[train] step=20590 tokens=337.3M loss=2.2380 lr=2.93e-04 tok/s=12488
[train] step=20600 tokens=337.5M loss=2.6898 lr=2.93e-04 tok/s=12488
[train] step=20610 tokens=337.7M loss=2.4464 lr=2.93e-04 tok/s=12488
[train] step=20620 tokens=337.8M loss=2.5038 lr=2.93e-04 tok/s=12488
[train] step=20630 tokens=338.0M loss=2.5254 lr=2.93e-04 tok/s=12488
```
