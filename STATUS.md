# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 11:28:52 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1750M / 3000M (58.3%) |
| Step | 106830 |
| Latest loss | 1.9766 |
| Avg loss (last 30 logged) | 2.0821 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 3:47:52 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.07 -> 1.94 -> 1.94 -> 2.17 -> 1.89 -> 2.26 -> 2.00 -> 1.66 -> 1.88 -> 2.39 -> 1.99 -> 2.14

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=106720 tokens=1748.5M loss=2.0179 lr=1.32e-04 tok/s=12488
[train] step=106730 tokens=1748.7M loss=2.0549 lr=1.32e-04 tok/s=12488
[train] step=106740 tokens=1748.8M loss=2.2486 lr=1.32e-04 tok/s=12488
[train] step=106750 tokens=1749.0M loss=1.9500 lr=1.32e-04 tok/s=12488
[train] step=106760 tokens=1749.2M loss=2.2247 lr=1.32e-04 tok/s=12488
[train] step=106770 tokens=1749.3M loss=2.2810 lr=1.32e-04 tok/s=12488
[train] step=106780 tokens=1749.5M loss=1.9306 lr=1.32e-04 tok/s=12488
[train] step=106790 tokens=1749.6M loss=1.5808 lr=1.32e-04 tok/s=12488
[train] step=106800 tokens=1749.8M loss=2.0453 lr=1.32e-04 tok/s=12488
[train] step=106810 tokens=1750.0M loss=2.1369 lr=1.31e-04 tok/s=12488
[train] step=106820 tokens=1750.1M loss=1.7931 lr=1.31e-04 tok/s=12488
[train] step=106830 tokens=1750.3M loss=1.9766 lr=1.31e-04 tok/s=12488
```
