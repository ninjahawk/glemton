# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 05:21:34 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2554M / 3000M (85.1%) |
| Step | 155900 |
| Latest loss | 2.0329 |
| Avg loss (last 30 logged) | 1.9576 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 9:54:47 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.99 -> 2.46 -> 1.68 -> 1.79 -> 1.97 -> 2.06 -> 1.76 -> 2.13 -> 2.05 -> 2.20 -> 2.17 -> 2.01

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
[train] step=155790 tokens=2552.5M loss=1.8153 lr=4.48e-05 tok/s=12489
[train] step=155800 tokens=2552.6M loss=1.9274 lr=4.48e-05 tok/s=12489
[train] step=155810 tokens=2552.8M loss=1.9219 lr=4.48e-05 tok/s=12489
[train] step=155820 tokens=2553.0M loss=2.0424 lr=4.48e-05 tok/s=12489
[train] step=155830 tokens=2553.1M loss=1.8406 lr=4.48e-05 tok/s=12489
[train] step=155840 tokens=2553.3M loss=1.9428 lr=4.47e-05 tok/s=12489
[train] step=155850 tokens=2553.4M loss=1.9781 lr=4.47e-05 tok/s=12489
[train] step=155860 tokens=2553.6M loss=2.1074 lr=4.47e-05 tok/s=12489
[train] step=155870 tokens=2553.8M loss=2.2433 lr=4.47e-05 tok/s=12489
[train] step=155880 tokens=2553.9M loss=2.0148 lr=4.47e-05 tok/s=12489
[train] step=155890 tokens=2554.1M loss=1.8634 lr=4.47e-05 tok/s=12489
[train] step=155900 tokens=2554.3M loss=2.0329 lr=4.47e-05 tok/s=12489
```
