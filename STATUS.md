# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 20:20:10 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2149M / 3000M (71.6%) |
| Step | 131150 |
| Latest loss | 2.1098 |
| Avg loss (last 30 logged) | 2.1401 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 18:55:50 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.94 -> 2.49 -> 1.84 -> 2.30 -> 2.02 -> 1.99 -> 2.13 -> 2.36 -> 2.29 -> 1.81 -> 2.56 -> 1.99

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
[train] step=131040 tokens=2147.0M loss=2.0626 lr=8.12e-05 tok/s=12490
[train] step=131050 tokens=2147.1M loss=2.1306 lr=8.11e-05 tok/s=12490
[train] step=131060 tokens=2147.3M loss=2.5507 lr=8.11e-05 tok/s=12490
[train] step=131070 tokens=2147.5M loss=1.9805 lr=8.11e-05 tok/s=12490
[train] step=131080 tokens=2147.6M loss=2.6800 lr=8.11e-05 tok/s=12490
[train] step=131090 tokens=2147.8M loss=1.8454 lr=8.11e-05 tok/s=12490
[train] step=131100 tokens=2147.9M loss=2.3376 lr=8.11e-05 tok/s=12490
[train] step=131110 tokens=2148.1M loss=2.2825 lr=8.10e-05 tok/s=12490
[train] step=131120 tokens=2148.3M loss=2.2478 lr=8.10e-05 tok/s=12490
[train] step=131130 tokens=2148.4M loss=1.9913 lr=8.10e-05 tok/s=12490
[train] step=131140 tokens=2148.6M loss=1.9415 lr=8.10e-05 tok/s=12490
[train] step=131150 tokens=2148.8M loss=2.1098 lr=8.10e-05 tok/s=12490
```
