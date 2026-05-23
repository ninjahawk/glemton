# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 07:28:15 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1570M / 3000M (52.3%) |
| Step | 95820 |
| Latest loss | 2.1616 |
| Avg loss (last 30 logged) | 2.0792 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 7:48:37 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.15 -> 2.05 -> 2.30 -> 2.29 -> 2.01 -> 2.03 -> 2.48 -> 2.04 -> 1.77 -> 1.75 -> 2.37 -> 2.19

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=95710 tokens=1568.1M loss=2.1135 lr=1.57e-04 tok/s=12488
[train] step=95720 tokens=1568.3M loss=2.3022 lr=1.57e-04 tok/s=12488
[train] step=95730 tokens=1568.4M loss=1.9065 lr=1.57e-04 tok/s=12488
[train] step=95740 tokens=1568.6M loss=2.6742 lr=1.57e-04 tok/s=12488
[train] step=95750 tokens=1568.8M loss=2.5472 lr=1.57e-04 tok/s=12488
[train] step=95760 tokens=1568.9M loss=1.8881 lr=1.57e-04 tok/s=12488
[train] step=95770 tokens=1569.1M loss=2.0307 lr=1.57e-04 tok/s=12488
[train] step=95780 tokens=1569.3M loss=2.0003 lr=1.57e-04 tok/s=12488
[train] step=95790 tokens=1569.4M loss=2.1924 lr=1.57e-04 tok/s=12488
[train] step=95800 tokens=1569.6M loss=1.9424 lr=1.57e-04 tok/s=12488
[train] step=95810 tokens=1569.8M loss=1.9156 lr=1.57e-04 tok/s=12488
[train] step=95820 tokens=1569.9M loss=2.1616 lr=1.57e-04 tok/s=12488
```
