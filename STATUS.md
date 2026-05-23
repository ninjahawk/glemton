# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 13:29:10 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1841M / 3000M (61.4%) |
| Step | 112340 |
| Latest loss | 2.1877 |
| Avg loss (last 30 logged) | 2.1371 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 1 day, 1:47:13 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.66 -> 1.68 -> 1.75 -> 1.89 -> 2.17 -> 2.25 -> 2.60 -> 2.37 -> 1.88 -> 2.46 -> 2.27 -> 2.45

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=112230 tokens=1838.8M loss=1.9037 lr=1.19e-04 tok/s=12489
[train] step=112240 tokens=1838.9M loss=2.0086 lr=1.19e-04 tok/s=12489
[train] step=112250 tokens=1839.1M loss=2.3984 lr=1.19e-04 tok/s=12489
[train] step=112260 tokens=1839.3M loss=2.3621 lr=1.19e-04 tok/s=12489
[train] step=112270 tokens=1839.4M loss=2.3763 lr=1.19e-04 tok/s=12489
[train] step=112280 tokens=1839.6M loss=1.9438 lr=1.19e-04 tok/s=12489
[train] step=112290 tokens=1839.8M loss=2.0483 lr=1.19e-04 tok/s=12489
[train] step=112300 tokens=1839.9M loss=2.3698 lr=1.19e-04 tok/s=12489
[train] step=112310 tokens=1840.1M loss=1.9851 lr=1.19e-04 tok/s=12489
[train] step=112320 tokens=1840.3M loss=2.4474 lr=1.19e-04 tok/s=12489
[train] step=112330 tokens=1840.4M loss=1.9080 lr=1.19e-04 tok/s=12489
[train] step=112340 tokens=1840.6M loss=2.1877 lr=1.19e-04 tok/s=12489
```
