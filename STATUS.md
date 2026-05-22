# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 19:36:26 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1036M / 3000M (34.5%) |
| Step | 63260 |
| Latest loss | 2.5423 |
| Avg loss (last 30 logged) | 2.2651 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 19:41:08 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.76 -> 2.17 -> 2.28 -> 2.17 -> 2.56 -> 1.91 -> 2.24 -> 2.34 -> 2.19 -> 2.19 -> 2.61 -> 2.24

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`

## Recent log tail
```
[train] step=63150 tokens=1034.6M loss=2.0773 lr=2.30e-04 tok/s=12485
[train] step=63160 tokens=1034.8M loss=1.9396 lr=2.30e-04 tok/s=12485
[train] step=63170 tokens=1035.0M loss=2.1237 lr=2.30e-04 tok/s=12485
[train] step=63180 tokens=1035.1M loss=2.3799 lr=2.30e-04 tok/s=12485
[train] step=63190 tokens=1035.3M loss=2.4555 lr=2.30e-04 tok/s=12485
[train] step=63200 tokens=1035.5M loss=2.3849 lr=2.30e-04 tok/s=12485
[train] step=63210 tokens=1035.6M loss=2.3859 lr=2.30e-04 tok/s=12485
[train] step=63220 tokens=1035.8M loss=1.9879 lr=2.30e-04 tok/s=12485
[train] step=63230 tokens=1036.0M loss=2.1821 lr=2.30e-04 tok/s=12485
[train] step=63240 tokens=1036.1M loss=2.2397 lr=2.30e-04 tok/s=12485
[train] step=63250 tokens=1036.3M loss=2.1080 lr=2.30e-04 tok/s=12485
[train] step=63260 tokens=1036.5M loss=2.5423 lr=2.30e-04 tok/s=12485
```
