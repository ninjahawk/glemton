# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 04:54:04 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 376M / 3000M (12.5%) |
| Step | 22920 |
| Latest loss | 2.5127 |
| Avg loss (last 30 logged) | 2.5115 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 2 days, 10:22:58 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.22 -> 2.56 -> 2.28 -> 2.51 -> 2.27 -> 2.30 -> 2.20 -> 2.41 -> 2.45 -> 2.47 -> 2.43 -> 2.40

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=22810 tokens=373.7M loss=2.5449 lr=2.91e-04 tok/s=12487
[train] step=22820 tokens=373.9M loss=2.4400 lr=2.91e-04 tok/s=12487
[train] step=22830 tokens=374.0M loss=2.6524 lr=2.91e-04 tok/s=12487
[train] step=22840 tokens=374.2M loss=2.6991 lr=2.91e-04 tok/s=12487
[train] step=22850 tokens=374.4M loss=2.4583 lr=2.91e-04 tok/s=12487
[train] step=22860 tokens=374.5M loss=2.4840 lr=2.91e-04 tok/s=12487
[train] step=22870 tokens=374.7M loss=2.9034 lr=2.91e-04 tok/s=12487
[train] step=22880 tokens=374.9M loss=2.4222 lr=2.91e-04 tok/s=12487
[train] step=22890 tokens=375.0M loss=2.4047 lr=2.91e-04 tok/s=12487
[train] step=22900 tokens=375.2M loss=2.6770 lr=2.91e-04 tok/s=12487
[train] step=22910 tokens=375.4M loss=2.5477 lr=2.91e-04 tok/s=12487
[train] step=22920 tokens=375.5M loss=2.5127 lr=2.91e-04 tok/s=12487
```
