# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 10:24:59 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 623M / 3000M (20.8%) |
| Step | 38040 |
| Latest loss | 2.4934 |
| Avg loss (last 30 logged) | 2.3595 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 4:53:22 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.62 -> 2.74 -> 2.21 -> 2.54 -> 2.20 -> 2.53 -> 2.26 -> 2.09 -> 2.22 -> 2.44 -> 2.56 -> 2.43

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=37930 tokens=621.4M loss=2.4075 lr=2.74e-04 tok/s=12483
[train] step=37940 tokens=621.6M loss=2.3299 lr=2.74e-04 tok/s=12483
[train] step=37950 tokens=621.8M loss=2.5891 lr=2.74e-04 tok/s=12483
[train] step=37960 tokens=621.9M loss=2.4141 lr=2.74e-04 tok/s=12483
[train] step=37970 tokens=622.1M loss=2.3060 lr=2.74e-04 tok/s=12483
[train] step=37980 tokens=622.3M loss=2.4677 lr=2.74e-04 tok/s=12483
[train] step=37990 tokens=622.4M loss=2.1855 lr=2.74e-04 tok/s=12483
[train] step=38000 tokens=622.6M loss=2.3073 lr=2.74e-04 tok/s=12483
[train] step=38010 tokens=622.8M loss=2.5240 lr=2.74e-04 tok/s=12483
[train] step=38020 tokens=622.9M loss=2.4282 lr=2.74e-04 tok/s=12483
[train] step=38030 tokens=623.1M loss=2.2664 lr=2.74e-04 tok/s=12483
[train] step=38040 tokens=623.2M loss=2.4934 lr=2.74e-04 tok/s=12483
```
