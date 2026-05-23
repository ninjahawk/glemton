# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 08:08:21 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1600M / 3000M (53.3%) |
| Step | 97660 |
| Latest loss | 1.8729 |
| Avg loss (last 30 logged) | 2.1466 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 7:08:19 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.15 -> 2.27 -> 1.93 -> 2.30 -> 1.80 -> 1.98 -> 2.23 -> 2.14 -> 1.79 -> 2.85 -> 2.35 -> 2.03

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=97560 tokens=1598.4M loss=2.1113 lr=1.53e-04 tok/s=12488
[train] step=97570 tokens=1598.6M loss=1.8614 lr=1.53e-04 tok/s=12488
[train] step=97580 tokens=1598.8M loss=2.2461 lr=1.53e-04 tok/s=12488
[train] step=97590 tokens=1598.9M loss=2.0883 lr=1.53e-04 tok/s=12488
[train] step=97600 tokens=1599.1M loss=1.9096 lr=1.53e-04 tok/s=12488
[train] step=97610 tokens=1599.2M loss=2.4382 lr=1.53e-04 tok/s=12488
[train] step=97620 tokens=1599.4M loss=2.1978 lr=1.53e-04 tok/s=12488
[train] step=97630 tokens=1599.6M loss=2.1796 lr=1.53e-04 tok/s=12488
[train] step=97640 tokens=1599.7M loss=2.0281 lr=1.53e-04 tok/s=12488
[train] step=97650 tokens=1599.9M loss=2.3632 lr=1.53e-04 tok/s=12488
[train] checkpoint -> checkpoints\glemton-350m\step_97657_tokens_1600M.pt
[train] step=97660 tokens=1600.1M loss=1.8729 lr=1.53e-04 tok/s=12488
```
