# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 14:09:16 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1871M / 3000M (62.4%) |
| Step | 114170 |
| Latest loss | 2.1110 |
| Avg loss (last 30 logged) | 2.0938 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 1 day, 1:07:11 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.04 -> 2.00 -> 1.80 -> 2.32 -> 2.34 -> 1.78 -> 2.65 -> 2.00 -> 1.84 -> 2.29 -> 2.27 -> 2.10

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=114060 tokens=1868.8M loss=2.1859 lr=1.15e-04 tok/s=12489
[train] step=114070 tokens=1868.9M loss=2.3015 lr=1.15e-04 tok/s=12489
[train] step=114080 tokens=1869.1M loss=2.0001 lr=1.15e-04 tok/s=12489
[train] step=114090 tokens=1869.3M loss=2.0696 lr=1.15e-04 tok/s=12489
[train] step=114100 tokens=1869.4M loss=2.2281 lr=1.15e-04 tok/s=12489
[train] step=114110 tokens=1869.6M loss=1.6357 lr=1.15e-04 tok/s=12489
[train] step=114120 tokens=1869.7M loss=1.8324 lr=1.15e-04 tok/s=12489
[train] step=114130 tokens=1869.9M loss=2.0465 lr=1.15e-04 tok/s=12489
[train] step=114140 tokens=1870.1M loss=2.1008 lr=1.15e-04 tok/s=12489
[train] step=114150 tokens=1870.2M loss=1.6559 lr=1.15e-04 tok/s=12489
[train] step=114160 tokens=1870.4M loss=2.3712 lr=1.15e-04 tok/s=12489
[train] step=114170 tokens=1870.6M loss=2.1110 lr=1.15e-04 tok/s=12489
```
