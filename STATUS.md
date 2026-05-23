# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 09:18:32 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1653M / 3000M (55.1%) |
| Step | 100870 |
| Latest loss | 2.2395 |
| Avg loss (last 30 logged) | 2.0410 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 5:58:07 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.81 -> 2.10 -> 2.01 -> 2.00 -> 2.72 -> 2.26 -> 2.50 -> 2.25 -> 2.35 -> 2.29 -> 2.10 -> 2.05

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=100760 tokens=1650.9M loss=2.1965 lr=1.45e-04 tok/s=12488
[train] step=100770 tokens=1651.0M loss=2.0747 lr=1.45e-04 tok/s=12488
[train] step=100780 tokens=1651.2M loss=1.9139 lr=1.45e-04 tok/s=12488
[train] step=100790 tokens=1651.3M loss=2.1562 lr=1.45e-04 tok/s=12488
[train] step=100800 tokens=1651.5M loss=2.1888 lr=1.45e-04 tok/s=12488
[train] step=100810 tokens=1651.7M loss=2.5877 lr=1.45e-04 tok/s=12488
[train] step=100820 tokens=1651.8M loss=1.5572 lr=1.45e-04 tok/s=12488
[train] step=100830 tokens=1652.0M loss=1.8291 lr=1.45e-04 tok/s=12488
[train] step=100840 tokens=1652.2M loss=1.8508 lr=1.45e-04 tok/s=12488
[train] step=100850 tokens=1652.3M loss=2.0513 lr=1.45e-04 tok/s=12488
[train] step=100860 tokens=1652.5M loss=2.0164 lr=1.45e-04 tok/s=12488
[train] step=100870 tokens=1652.7M loss=2.2395 lr=1.45e-04 tok/s=12488
```
