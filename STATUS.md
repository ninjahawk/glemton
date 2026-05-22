# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 00:33:21 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 180M / 3000M (6.0%) |
| Step | 11000 |
| Latest loss | 2.3678 |
| Avg loss (last 30 logged) | 2.5619 |
| Throughput | 12,491 tok/s |
| ETA to 3B tokens | 2 days, 14:42:26 |
| Projected finish | Sun 2026-05-24 15:15 |

## Loss trajectory (sampled)
2.64 -> 2.65 -> 2.92 -> 3.00 -> 2.63 -> 3.10 -> 2.71 -> 2.79 -> 2.11 -> 2.37 -> 2.63 -> 3.04

## Checkpoints on disk
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=10890 tokens=178.4M loss=2.6375 lr=2.98e-04 tok/s=12491
[train] step=10900 tokens=178.6M loss=2.7879 lr=2.98e-04 tok/s=12491
[train] step=10910 tokens=178.7M loss=2.6409 lr=2.98e-04 tok/s=12491
[train] step=10920 tokens=178.9M loss=2.5056 lr=2.98e-04 tok/s=12491
[train] step=10930 tokens=179.1M loss=2.6272 lr=2.98e-04 tok/s=12491
[train] step=10940 tokens=179.2M loss=2.7673 lr=2.98e-04 tok/s=12491
[train] step=10950 tokens=179.4M loss=2.5013 lr=2.98e-04 tok/s=12491
[train] step=10960 tokens=179.6M loss=2.4691 lr=2.98e-04 tok/s=12491
[train] step=10970 tokens=179.7M loss=3.0351 lr=2.98e-04 tok/s=12491
[train] step=10980 tokens=179.9M loss=2.5310 lr=2.98e-04 tok/s=12491
[train] step=10990 tokens=180.1M loss=2.7279 lr=2.98e-04 tok/s=12491
[train] step=11000 tokens=180.2M loss=2.3678 lr=2.98e-04 tok/s=12491
```
