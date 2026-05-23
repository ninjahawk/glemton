# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 12:08:58 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1780M / 3000M (59.3%) |
| Step | 108670 |
| Latest loss | 2.2571 |
| Avg loss (last 30 logged) | 2.0132 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 3:07:41 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.30 -> 2.21 -> 2.39 -> 2.16 -> 1.90 -> 1.67 -> 1.71 -> 1.56 -> 2.31 -> 2.04 -> 2.26 -> 1.67

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=108560 tokens=1778.6M loss=2.2425 lr=1.28e-04 tok/s=12488
[train] step=108570 tokens=1778.8M loss=1.8728 lr=1.28e-04 tok/s=12488
[train] step=108580 tokens=1779.0M loss=1.5083 lr=1.28e-04 tok/s=12488
[train] step=108590 tokens=1779.1M loss=1.9719 lr=1.27e-04 tok/s=12488
[train] step=108600 tokens=1779.3M loss=1.9550 lr=1.27e-04 tok/s=12488
[train] step=108610 tokens=1779.5M loss=2.1188 lr=1.27e-04 tok/s=12488
[train] step=108620 tokens=1779.6M loss=1.7433 lr=1.27e-04 tok/s=12488
[train] step=108630 tokens=1779.8M loss=1.7432 lr=1.27e-04 tok/s=12488
[train] step=108640 tokens=1780.0M loss=1.6731 lr=1.27e-04 tok/s=12488
[train] step=108650 tokens=1780.1M loss=1.8271 lr=1.27e-04 tok/s=12488
[train] step=108660 tokens=1780.3M loss=1.9657 lr=1.27e-04 tok/s=12488
[train] step=108670 tokens=1780.4M loss=2.2571 lr=1.27e-04 tok/s=12488
```
