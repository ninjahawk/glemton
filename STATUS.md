# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 21:06:40 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1104M / 3000M (36.8%) |
| Step | 67390 |
| Latest loss | 2.2832 |
| Avg loss (last 30 logged) | 2.2320 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 18:10:54 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.39 -> 2.15 -> 2.59 -> 1.91 -> 2.42 -> 2.24 -> 2.45 -> 1.97 -> 1.93 -> 1.93 -> 2.05 -> 2.22

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`

## Recent log tail
```
[train] step=67280 tokens=1102.3M loss=2.3587 lr=2.22e-04 tok/s=12486
[train] step=67290 tokens=1102.5M loss=2.7942 lr=2.22e-04 tok/s=12486
[train] step=67300 tokens=1102.6M loss=2.2514 lr=2.22e-04 tok/s=12485
[train] step=67310 tokens=1102.8M loss=2.1033 lr=2.22e-04 tok/s=12485
[train] step=67320 tokens=1103.0M loss=2.4383 lr=2.22e-04 tok/s=12485
[train] step=67330 tokens=1103.1M loss=2.1091 lr=2.22e-04 tok/s=12485
[train] step=67340 tokens=1103.3M loss=2.5731 lr=2.22e-04 tok/s=12485
[train] step=67350 tokens=1103.5M loss=2.1729 lr=2.22e-04 tok/s=12485
[train] step=67360 tokens=1103.6M loss=2.1993 lr=2.21e-04 tok/s=12485
[train] step=67370 tokens=1103.8M loss=2.2189 lr=2.21e-04 tok/s=12485
[train] step=67380 tokens=1104.0M loss=1.8725 lr=2.21e-04 tok/s=12485
[train] step=67390 tokens=1104.1M loss=2.2832 lr=2.21e-04 tok/s=12485
```
