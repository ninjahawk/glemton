# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 08:12:00 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2682M / 3000M (89.4%) |
| Step | 163690 |
| Latest loss | 2.1161 |
| Avg loss (last 30 logged) | 2.1125 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 7:04:30 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.17 -> 2.34 -> 1.92 -> 2.25 -> 2.11 -> 2.45 -> 2.34 -> 2.52 -> 2.25 -> 2.19 -> 2.03 -> 2.23

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
[train] step=163580 tokens=2680.1M loss=2.1411 lr=3.76e-05 tok/s=12489
[train] step=163590 tokens=2680.3M loss=2.1222 lr=3.76e-05 tok/s=12489
[train] step=163600 tokens=2680.4M loss=2.2083 lr=3.76e-05 tok/s=12489
[train] step=163610 tokens=2680.6M loss=2.2555 lr=3.76e-05 tok/s=12489
[train] step=163620 tokens=2680.8M loss=2.0340 lr=3.76e-05 tok/s=12489
[train] step=163630 tokens=2680.9M loss=2.3589 lr=3.76e-05 tok/s=12489
[train] step=163640 tokens=2681.1M loss=2.0900 lr=3.76e-05 tok/s=12489
[train] step=163650 tokens=2681.2M loss=1.8323 lr=3.76e-05 tok/s=12489
[train] step=163660 tokens=2681.4M loss=2.2291 lr=3.76e-05 tok/s=12489
[train] step=163670 tokens=2681.6M loss=2.1026 lr=3.76e-05 tok/s=12489
[train] step=163680 tokens=2681.7M loss=2.2133 lr=3.76e-05 tok/s=12489
[train] step=163690 tokens=2681.9M loss=2.1161 lr=3.75e-05 tok/s=12489
```
