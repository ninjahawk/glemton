# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 02:41:08 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2434M / 3000M (81.1%) |
| Step | 148560 |
| Latest loss | 2.4600 |
| Avg loss (last 30 logged) | 2.0404 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 12:35:19 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.84 -> 1.89 -> 2.49 -> 2.15 -> 2.16 -> 1.77 -> 2.38 -> 2.17 -> 2.46 -> 1.94 -> 2.12 -> 2.43

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
[train] step=148450 tokens=2432.2M loss=1.8416 lr=5.35e-05 tok/s=12489
[train] step=148460 tokens=2432.4M loss=2.0509 lr=5.35e-05 tok/s=12489
[train] step=148470 tokens=2432.5M loss=1.7784 lr=5.35e-05 tok/s=12489
[train] step=148480 tokens=2432.7M loss=2.2575 lr=5.35e-05 tok/s=12489
[train] step=148490 tokens=2432.9M loss=2.0025 lr=5.35e-05 tok/s=12489
[train] step=148500 tokens=2433.0M loss=2.3223 lr=5.35e-05 tok/s=12489
[train] step=148510 tokens=2433.2M loss=1.6716 lr=5.35e-05 tok/s=12489
[train] step=148520 tokens=2433.4M loss=1.9689 lr=5.35e-05 tok/s=12489
[train] step=148530 tokens=2433.5M loss=1.8254 lr=5.34e-05 tok/s=12489
[train] step=148540 tokens=2433.7M loss=2.4301 lr=5.34e-05 tok/s=12489
[train] step=148550 tokens=2433.8M loss=2.3438 lr=5.34e-05 tok/s=12489
[train] step=148560 tokens=2434.0M loss=2.4600 lr=5.34e-05 tok/s=12489
```
