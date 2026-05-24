# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 01:10:55 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2366M / 3000M (78.9%) |
| Step | 144440 |
| Latest loss | 1.6840 |
| Avg loss (last 30 logged) | 2.1506 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 14:05:24 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.18 -> 1.68 -> 2.20 -> 2.11 -> 1.56 -> 2.32 -> 2.37 -> 2.46 -> 2.11 -> 2.91 -> 2.17 -> 1.73

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
[train] step=144330 tokens=2364.7M loss=1.9930 lr=5.93e-05 tok/s=12489
[train] step=144340 tokens=2364.9M loss=2.3755 lr=5.92e-05 tok/s=12489
[train] step=144350 tokens=2365.0M loss=2.1414 lr=5.92e-05 tok/s=12489
[train] step=144360 tokens=2365.2M loss=2.1345 lr=5.92e-05 tok/s=12489
[train] step=144370 tokens=2365.4M loss=2.3133 lr=5.92e-05 tok/s=12489
[train] step=144380 tokens=2365.5M loss=2.0835 lr=5.92e-05 tok/s=12489
[train] step=144390 tokens=2365.7M loss=2.2343 lr=5.92e-05 tok/s=12489
[train] step=144400 tokens=2365.8M loss=2.3101 lr=5.92e-05 tok/s=12489
[train] step=144410 tokens=2366.0M loss=1.7284 lr=5.91e-05 tok/s=12489
[train] step=144420 tokens=2366.2M loss=1.8985 lr=5.91e-05 tok/s=12489
[train] step=144430 tokens=2366.3M loss=2.4381 lr=5.91e-05 tok/s=12489
[train] step=144440 tokens=2366.5M loss=1.6840 lr=5.91e-05 tok/s=12489
```
