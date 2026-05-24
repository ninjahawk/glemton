# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 04:41:28 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2524M / 3000M (84.1%) |
| Step | 154070 |
| Latest loss | 1.8999 |
| Avg loss (last 30 logged) | 2.0702 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 10:34:49 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.85 -> 2.37 -> 2.25 -> 2.14 -> 2.19 -> 1.91 -> 2.27 -> 1.98 -> 2.61 -> 2.15 -> 2.24 -> 1.50

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
[train] step=153960 tokens=2522.5M loss=1.7936 lr=4.68e-05 tok/s=12489
[train] step=153970 tokens=2522.6M loss=1.9621 lr=4.68e-05 tok/s=12489
[train] step=153980 tokens=2522.8M loss=1.7886 lr=4.68e-05 tok/s=12489
[train] step=153990 tokens=2523.0M loss=2.0005 lr=4.68e-05 tok/s=12489
[train] step=154000 tokens=2523.1M loss=2.1402 lr=4.68e-05 tok/s=12489
[train] step=154010 tokens=2523.3M loss=2.4646 lr=4.67e-05 tok/s=12489
[train] step=154020 tokens=2523.5M loss=2.2676 lr=4.67e-05 tok/s=12489
[train] step=154030 tokens=2523.6M loss=2.0008 lr=4.67e-05 tok/s=12489
[train] step=154040 tokens=2523.8M loss=1.8757 lr=4.67e-05 tok/s=12489
[train] step=154050 tokens=2524.0M loss=1.4985 lr=4.67e-05 tok/s=12489
[train] step=154060 tokens=2524.1M loss=2.3444 lr=4.67e-05 tok/s=12489
[train] step=154070 tokens=2524.3M loss=1.8999 lr=4.67e-05 tok/s=12489
```
