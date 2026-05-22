# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 13:15:28 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 751M / 3000M (25.0%) |
| Step | 45830 |
| Latest loss | 2.2924 |
| Avg loss (last 30 logged) | 2.3602 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 2:02:53 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.25 -> 2.20 -> 1.96 -> 2.07 -> 2.85 -> 2.44 -> 2.01 -> 2.23 -> 2.13 -> 2.49 -> 2.46 -> 2.29

## Checkpoints on disk
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`

## Recent log tail
```
[train] step=45720 tokens=749.1M loss=2.5428 lr=2.62e-04 tok/s=12483
[train] step=45730 tokens=749.2M loss=2.2286 lr=2.62e-04 tok/s=12483
[train] step=45740 tokens=749.4M loss=2.7182 lr=2.62e-04 tok/s=12483
[train] step=45750 tokens=749.6M loss=2.2543 lr=2.62e-04 tok/s=12483
[train] step=45760 tokens=749.7M loss=2.7835 lr=2.62e-04 tok/s=12483
[train] step=45770 tokens=749.9M loss=2.5631 lr=2.62e-04 tok/s=12483
[train] step=45780 tokens=750.1M loss=2.2120 lr=2.62e-04 tok/s=12483
[train] step=45790 tokens=750.2M loss=2.1566 lr=2.62e-04 tok/s=12483
[train] step=45800 tokens=750.4M loss=1.9153 lr=2.62e-04 tok/s=12483
[train] step=45810 tokens=750.6M loss=2.2907 lr=2.62e-04 tok/s=12483
[train] step=45820 tokens=750.7M loss=2.0829 lr=2.62e-04 tok/s=12483
[train] step=45830 tokens=750.9M loss=2.2924 lr=2.62e-04 tok/s=12483
```
