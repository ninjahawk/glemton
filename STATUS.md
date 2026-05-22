# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-21 23:53:14 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 150M / 3000M (5.0%) |
| Step | 9160 |
| Latest loss | 2.2588 |
| Avg loss (last 30 logged) | 2.5523 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 2 days, 15:23:12 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.90 -> 2.71 -> 2.55 -> 2.42 -> 3.00 -> 2.66 -> 2.58 -> 2.70 -> 2.71 -> 2.70 -> 2.40 -> 2.73

## Checkpoints on disk
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=9050 tokens=148.3M loss=2.6101 lr=2.99e-04 tok/s=12489
[train] step=9060 tokens=148.4M loss=2.5630 lr=2.99e-04 tok/s=12489
[train] step=9070 tokens=148.6M loss=2.5851 lr=2.99e-04 tok/s=12489
[train] step=9080 tokens=148.8M loss=2.3213 lr=2.99e-04 tok/s=12489
[train] step=9090 tokens=148.9M loss=2.4574 lr=2.99e-04 tok/s=12489
[train] step=9100 tokens=149.1M loss=2.5518 lr=2.99e-04 tok/s=12489
[train] step=9110 tokens=149.3M loss=2.3991 lr=2.99e-04 tok/s=12489
[train] step=9120 tokens=149.4M loss=2.4808 lr=2.99e-04 tok/s=12489
[train] step=9130 tokens=149.6M loss=2.4914 lr=2.99e-04 tok/s=12489
[train] step=9140 tokens=149.7M loss=2.7293 lr=2.99e-04 tok/s=12489
[train] step=9150 tokens=149.9M loss=2.4622 lr=2.99e-04 tok/s=12489
[train] step=9160 tokens=150.1M loss=2.2588 lr=2.99e-04 tok/s=12489
```
