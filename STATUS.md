# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 07:31:54 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2652M / 3000M (88.4%) |
| Step | 161860 |
| Latest loss | 1.9849 |
| Avg loss (last 30 logged) | 2.0432 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 7:44:32 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.91 -> 2.19 -> 1.87 -> 2.04 -> 2.19 -> 1.55 -> 1.92 -> 1.59 -> 2.62 -> 2.03 -> 1.96 -> 2.19

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
[train] step=161750 tokens=2650.1M loss=1.9513 lr=3.91e-05 tok/s=12489
[train] step=161760 tokens=2650.3M loss=2.1216 lr=3.91e-05 tok/s=12489
[train] step=161770 tokens=2650.4M loss=2.1341 lr=3.91e-05 tok/s=12489
[train] step=161780 tokens=2650.6M loss=2.1161 lr=3.91e-05 tok/s=12489
[train] step=161790 tokens=2650.8M loss=2.2383 lr=3.91e-05 tok/s=12489
[train] step=161800 tokens=2650.9M loss=2.0209 lr=3.91e-05 tok/s=12489
[train] step=161810 tokens=2651.1M loss=2.1133 lr=3.91e-05 tok/s=12489
[train] step=161820 tokens=2651.3M loss=1.9508 lr=3.91e-05 tok/s=12489
[train] step=161830 tokens=2651.4M loss=1.9367 lr=3.90e-05 tok/s=12489
[train] step=161840 tokens=2651.6M loss=2.1902 lr=3.90e-05 tok/s=12489
[train] step=161850 tokens=2651.8M loss=1.9722 lr=3.90e-05 tok/s=12489
[train] step=161860 tokens=2651.9M loss=1.9849 lr=3.90e-05 tok/s=12489
```
