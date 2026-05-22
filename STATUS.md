# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 00:23:19 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 173M / 3000M (5.8%) |
| Step | 10540 |
| Latest loss | 2.5540 |
| Avg loss (last 30 logged) | 2.5400 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 2 days, 14:52:45 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
3.55 -> 3.24 -> 2.93 -> 2.53 -> 2.63 -> 2.65 -> 2.90 -> 2.60 -> 3.10 -> 2.50 -> 2.56 -> 2.60

## Checkpoints on disk
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=10430 tokens=170.9M loss=2.7052 lr=2.98e-04 tok/s=12490
[train] step=10440 tokens=171.0M loss=2.5806 lr=2.98e-04 tok/s=12490
[train] step=10450 tokens=171.2M loss=2.3268 lr=2.98e-04 tok/s=12490
[train] step=10460 tokens=171.4M loss=2.6996 lr=2.98e-04 tok/s=12490
[train] step=10470 tokens=171.5M loss=2.8174 lr=2.98e-04 tok/s=12490
[train] step=10480 tokens=171.7M loss=2.4114 lr=2.98e-04 tok/s=12490
[train] step=10490 tokens=171.9M loss=2.7023 lr=2.98e-04 tok/s=12490
[train] step=10500 tokens=172.0M loss=2.4007 lr=2.98e-04 tok/s=12490
[train] step=10510 tokens=172.2M loss=2.6026 lr=2.98e-04 tok/s=12490
[train] step=10520 tokens=172.4M loss=2.3058 lr=2.98e-04 tok/s=12490
[train] step=10530 tokens=172.5M loss=2.5907 lr=2.98e-04 tok/s=12490
[train] step=10540 tokens=172.7M loss=2.5540 lr=2.98e-04 tok/s=12490
```
