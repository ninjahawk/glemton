# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 05:37:58 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1487M / 3000M (49.6%) |
| Step | 90780 |
| Latest loss | 1.9926 |
| Avg loss (last 30 logged) | 2.1435 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 9:38:52 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.67 -> 2.18 -> 2.46 -> 2.19 -> 1.75 -> 1.99 -> 1.78 -> 2.09 -> 1.97 -> 2.07 -> 2.26 -> 2.12

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`

## Recent log tail
```
[train] step=90670 tokens=1485.5M loss=2.1374 lr=1.69e-04 tok/s=12488
[train] step=90680 tokens=1485.7M loss=1.7837 lr=1.69e-04 tok/s=12488
[train] step=90690 tokens=1485.9M loss=2.5153 lr=1.69e-04 tok/s=12488
[train] step=90700 tokens=1486.0M loss=2.1111 lr=1.69e-04 tok/s=12488
[train] step=90710 tokens=1486.2M loss=1.8559 lr=1.69e-04 tok/s=12488
[train] step=90720 tokens=1486.4M loss=2.4692 lr=1.69e-04 tok/s=12488
[train] step=90730 tokens=1486.5M loss=2.3727 lr=1.69e-04 tok/s=12488
[train] step=90740 tokens=1486.7M loss=2.2771 lr=1.69e-04 tok/s=12488
[train] step=90750 tokens=1486.8M loss=2.1178 lr=1.69e-04 tok/s=12488
[train] step=90760 tokens=1487.0M loss=1.7809 lr=1.69e-04 tok/s=12488
[train] step=90770 tokens=1487.2M loss=2.6236 lr=1.69e-04 tok/s=12488
[train] step=90780 tokens=1487.3M loss=1.9926 lr=1.69e-04 tok/s=12488
```
