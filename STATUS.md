# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 07:01:49 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2629M / 3000M (87.6%) |
| Step | 160480 |
| Latest loss | 2.0732 |
| Avg loss (last 30 logged) | 2.0971 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 8:14:42 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.92 -> 1.79 -> 2.08 -> 1.88 -> 2.26 -> 1.82 -> 2.21 -> 1.69 -> 1.61 -> 1.96 -> 1.81 -> 2.03

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
[train] step=160370 tokens=2627.5M loss=1.8089 lr=4.03e-05 tok/s=12489
[train] step=160380 tokens=2627.7M loss=2.4616 lr=4.03e-05 tok/s=12489
[train] step=160390 tokens=2627.8M loss=2.1133 lr=4.03e-05 tok/s=12489
[train] step=160400 tokens=2628.0M loss=1.8499 lr=4.03e-05 tok/s=12489
[train] step=160410 tokens=2628.2M loss=2.4620 lr=4.03e-05 tok/s=12489
[train] step=160420 tokens=2628.3M loss=1.5982 lr=4.03e-05 tok/s=12489
[train] step=160430 tokens=2628.5M loss=2.1939 lr=4.03e-05 tok/s=12489
[train] step=160440 tokens=2628.6M loss=2.0416 lr=4.02e-05 tok/s=12489
[train] step=160450 tokens=2628.8M loss=2.0822 lr=4.02e-05 tok/s=12489
[train] step=160460 tokens=2629.0M loss=2.0322 lr=4.02e-05 tok/s=12489
[train] step=160470 tokens=2629.1M loss=1.5770 lr=4.02e-05 tok/s=12489
[train] step=160480 tokens=2629.3M loss=2.0732 lr=4.02e-05 tok/s=12489
```
