# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 19:50:06 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2126M / 3000M (70.9%) |
| Step | 129770 |
| Latest loss | 2.0924 |
| Avg loss (last 30 logged) | 2.1727 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 19:25:59 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.07 -> 2.18 -> 2.09 -> 2.28 -> 1.90 -> 1.88 -> 1.90 -> 2.22 -> 2.80 -> 1.82 -> 1.72 -> 1.88

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
[train] step=129660 tokens=2124.3M loss=2.3006 lr=8.37e-05 tok/s=12490
[train] step=129670 tokens=2124.5M loss=1.7905 lr=8.37e-05 tok/s=12490
[train] step=129680 tokens=2124.7M loss=2.2004 lr=8.37e-05 tok/s=12490
[train] step=129690 tokens=2124.8M loss=2.6266 lr=8.37e-05 tok/s=12490
[train] step=129700 tokens=2125.0M loss=2.0859 lr=8.36e-05 tok/s=12490
[train] step=129710 tokens=2125.2M loss=2.0754 lr=8.36e-05 tok/s=12490
[train] step=129720 tokens=2125.3M loss=2.2895 lr=8.36e-05 tok/s=12490
[train] step=129730 tokens=2125.5M loss=2.0664 lr=8.36e-05 tok/s=12490
[train] step=129740 tokens=2125.7M loss=2.4526 lr=8.36e-05 tok/s=12490
[train] step=129750 tokens=2125.8M loss=1.8831 lr=8.36e-05 tok/s=12490
[train] step=129760 tokens=2126.0M loss=1.9302 lr=8.35e-05 tok/s=12490
[train] step=129770 tokens=2126.2M loss=2.0924 lr=8.35e-05 tok/s=12490
```
