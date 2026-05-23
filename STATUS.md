# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 08:38:26 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1622M / 3000M (54.1%) |
| Step | 99030 |
| Latest loss | 2.2866 |
| Avg loss (last 30 logged) | 2.1499 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 6:38:25 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.13 -> 2.11 -> 1.84 -> 1.81 -> 2.08 -> 2.05 -> 1.95 -> 1.95 -> 2.41 -> 2.02 -> 1.90 -> 2.36

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=98920 tokens=1620.7M loss=2.5056 lr=1.50e-04 tok/s=12488
[train] step=98930 tokens=1620.9M loss=2.1002 lr=1.50e-04 tok/s=12488
[train] step=98940 tokens=1621.0M loss=1.9537 lr=1.50e-04 tok/s=12488
[train] step=98950 tokens=1621.2M loss=2.1836 lr=1.50e-04 tok/s=12488
[train] step=98960 tokens=1621.4M loss=2.1098 lr=1.50e-04 tok/s=12488
[train] step=98970 tokens=1621.5M loss=2.0251 lr=1.49e-04 tok/s=12488
[train] step=98980 tokens=1621.7M loss=1.9299 lr=1.49e-04 tok/s=12488
[train] step=98990 tokens=1621.9M loss=2.2237 lr=1.49e-04 tok/s=12488
[train] step=99000 tokens=1622.0M loss=2.4321 lr=1.49e-04 tok/s=12488
[train] step=99010 tokens=1622.2M loss=2.3575 lr=1.49e-04 tok/s=12488
[train] step=99020 tokens=1622.3M loss=2.6034 lr=1.49e-04 tok/s=12488
[train] step=99030 tokens=1622.5M loss=2.2866 lr=1.49e-04 tok/s=12488
```
