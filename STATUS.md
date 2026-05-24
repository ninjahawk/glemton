# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 05:11:32 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2547M / 3000M (84.9%) |
| Step | 155440 |
| Latest loss | 1.5672 |
| Avg loss (last 30 logged) | 2.0802 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 10:04:55 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.14 -> 2.43 -> 1.76 -> 2.22 -> 1.95 -> 2.12 -> 2.18 -> 1.86 -> 1.96 -> 2.27 -> 2.00 -> 2.38

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
[train] step=155330 tokens=2544.9M loss=2.0255 lr=4.53e-05 tok/s=12489
[train] step=155340 tokens=2545.1M loss=1.8265 lr=4.53e-05 tok/s=12489
[train] step=155350 tokens=2545.3M loss=1.8920 lr=4.53e-05 tok/s=12489
[train] step=155360 tokens=2545.4M loss=2.1836 lr=4.53e-05 tok/s=12489
[train] step=155370 tokens=2545.6M loss=1.7261 lr=4.52e-05 tok/s=12489
[train] step=155380 tokens=2545.7M loss=2.0459 lr=4.52e-05 tok/s=12489
[train] step=155390 tokens=2545.9M loss=2.2003 lr=4.52e-05 tok/s=12489
[train] step=155400 tokens=2546.1M loss=2.0837 lr=4.52e-05 tok/s=12489
[train] step=155410 tokens=2546.2M loss=1.9888 lr=4.52e-05 tok/s=12489
[train] step=155420 tokens=2546.4M loss=2.3813 lr=4.52e-05 tok/s=12489
[train] step=155430 tokens=2546.6M loss=1.8619 lr=4.52e-05 tok/s=12489
[train] step=155440 tokens=2546.7M loss=1.5672 lr=4.52e-05 tok/s=12489
```
