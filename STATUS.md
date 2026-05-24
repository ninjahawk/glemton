# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 11:32:30 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2831M / 3000M (94.4%) |
| Step | 172800 |
| Latest loss | 1.7502 |
| Avg loss (last 30 logged) | 1.9821 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 3:45:21 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.13 -> 1.73 -> 2.16 -> 1.88 -> 1.99 -> 1.94 -> 1.89 -> 1.94 -> 2.42 -> 1.59 -> 2.31 -> 2.27

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_170899_tokens_2800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=172690 tokens=2829.4M loss=2.0134 lr=3.22e-05 tok/s=12484
[train] step=172700 tokens=2829.5M loss=1.6811 lr=3.22e-05 tok/s=12484
[train] step=172710 tokens=2829.7M loss=1.6080 lr=3.22e-05 tok/s=12484
[train] step=172720 tokens=2829.8M loss=1.9797 lr=3.22e-05 tok/s=12484
[train] step=172730 tokens=2830.0M loss=1.5720 lr=3.22e-05 tok/s=12484
[train] step=172740 tokens=2830.2M loss=1.8107 lr=3.22e-05 tok/s=12484
[train] step=172750 tokens=2830.3M loss=2.2352 lr=3.22e-05 tok/s=12484
[train] step=172760 tokens=2830.5M loss=1.8219 lr=3.22e-05 tok/s=12484
[train] step=172770 tokens=2830.7M loss=1.8017 lr=3.22e-05 tok/s=12484
[train] step=172780 tokens=2830.8M loss=2.2655 lr=3.21e-05 tok/s=12484
[train] step=172790 tokens=2831.0M loss=1.8560 lr=3.21e-05 tok/s=12484
[train] step=172800 tokens=2831.2M loss=1.7502 lr=3.21e-05 tok/s=12484
```
