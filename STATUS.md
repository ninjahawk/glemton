# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 19:46:28 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1044M / 3000M (34.8%) |
| Step | 63720 |
| Latest loss | 1.9004 |
| Avg loss (last 30 logged) | 2.2615 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 19:31:08 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.96 -> 1.99 -> 2.25 -> 2.10 -> 2.33 -> 2.37 -> 2.12 -> 2.42 -> 2.19 -> 2.63 -> 2.59 -> 2.08

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`

## Recent log tail
```
[train] step=63610 tokens=1042.2M loss=2.1742 lr=2.29e-04 tok/s=12485
[train] step=63620 tokens=1042.4M loss=2.3052 lr=2.29e-04 tok/s=12485
[train] step=63630 tokens=1042.5M loss=2.1245 lr=2.29e-04 tok/s=12485
[train] step=63640 tokens=1042.7M loss=2.4297 lr=2.29e-04 tok/s=12485
[train] step=63650 tokens=1042.8M loss=1.8174 lr=2.29e-04 tok/s=12485
[train] step=63660 tokens=1043.0M loss=1.8437 lr=2.29e-04 tok/s=12485
[train] step=63670 tokens=1043.2M loss=2.5102 lr=2.29e-04 tok/s=12485
[train] step=63680 tokens=1043.3M loss=2.4669 lr=2.29e-04 tok/s=12485
[train] step=63690 tokens=1043.5M loss=2.2970 lr=2.29e-04 tok/s=12485
[train] step=63700 tokens=1043.7M loss=2.0819 lr=2.29e-04 tok/s=12485
[train] step=63710 tokens=1043.8M loss=2.5444 lr=2.29e-04 tok/s=12485
[train] step=63720 tokens=1044.0M loss=1.9004 lr=2.29e-04 tok/s=12485
```
