# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 01:20:56 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2374M / 3000M (79.1%) |
| Step | 144900 |
| Latest loss | 2.2492 |
| Avg loss (last 30 logged) | 2.0899 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 13:55:24 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.73 -> 2.13 -> 2.21 -> 2.63 -> 2.22 -> 1.96 -> 2.35 -> 2.01 -> 2.41 -> 2.25 -> 1.89 -> 2.30

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
[train] step=144790 tokens=2372.2M loss=2.0711 lr=5.86e-05 tok/s=12489
[train] step=144800 tokens=2372.4M loss=2.2069 lr=5.86e-05 tok/s=12489
[train] step=144810 tokens=2372.6M loss=1.9139 lr=5.86e-05 tok/s=12489
[train] step=144820 tokens=2372.7M loss=2.0707 lr=5.85e-05 tok/s=12489
[train] step=144830 tokens=2372.9M loss=2.0729 lr=5.85e-05 tok/s=12489
[train] step=144840 tokens=2373.1M loss=2.1685 lr=5.85e-05 tok/s=12489
[train] step=144850 tokens=2373.2M loss=2.3888 lr=5.85e-05 tok/s=12489
[train] step=144860 tokens=2373.4M loss=2.5303 lr=5.85e-05 tok/s=12489
[train] step=144870 tokens=2373.6M loss=2.3043 lr=5.85e-05 tok/s=12489
[train] step=144880 tokens=2373.7M loss=2.4824 lr=5.85e-05 tok/s=12489
[train] step=144890 tokens=2373.9M loss=1.8483 lr=5.84e-05 tok/s=12489
[train] step=144900 tokens=2374.0M loss=2.2492 lr=5.84e-05 tok/s=12489
```
