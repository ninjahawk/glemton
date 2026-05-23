# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 10:08:40 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1690M / 3000M (56.3%) |
| Step | 103160 |
| Latest loss | 2.3811 |
| Avg loss (last 30 logged) | 2.2111 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 5:08:04 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.97 -> 2.12 -> 2.46 -> 2.04 -> 1.56 -> 2.25 -> 2.26 -> 2.15 -> 2.18 -> 1.89 -> 2.23 -> 1.79

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=103050 tokens=1688.4M loss=2.3010 lr=1.40e-04 tok/s=12488
[train] step=103060 tokens=1688.5M loss=2.4029 lr=1.40e-04 tok/s=12488
[train] step=103070 tokens=1688.7M loss=2.2556 lr=1.40e-04 tok/s=12488
[train] step=103080 tokens=1688.9M loss=2.0600 lr=1.40e-04 tok/s=12488
[train] step=103090 tokens=1689.0M loss=2.7590 lr=1.40e-04 tok/s=12488
[train] step=103100 tokens=1689.2M loss=2.1661 lr=1.40e-04 tok/s=12488
[train] step=103110 tokens=1689.4M loss=2.5315 lr=1.40e-04 tok/s=12488
[train] step=103120 tokens=1689.5M loss=2.4001 lr=1.40e-04 tok/s=12488
[train] step=103130 tokens=1689.7M loss=1.7927 lr=1.40e-04 tok/s=12488
[train] step=103140 tokens=1689.8M loss=1.9644 lr=1.40e-04 tok/s=12488
[train] step=103150 tokens=1690.0M loss=2.3916 lr=1.40e-04 tok/s=12488
[train] step=103160 tokens=1690.2M loss=2.3811 lr=1.40e-04 tok/s=12488
```
