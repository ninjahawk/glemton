# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 21:10:18 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2186M / 3000M (72.9%) |
| Step | 133440 |
| Latest loss | 2.1537 |
| Avg loss (last 30 logged) | 2.1597 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 18:05:53 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.61 -> 1.70 -> 1.91 -> 2.13 -> 2.34 -> 2.15 -> 2.03 -> 1.66 -> 2.11 -> 2.12 -> 2.06 -> 2.38

## Checkpoints on disk
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=133330 tokens=2184.5M loss=2.0591 lr=7.70e-05 tok/s=12489
[train] step=133340 tokens=2184.6M loss=2.2369 lr=7.70e-05 tok/s=12489
[train] step=133350 tokens=2184.8M loss=2.2370 lr=7.70e-05 tok/s=12489
[train] step=133360 tokens=2185.0M loss=2.1383 lr=7.70e-05 tok/s=12489
[train] step=133370 tokens=2185.1M loss=2.1560 lr=7.70e-05 tok/s=12489
[train] step=133380 tokens=2185.3M loss=2.1050 lr=7.70e-05 tok/s=12489
[train] step=133390 tokens=2185.5M loss=2.1277 lr=7.69e-05 tok/s=12489
[train] step=133400 tokens=2185.6M loss=1.7398 lr=7.69e-05 tok/s=12489
[train] step=133410 tokens=2185.8M loss=2.3789 lr=7.69e-05 tok/s=12489
[train] step=133420 tokens=2186.0M loss=2.1063 lr=7.69e-05 tok/s=12489
[train] step=133430 tokens=2186.1M loss=1.9054 lr=7.69e-05 tok/s=12489
[train] step=133440 tokens=2186.3M loss=2.1537 lr=7.68e-05 tok/s=12489
```
