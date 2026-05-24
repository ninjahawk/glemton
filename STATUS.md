# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 04:31:26 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2517M / 3000M (83.9%) |
| Step | 153610 |
| Latest loss | 2.3860 |
| Avg loss (last 30 logged) | 2.0855 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 10:44:58 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.91 -> 2.12 -> 1.68 -> 2.40 -> 2.35 -> 1.77 -> 2.27 -> 2.38 -> 1.98 -> 2.18 -> 2.51 -> 2.41

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
[train] step=153500 tokens=2514.9M loss=1.9836 lr=4.73e-05 tok/s=12489
[train] step=153510 tokens=2515.1M loss=1.9246 lr=4.73e-05 tok/s=12489
[train] step=153520 tokens=2515.3M loss=2.5383 lr=4.73e-05 tok/s=12489
[train] step=153530 tokens=2515.4M loss=1.9966 lr=4.73e-05 tok/s=12489
[train] step=153540 tokens=2515.6M loss=2.1917 lr=4.73e-05 tok/s=12489
[train] step=153550 tokens=2515.8M loss=1.8640 lr=4.73e-05 tok/s=12489
[train] step=153560 tokens=2515.9M loss=2.2621 lr=4.73e-05 tok/s=12489
[train] step=153570 tokens=2516.1M loss=1.9688 lr=4.72e-05 tok/s=12489
[train] step=153580 tokens=2516.3M loss=1.9737 lr=4.72e-05 tok/s=12489
[train] step=153590 tokens=2516.4M loss=2.4146 lr=4.72e-05 tok/s=12489
[train] step=153600 tokens=2516.6M loss=2.3936 lr=4.72e-05 tok/s=12489
[train] step=153610 tokens=2516.7M loss=2.3860 lr=4.72e-05 tok/s=12489
```
