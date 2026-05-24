# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 00:30:49 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2336M / 3000M (77.9%) |
| Step | 142610 |
| Latest loss | 1.9252 |
| Avg loss (last 30 logged) | 2.0819 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 14:45:26 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.89 -> 2.18 -> 2.38 -> 1.82 -> 2.07 -> 2.17 -> 1.96 -> 2.44 -> 1.79 -> 2.08 -> 2.53 -> 2.20

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=142500 tokens=2334.7M loss=1.8088 lr=6.20e-05 tok/s=12489
[train] step=142510 tokens=2334.9M loss=2.1483 lr=6.20e-05 tok/s=12489
[train] step=142520 tokens=2335.0M loss=2.5119 lr=6.19e-05 tok/s=12489
[train] step=142530 tokens=2335.2M loss=2.7500 lr=6.19e-05 tok/s=12489
[train] step=142540 tokens=2335.4M loss=2.0359 lr=6.19e-05 tok/s=12489
[train] step=142550 tokens=2335.5M loss=2.0478 lr=6.19e-05 tok/s=12489
[train] step=142560 tokens=2335.7M loss=2.2231 lr=6.19e-05 tok/s=12489
[train] step=142570 tokens=2335.9M loss=2.1037 lr=6.19e-05 tok/s=12489
[train] step=142580 tokens=2336.0M loss=1.7568 lr=6.18e-05 tok/s=12489
[train] step=142590 tokens=2336.2M loss=2.2008 lr=6.18e-05 tok/s=12489
[train] step=142600 tokens=2336.4M loss=1.8037 lr=6.18e-05 tok/s=12489
[train] step=142610 tokens=2336.5M loss=1.9252 lr=6.18e-05 tok/s=12489
```
