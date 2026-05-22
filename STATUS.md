# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 12:25:20 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 713M / 3000M (23.8%) |
| Step | 43540 |
| Latest loss | 2.4958 |
| Avg loss (last 30 logged) | 2.3856 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 2:52:57 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.36 -> 2.19 -> 2.20 -> 2.65 -> 2.87 -> 2.42 -> 2.40 -> 2.34 -> 2.07 -> 2.26 -> 2.39 -> 2.19

## Checkpoints on disk
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`

## Recent log tail
```
[train] step=43430 tokens=711.6M loss=2.3138 lr=2.66e-04 tok/s=12483
[train] step=43440 tokens=711.7M loss=2.1973 lr=2.66e-04 tok/s=12483
[train] step=43450 tokens=711.9M loss=2.4248 lr=2.66e-04 tok/s=12483
[train] step=43460 tokens=712.0M loss=2.3452 lr=2.66e-04 tok/s=12483
[train] step=43470 tokens=712.2M loss=2.0974 lr=2.66e-04 tok/s=12483
[train] step=43480 tokens=712.4M loss=2.1159 lr=2.66e-04 tok/s=12483
[train] step=43490 tokens=712.5M loss=2.6281 lr=2.66e-04 tok/s=12483
[train] step=43500 tokens=712.7M loss=2.8532 lr=2.66e-04 tok/s=12483
[train] step=43510 tokens=712.9M loss=2.2824 lr=2.66e-04 tok/s=12483
[train] step=43520 tokens=713.0M loss=2.1875 lr=2.66e-04 tok/s=12483
[train] step=43530 tokens=713.2M loss=2.4839 lr=2.66e-04 tok/s=12483
[train] step=43540 tokens=713.4M loss=2.4958 lr=2.66e-04 tok/s=12483
```
