# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 13:09:07 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1826M / 3000M (60.9%) |
| Step | 111420 |
| Latest loss | 2.0299 |
| Avg loss (last 30 logged) | 2.1002 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 2:07:30 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.77 -> 1.91 -> 1.91 -> 1.99 -> 2.43 -> 2.13 -> 2.38 -> 2.34 -> 2.06 -> 1.76 -> 2.17 -> 1.81

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=111310 tokens=1823.7M loss=1.8400 lr=1.21e-04 tok/s=12488
[train] step=111320 tokens=1823.9M loss=2.3025 lr=1.21e-04 tok/s=12488
[train] step=111330 tokens=1824.0M loss=1.8830 lr=1.21e-04 tok/s=12488
[train] step=111340 tokens=1824.2M loss=1.9818 lr=1.21e-04 tok/s=12488
[train] step=111350 tokens=1824.4M loss=2.1164 lr=1.21e-04 tok/s=12488
[train] step=111360 tokens=1824.5M loss=1.9427 lr=1.21e-04 tok/s=12488
[train] step=111370 tokens=1824.7M loss=2.1522 lr=1.21e-04 tok/s=12488
[train] step=111380 tokens=1824.8M loss=2.6407 lr=1.21e-04 tok/s=12488
[train] step=111390 tokens=1825.0M loss=1.8869 lr=1.21e-04 tok/s=12488
[train] step=111400 tokens=1825.2M loss=1.8125 lr=1.21e-04 tok/s=12488
[train] step=111410 tokens=1825.3M loss=2.7368 lr=1.21e-04 tok/s=12488
[train] step=111420 tokens=1825.5M loss=2.0299 lr=1.21e-04 tok/s=12488
```
