# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 22:20:29 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2239M / 3000M (74.6%) |
| Step | 136640 |
| Latest loss | 2.4116 |
| Avg loss (last 30 logged) | 2.0359 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 16:55:57 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.34 -> 2.08 -> 2.11 -> 1.91 -> 1.59 -> 1.59 -> 1.87 -> 2.30 -> 1.83 -> 2.44 -> 2.00 -> 1.59

## Checkpoints on disk
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=136530 tokens=2236.9M loss=1.8829 lr=7.15e-05 tok/s=12489
[train] step=136540 tokens=2237.1M loss=1.6915 lr=7.15e-05 tok/s=12489
[train] step=136550 tokens=2237.2M loss=1.8786 lr=7.15e-05 tok/s=12489
[train] step=136560 tokens=2237.4M loss=2.1784 lr=7.15e-05 tok/s=12489
[train] step=136570 tokens=2237.6M loss=2.1139 lr=7.14e-05 tok/s=12489
[train] step=136580 tokens=2237.7M loss=1.9064 lr=7.14e-05 tok/s=12489
[train] step=136590 tokens=2237.9M loss=1.7049 lr=7.14e-05 tok/s=12489
[train] step=136600 tokens=2238.1M loss=1.8507 lr=7.14e-05 tok/s=12489
[train] step=136610 tokens=2238.2M loss=1.9433 lr=7.14e-05 tok/s=12489
[train] step=136620 tokens=2238.4M loss=1.5940 lr=7.14e-05 tok/s=12489
[train] step=136630 tokens=2238.5M loss=1.8991 lr=7.13e-05 tok/s=12489
[train] step=136640 tokens=2238.7M loss=2.4116 lr=7.13e-05 tok/s=12489
```
