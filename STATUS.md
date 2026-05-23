# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 13:19:09 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1833M / 3000M (61.1%) |
| Step | 111880 |
| Latest loss | 2.0655 |
| Avg loss (last 30 logged) | 2.0722 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 1:57:29 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.91 -> 2.24 -> 2.29 -> 2.50 -> 2.03 -> 2.18 -> 2.15 -> 1.67 -> 2.27 -> 2.12 -> 1.67 -> 1.62

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=111770 tokens=1831.2M loss=2.2245 lr=1.20e-04 tok/s=12488
[train] step=111780 tokens=1831.4M loss=2.2130 lr=1.20e-04 tok/s=12488
[train] step=111790 tokens=1831.6M loss=2.0635 lr=1.20e-04 tok/s=12488
[train] step=111800 tokens=1831.7M loss=2.1481 lr=1.20e-04 tok/s=12488
[train] step=111810 tokens=1831.9M loss=2.3413 lr=1.20e-04 tok/s=12488
[train] step=111820 tokens=1832.1M loss=1.9500 lr=1.20e-04 tok/s=12488
[train] step=111830 tokens=1832.2M loss=2.3424 lr=1.20e-04 tok/s=12488
[train] step=111840 tokens=1832.4M loss=2.2502 lr=1.20e-04 tok/s=12488
[train] step=111850 tokens=1832.6M loss=2.1405 lr=1.20e-04 tok/s=12488
[train] step=111860 tokens=1832.7M loss=1.6177 lr=1.20e-04 tok/s=12488
[train] step=111870 tokens=1832.9M loss=1.8311 lr=1.20e-04 tok/s=12488
[train] step=111880 tokens=1833.0M loss=2.0655 lr=1.20e-04 tok/s=12488
```
