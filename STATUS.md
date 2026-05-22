# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 03:43:52 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 323M / 3000M (10.8%) |
| Step | 19710 |
| Latest loss | 2.3543 |
| Avg loss (last 30 logged) | 2.4788 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 2 days, 11:32:53 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.51 -> 2.90 -> 2.39 -> 2.40 -> 2.34 -> 2.65 -> 2.35 -> 2.32 -> 2.55 -> 2.63 -> 2.36 -> 2.85

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=19600 tokens=321.1M loss=2.3207 lr=2.93e-04 tok/s=12488
[train] step=19610 tokens=321.3M loss=2.4813 lr=2.93e-04 tok/s=12488
[train] step=19620 tokens=321.5M loss=2.5498 lr=2.93e-04 tok/s=12488
[train] step=19630 tokens=321.6M loss=2.3957 lr=2.93e-04 tok/s=12488
[train] step=19640 tokens=321.8M loss=2.6957 lr=2.93e-04 tok/s=12488
[train] step=19650 tokens=321.9M loss=2.4285 lr=2.93e-04 tok/s=12488
[train] step=19660 tokens=322.1M loss=2.4845 lr=2.93e-04 tok/s=12488
[train] step=19670 tokens=322.3M loss=2.2957 lr=2.93e-04 tok/s=12488
[train] step=19680 tokens=322.4M loss=2.6378 lr=2.93e-04 tok/s=12488
[train] step=19690 tokens=322.6M loss=2.8495 lr=2.93e-04 tok/s=12488
[train] step=19700 tokens=322.8M loss=2.2262 lr=2.93e-04 tok/s=12488
[train] step=19710 tokens=322.9M loss=2.3543 lr=2.93e-04 tok/s=12488
```
