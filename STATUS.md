# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 07:51:57 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2667M / 3000M (88.9%) |
| Step | 162770 |
| Latest loss | 1.9441 |
| Avg loss (last 30 logged) | 2.0884 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 7:24:39 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.15 -> 2.12 -> 1.83 -> 2.10 -> 2.19 -> 2.30 -> 2.29 -> 1.85 -> 1.95 -> 1.88 -> 2.33 -> 2.28

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=162660 tokens=2665.0M loss=2.2933 lr=3.84e-05 tok/s=12489
[train] step=162670 tokens=2665.2M loss=2.2501 lr=3.84e-05 tok/s=12489
[train] step=162680 tokens=2665.3M loss=2.0809 lr=3.83e-05 tok/s=12489
[train] step=162690 tokens=2665.5M loss=2.0076 lr=3.83e-05 tok/s=12489
[train] step=162700 tokens=2665.7M loss=1.6936 lr=3.83e-05 tok/s=12489
[train] step=162710 tokens=2665.8M loss=2.1333 lr=3.83e-05 tok/s=12489
[train] step=162720 tokens=2666.0M loss=1.8105 lr=3.83e-05 tok/s=12489
[train] step=162730 tokens=2666.2M loss=1.7790 lr=3.83e-05 tok/s=12489
[train] step=162740 tokens=2666.3M loss=2.2761 lr=3.83e-05 tok/s=12489
[train] step=162750 tokens=2666.5M loss=2.2017 lr=3.83e-05 tok/s=12489
[train] step=162760 tokens=2666.7M loss=2.1850 lr=3.83e-05 tok/s=12489
[train] step=162770 tokens=2666.8M loss=1.9441 lr=3.83e-05 tok/s=12489
```
