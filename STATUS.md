# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 06:21:43 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2599M / 3000M (86.6%) |
| Step | 158650 |
| Latest loss | 1.7550 |
| Avg loss (last 30 logged) | 2.0248 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 8:54:44 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.48 -> 1.89 -> 2.17 -> 2.15 -> 2.11 -> 1.56 -> 1.76 -> 1.85 -> 2.20 -> 1.82 -> 2.22 -> 2.11

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=158540 tokens=2597.5M loss=2.1852 lr=4.20e-05 tok/s=12489
[train] step=158550 tokens=2597.7M loss=2.0084 lr=4.20e-05 tok/s=12489
[train] step=158560 tokens=2597.8M loss=1.9356 lr=4.20e-05 tok/s=12489
[train] step=158570 tokens=2598.0M loss=1.7623 lr=4.20e-05 tok/s=12489
[train] step=158580 tokens=2598.2M loss=2.0779 lr=4.20e-05 tok/s=12489
[train] step=158590 tokens=2598.3M loss=1.9248 lr=4.20e-05 tok/s=12489
[train] step=158600 tokens=2598.5M loss=2.1164 lr=4.20e-05 tok/s=12489
[train] step=158610 tokens=2598.7M loss=2.0762 lr=4.19e-05 tok/s=12489
[train] step=158620 tokens=2598.8M loss=2.1110 lr=4.19e-05 tok/s=12489
[train] step=158630 tokens=2599.0M loss=2.0353 lr=4.19e-05 tok/s=12489
[train] step=158640 tokens=2599.2M loss=1.8710 lr=4.19e-05 tok/s=12489
[train] step=158650 tokens=2599.3M loss=1.7550 lr=4.19e-05 tok/s=12489
```
