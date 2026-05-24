# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 02:21:05 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2419M / 3000M (80.6%) |
| Step | 147650 |
| Latest loss | 1.6861 |
| Avg loss (last 30 logged) | 2.0747 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 12:55:12 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.94 -> 1.99 -> 1.85 -> 2.06 -> 1.77 -> 2.18 -> 1.93 -> 2.38 -> 2.09 -> 2.04 -> 2.15 -> 1.95

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
[train] step=147540 tokens=2417.3M loss=2.0956 lr=5.48e-05 tok/s=12489
[train] step=147550 tokens=2417.5M loss=2.4567 lr=5.47e-05 tok/s=12489
[train] step=147560 tokens=2417.6M loss=2.2262 lr=5.47e-05 tok/s=12489
[train] step=147570 tokens=2417.8M loss=2.5259 lr=5.47e-05 tok/s=12489
[train] step=147580 tokens=2418.0M loss=2.4406 lr=5.47e-05 tok/s=12489
[train] step=147590 tokens=2418.1M loss=2.0933 lr=5.47e-05 tok/s=12489
[train] step=147600 tokens=2418.3M loss=1.9645 lr=5.47e-05 tok/s=12489
[train] step=147610 tokens=2418.4M loss=1.7510 lr=5.47e-05 tok/s=12489
[train] step=147620 tokens=2418.6M loss=2.1390 lr=5.47e-05 tok/s=12489
[train] step=147630 tokens=2418.8M loss=1.9513 lr=5.46e-05 tok/s=12489
[train] step=147640 tokens=2418.9M loss=2.0939 lr=5.46e-05 tok/s=12489
[train] step=147650 tokens=2419.1M loss=1.6861 lr=5.46e-05 tok/s=12489
```
