# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 03:53:54 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 330M / 3000M (11.0%) |
| Step | 20170 |
| Latest loss | 2.5113 |
| Avg loss (last 30 logged) | 2.4953 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 2 days, 11:22:45 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.31 -> 2.39 -> 2.23 -> 2.30 -> 2.60 -> 2.64 -> 2.59 -> 2.57 -> 2.17 -> 2.57 -> 2.23 -> 2.69

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=20060 tokens=328.7M loss=2.6500 lr=2.93e-04 tok/s=12488
[train] step=20070 tokens=328.8M loss=2.7413 lr=2.93e-04 tok/s=12488
[train] step=20080 tokens=329.0M loss=2.3963 lr=2.93e-04 tok/s=12488
[train] step=20090 tokens=329.2M loss=2.3015 lr=2.93e-04 tok/s=12488
[train] step=20100 tokens=329.3M loss=2.6139 lr=2.93e-04 tok/s=12488
[train] step=20110 tokens=329.5M loss=2.5866 lr=2.93e-04 tok/s=12488
[train] step=20120 tokens=329.6M loss=2.5597 lr=2.93e-04 tok/s=12488
[train] step=20130 tokens=329.8M loss=2.2937 lr=2.93e-04 tok/s=12488
[train] step=20140 tokens=330.0M loss=2.6242 lr=2.93e-04 tok/s=12488
[train] step=20150 tokens=330.1M loss=2.6920 lr=2.93e-04 tok/s=12488
[train] step=20160 tokens=330.3M loss=2.5494 lr=2.93e-04 tok/s=12488
[train] step=20170 tokens=330.5M loss=2.5113 lr=2.93e-04 tok/s=12488
```
