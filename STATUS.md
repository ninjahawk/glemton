# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 03:13:47 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 300M / 3000M (10.0%) |
| Step | 18340 |
| Latest loss | 2.7751 |
| Avg loss (last 30 logged) | 2.5498 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 2 days, 12:02:30 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.55 -> 2.70 -> 2.59 -> 2.56 -> 2.42 -> 2.75 -> 2.23 -> 2.19 -> 2.67 -> 2.67 -> 2.42 -> 2.45

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=18240 tokens=298.8M loss=2.5627 lr=2.94e-04 tok/s=12489
[train] step=18250 tokens=299.0M loss=2.9646 lr=2.94e-04 tok/s=12489
[train] step=18260 tokens=299.2M loss=2.4425 lr=2.94e-04 tok/s=12489
[train] step=18270 tokens=299.3M loss=2.5399 lr=2.94e-04 tok/s=12489
[train] step=18280 tokens=299.5M loss=2.9311 lr=2.94e-04 tok/s=12489
[train] step=18290 tokens=299.7M loss=2.3023 lr=2.94e-04 tok/s=12489
[train] step=18300 tokens=299.8M loss=2.2986 lr=2.94e-04 tok/s=12489
[train] step=18310 tokens=300.0M loss=2.3187 lr=2.94e-04 tok/s=12489
[train] checkpoint -> checkpoints\glemton-350m\step_18311_tokens_300M.pt
[train] step=18320 tokens=300.2M loss=2.4529 lr=2.94e-04 tok/s=12489
[train] step=18330 tokens=300.3M loss=2.3272 lr=2.94e-04 tok/s=12489
[train] step=18340 tokens=300.5M loss=2.7751 lr=2.94e-04 tok/s=12489
```
