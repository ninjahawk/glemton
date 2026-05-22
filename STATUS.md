# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 04:13:57 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 346M / 3000M (11.5%) |
| Step | 21090 |
| Latest loss | 2.2943 |
| Avg loss (last 30 logged) | 2.4386 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 2 days, 11:02:44 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.20 -> 2.70 -> 2.36 -> 2.29 -> 2.36 -> 2.37 -> 2.61 -> 2.76 -> 2.40 -> 2.45 -> 2.29 -> 2.93

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=20980 tokens=343.7M loss=2.2549 lr=2.92e-04 tok/s=12488
[train] step=20990 tokens=343.9M loss=2.1985 lr=2.92e-04 tok/s=12488
[train] step=21000 tokens=344.1M loss=2.3221 lr=2.92e-04 tok/s=12488
[train] step=21010 tokens=344.2M loss=2.6893 lr=2.92e-04 tok/s=12488
[train] step=21020 tokens=344.4M loss=2.3812 lr=2.92e-04 tok/s=12488
[train] step=21030 tokens=344.6M loss=2.3941 lr=2.92e-04 tok/s=12488
[train] step=21040 tokens=344.7M loss=2.1872 lr=2.92e-04 tok/s=12488
[train] step=21050 tokens=344.9M loss=2.4986 lr=2.92e-04 tok/s=12488
[train] step=21060 tokens=345.0M loss=2.3282 lr=2.92e-04 tok/s=12488
[train] step=21070 tokens=345.2M loss=2.9308 lr=2.92e-04 tok/s=12488
[train] step=21080 tokens=345.4M loss=2.3463 lr=2.92e-04 tok/s=12488
[train] step=21090 tokens=345.5M loss=2.2943 lr=2.92e-04 tok/s=12488
```
