# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 18:09:50 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2051M / 3000M (68.4%) |
| Step | 125180 |
| Latest loss | 2.2353 |
| Avg loss (last 30 logged) | 2.0610 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 21:06:28 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.11 -> 2.80 -> 2.51 -> 2.58 -> 1.81 -> 2.43 -> 2.01 -> 2.05 -> 1.93 -> 2.28 -> 2.08 -> 1.64

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=125070 tokens=2049.1M loss=1.8958 lr=9.25e-05 tok/s=12490
[train] step=125080 tokens=2049.3M loss=1.9276 lr=9.25e-05 tok/s=12490
[train] step=125090 tokens=2049.5M loss=2.0127 lr=9.25e-05 tok/s=12490
[train] step=125100 tokens=2049.6M loss=2.0011 lr=9.25e-05 tok/s=12490
[train] step=125110 tokens=2049.8M loss=1.6374 lr=9.24e-05 tok/s=12490
[train] step=125120 tokens=2050.0M loss=1.9954 lr=9.24e-05 tok/s=12490
[train] step=125130 tokens=2050.1M loss=1.9146 lr=9.24e-05 tok/s=12490
[train] step=125140 tokens=2050.3M loss=2.2975 lr=9.24e-05 tok/s=12490
[train] step=125150 tokens=2050.5M loss=1.9782 lr=9.24e-05 tok/s=12490
[train] step=125160 tokens=2050.6M loss=1.6418 lr=9.23e-05 tok/s=12490
[train] step=125170 tokens=2050.8M loss=1.8202 lr=9.23e-05 tok/s=12490
[train] step=125180 tokens=2050.9M loss=2.2353 lr=9.23e-05 tok/s=12490
```
