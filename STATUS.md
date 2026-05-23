# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 11:48:55 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1765M / 3000M (58.8%) |
| Step | 107750 |
| Latest loss | 2.0902 |
| Avg loss (last 30 logged) | 2.0731 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 3:27:42 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.95 -> 1.96 -> 2.19 -> 2.17 -> 2.43 -> 2.23 -> 2.00 -> 1.93 -> 2.25 -> 2.18 -> 2.38 -> 2.72

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=107640 tokens=1763.6M loss=1.8748 lr=1.30e-04 tok/s=12488
[train] step=107650 tokens=1763.7M loss=2.3052 lr=1.30e-04 tok/s=12488
[train] step=107660 tokens=1763.9M loss=1.9958 lr=1.30e-04 tok/s=12488
[train] step=107670 tokens=1764.1M loss=1.9485 lr=1.30e-04 tok/s=12488
[train] step=107680 tokens=1764.2M loss=1.7805 lr=1.30e-04 tok/s=12488
[train] step=107690 tokens=1764.4M loss=2.7392 lr=1.30e-04 tok/s=12488
[train] step=107700 tokens=1764.6M loss=1.9893 lr=1.29e-04 tok/s=12488
[train] step=107710 tokens=1764.7M loss=2.2499 lr=1.29e-04 tok/s=12488
[train] step=107720 tokens=1764.9M loss=2.3675 lr=1.29e-04 tok/s=12488
[train] step=107730 tokens=1765.0M loss=2.7154 lr=1.29e-04 tok/s=12488
[train] step=107740 tokens=1765.2M loss=2.1926 lr=1.29e-04 tok/s=12488
[train] step=107750 tokens=1765.4M loss=2.0902 lr=1.29e-04 tok/s=12488
```
