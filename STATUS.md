# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 12:45:23 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 728M / 3000M (24.3%) |
| Step | 44460 |
| Latest loss | 2.5176 |
| Avg loss (last 30 logged) | 2.4059 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 2:32:55 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.18 -> 2.09 -> 2.31 -> 2.33 -> 2.28 -> 2.39 -> 2.59 -> 2.24 -> 2.42 -> 2.24 -> 2.34 -> 2.41

## Checkpoints on disk
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`

## Recent log tail
```
[train] step=44350 tokens=726.6M loss=2.7787 lr=2.65e-04 tok/s=12483
[train] step=44360 tokens=726.8M loss=2.3264 lr=2.65e-04 tok/s=12483
[train] step=44370 tokens=727.0M loss=2.6629 lr=2.65e-04 tok/s=12483
[train] step=44380 tokens=727.1M loss=2.2672 lr=2.65e-04 tok/s=12483
[train] step=44390 tokens=727.3M loss=2.4240 lr=2.65e-04 tok/s=12483
[train] step=44400 tokens=727.4M loss=2.1690 lr=2.65e-04 tok/s=12483
[train] step=44410 tokens=727.6M loss=2.3755 lr=2.65e-04 tok/s=12483
[train] step=44420 tokens=727.8M loss=2.5023 lr=2.64e-04 tok/s=12483
[train] step=44430 tokens=727.9M loss=2.7004 lr=2.64e-04 tok/s=12483
[train] step=44440 tokens=728.1M loss=2.4118 lr=2.64e-04 tok/s=12483
[train] step=44450 tokens=728.3M loss=2.4398 lr=2.64e-04 tok/s=12483
[train] step=44460 tokens=728.4M loss=2.5176 lr=2.64e-04 tok/s=12483
```
