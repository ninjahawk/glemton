# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 09:38:35 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1668M / 3000M (55.6%) |
| Step | 101790 |
| Latest loss | 2.2062 |
| Avg loss (last 30 logged) | 2.1371 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 5:38:06 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.13 -> 2.26 -> 1.69 -> 2.16 -> 2.14 -> 2.45 -> 2.45 -> 2.25 -> 2.07 -> 2.02 -> 2.20 -> 1.80

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=101680 tokens=1665.9M loss=2.2609 lr=1.43e-04 tok/s=12488
[train] step=101690 tokens=1666.1M loss=1.8600 lr=1.43e-04 tok/s=12488
[train] step=101700 tokens=1666.3M loss=2.1897 lr=1.43e-04 tok/s=12488
[train] step=101710 tokens=1666.4M loss=2.3424 lr=1.43e-04 tok/s=12488
[train] step=101720 tokens=1666.6M loss=2.2794 lr=1.43e-04 tok/s=12488
[train] step=101730 tokens=1666.7M loss=1.8406 lr=1.43e-04 tok/s=12488
[train] step=101740 tokens=1666.9M loss=2.2680 lr=1.43e-04 tok/s=12488
[train] step=101750 tokens=1667.1M loss=2.3113 lr=1.43e-04 tok/s=12488
[train] step=101760 tokens=1667.2M loss=1.7999 lr=1.43e-04 tok/s=12488
[train] step=101770 tokens=1667.4M loss=1.8487 lr=1.43e-04 tok/s=12488
[train] step=101780 tokens=1667.6M loss=1.6572 lr=1.43e-04 tok/s=12488
[train] step=101790 tokens=1667.7M loss=2.2062 lr=1.43e-04 tok/s=12488
```
