# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 04:27:48 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1435M / 3000M (47.8%) |
| Step | 87570 |
| Latest loss | 2.0461 |
| Avg loss (last 30 logged) | 2.0976 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 10:49:14 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.84 -> 2.92 -> 1.60 -> 2.10 -> 2.00 -> 1.82 -> 2.74 -> 1.83 -> 1.78 -> 2.11 -> 2.03 -> 1.81

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`

## Recent log tail
```
[train] step=87460 tokens=1432.9M loss=2.3972 lr=1.76e-04 tok/s=12487
[train] step=87470 tokens=1433.1M loss=2.4646 lr=1.76e-04 tok/s=12487
[train] step=87480 tokens=1433.3M loss=1.8051 lr=1.76e-04 tok/s=12487
[train] step=87490 tokens=1433.4M loss=2.0125 lr=1.76e-04 tok/s=12487
[train] step=87500 tokens=1433.6M loss=2.3129 lr=1.76e-04 tok/s=12487
[train] step=87510 tokens=1433.8M loss=1.8075 lr=1.76e-04 tok/s=12487
[train] step=87520 tokens=1433.9M loss=2.1017 lr=1.76e-04 tok/s=12487
[train] step=87530 tokens=1434.1M loss=2.4452 lr=1.76e-04 tok/s=12487
[train] step=87540 tokens=1434.3M loss=2.0172 lr=1.76e-04 tok/s=12487
[train] step=87550 tokens=1434.4M loss=1.8127 lr=1.76e-04 tok/s=12487
[train] step=87560 tokens=1434.6M loss=1.9914 lr=1.76e-04 tok/s=12487
[train] step=87570 tokens=1434.7M loss=2.0461 lr=1.76e-04 tok/s=12487
```
