# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 22:10:27 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2231M / 3000M (74.4%) |
| Step | 136190 |
| Latest loss | 2.0428 |
| Avg loss (last 30 logged) | 2.0987 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 17:05:50 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.89 -> 1.69 -> 2.04 -> 1.72 -> 1.98 -> 1.87 -> 1.62 -> 2.10 -> 1.97 -> 1.83 -> 1.70 -> 1.84

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
[train] step=136080 tokens=2229.5M loss=1.9925 lr=7.23e-05 tok/s=12489
[train] step=136090 tokens=2229.7M loss=2.1046 lr=7.23e-05 tok/s=12489
[train] step=136100 tokens=2229.9M loss=1.6760 lr=7.22e-05 tok/s=12489
[train] step=136110 tokens=2230.0M loss=2.2620 lr=7.22e-05 tok/s=12489
[train] step=136120 tokens=2230.2M loss=2.5508 lr=7.22e-05 tok/s=12489
[train] step=136130 tokens=2230.4M loss=2.8402 lr=7.22e-05 tok/s=12489
[train] step=136140 tokens=2230.5M loss=2.4023 lr=7.22e-05 tok/s=12489
[train] step=136150 tokens=2230.7M loss=1.8189 lr=7.22e-05 tok/s=12489
[train] step=136160 tokens=2230.8M loss=2.0285 lr=7.21e-05 tok/s=12489
[train] step=136170 tokens=2231.0M loss=1.8389 lr=7.21e-05 tok/s=12489
[train] step=136180 tokens=2231.2M loss=2.1808 lr=7.21e-05 tok/s=12489
[train] step=136190 tokens=2231.3M loss=2.0428 lr=7.21e-05 tok/s=12489
```
