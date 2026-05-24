# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 01:30:58 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2382M / 3000M (79.4%) |
| Step | 145360 |
| Latest loss | 1.7854 |
| Avg loss (last 30 logged) | 2.0352 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 13:45:15 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.12 -> 1.97 -> 2.16 -> 2.11 -> 1.96 -> 2.33 -> 1.67 -> 2.21 -> 2.38 -> 1.84 -> 1.80 -> 1.96

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
[train] step=145250 tokens=2379.8M loss=2.2723 lr=5.79e-05 tok/s=12489
[train] step=145260 tokens=2379.9M loss=2.2073 lr=5.79e-05 tok/s=12489
[train] step=145270 tokens=2380.1M loss=1.7128 lr=5.79e-05 tok/s=12489
[train] step=145280 tokens=2380.3M loss=2.4330 lr=5.79e-05 tok/s=12489
[train] step=145290 tokens=2380.4M loss=2.1155 lr=5.79e-05 tok/s=12489
[train] step=145300 tokens=2380.6M loss=2.0903 lr=5.79e-05 tok/s=12489
[train] step=145310 tokens=2380.8M loss=1.9328 lr=5.78e-05 tok/s=12489
[train] step=145320 tokens=2380.9M loss=1.7665 lr=5.78e-05 tok/s=12489
[train] step=145330 tokens=2381.1M loss=1.9572 lr=5.78e-05 tok/s=12489
[train] step=145340 tokens=2381.3M loss=2.2343 lr=5.78e-05 tok/s=12489
[train] step=145350 tokens=2381.4M loss=1.7609 lr=5.78e-05 tok/s=12489
[train] step=145360 tokens=2381.6M loss=1.7854 lr=5.78e-05 tok/s=12489
```
