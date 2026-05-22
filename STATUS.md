# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 13:25:30 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 758M / 3000M (25.3%) |
| Step | 46290 |
| Latest loss | 2.1588 |
| Avg loss (last 30 logged) | 2.3320 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 1:52:52 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.37 -> 2.18 -> 2.40 -> 2.23 -> 2.31 -> 2.68 -> 2.13 -> 2.20 -> 2.09 -> 2.64 -> 2.47 -> 2.66

## Checkpoints on disk
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`

## Recent log tail
```
[train] step=46180 tokens=756.6M loss=2.0812 lr=2.62e-04 tok/s=12483
[train] step=46190 tokens=756.8M loss=2.3711 lr=2.62e-04 tok/s=12483
[train] step=46200 tokens=756.9M loss=2.2622 lr=2.62e-04 tok/s=12483
[train] step=46210 tokens=757.1M loss=2.6512 lr=2.62e-04 tok/s=12483
[train] step=46220 tokens=757.3M loss=2.6842 lr=2.62e-04 tok/s=12483
[train] step=46230 tokens=757.4M loss=2.5140 lr=2.62e-04 tok/s=12483
[train] step=46240 tokens=757.6M loss=2.3508 lr=2.62e-04 tok/s=12483
[train] step=46250 tokens=757.8M loss=2.6755 lr=2.62e-04 tok/s=12483
[train] step=46260 tokens=757.9M loss=2.2460 lr=2.62e-04 tok/s=12483
[train] step=46270 tokens=758.1M loss=2.6595 lr=2.62e-04 tok/s=12483
[train] step=46280 tokens=758.3M loss=2.2116 lr=2.62e-04 tok/s=12483
[train] step=46290 tokens=758.4M loss=2.1588 lr=2.61e-04 tok/s=12483
```
