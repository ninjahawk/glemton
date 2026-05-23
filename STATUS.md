# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 07:18:14 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1562M / 3000M (52.1%) |
| Step | 95370 |
| Latest loss | 2.2802 |
| Avg loss (last 30 logged) | 2.1555 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 7:58:30 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.48 -> 2.32 -> 2.22 -> 2.33 -> 2.37 -> 2.32 -> 2.20 -> 2.01 -> 1.82 -> 2.32 -> 2.54 -> 2.22

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=95260 tokens=1560.7M loss=2.7947 lr=1.58e-04 tok/s=12488
[train] step=95270 tokens=1560.9M loss=1.7549 lr=1.58e-04 tok/s=12488
[train] step=95280 tokens=1561.1M loss=2.4010 lr=1.58e-04 tok/s=12488
[train] step=95290 tokens=1561.2M loss=1.8908 lr=1.58e-04 tok/s=12488
[train] step=95300 tokens=1561.4M loss=2.2491 lr=1.58e-04 tok/s=12488
[train] step=95310 tokens=1561.6M loss=1.9320 lr=1.58e-04 tok/s=12488
[train] step=95320 tokens=1561.7M loss=1.7084 lr=1.58e-04 tok/s=12488
[train] step=95330 tokens=1561.9M loss=1.7972 lr=1.58e-04 tok/s=12488
[train] step=95340 tokens=1562.1M loss=2.4307 lr=1.58e-04 tok/s=12488
[train] step=95350 tokens=1562.2M loss=2.2187 lr=1.58e-04 tok/s=12488
[train] step=95360 tokens=1562.4M loss=2.5062 lr=1.58e-04 tok/s=12488
[train] step=95370 tokens=1562.5M loss=2.2802 lr=1.58e-04 tok/s=12488
```
