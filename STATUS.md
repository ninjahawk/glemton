# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 18:19:52 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2058M / 3000M (68.6%) |
| Step | 125640 |
| Latest loss | 2.0412 |
| Avg loss (last 30 logged) | 2.0426 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 20:56:20 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.19 -> 2.12 -> 1.79 -> 2.45 -> 2.25 -> 1.64 -> 2.13 -> 1.76 -> 2.01 -> 1.82 -> 2.34 -> 2.17

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
[train] step=125530 tokens=2056.7M loss=1.8355 lr=9.16e-05 tok/s=12490
[train] step=125540 tokens=2056.8M loss=2.1651 lr=9.16e-05 tok/s=12490
[train] step=125550 tokens=2057.0M loss=2.0132 lr=9.16e-05 tok/s=12490
[train] step=125560 tokens=2057.2M loss=1.9714 lr=9.16e-05 tok/s=12490
[train] step=125570 tokens=2057.3M loss=1.9038 lr=9.15e-05 tok/s=12490
[train] step=125580 tokens=2057.5M loss=2.5187 lr=9.15e-05 tok/s=12490
[train] step=125590 tokens=2057.7M loss=1.9925 lr=9.15e-05 tok/s=12490
[train] step=125600 tokens=2057.8M loss=1.5066 lr=9.15e-05 tok/s=12490
[train] step=125610 tokens=2058.0M loss=1.8858 lr=9.15e-05 tok/s=12490
[train] step=125620 tokens=2058.2M loss=2.1695 lr=9.14e-05 tok/s=12490
[train] step=125630 tokens=2058.3M loss=1.6491 lr=9.14e-05 tok/s=12490
[train] step=125640 tokens=2058.5M loss=2.0412 lr=9.14e-05 tok/s=12490
```
