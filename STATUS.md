# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 13:45:33 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 774M / 3000M (25.8%) |
| Step | 47210 |
| Latest loss | 2.3937 |
| Avg loss (last 30 logged) | 2.3764 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 1:32:42 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.40 -> 2.21 -> 2.49 -> 2.15 -> 2.33 -> 2.16 -> 2.38 -> 2.17 -> 2.37 -> 2.20 -> 2.14 -> 1.97

## Checkpoints on disk
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`

## Recent log tail
```
[train] step=47100 tokens=771.7M loss=2.2069 lr=2.60e-04 tok/s=12483
[train] step=47110 tokens=771.9M loss=2.2667 lr=2.60e-04 tok/s=12483
[train] step=47120 tokens=772.0M loss=2.6596 lr=2.60e-04 tok/s=12483
[train] step=47130 tokens=772.2M loss=2.2594 lr=2.60e-04 tok/s=12483
[train] step=47140 tokens=772.3M loss=2.2346 lr=2.60e-04 tok/s=12483
[train] step=47150 tokens=772.5M loss=2.3942 lr=2.60e-04 tok/s=12483
[train] step=47160 tokens=772.7M loss=2.3146 lr=2.60e-04 tok/s=12483
[train] step=47170 tokens=772.8M loss=2.0235 lr=2.60e-04 tok/s=12483
[train] step=47180 tokens=773.0M loss=1.9726 lr=2.60e-04 tok/s=12483
[train] step=47190 tokens=773.2M loss=2.6243 lr=2.60e-04 tok/s=12483
[train] step=47200 tokens=773.3M loss=2.6284 lr=2.60e-04 tok/s=12483
[train] step=47210 tokens=773.5M loss=2.3937 lr=2.60e-04 tok/s=12483
```
