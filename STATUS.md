# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 11:18:51 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1743M / 3000M (58.1%) |
| Step | 106370 |
| Latest loss | 2.0703 |
| Avg loss (last 30 logged) | 2.0175 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 3:57:52 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.16 -> 2.30 -> 2.07 -> 2.21 -> 1.94 -> 1.95 -> 1.71 -> 2.42 -> 2.03 -> 1.95 -> 2.31 -> 2.04

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=106260 tokens=1741.0M loss=1.8037 lr=1.33e-04 tok/s=12488
[train] step=106270 tokens=1741.1M loss=1.9632 lr=1.33e-04 tok/s=12488
[train] step=106280 tokens=1741.3M loss=2.1112 lr=1.33e-04 tok/s=12488
[train] step=106290 tokens=1741.5M loss=1.9455 lr=1.33e-04 tok/s=12488
[train] step=106300 tokens=1741.6M loss=1.9304 lr=1.33e-04 tok/s=12488
[train] step=106310 tokens=1741.8M loss=1.6004 lr=1.33e-04 tok/s=12488
[train] step=106320 tokens=1741.9M loss=2.1998 lr=1.33e-04 tok/s=12488
[train] step=106330 tokens=1742.1M loss=1.8976 lr=1.33e-04 tok/s=12488
[train] step=106340 tokens=1742.3M loss=1.9410 lr=1.33e-04 tok/s=12488
[train] step=106350 tokens=1742.4M loss=2.0350 lr=1.33e-04 tok/s=12488
[train] step=106360 tokens=1742.6M loss=2.2580 lr=1.33e-04 tok/s=12488
[train] step=106370 tokens=1742.8M loss=2.0703 lr=1.32e-04 tok/s=12488
```
