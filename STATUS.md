# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 06:38:08 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1532M / 3000M (51.1%) |
| Step | 93530 |
| Latest loss | 2.0057 |
| Avg loss (last 30 logged) | 2.1622 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 8:38:40 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.97 -> 1.88 -> 2.21 -> 2.17 -> 1.92 -> 2.54 -> 2.33 -> 1.92 -> 2.09 -> 2.66 -> 2.19 -> 2.14

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=93420 tokens=1530.6M loss=2.6084 lr=1.62e-04 tok/s=12488
[train] step=93430 tokens=1530.8M loss=1.8630 lr=1.62e-04 tok/s=12488
[train] step=93440 tokens=1530.9M loss=2.4481 lr=1.62e-04 tok/s=12488
[train] step=93450 tokens=1531.1M loss=2.4626 lr=1.62e-04 tok/s=12488
[train] step=93460 tokens=1531.2M loss=2.2506 lr=1.62e-04 tok/s=12488
[train] step=93470 tokens=1531.4M loss=2.0265 lr=1.62e-04 tok/s=12488
[train] step=93480 tokens=1531.6M loss=2.0138 lr=1.62e-04 tok/s=12488
[train] step=93490 tokens=1531.7M loss=1.9669 lr=1.62e-04 tok/s=12488
[train] step=93500 tokens=1531.9M loss=2.1119 lr=1.62e-04 tok/s=12488
[train] step=93510 tokens=1532.1M loss=2.1415 lr=1.62e-04 tok/s=12488
[train] step=93520 tokens=1532.2M loss=2.0234 lr=1.62e-04 tok/s=12488
[train] step=93530 tokens=1532.4M loss=2.0057 lr=1.62e-04 tok/s=12488
```
