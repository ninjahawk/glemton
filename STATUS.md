# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 12:35:22 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 721M / 3000M (24.0%) |
| Step | 44000 |
| Latest loss | 2.2987 |
| Avg loss (last 30 logged) | 2.3473 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 2:42:56 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.71 -> 2.10 -> 2.34 -> 2.16 -> 2.71 -> 2.15 -> 2.65 -> 2.16 -> 2.40 -> 2.15 -> 2.07 -> 2.29

## Checkpoints on disk
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`

## Recent log tail
```
[train] step=43890 tokens=719.1M loss=2.2127 lr=2.65e-04 tok/s=12483
[train] step=43900 tokens=719.3M loss=2.5627 lr=2.65e-04 tok/s=12483
[train] step=43910 tokens=719.4M loss=2.5344 lr=2.65e-04 tok/s=12483
[train] step=43920 tokens=719.6M loss=2.7110 lr=2.65e-04 tok/s=12483
[train] step=43930 tokens=719.7M loss=2.2982 lr=2.65e-04 tok/s=12483
[train] step=43940 tokens=719.9M loss=2.1550 lr=2.65e-04 tok/s=12483
[train] step=43950 tokens=720.1M loss=2.3077 lr=2.65e-04 tok/s=12483
[train] step=43960 tokens=720.2M loss=2.3144 lr=2.65e-04 tok/s=12483
[train] step=43970 tokens=720.4M loss=2.6599 lr=2.65e-04 tok/s=12483
[train] step=43980 tokens=720.6M loss=2.2878 lr=2.65e-04 tok/s=12483
[train] step=43990 tokens=720.7M loss=2.1236 lr=2.65e-04 tok/s=12483
[train] step=44000 tokens=720.9M loss=2.2987 lr=2.65e-04 tok/s=12483
```
