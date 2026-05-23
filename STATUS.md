# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 01:57:25 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1322M / 3000M (44.1%) |
| Step | 80690 |
| Latest loss | 2.2035 |
| Avg loss (last 30 logged) | 2.2660 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 13:19:39 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.43 -> 2.42 -> 1.90 -> 2.00 -> 2.08 -> 1.89 -> 1.88 -> 2.24 -> 2.08 -> 2.00 -> 2.19 -> 2.63

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`

## Recent log tail
```
[train] step=80580 tokens=1320.2M loss=2.2300 lr=1.92e-04 tok/s=12487
[train] step=80590 tokens=1320.4M loss=2.2900 lr=1.92e-04 tok/s=12487
[train] step=80600 tokens=1320.6M loss=2.1551 lr=1.92e-04 tok/s=12487
[train] step=80610 tokens=1320.7M loss=2.6826 lr=1.92e-04 tok/s=12487
[train] step=80620 tokens=1320.9M loss=1.9055 lr=1.92e-04 tok/s=12487
[train] step=80630 tokens=1321.0M loss=2.4866 lr=1.92e-04 tok/s=12487
[train] step=80640 tokens=1321.2M loss=2.2421 lr=1.92e-04 tok/s=12487
[train] step=80650 tokens=1321.4M loss=2.1401 lr=1.92e-04 tok/s=12487
[train] step=80660 tokens=1321.5M loss=2.9309 lr=1.92e-04 tok/s=12487
[train] step=80670 tokens=1321.7M loss=2.6290 lr=1.92e-04 tok/s=12487
[train] step=80680 tokens=1321.9M loss=1.9381 lr=1.92e-04 tok/s=12487
[train] step=80690 tokens=1322.0M loss=2.2035 lr=1.92e-04 tok/s=12487
```
