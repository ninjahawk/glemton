# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 16:09:32 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1961M / 3000M (65.4%) |
| Step | 119680 |
| Latest loss | 2.2214 |
| Avg loss (last 30 logged) | 2.0643 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 23:06:49 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.04 -> 1.55 -> 1.72 -> 2.24 -> 1.71 -> 1.91 -> 1.89 -> 1.80 -> 1.74 -> 2.44 -> 2.21 -> 1.69

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=119570 tokens=1959.0M loss=2.4170 lr=1.04e-04 tok/s=12489
[train] step=119580 tokens=1959.2M loss=2.0785 lr=1.04e-04 tok/s=12489
[train] step=119590 tokens=1959.4M loss=2.0971 lr=1.04e-04 tok/s=12489
[train] step=119600 tokens=1959.5M loss=1.5662 lr=1.04e-04 tok/s=12489
[train] step=119610 tokens=1959.7M loss=2.2092 lr=1.04e-04 tok/s=12489
[train] step=119620 tokens=1959.9M loss=2.3000 lr=1.04e-04 tok/s=12489
[train] step=119630 tokens=1960.0M loss=2.4663 lr=1.04e-04 tok/s=12489
[train] step=119640 tokens=1960.2M loss=1.9118 lr=1.04e-04 tok/s=12489
[train] step=119650 tokens=1960.3M loss=2.2496 lr=1.04e-04 tok/s=12489
[train] step=119660 tokens=1960.5M loss=1.6863 lr=1.03e-04 tok/s=12489
[train] step=119670 tokens=1960.7M loss=1.7375 lr=1.03e-04 tok/s=12489
[train] step=119680 tokens=1960.8M loss=2.2214 lr=1.03e-04 tok/s=12489
```
