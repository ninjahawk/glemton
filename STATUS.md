# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 06:11:42 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2592M / 3000M (86.4%) |
| Step | 158190 |
| Latest loss | 1.6845 |
| Avg loss (last 30 logged) | 2.0616 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 9:04:44 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.88 -> 1.95 -> 1.73 -> 2.19 -> 1.98 -> 1.81 -> 1.91 -> 2.08 -> 1.87 -> 2.10 -> 1.93 -> 2.59

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=158080 tokens=2590.0M loss=2.3481 lr=4.25e-05 tok/s=12489
[train] step=158090 tokens=2590.1M loss=1.6294 lr=4.24e-05 tok/s=12489
[train] step=158100 tokens=2590.3M loss=2.0884 lr=4.24e-05 tok/s=12489
[train] step=158110 tokens=2590.5M loss=2.0944 lr=4.24e-05 tok/s=12489
[train] step=158120 tokens=2590.6M loss=1.8972 lr=4.24e-05 tok/s=12489
[train] step=158130 tokens=2590.8M loss=2.0095 lr=4.24e-05 tok/s=12489
[train] step=158140 tokens=2591.0M loss=2.1538 lr=4.24e-05 tok/s=12489
[train] step=158150 tokens=2591.1M loss=2.2644 lr=4.24e-05 tok/s=12489
[train] step=158160 tokens=2591.3M loss=2.5912 lr=4.24e-05 tok/s=12489
[train] step=158170 tokens=2591.5M loss=2.0220 lr=4.24e-05 tok/s=12489
[train] step=158180 tokens=2591.6M loss=2.0300 lr=4.24e-05 tok/s=12489
[train] step=158190 tokens=2591.8M loss=1.6845 lr=4.24e-05 tok/s=12489
```
