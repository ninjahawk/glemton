# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 06:31:45 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2607M / 3000M (86.9%) |
| Step | 159110 |
| Latest loss | 2.1477 |
| Avg loss (last 30 logged) | 1.9645 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 8:44:35 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.09 -> 1.82 -> 2.14 -> 2.20 -> 2.13 -> 2.17 -> 2.41 -> 2.30 -> 2.09 -> 2.27 -> 1.62 -> 1.74

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=159000 tokens=2605.1M loss=2.4709 lr=4.16e-05 tok/s=12489
[train] step=159010 tokens=2605.2M loss=2.1655 lr=4.16e-05 tok/s=12489
[train] step=159020 tokens=2605.4M loss=1.8221 lr=4.16e-05 tok/s=12489
[train] step=159030 tokens=2605.5M loss=1.9983 lr=4.15e-05 tok/s=12489
[train] step=159040 tokens=2605.7M loss=1.6315 lr=4.15e-05 tok/s=12489
[train] step=159050 tokens=2605.9M loss=1.6206 lr=4.15e-05 tok/s=12489
[train] step=159060 tokens=2606.0M loss=1.9362 lr=4.15e-05 tok/s=12489
[train] step=159070 tokens=2606.2M loss=2.1481 lr=4.15e-05 tok/s=12489
[train] step=159080 tokens=2606.4M loss=2.3985 lr=4.15e-05 tok/s=12489
[train] step=159090 tokens=2606.5M loss=1.7400 lr=4.15e-05 tok/s=12489
[train] step=159100 tokens=2606.7M loss=2.2542 lr=4.15e-05 tok/s=12489
[train] step=159110 tokens=2606.9M loss=2.1477 lr=4.15e-05 tok/s=12489
```
