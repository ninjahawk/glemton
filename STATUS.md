# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 13:35:32 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 766M / 3000M (25.5%) |
| Step | 46750 |
| Latest loss | 2.8028 |
| Avg loss (last 30 logged) | 2.3847 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 1:42:43 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.16 -> 2.78 -> 2.07 -> 2.52 -> 2.38 -> 2.13 -> 2.22 -> 2.42 -> 2.23 -> 2.25 -> 2.21 -> 2.64

## Checkpoints on disk
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`

## Recent log tail
```
[train] step=46640 tokens=764.1M loss=2.8564 lr=2.61e-04 tok/s=12483
[train] step=46650 tokens=764.3M loss=2.4004 lr=2.61e-04 tok/s=12483
[train] step=46660 tokens=764.5M loss=2.4372 lr=2.61e-04 tok/s=12483
[train] step=46670 tokens=764.6M loss=2.5753 lr=2.61e-04 tok/s=12483
[train] step=46680 tokens=764.8M loss=2.1860 lr=2.61e-04 tok/s=12483
[train] step=46690 tokens=765.0M loss=2.3747 lr=2.61e-04 tok/s=12483
[train] step=46700 tokens=765.1M loss=2.1245 lr=2.61e-04 tok/s=12483
[train] step=46710 tokens=765.3M loss=2.1706 lr=2.61e-04 tok/s=12483
[train] step=46720 tokens=765.5M loss=2.6361 lr=2.61e-04 tok/s=12483
[train] step=46730 tokens=765.6M loss=2.3414 lr=2.61e-04 tok/s=12483
[train] step=46740 tokens=765.8M loss=2.1132 lr=2.61e-04 tok/s=12483
[train] step=46750 tokens=766.0M loss=2.8028 lr=2.61e-04 tok/s=12483
```
