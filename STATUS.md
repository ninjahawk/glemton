# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 01:33:31 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 225M / 3000M (7.5%) |
| Step | 13750 |
| Latest loss | 2.4342 |
| Avg loss (last 30 logged) | 2.5390 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 2 days, 13:42:33 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.96 -> 2.71 -> 2.87 -> 2.50 -> 2.66 -> 2.43 -> 2.31 -> 2.52 -> 2.62 -> 2.34 -> 2.43 -> 2.51

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=13640 tokens=223.5M loss=2.6651 lr=2.97e-04 tok/s=12490
[train] step=13650 tokens=223.6M loss=2.2695 lr=2.97e-04 tok/s=12490
[train] step=13660 tokens=223.8M loss=2.3700 lr=2.97e-04 tok/s=12490
[train] step=13670 tokens=224.0M loss=2.4156 lr=2.97e-04 tok/s=12490
[train] step=13680 tokens=224.1M loss=2.6394 lr=2.97e-04 tok/s=12490
[train] step=13690 tokens=224.3M loss=2.9202 lr=2.97e-04 tok/s=12490
[train] step=13700 tokens=224.5M loss=2.7805 lr=2.97e-04 tok/s=12490
[train] step=13710 tokens=224.6M loss=2.8910 lr=2.97e-04 tok/s=12490
[train] step=13720 tokens=224.8M loss=2.2072 lr=2.97e-04 tok/s=12490
[train] step=13730 tokens=225.0M loss=2.5112 lr=2.97e-04 tok/s=12490
[train] step=13740 tokens=225.1M loss=2.4644 lr=2.97e-04 tok/s=12490
[train] step=13750 tokens=225.3M loss=2.4342 lr=2.97e-04 tok/s=12490
```
