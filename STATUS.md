# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 23:10:36 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2276M / 3000M (75.9%) |
| Step | 138940 |
| Latest loss | 1.6477 |
| Avg loss (last 30 logged) | 2.0819 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 16:05:38 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.11 -> 2.28 -> 2.53 -> 1.75 -> 1.85 -> 1.93 -> 2.63 -> 1.71 -> 2.68 -> 1.90 -> 1.99 -> 2.42

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
[train] step=138830 tokens=2274.6M loss=1.8947 lr=6.77e-05 tok/s=12489
[train] step=138840 tokens=2274.8M loss=1.5612 lr=6.77e-05 tok/s=12489
[train] step=138850 tokens=2274.9M loss=2.6151 lr=6.77e-05 tok/s=12489
[train] step=138860 tokens=2275.1M loss=2.2461 lr=6.77e-05 tok/s=12489
[train] step=138870 tokens=2275.2M loss=2.2410 lr=6.76e-05 tok/s=12489
[train] step=138880 tokens=2275.4M loss=1.5969 lr=6.76e-05 tok/s=12489
[train] step=138890 tokens=2275.6M loss=2.4423 lr=6.76e-05 tok/s=12489
[train] step=138900 tokens=2275.7M loss=2.0513 lr=6.76e-05 tok/s=12489
[train] step=138910 tokens=2275.9M loss=2.4245 lr=6.76e-05 tok/s=12489
[train] step=138920 tokens=2276.1M loss=2.0716 lr=6.76e-05 tok/s=12489
[train] step=138930 tokens=2276.2M loss=2.1514 lr=6.75e-05 tok/s=12489
[train] step=138940 tokens=2276.4M loss=1.6477 lr=6.75e-05 tok/s=12489
```
