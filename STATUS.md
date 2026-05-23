# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 07:58:20 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1592M / 3000M (53.1%) |
| Step | 97200 |
| Latest loss | 2.4516 |
| Avg loss (last 30 logged) | 2.1688 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 7:18:28 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.78 -> 1.90 -> 1.97 -> 1.92 -> 2.24 -> 1.68 -> 1.90 -> 2.74 -> 2.30 -> 1.88 -> 2.05 -> 1.95

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=97090 tokens=1590.7M loss=1.9281 lr=1.54e-04 tok/s=12488
[train] step=97100 tokens=1590.9M loss=2.1629 lr=1.54e-04 tok/s=12488
[train] step=97110 tokens=1591.1M loss=2.0825 lr=1.54e-04 tok/s=12488
[train] step=97120 tokens=1591.2M loss=2.2344 lr=1.54e-04 tok/s=12488
[train] step=97130 tokens=1591.4M loss=2.2159 lr=1.54e-04 tok/s=12488
[train] step=97140 tokens=1591.5M loss=2.5415 lr=1.54e-04 tok/s=12488
[train] step=97150 tokens=1591.7M loss=2.0517 lr=1.54e-04 tok/s=12488
[train] step=97160 tokens=1591.9M loss=2.1200 lr=1.54e-04 tok/s=12488
[train] step=97170 tokens=1592.0M loss=1.9455 lr=1.54e-04 tok/s=12488
[train] step=97180 tokens=1592.2M loss=1.9721 lr=1.54e-04 tok/s=12488
[train] step=97190 tokens=1592.4M loss=2.2709 lr=1.54e-04 tok/s=12488
[train] step=97200 tokens=1592.5M loss=2.4516 lr=1.54e-04 tok/s=12488
```
