# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 06:08:03 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1510M / 3000M (50.3%) |
| Step | 92160 |
| Latest loss | 2.1461 |
| Avg loss (last 30 logged) | 2.0894 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 9:08:42 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.51 -> 2.44 -> 1.94 -> 2.57 -> 2.42 -> 1.93 -> 2.20 -> 2.59 -> 1.98 -> 2.36 -> 2.04 -> 2.42

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=92050 tokens=1508.1M loss=2.3164 lr=1.66e-04 tok/s=12488
[train] step=92060 tokens=1508.3M loss=1.8602 lr=1.66e-04 tok/s=12488
[train] step=92070 tokens=1508.5M loss=2.3073 lr=1.66e-04 tok/s=12488
[train] step=92080 tokens=1508.6M loss=1.8472 lr=1.66e-04 tok/s=12488
[train] step=92090 tokens=1508.8M loss=2.0737 lr=1.66e-04 tok/s=12488
[train] step=92100 tokens=1509.0M loss=2.0984 lr=1.66e-04 tok/s=12488
[train] step=92110 tokens=1509.1M loss=2.3231 lr=1.65e-04 tok/s=12488
[train] step=92120 tokens=1509.3M loss=2.0413 lr=1.65e-04 tok/s=12488
[train] step=92130 tokens=1509.5M loss=2.2618 lr=1.65e-04 tok/s=12488
[train] step=92140 tokens=1509.6M loss=2.4250 lr=1.65e-04 tok/s=12488
[train] step=92150 tokens=1509.8M loss=1.9549 lr=1.65e-04 tok/s=12488
[train] step=92160 tokens=1509.9M loss=2.1461 lr=1.65e-04 tok/s=12488
```
