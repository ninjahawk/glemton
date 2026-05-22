# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 08:24:39 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 533M / 3000M (17.8%) |
| Step | 32540 |
| Latest loss | 2.0730 |
| Avg loss (last 30 logged) | 2.3950 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 6:53:24 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.33 -> 2.03 -> 2.45 -> 2.04 -> 2.57 -> 2.07 -> 2.61 -> 2.45 -> 2.02 -> 2.28 -> 2.50 -> 2.18

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`

## Recent log tail
```
[train] step=32430 tokens=531.3M loss=2.1300 lr=2.81e-04 tok/s=12484
[train] step=32440 tokens=531.5M loss=2.3149 lr=2.81e-04 tok/s=12484
[train] step=32450 tokens=531.7M loss=2.6204 lr=2.81e-04 tok/s=12484
[train] step=32460 tokens=531.8M loss=2.3778 lr=2.81e-04 tok/s=12484
[train] step=32470 tokens=532.0M loss=2.5316 lr=2.81e-04 tok/s=12484
[train] step=32480 tokens=532.2M loss=2.4764 lr=2.81e-04 tok/s=12484
[train] step=32490 tokens=532.3M loss=2.3160 lr=2.81e-04 tok/s=12484
[train] step=32500 tokens=532.5M loss=2.0311 lr=2.81e-04 tok/s=12484
[train] step=32510 tokens=532.6M loss=2.6740 lr=2.81e-04 tok/s=12484
[train] step=32520 tokens=532.8M loss=2.1840 lr=2.81e-04 tok/s=12484
[train] step=32530 tokens=533.0M loss=2.3185 lr=2.81e-04 tok/s=12484
[train] step=32540 tokens=533.1M loss=2.0730 lr=2.81e-04 tok/s=12484
```
