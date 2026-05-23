# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 15:19:24 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1923M / 3000M (64.1%) |
| Step | 117390 |
| Latest loss | 2.0520 |
| Avg loss (last 30 logged) | 2.1193 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 23:56:51 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.88 -> 2.30 -> 2.31 -> 2.33 -> 2.45 -> 2.14 -> 1.83 -> 1.92 -> 1.72 -> 2.52 -> 2.18 -> 2.13

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
[train] step=117280 tokens=1921.5M loss=2.4630 lr=1.08e-04 tok/s=12489
[train] step=117290 tokens=1921.7M loss=2.4310 lr=1.08e-04 tok/s=12489
[train] step=117300 tokens=1921.8M loss=2.2094 lr=1.08e-04 tok/s=12489
[train] step=117310 tokens=1922.0M loss=2.0279 lr=1.08e-04 tok/s=12489
[train] step=117320 tokens=1922.2M loss=2.1159 lr=1.08e-04 tok/s=12489
[train] step=117330 tokens=1922.3M loss=1.9519 lr=1.08e-04 tok/s=12489
[train] step=117340 tokens=1922.5M loss=2.5821 lr=1.08e-04 tok/s=12489
[train] step=117350 tokens=1922.7M loss=1.7139 lr=1.08e-04 tok/s=12489
[train] step=117360 tokens=1922.8M loss=2.1862 lr=1.08e-04 tok/s=12489
[train] step=117370 tokens=1923.0M loss=2.1342 lr=1.08e-04 tok/s=12489
[train] step=117380 tokens=1923.2M loss=2.2261 lr=1.08e-04 tok/s=12489
[train] step=117390 tokens=1923.3M loss=2.0520 lr=1.08e-04 tok/s=12489
```
