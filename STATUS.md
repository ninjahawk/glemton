# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 00:13:17 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 165M / 3000M (5.5%) |
| Step | 10080 |
| Latest loss | 3.0313 |
| Avg loss (last 30 logged) | 2.5930 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 2 days, 15:02:45 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.84 -> 2.54 -> 2.65 -> 2.66 -> 2.84 -> 2.75 -> 3.19 -> 2.80 -> 2.59 -> 2.71 -> 2.51 -> 2.60

## Checkpoints on disk
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=9970 tokens=163.3M loss=2.8712 lr=2.99e-04 tok/s=12490
[train] step=9980 tokens=163.5M loss=2.1058 lr=2.99e-04 tok/s=12490
[train] step=9990 tokens=163.7M loss=2.7015 lr=2.99e-04 tok/s=12490
[train] step=10000 tokens=163.8M loss=2.4288 lr=2.99e-04 tok/s=12490
[train] step=10010 tokens=164.0M loss=2.7759 lr=2.99e-04 tok/s=12490
[train] step=10020 tokens=164.2M loss=2.5020 lr=2.99e-04 tok/s=12490
[train] step=10030 tokens=164.3M loss=2.5128 lr=2.99e-04 tok/s=12490
[train] step=10040 tokens=164.5M loss=2.6027 lr=2.99e-04 tok/s=12490
[train] step=10050 tokens=164.7M loss=2.3074 lr=2.99e-04 tok/s=12490
[train] step=10060 tokens=164.8M loss=2.6037 lr=2.99e-04 tok/s=12490
[train] step=10070 tokens=165.0M loss=2.3854 lr=2.99e-04 tok/s=12490
[train] step=10080 tokens=165.2M loss=3.0313 lr=2.99e-04 tok/s=12490
```
