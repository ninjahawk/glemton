# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 02:51:10 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2442M / 3000M (81.4%) |
| Step | 149020 |
| Latest loss | 2.2732 |
| Avg loss (last 30 logged) | 2.0157 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 12:25:19 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.92 -> 2.09 -> 1.69 -> 1.84 -> 1.97 -> 2.17 -> 1.99 -> 2.24 -> 2.25 -> 2.14 -> 2.12 -> 1.86

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
[train] step=148910 tokens=2439.7M loss=2.3282 lr=5.29e-05 tok/s=12489
[train] step=148920 tokens=2439.9M loss=2.0223 lr=5.29e-05 tok/s=12489
[train] step=148930 tokens=2440.1M loss=1.8416 lr=5.29e-05 tok/s=12489
[train] step=148940 tokens=2440.2M loss=2.3885 lr=5.29e-05 tok/s=12489
[train] step=148950 tokens=2440.4M loss=2.2173 lr=5.29e-05 tok/s=12489
[train] step=148960 tokens=2440.6M loss=1.7739 lr=5.29e-05 tok/s=12489
[train] step=148970 tokens=2440.7M loss=2.1542 lr=5.29e-05 tok/s=12489
[train] step=148980 tokens=2440.9M loss=1.9909 lr=5.29e-05 tok/s=12489
[train] step=148990 tokens=2441.1M loss=2.1750 lr=5.28e-05 tok/s=12489
[train] step=149000 tokens=2441.2M loss=1.8621 lr=5.28e-05 tok/s=12489
[train] step=149010 tokens=2441.4M loss=2.1229 lr=5.28e-05 tok/s=12489
[train] step=149020 tokens=2441.5M loss=2.2732 lr=5.28e-05 tok/s=12489
```
