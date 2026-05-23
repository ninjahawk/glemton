# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 16:29:35 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1976M / 3000M (65.9%) |
| Step | 120600 |
| Latest loss | 2.2659 |
| Avg loss (last 30 logged) | 2.0494 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 22:46:40 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.96 -> 2.03 -> 1.93 -> 2.42 -> 1.81 -> 2.23 -> 2.58 -> 1.75 -> 2.08 -> 2.36 -> 1.63 -> 2.15

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=120490 tokens=1974.1M loss=2.0297 lr=1.02e-04 tok/s=12489
[train] step=120500 tokens=1974.3M loss=2.1872 lr=1.02e-04 tok/s=12489
[train] step=120510 tokens=1974.4M loss=2.6157 lr=1.02e-04 tok/s=12489
[train] step=120520 tokens=1974.6M loss=1.7806 lr=1.02e-04 tok/s=12489
[train] step=120530 tokens=1974.8M loss=2.1453 lr=1.02e-04 tok/s=12489
[train] step=120540 tokens=1974.9M loss=1.7489 lr=1.02e-04 tok/s=12489
[train] step=120550 tokens=1975.1M loss=2.2221 lr=1.02e-04 tok/s=12489
[train] step=120560 tokens=1975.3M loss=1.7728 lr=1.02e-04 tok/s=12489
[train] step=120570 tokens=1975.4M loss=2.1514 lr=1.02e-04 tok/s=12489
[train] step=120580 tokens=1975.6M loss=2.5184 lr=1.02e-04 tok/s=12489
[train] step=120590 tokens=1975.7M loss=2.1103 lr=1.02e-04 tok/s=12489
[train] step=120600 tokens=1975.9M loss=2.2659 lr=1.02e-04 tok/s=12489
```
