# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 03:21:15 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2464M / 3000M (82.1%) |
| Step | 150400 |
| Latest loss | 2.0210 |
| Avg loss (last 30 logged) | 2.0638 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 11:55:01 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.88 -> 1.90 -> 2.63 -> 1.65 -> 1.88 -> 1.82 -> 1.80 -> 2.03 -> 2.36 -> 2.21 -> 2.55 -> 1.74

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
[train] step=150290 tokens=2462.4M loss=2.1228 lr=5.12e-05 tok/s=12489
[train] step=150300 tokens=2462.5M loss=2.2731 lr=5.12e-05 tok/s=12489
[train] step=150310 tokens=2462.7M loss=2.6210 lr=5.12e-05 tok/s=12489
[train] step=150320 tokens=2462.8M loss=1.8761 lr=5.11e-05 tok/s=12489
[train] step=150330 tokens=2463.0M loss=1.9730 lr=5.11e-05 tok/s=12489
[train] step=150340 tokens=2463.2M loss=1.8357 lr=5.11e-05 tok/s=12489
[train] step=150350 tokens=2463.3M loss=2.2460 lr=5.11e-05 tok/s=12489
[train] step=150360 tokens=2463.5M loss=2.5774 lr=5.11e-05 tok/s=12489
[train] step=150370 tokens=2463.7M loss=2.0758 lr=5.11e-05 tok/s=12489
[train] step=150380 tokens=2463.8M loss=1.7373 lr=5.11e-05 tok/s=12489
[train] step=150390 tokens=2464.0M loss=2.3814 lr=5.11e-05 tok/s=12489
[train] step=150400 tokens=2464.2M loss=2.0210 lr=5.10e-05 tok/s=12489
```
