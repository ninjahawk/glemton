# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 22:00:25 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2224M / 3000M (74.1%) |
| Step | 135730 |
| Latest loss | 2.2547 |
| Avg loss (last 30 logged) | 2.0248 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 17:15:50 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.61 -> 1.89 -> 2.14 -> 2.10 -> 1.74 -> 2.47 -> 1.51 -> 2.06 -> 2.46 -> 2.05 -> 2.01 -> 1.94

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
[train] step=135620 tokens=2222.0M loss=1.8182 lr=7.31e-05 tok/s=12489
[train] step=135630 tokens=2222.2M loss=1.8254 lr=7.30e-05 tok/s=12489
[train] step=135640 tokens=2222.3M loss=1.6564 lr=7.30e-05 tok/s=12489
[train] step=135650 tokens=2222.5M loss=1.9350 lr=7.30e-05 tok/s=12489
[train] step=135660 tokens=2222.7M loss=1.7856 lr=7.30e-05 tok/s=12489
[train] step=135670 tokens=2222.8M loss=2.0446 lr=7.30e-05 tok/s=12489
[train] step=135680 tokens=2223.0M loss=2.2779 lr=7.30e-05 tok/s=12489
[train] step=135690 tokens=2223.1M loss=2.0702 lr=7.29e-05 tok/s=12489
[train] step=135700 tokens=2223.3M loss=2.2700 lr=7.29e-05 tok/s=12489
[train] step=135710 tokens=2223.5M loss=1.9382 lr=7.29e-05 tok/s=12489
[train] step=135720 tokens=2223.6M loss=2.2111 lr=7.29e-05 tok/s=12489
[train] step=135730 tokens=2223.8M loss=2.2547 lr=7.29e-05 tok/s=12489
```
