# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 19:20:01 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2104M / 3000M (70.1%) |
| Step | 128390 |
| Latest loss | 1.8359 |
| Avg loss (last 30 logged) | 2.0246 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 19:56:17 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.87 -> 1.90 -> 1.99 -> 1.84 -> 1.92 -> 2.12 -> 2.01 -> 1.74 -> 2.01 -> 1.75 -> 2.16 -> 1.90

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=128280 tokens=2101.7M loss=1.9048 lr=8.63e-05 tok/s=12490
[train] step=128290 tokens=2101.9M loss=1.8979 lr=8.63e-05 tok/s=12490
[train] step=128300 tokens=2102.1M loss=2.1354 lr=8.63e-05 tok/s=12490
[train] step=128310 tokens=2102.2M loss=1.9710 lr=8.63e-05 tok/s=12490
[train] step=128320 tokens=2102.4M loss=2.2479 lr=8.62e-05 tok/s=12490
[train] step=128330 tokens=2102.6M loss=2.0878 lr=8.62e-05 tok/s=12490
[train] step=128340 tokens=2102.7M loss=1.7809 lr=8.62e-05 tok/s=12490
[train] step=128350 tokens=2102.9M loss=2.1196 lr=8.62e-05 tok/s=12490
[train] step=128360 tokens=2103.1M loss=1.9494 lr=8.62e-05 tok/s=12490
[train] step=128370 tokens=2103.2M loss=1.9034 lr=8.61e-05 tok/s=12490
[train] step=128380 tokens=2103.4M loss=2.1944 lr=8.61e-05 tok/s=12490
[train] step=128390 tokens=2103.5M loss=1.8359 lr=8.61e-05 tok/s=12490
```
