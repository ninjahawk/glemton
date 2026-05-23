# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 08:48:27 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1630M / 3000M (54.3%) |
| Step | 99490 |
| Latest loss | 2.3137 |
| Avg loss (last 30 logged) | 2.1692 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 6:28:25 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.03 -> 2.18 -> 1.71 -> 1.94 -> 2.12 -> 2.24 -> 2.44 -> 2.45 -> 1.63 -> 2.09 -> 2.03 -> 2.04

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=99380 tokens=1628.2M loss=2.3596 lr=1.49e-04 tok/s=12488
[train] step=99390 tokens=1628.4M loss=2.9638 lr=1.49e-04 tok/s=12488
[train] step=99400 tokens=1628.6M loss=2.1697 lr=1.48e-04 tok/s=12488
[train] step=99410 tokens=1628.7M loss=2.0789 lr=1.48e-04 tok/s=12488
[train] step=99420 tokens=1628.9M loss=2.4609 lr=1.48e-04 tok/s=12488
[train] step=99430 tokens=1629.1M loss=2.2532 lr=1.48e-04 tok/s=12488
[train] step=99440 tokens=1629.2M loss=1.7772 lr=1.48e-04 tok/s=12488
[train] step=99450 tokens=1629.4M loss=2.1395 lr=1.48e-04 tok/s=12488
[train] step=99460 tokens=1629.6M loss=2.1849 lr=1.48e-04 tok/s=12488
[train] step=99470 tokens=1629.7M loss=2.0424 lr=1.48e-04 tok/s=12488
[train] step=99480 tokens=1629.9M loss=1.7362 lr=1.48e-04 tok/s=12488
[train] step=99490 tokens=1630.0M loss=2.3137 lr=1.48e-04 tok/s=12488
```
