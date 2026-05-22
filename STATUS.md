# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 03:23:49 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 308M / 3000M (10.3%) |
| Step | 18790 |
| Latest loss | 2.6296 |
| Avg loss (last 30 logged) | 2.5309 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 2 days, 11:52:54 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.92 -> 2.44 -> 2.89 -> 2.71 -> 2.58 -> 3.06 -> 2.41 -> 2.35 -> 2.95 -> 2.54 -> 2.63 -> 2.47

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=18680 tokens=306.1M loss=2.7010 lr=2.94e-04 tok/s=12488
[train] step=18690 tokens=306.2M loss=2.3097 lr=2.94e-04 tok/s=12488
[train] step=18700 tokens=306.4M loss=2.5514 lr=2.94e-04 tok/s=12488
[train] step=18710 tokens=306.5M loss=2.5268 lr=2.94e-04 tok/s=12488
[train] step=18720 tokens=306.7M loss=2.6775 lr=2.94e-04 tok/s=12488
[train] step=18730 tokens=306.9M loss=2.3782 lr=2.94e-04 tok/s=12488
[train] step=18740 tokens=307.0M loss=2.4461 lr=2.94e-04 tok/s=12488
[train] step=18750 tokens=307.2M loss=2.7369 lr=2.94e-04 tok/s=12488
[train] step=18760 tokens=307.4M loss=2.3634 lr=2.94e-04 tok/s=12488
[train] step=18770 tokens=307.5M loss=2.4743 lr=2.94e-04 tok/s=12488
[train] step=18780 tokens=307.7M loss=2.3696 lr=2.94e-04 tok/s=12488
[train] step=18790 tokens=307.9M loss=2.6296 lr=2.94e-04 tok/s=12488
```
