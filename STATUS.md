# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 03:03:46 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 293M / 3000M (9.8%) |
| Step | 17880 |
| Latest loss | 2.4668 |
| Avg loss (last 30 logged) | 2.4950 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 2 days, 12:12:38 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.91 -> 2.57 -> 2.42 -> 2.68 -> 2.42 -> 2.87 -> 2.76 -> 2.48 -> 2.46 -> 2.31 -> 2.72 -> 2.60

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=17770 tokens=291.1M loss=2.7049 lr=2.95e-04 tok/s=12489
[train] step=17780 tokens=291.3M loss=2.9491 lr=2.95e-04 tok/s=12489
[train] step=17790 tokens=291.5M loss=2.3861 lr=2.95e-04 tok/s=12489
[train] step=17800 tokens=291.6M loss=2.5562 lr=2.95e-04 tok/s=12489
[train] step=17810 tokens=291.8M loss=2.5362 lr=2.95e-04 tok/s=12489
[train] step=17820 tokens=292.0M loss=2.5222 lr=2.95e-04 tok/s=12489
[train] step=17830 tokens=292.1M loss=2.3246 lr=2.95e-04 tok/s=12489
[train] step=17840 tokens=292.3M loss=2.6018 lr=2.95e-04 tok/s=12489
[train] step=17850 tokens=292.5M loss=2.5988 lr=2.95e-04 tok/s=12489
[train] step=17860 tokens=292.6M loss=2.5130 lr=2.95e-04 tok/s=12489
[train] step=17870 tokens=292.8M loss=2.8178 lr=2.95e-04 tok/s=12489
[train] step=17880 tokens=292.9M loss=2.4668 lr=2.95e-04 tok/s=12489
```
