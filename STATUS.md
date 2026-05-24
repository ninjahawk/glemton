# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 20:50:15 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2171M / 3000M (72.4%) |
| Step | 132520 |
| Latest loss | 2.3646 |
| Avg loss (last 30 logged) | 2.0431 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 18:26:02 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.94 -> 2.04 -> 2.00 -> 2.02 -> 1.82 -> 1.90 -> 2.23 -> 2.24 -> 2.39 -> 2.27 -> 2.21 -> 1.76

## Checkpoints on disk
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=132410 tokens=2169.4M loss=1.8900 lr=7.87e-05 tok/s=12490
[train] step=132420 tokens=2169.6M loss=2.1051 lr=7.87e-05 tok/s=12490
[train] step=132430 tokens=2169.7M loss=2.4151 lr=7.86e-05 tok/s=12490
[train] step=132440 tokens=2169.9M loss=2.2098 lr=7.86e-05 tok/s=12489
[train] step=132450 tokens=2170.1M loss=1.6313 lr=7.86e-05 tok/s=12489
[train] step=132460 tokens=2170.2M loss=1.9399 lr=7.86e-05 tok/s=12489
[train] step=132470 tokens=2170.4M loss=2.1902 lr=7.86e-05 tok/s=12489
[train] step=132480 tokens=2170.6M loss=2.0813 lr=7.86e-05 tok/s=12489
[train] step=132490 tokens=2170.7M loss=1.7593 lr=7.85e-05 tok/s=12489
[train] step=132500 tokens=2170.9M loss=2.2372 lr=7.85e-05 tok/s=12489
[train] step=132510 tokens=2171.0M loss=1.9768 lr=7.85e-05 tok/s=12489
[train] step=132520 tokens=2171.2M loss=2.3646 lr=7.85e-05 tok/s=12489
```
