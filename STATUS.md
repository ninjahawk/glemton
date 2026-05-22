# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 19:06:22 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1014M / 3000M (33.8%) |
| Step | 61880 |
| Latest loss | 2.1554 |
| Avg loss (last 30 logged) | 2.2807 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 20:11:26 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.23 -> 2.01 -> 2.31 -> 2.07 -> 2.25 -> 2.24 -> 2.29 -> 1.90 -> 2.62 -> 2.32 -> 1.91 -> 2.33

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`

## Recent log tail
```
[train] step=61770 tokens=1012.0M loss=2.1118 lr=2.33e-04 tok/s=12485
[train] step=61780 tokens=1012.2M loss=2.4388 lr=2.33e-04 tok/s=12485
[train] step=61790 tokens=1012.4M loss=2.0229 lr=2.33e-04 tok/s=12485
[train] step=61800 tokens=1012.5M loss=2.3004 lr=2.33e-04 tok/s=12485
[train] step=61810 tokens=1012.7M loss=2.1744 lr=2.33e-04 tok/s=12485
[train] step=61820 tokens=1012.9M loss=2.1851 lr=2.33e-04 tok/s=12485
[train] step=61830 tokens=1013.0M loss=2.2769 lr=2.33e-04 tok/s=12485
[train] step=61840 tokens=1013.2M loss=2.3763 lr=2.33e-04 tok/s=12485
[train] step=61850 tokens=1013.4M loss=2.1474 lr=2.33e-04 tok/s=12485
[train] step=61860 tokens=1013.5M loss=2.3309 lr=2.33e-04 tok/s=12485
[train] step=61870 tokens=1013.7M loss=2.2918 lr=2.33e-04 tok/s=12485
[train] step=61880 tokens=1013.8M loss=2.1554 lr=2.33e-04 tok/s=12485
```
