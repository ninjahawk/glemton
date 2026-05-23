# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 07:08:12 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1555M / 3000M (51.8%) |
| Step | 94910 |
| Latest loss | 2.1461 |
| Avg loss (last 30 logged) | 2.1489 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 8:08:31 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.10 -> 2.22 -> 1.73 -> 2.68 -> 1.80 -> 1.82 -> 2.55 -> 2.23 -> 2.21 -> 2.09 -> 2.06 -> 2.12

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=94800 tokens=1553.2M loss=1.7684 lr=1.59e-04 tok/s=12488
[train] step=94810 tokens=1553.4M loss=2.4012 lr=1.59e-04 tok/s=12488
[train] step=94820 tokens=1553.5M loss=2.1603 lr=1.59e-04 tok/s=12488
[train] step=94830 tokens=1553.7M loss=2.1676 lr=1.59e-04 tok/s=12488
[train] step=94840 tokens=1553.9M loss=2.2942 lr=1.59e-04 tok/s=12488
[train] step=94850 tokens=1554.0M loss=2.2719 lr=1.59e-04 tok/s=12488
[train] step=94860 tokens=1554.2M loss=2.2418 lr=1.59e-04 tok/s=12488
[train] step=94870 tokens=1554.4M loss=2.1878 lr=1.59e-04 tok/s=12488
[train] step=94880 tokens=1554.5M loss=2.4950 lr=1.59e-04 tok/s=12488
[train] step=94890 tokens=1554.7M loss=2.1245 lr=1.59e-04 tok/s=12488
[train] step=94900 tokens=1554.8M loss=2.2447 lr=1.59e-04 tok/s=12488
[train] step=94910 tokens=1555.0M loss=2.1461 lr=1.59e-04 tok/s=12488
```
