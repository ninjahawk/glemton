# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 12:39:03 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1803M / 3000M (60.1%) |
| Step | 110040 |
| Latest loss | 1.7795 |
| Avg loss (last 30 logged) | 2.0708 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 2:37:40 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.55 -> 2.02 -> 2.21 -> 1.96 -> 2.25 -> 2.25 -> 1.78 -> 1.52 -> 2.37 -> 1.81 -> 2.33 -> 1.65

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=109930 tokens=1801.1M loss=2.0620 lr=1.24e-04 tok/s=12488
[train] step=109940 tokens=1801.3M loss=2.1567 lr=1.24e-04 tok/s=12488
[train] step=109950 tokens=1801.4M loss=1.9697 lr=1.24e-04 tok/s=12488
[train] step=109960 tokens=1801.6M loss=1.7810 lr=1.24e-04 tok/s=12488
[train] step=109970 tokens=1801.7M loss=2.0446 lr=1.24e-04 tok/s=12488
[train] step=109980 tokens=1801.9M loss=2.1799 lr=1.24e-04 tok/s=12488
[train] step=109990 tokens=1802.1M loss=2.3309 lr=1.24e-04 tok/s=12488
[train] step=110000 tokens=1802.2M loss=1.8975 lr=1.24e-04 tok/s=12488
[train] step=110010 tokens=1802.4M loss=2.1657 lr=1.24e-04 tok/s=12488
[train] step=110020 tokens=1802.6M loss=1.6508 lr=1.24e-04 tok/s=12488
[train] step=110030 tokens=1802.7M loss=2.3426 lr=1.24e-04 tok/s=12488
[train] step=110040 tokens=1802.9M loss=1.7795 lr=1.24e-04 tok/s=12488
```
