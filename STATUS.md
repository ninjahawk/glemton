# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 08:01:58 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2674M / 3000M (89.1%) |
| Step | 163230 |
| Latest loss | 2.2148 |
| Avg loss (last 30 logged) | 2.1093 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 7:14:30 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.34 -> 2.00 -> 1.88 -> 1.49 -> 2.17 -> 1.79 -> 2.49 -> 2.28 -> 2.07 -> 2.13 -> 1.85 -> 2.03

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
[train] step=163120 tokens=2672.6M loss=1.6836 lr=3.80e-05 tok/s=12489
[train] step=163130 tokens=2672.7M loss=1.8208 lr=3.80e-05 tok/s=12489
[train] step=163140 tokens=2672.9M loss=1.7269 lr=3.80e-05 tok/s=12489
[train] step=163150 tokens=2673.0M loss=2.0267 lr=3.80e-05 tok/s=12489
[train] step=163160 tokens=2673.2M loss=1.9099 lr=3.80e-05 tok/s=12489
[train] step=163170 tokens=2673.4M loss=2.2512 lr=3.80e-05 tok/s=12489
[train] step=163180 tokens=2673.5M loss=2.8980 lr=3.79e-05 tok/s=12489
[train] step=163190 tokens=2673.7M loss=2.6438 lr=3.79e-05 tok/s=12489
[train] step=163200 tokens=2673.9M loss=2.0347 lr=3.79e-05 tok/s=12489
[train] step=163210 tokens=2674.0M loss=1.7914 lr=3.79e-05 tok/s=12489
[train] step=163220 tokens=2674.2M loss=2.3827 lr=3.79e-05 tok/s=12489
[train] step=163230 tokens=2674.4M loss=2.2148 lr=3.79e-05 tok/s=12489
```
