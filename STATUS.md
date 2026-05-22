# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-21 23:33:10 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 135M / 3000M (4.5%) |
| Step | 8250 |
| Latest loss | 3.3918 |
| Avg loss (last 30 logged) | 2.7329 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 2 days, 15:43:24 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
3.26 -> 2.55 -> 2.72 -> 2.94 -> 2.36 -> 2.71 -> 3.09 -> 2.63 -> 2.54 -> 2.62 -> 2.60 -> 2.41

## Checkpoints on disk
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=8140 tokens=133.4M loss=3.0954 lr=2.99e-04 tok/s=12488
[train] step=8150 tokens=133.5M loss=2.7119 lr=2.99e-04 tok/s=12488
[train] step=8160 tokens=133.7M loss=3.0229 lr=2.99e-04 tok/s=12488
[train] step=8170 tokens=133.9M loss=2.8464 lr=2.99e-04 tok/s=12488
[train] step=8180 tokens=134.0M loss=2.3294 lr=2.99e-04 tok/s=12488
[train] step=8190 tokens=134.2M loss=2.4591 lr=2.99e-04 tok/s=12488
[train] step=8200 tokens=134.3M loss=2.6311 lr=2.99e-04 tok/s=12488
[train] step=8210 tokens=134.5M loss=2.6391 lr=2.99e-04 tok/s=12488
[train] step=8220 tokens=134.7M loss=2.7578 lr=2.99e-04 tok/s=12488
[train] step=8230 tokens=134.8M loss=2.4142 lr=2.99e-04 tok/s=12488
[train] step=8240 tokens=135.0M loss=2.3961 lr=2.99e-04 tok/s=12488
[train] step=8250 tokens=135.2M loss=3.3918 lr=2.99e-04 tok/s=12488
```
