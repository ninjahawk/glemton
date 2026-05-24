# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 08:32:03 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2697M / 3000M (89.9%) |
| Step | 164610 |
| Latest loss | 1.8155 |
| Avg loss (last 30 logged) | 2.1437 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 6:44:21 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.67 -> 1.93 -> 2.23 -> 2.13 -> 2.24 -> 1.95 -> 2.26 -> 1.84 -> 2.12 -> 2.06 -> 2.29 -> 2.09

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=164500 tokens=2695.2M loss=2.2350 lr=3.69e-05 tok/s=12489
[train] step=164510 tokens=2695.3M loss=1.8664 lr=3.69e-05 tok/s=12489
[train] step=164520 tokens=2695.5M loss=2.2539 lr=3.69e-05 tok/s=12489
[train] step=164530 tokens=2695.7M loss=2.0726 lr=3.69e-05 tok/s=12489
[train] step=164540 tokens=2695.8M loss=1.8305 lr=3.69e-05 tok/s=12489
[train] step=164550 tokens=2696.0M loss=1.7450 lr=3.69e-05 tok/s=12489
[train] step=164560 tokens=2696.2M loss=2.4830 lr=3.69e-05 tok/s=12489
[train] step=164570 tokens=2696.3M loss=2.6097 lr=3.69e-05 tok/s=12489
[train] step=164580 tokens=2696.5M loss=2.0869 lr=3.69e-05 tok/s=12489
[train] step=164590 tokens=2696.6M loss=2.2125 lr=3.69e-05 tok/s=12489
[train] step=164600 tokens=2696.8M loss=2.1981 lr=3.69e-05 tok/s=12489
[train] step=164610 tokens=2697.0M loss=1.8155 lr=3.69e-05 tok/s=12489
```
