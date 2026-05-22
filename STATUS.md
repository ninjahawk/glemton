# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 00:03:15 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 158M / 3000M (5.3%) |
| Step | 9620 |
| Latest loss | 2.4235 |
| Avg loss (last 30 logged) | 2.6243 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 2 days, 15:12:54 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.70 -> 2.62 -> 3.33 -> 2.94 -> 2.72 -> 2.79 -> 3.24 -> 2.69 -> 2.51 -> 2.82 -> 2.62 -> 2.37

## Checkpoints on disk
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=9510 tokens=155.8M loss=2.6656 lr=2.99e-04 tok/s=12490
[train] step=9520 tokens=156.0M loss=3.1018 lr=2.99e-04 tok/s=12490
[train] step=9530 tokens=156.1M loss=2.2654 lr=2.99e-04 tok/s=12490
[train] step=9540 tokens=156.3M loss=2.6356 lr=2.99e-04 tok/s=12490
[train] step=9550 tokens=156.5M loss=2.3809 lr=2.99e-04 tok/s=12490
[train] step=9560 tokens=156.6M loss=2.9273 lr=2.99e-04 tok/s=12490
[train] step=9570 tokens=156.8M loss=2.4330 lr=2.99e-04 tok/s=12490
[train] step=9580 tokens=157.0M loss=2.8133 lr=2.99e-04 tok/s=12490
[train] step=9590 tokens=157.1M loss=2.9771 lr=2.99e-04 tok/s=12490
[train] step=9600 tokens=157.3M loss=2.3680 lr=2.99e-04 tok/s=12490
[train] step=9610 tokens=157.5M loss=2.6501 lr=2.99e-04 tok/s=12490
[train] step=9620 tokens=157.6M loss=2.4235 lr=2.99e-04 tok/s=12490
```
