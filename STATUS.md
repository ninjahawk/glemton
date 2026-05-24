# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 02:31:07 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2427M / 3000M (80.9%) |
| Step | 148110 |
| Latest loss | 2.1052 |
| Avg loss (last 30 logged) | 2.1543 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 12:45:12 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.76 -> 2.07 -> 2.18 -> 1.69 -> 2.26 -> 2.55 -> 2.32 -> 2.22 -> 2.32 -> 2.11 -> 2.45 -> 1.80

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
[train] step=148000 tokens=2424.8M loss=2.6420 lr=5.41e-05 tok/s=12489
[train] step=148010 tokens=2425.0M loss=2.2516 lr=5.41e-05 tok/s=12489
[train] step=148020 tokens=2425.2M loss=1.7997 lr=5.41e-05 tok/s=12489
[train] step=148030 tokens=2425.3M loss=2.6563 lr=5.41e-05 tok/s=12489
[train] step=148040 tokens=2425.5M loss=2.2925 lr=5.41e-05 tok/s=12489
[train] step=148050 tokens=2425.7M loss=1.9834 lr=5.41e-05 tok/s=12489
[train] step=148060 tokens=2425.8M loss=1.9022 lr=5.41e-05 tok/s=12489
[train] step=148070 tokens=2426.0M loss=1.8833 lr=5.41e-05 tok/s=12489
[train] step=148080 tokens=2426.1M loss=2.0427 lr=5.40e-05 tok/s=12489
[train] step=148090 tokens=2426.3M loss=1.8044 lr=5.40e-05 tok/s=12489
[train] step=148100 tokens=2426.5M loss=2.7365 lr=5.40e-05 tok/s=12489
[train] step=148110 tokens=2426.6M loss=2.1052 lr=5.40e-05 tok/s=12489
```
