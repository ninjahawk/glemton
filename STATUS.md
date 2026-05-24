# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 02:01:02 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2404M / 3000M (80.1%) |
| Step | 146730 |
| Latest loss | 2.3295 |
| Avg loss (last 30 logged) | 2.0961 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 13:15:21 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.22 -> 2.04 -> 1.79 -> 1.96 -> 2.31 -> 2.01 -> 2.10 -> 1.84 -> 1.75 -> 1.85 -> 1.95 -> 1.75

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=146620 tokens=2402.2M loss=1.9848 lr=5.60e-05 tok/s=12489
[train] step=146630 tokens=2402.4M loss=2.0101 lr=5.60e-05 tok/s=12489
[train] step=146640 tokens=2402.5M loss=2.0927 lr=5.60e-05 tok/s=12489
[train] step=146650 tokens=2402.7M loss=1.9245 lr=5.60e-05 tok/s=12489
[train] step=146660 tokens=2402.9M loss=1.9626 lr=5.60e-05 tok/s=12489
[train] step=146670 tokens=2403.0M loss=1.7093 lr=5.59e-05 tok/s=12489
[train] step=146680 tokens=2403.2M loss=1.9514 lr=5.59e-05 tok/s=12489
[train] step=146690 tokens=2403.4M loss=1.9674 lr=5.59e-05 tok/s=12489
[train] step=146700 tokens=2403.5M loss=1.8537 lr=5.59e-05 tok/s=12489
[train] step=146710 tokens=2403.7M loss=1.7463 lr=5.59e-05 tok/s=12489
[train] step=146720 tokens=2403.9M loss=2.4814 lr=5.59e-05 tok/s=12489
[train] step=146730 tokens=2404.0M loss=2.3295 lr=5.59e-05 tok/s=12489
```
