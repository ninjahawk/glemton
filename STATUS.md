# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 12:29:01 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1796M / 3000M (59.9%) |
| Step | 109590 |
| Latest loss | 1.7452 |
| Avg loss (last 30 logged) | 2.1053 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 2:47:32 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.30 -> 1.80 -> 1.62 -> 2.33 -> 2.07 -> 1.84 -> 1.95 -> 2.10 -> 1.87 -> 2.22 -> 1.81 -> 2.37

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=109480 tokens=1793.7M loss=2.0569 lr=1.25e-04 tok/s=12488
[train] step=109490 tokens=1793.9M loss=1.7605 lr=1.25e-04 tok/s=12488
[train] step=109500 tokens=1794.0M loss=2.0981 lr=1.25e-04 tok/s=12488
[train] step=109510 tokens=1794.2M loss=2.6191 lr=1.25e-04 tok/s=12488
[train] step=109520 tokens=1794.4M loss=1.8730 lr=1.25e-04 tok/s=12488
[train] step=109530 tokens=1794.5M loss=2.1489 lr=1.25e-04 tok/s=12488
[train] step=109540 tokens=1794.7M loss=1.8172 lr=1.25e-04 tok/s=12488
[train] step=109550 tokens=1794.9M loss=2.0319 lr=1.25e-04 tok/s=12488
[train] step=109560 tokens=1795.0M loss=2.3675 lr=1.25e-04 tok/s=12488
[train] step=109570 tokens=1795.2M loss=2.4818 lr=1.25e-04 tok/s=12488
[train] step=109580 tokens=1795.4M loss=1.7059 lr=1.25e-04 tok/s=12488
[train] step=109590 tokens=1795.5M loss=1.7452 lr=1.25e-04 tok/s=12488
```
