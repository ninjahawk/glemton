# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 18:59:58 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2089M / 3000M (69.6%) |
| Step | 127480 |
| Latest loss | 1.9297 |
| Avg loss (last 30 logged) | 2.0670 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 20:16:10 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.12 -> 2.12 -> 2.58 -> 2.20 -> 2.30 -> 1.95 -> 1.75 -> 1.97 -> 2.16 -> 1.86 -> 2.09 -> 2.16

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
[train] step=127370 tokens=2086.8M loss=2.1428 lr=8.81e-05 tok/s=12490
[train] step=127380 tokens=2087.0M loss=2.0149 lr=8.80e-05 tok/s=12490
[train] step=127390 tokens=2087.2M loss=2.3652 lr=8.80e-05 tok/s=12490
[train] step=127400 tokens=2087.3M loss=1.7558 lr=8.80e-05 tok/s=12490
[train] step=127410 tokens=2087.5M loss=2.1672 lr=8.80e-05 tok/s=12490
[train] step=127420 tokens=2087.6M loss=2.1654 lr=8.80e-05 tok/s=12490
[train] step=127430 tokens=2087.8M loss=2.1112 lr=8.79e-05 tok/s=12490
[train] step=127440 tokens=2088.0M loss=1.9031 lr=8.79e-05 tok/s=12490
[train] step=127450 tokens=2088.1M loss=2.1573 lr=8.79e-05 tok/s=12490
[train] step=127460 tokens=2088.3M loss=2.3846 lr=8.79e-05 tok/s=12490
[train] step=127470 tokens=2088.5M loss=1.6994 lr=8.79e-05 tok/s=12490
[train] step=127480 tokens=2088.6M loss=1.9297 lr=8.78e-05 tok/s=12490
```
