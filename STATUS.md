# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 06:01:40 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2584M / 3000M (86.1%) |
| Step | 157730 |
| Latest loss | 2.3328 |
| Avg loss (last 30 logged) | 2.1449 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 9:14:53 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.90 -> 2.18 -> 2.48 -> 2.09 -> 2.20 -> 1.64 -> 1.81 -> 1.99 -> 2.03 -> 1.39 -> 1.80 -> 2.55

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
[train] step=157620 tokens=2582.4M loss=2.0624 lr=4.29e-05 tok/s=12489
[train] step=157630 tokens=2582.6M loss=2.2011 lr=4.29e-05 tok/s=12489
[train] step=157640 tokens=2582.8M loss=2.0448 lr=4.29e-05 tok/s=12489
[train] step=157650 tokens=2582.9M loss=1.9325 lr=4.29e-05 tok/s=12489
[train] step=157660 tokens=2583.1M loss=1.5809 lr=4.29e-05 tok/s=12489
[train] step=157670 tokens=2583.3M loss=2.5481 lr=4.29e-05 tok/s=12489
[train] step=157680 tokens=2583.4M loss=2.2706 lr=4.29e-05 tok/s=12489
[train] step=157690 tokens=2583.6M loss=2.2134 lr=4.28e-05 tok/s=12489
[train] step=157700 tokens=2583.8M loss=2.5473 lr=4.28e-05 tok/s=12489
[train] step=157710 tokens=2583.9M loss=2.2990 lr=4.28e-05 tok/s=12489
[train] step=157720 tokens=2584.1M loss=1.8842 lr=4.28e-05 tok/s=12489
[train] step=157730 tokens=2584.2M loss=2.3328 lr=4.28e-05 tok/s=12489
```
