# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 23:50:42 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2306M / 3000M (76.9%) |
| Step | 140770 |
| Latest loss | 2.1117 |
| Avg loss (last 30 logged) | 2.0034 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 15:25:36 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.69 -> 2.06 -> 2.29 -> 2.02 -> 1.73 -> 2.04 -> 1.85 -> 2.59 -> 1.58 -> 2.39 -> 1.84 -> 2.16

## Checkpoints on disk
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=140660 tokens=2304.6M loss=1.9562 lr=6.48e-05 tok/s=12489
[train] step=140670 tokens=2304.7M loss=2.2534 lr=6.48e-05 tok/s=12489
[train] step=140680 tokens=2304.9M loss=1.6182 lr=6.48e-05 tok/s=12489
[train] step=140690 tokens=2305.1M loss=1.9406 lr=6.47e-05 tok/s=12489
[train] step=140700 tokens=2305.2M loss=1.7910 lr=6.47e-05 tok/s=12489
[train] step=140710 tokens=2305.4M loss=2.4445 lr=6.47e-05 tok/s=12489
[train] step=140720 tokens=2305.6M loss=1.5502 lr=6.47e-05 tok/s=12489
[train] step=140730 tokens=2305.7M loss=1.7971 lr=6.47e-05 tok/s=12489
[train] step=140740 tokens=2305.9M loss=2.0396 lr=6.47e-05 tok/s=12489
[train] step=140750 tokens=2306.0M loss=2.1564 lr=6.47e-05 tok/s=12489
[train] step=140760 tokens=2306.2M loss=1.6274 lr=6.46e-05 tok/s=12489
[train] step=140770 tokens=2306.4M loss=2.1117 lr=6.46e-05 tok/s=12489
```
