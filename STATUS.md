# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 14:39:18 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1893M / 3000M (63.1%) |
| Step | 115550 |
| Latest loss | 2.5177 |
| Avg loss (last 30 logged) | 2.0556 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 1 day, 0:37:01 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.61 -> 1.89 -> 2.67 -> 1.92 -> 2.13 -> 1.76 -> 2.19 -> 2.25 -> 2.09 -> 2.76 -> 1.99 -> 2.11

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=115440 tokens=1891.4M loss=2.7310 lr=1.12e-04 tok/s=12489
[train] step=115450 tokens=1891.5M loss=2.1805 lr=1.12e-04 tok/s=12489
[train] step=115460 tokens=1891.7M loss=1.9909 lr=1.12e-04 tok/s=12489
[train] step=115470 tokens=1891.9M loss=1.8480 lr=1.12e-04 tok/s=12489
[train] step=115480 tokens=1892.0M loss=1.8385 lr=1.12e-04 tok/s=12489
[train] step=115490 tokens=1892.2M loss=1.9312 lr=1.12e-04 tok/s=12489
[train] step=115500 tokens=1892.4M loss=2.0745 lr=1.12e-04 tok/s=12489
[train] step=115510 tokens=1892.5M loss=2.4255 lr=1.12e-04 tok/s=12489
[train] step=115520 tokens=1892.7M loss=2.1056 lr=1.12e-04 tok/s=12489
[train] step=115530 tokens=1892.8M loss=1.5931 lr=1.12e-04 tok/s=12489
[train] step=115540 tokens=1893.0M loss=1.8167 lr=1.12e-04 tok/s=12489
[train] step=115550 tokens=1893.2M loss=2.5177 lr=1.12e-04 tok/s=12489
```
