# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 22:30:30 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2246M / 3000M (74.9%) |
| Step | 137100 |
| Latest loss | 2.0568 |
| Avg loss (last 30 logged) | 2.0454 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 16:45:57 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.80 -> 2.08 -> 2.03 -> 2.27 -> 2.11 -> 1.96 -> 2.37 -> 2.02 -> 2.10 -> 2.03 -> 2.14 -> 2.06

## Checkpoints on disk
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=136990 tokens=2244.4M loss=2.0571 lr=7.07e-05 tok/s=12489
[train] step=137000 tokens=2244.6M loss=2.5870 lr=7.07e-05 tok/s=12489
[train] step=137010 tokens=2244.8M loss=2.2124 lr=7.07e-05 tok/s=12489
[train] step=137020 tokens=2244.9M loss=2.4348 lr=7.07e-05 tok/s=12489
[train] step=137030 tokens=2245.1M loss=2.3688 lr=7.07e-05 tok/s=12489
[train] step=137040 tokens=2245.3M loss=1.9035 lr=7.07e-05 tok/s=12489
[train] step=137050 tokens=2245.4M loss=2.1158 lr=7.06e-05 tok/s=12489
[train] step=137060 tokens=2245.6M loss=2.1604 lr=7.06e-05 tok/s=12489
[train] step=137070 tokens=2245.8M loss=2.4555 lr=7.06e-05 tok/s=12489
[train] step=137080 tokens=2245.9M loss=2.0581 lr=7.06e-05 tok/s=12489
[train] step=137090 tokens=2246.1M loss=2.2555 lr=7.06e-05 tok/s=12489
[train] step=137100 tokens=2246.2M loss=2.0568 lr=7.06e-05 tok/s=12489
```
