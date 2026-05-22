# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 02:43:43 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 278M / 3000M (9.3%) |
| Step | 16960 |
| Latest loss | 2.3794 |
| Avg loss (last 30 logged) | 2.5405 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 2 days, 12:32:22 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.46 -> 2.84 -> 2.90 -> 2.67 -> 2.48 -> 2.13 -> 2.64 -> 2.44 -> 2.40 -> 2.49 -> 2.20 -> 2.70

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=16850 tokens=276.1M loss=2.3935 lr=2.95e-04 tok/s=12490
[train] step=16860 tokens=276.2M loss=2.4558 lr=2.95e-04 tok/s=12490
[train] step=16870 tokens=276.4M loss=2.5698 lr=2.95e-04 tok/s=12490
[train] step=16880 tokens=276.6M loss=2.5814 lr=2.95e-04 tok/s=12490
[train] step=16890 tokens=276.7M loss=2.5315 lr=2.95e-04 tok/s=12490
[train] step=16900 tokens=276.9M loss=2.5951 lr=2.95e-04 tok/s=12490
[train] step=16910 tokens=277.1M loss=2.5072 lr=2.95e-04 tok/s=12490
[train] step=16920 tokens=277.2M loss=2.4316 lr=2.95e-04 tok/s=12490
[train] step=16930 tokens=277.4M loss=2.6966 lr=2.95e-04 tok/s=12490
[train] step=16940 tokens=277.5M loss=2.5870 lr=2.95e-04 tok/s=12490
[train] step=16950 tokens=277.7M loss=2.5055 lr=2.95e-04 tok/s=12490
[train] step=16960 tokens=277.9M loss=2.3794 lr=2.95e-04 tok/s=12490
```
