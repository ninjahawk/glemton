# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 14:29:20 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1886M / 3000M (62.9%) |
| Step | 115090 |
| Latest loss | 1.8065 |
| Avg loss (last 30 logged) | 2.1732 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 1 day, 0:47:10 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.27 -> 2.05 -> 2.05 -> 2.30 -> 1.50 -> 2.05 -> 1.79 -> 1.88 -> 2.30 -> 2.31 -> 2.33 -> 2.45

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=114980 tokens=1883.8M loss=2.4541 lr=1.13e-04 tok/s=12489
[train] step=114990 tokens=1884.0M loss=1.9447 lr=1.13e-04 tok/s=12489
[train] step=115000 tokens=1884.2M loss=2.0250 lr=1.13e-04 tok/s=12489
[train] step=115010 tokens=1884.3M loss=2.6411 lr=1.13e-04 tok/s=12489
[train] step=115020 tokens=1884.5M loss=2.1011 lr=1.13e-04 tok/s=12489
[train] step=115030 tokens=1884.7M loss=2.4979 lr=1.13e-04 tok/s=12489
[train] step=115040 tokens=1884.8M loss=2.1236 lr=1.13e-04 tok/s=12489
[train] step=115050 tokens=1885.0M loss=1.9039 lr=1.13e-04 tok/s=12489
[train] step=115060 tokens=1885.1M loss=2.4522 lr=1.13e-04 tok/s=12489
[train] step=115070 tokens=1885.3M loss=1.8148 lr=1.13e-04 tok/s=12489
[train] step=115080 tokens=1885.5M loss=2.0260 lr=1.13e-04 tok/s=12489
[train] step=115090 tokens=1885.6M loss=1.8065 lr=1.13e-04 tok/s=12489
```
