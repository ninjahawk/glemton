# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 04:01:21 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2494M / 3000M (83.1%) |
| Step | 152230 |
| Latest loss | 2.6240 |
| Avg loss (last 30 logged) | 2.1551 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 11:15:07 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.41 -> 2.46 -> 2.05 -> 1.70 -> 2.13 -> 1.99 -> 2.79 -> 2.08 -> 2.08 -> 1.55 -> 2.21 -> 2.11

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
[train] step=152120 tokens=2492.3M loss=2.4342 lr=4.89e-05 tok/s=12489
[train] step=152130 tokens=2492.5M loss=1.9861 lr=4.89e-05 tok/s=12489
[train] step=152140 tokens=2492.7M loss=2.1194 lr=4.89e-05 tok/s=12489
[train] step=152150 tokens=2492.8M loss=2.0701 lr=4.89e-05 tok/s=12489
[train] step=152160 tokens=2493.0M loss=2.1958 lr=4.89e-05 tok/s=12489
[train] step=152170 tokens=2493.2M loss=1.8824 lr=4.89e-05 tok/s=12489
[train] step=152180 tokens=2493.3M loss=1.8059 lr=4.89e-05 tok/s=12489
[train] step=152190 tokens=2493.5M loss=1.9125 lr=4.89e-05 tok/s=12489
[train] step=152200 tokens=2493.6M loss=2.1146 lr=4.88e-05 tok/s=12489
[train] step=152210 tokens=2493.8M loss=2.5279 lr=4.88e-05 tok/s=12489
[train] step=152220 tokens=2494.0M loss=2.4667 lr=4.88e-05 tok/s=12489
[train] step=152230 tokens=2494.1M loss=2.6240 lr=4.88e-05 tok/s=12489
```
