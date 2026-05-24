# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 04:11:23 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2502M / 3000M (83.4%) |
| Step | 152690 |
| Latest loss | 2.0406 |
| Avg loss (last 30 logged) | 2.1012 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 11:04:59 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.92 -> 1.93 -> 1.85 -> 1.80 -> 2.58 -> 2.30 -> 2.02 -> 1.78 -> 2.10 -> 2.28 -> 2.44 -> 1.81

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] checkpoint -> checkpoints\glemton-350m\step_152588_tokens_2500M.pt
[train] step=152590 tokens=2500.0M loss=2.5404 lr=4.84e-05 tok/s=12489
[train] step=152600 tokens=2500.2M loss=1.9817 lr=4.84e-05 tok/s=12489
[train] step=152610 tokens=2500.4M loss=1.7127 lr=4.84e-05 tok/s=12489
[train] step=152620 tokens=2500.5M loss=1.4894 lr=4.83e-05 tok/s=12489
[train] step=152630 tokens=2500.7M loss=2.3127 lr=4.83e-05 tok/s=12489
[train] step=152640 tokens=2500.9M loss=1.9365 lr=4.83e-05 tok/s=12489
[train] step=152650 tokens=2501.0M loss=1.9699 lr=4.83e-05 tok/s=12489
[train] step=152660 tokens=2501.2M loss=2.0833 lr=4.83e-05 tok/s=12489
[train] step=152670 tokens=2501.3M loss=1.8079 lr=4.83e-05 tok/s=12489
[train] step=152680 tokens=2501.5M loss=1.8057 lr=4.83e-05 tok/s=12489
[train] step=152690 tokens=2501.7M loss=2.0406 lr=4.83e-05 tok/s=12489
```
