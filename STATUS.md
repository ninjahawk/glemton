# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 06:41:46 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2614M / 3000M (87.1%) |
| Step | 159560 |
| Latest loss | 2.2051 |
| Avg loss (last 30 logged) | 2.1101 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 8:34:51 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.58 -> 1.92 -> 1.68 -> 1.51 -> 1.79 -> 2.11 -> 1.36 -> 2.16 -> 2.01 -> 2.23 -> 1.88 -> 2.95

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
[train] step=159450 tokens=2612.4M loss=2.1133 lr=4.11e-05 tok/s=12489
[train] step=159460 tokens=2612.6M loss=2.2399 lr=4.11e-05 tok/s=12489
[train] step=159470 tokens=2612.8M loss=1.6074 lr=4.11e-05 tok/s=12489
[train] step=159480 tokens=2612.9M loss=2.2604 lr=4.11e-05 tok/s=12489
[train] step=159490 tokens=2613.1M loss=2.1410 lr=4.11e-05 tok/s=12489
[train] step=159500 tokens=2613.2M loss=1.7333 lr=4.11e-05 tok/s=12489
[train] step=159510 tokens=2613.4M loss=2.2050 lr=4.11e-05 tok/s=12489
[train] step=159520 tokens=2613.6M loss=2.2612 lr=4.11e-05 tok/s=12489
[train] step=159530 tokens=2613.7M loss=2.1931 lr=4.11e-05 tok/s=12489
[train] step=159540 tokens=2613.9M loss=2.9546 lr=4.11e-05 tok/s=12489
[train] step=159550 tokens=2614.1M loss=2.4807 lr=4.11e-05 tok/s=12489
[train] step=159560 tokens=2614.2M loss=2.2051 lr=4.10e-05 tok/s=12489
```
