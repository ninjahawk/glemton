# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 04:21:24 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2509M / 3000M (83.6%) |
| Step | 153150 |
| Latest loss | 1.7804 |
| Avg loss (last 30 logged) | 2.0610 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 10:54:58 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.47 -> 1.80 -> 1.91 -> 2.19 -> 2.18 -> 1.98 -> 2.22 -> 2.53 -> 2.12 -> 2.08 -> 1.74 -> 2.38

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
[train] step=153040 tokens=2507.4M loss=1.9070 lr=4.79e-05 tok/s=12489
[train] step=153050 tokens=2507.6M loss=2.2280 lr=4.78e-05 tok/s=12489
[train] step=153060 tokens=2507.7M loss=2.6135 lr=4.78e-05 tok/s=12489
[train] step=153070 tokens=2507.9M loss=2.5755 lr=4.78e-05 tok/s=12489
[train] step=153080 tokens=2508.1M loss=2.0743 lr=4.78e-05 tok/s=12489
[train] step=153090 tokens=2508.2M loss=1.8807 lr=4.78e-05 tok/s=12489
[train] step=153100 tokens=2508.4M loss=1.8768 lr=4.78e-05 tok/s=12489
[train] step=153110 tokens=2508.6M loss=1.9481 lr=4.78e-05 tok/s=12489
[train] step=153120 tokens=2508.7M loss=1.6046 lr=4.78e-05 tok/s=12489
[train] step=153130 tokens=2508.9M loss=2.3834 lr=4.78e-05 tok/s=12489
[train] step=153140 tokens=2509.0M loss=2.0221 lr=4.77e-05 tok/s=12489
[train] step=153150 tokens=2509.2M loss=1.7804 lr=4.77e-05 tok/s=12489
```
