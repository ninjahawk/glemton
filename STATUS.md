# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 03:51:19 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2487M / 3000M (82.9%) |
| Step | 151770 |
| Latest loss | 1.8948 |
| Avg loss (last 30 logged) | 2.0319 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 11:25:08 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.11 -> 2.55 -> 1.98 -> 1.74 -> 1.91 -> 1.97 -> 1.91 -> 1.85 -> 2.37 -> 2.25 -> 2.14 -> 2.19

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=151660 tokens=2484.8M loss=2.2387 lr=4.95e-05 tok/s=12489
[train] step=151670 tokens=2485.0M loss=1.2336 lr=4.95e-05 tok/s=12489
[train] step=151680 tokens=2485.1M loss=2.1036 lr=4.95e-05 tok/s=12489
[train] step=151690 tokens=2485.3M loss=2.2616 lr=4.95e-05 tok/s=12489
[train] step=151700 tokens=2485.5M loss=2.0357 lr=4.94e-05 tok/s=12489
[train] step=151710 tokens=2485.6M loss=1.8347 lr=4.94e-05 tok/s=12489
[train] step=151720 tokens=2485.8M loss=2.0874 lr=4.94e-05 tok/s=12489
[train] step=151730 tokens=2485.9M loss=2.3985 lr=4.94e-05 tok/s=12489
[train] step=151740 tokens=2486.1M loss=2.1929 lr=4.94e-05 tok/s=12489
[train] step=151750 tokens=2486.3M loss=2.2253 lr=4.94e-05 tok/s=12489
[train] step=151760 tokens=2486.4M loss=2.6259 lr=4.94e-05 tok/s=12489
[train] step=151770 tokens=2486.6M loss=1.8948 lr=4.94e-05 tok/s=12489
```
