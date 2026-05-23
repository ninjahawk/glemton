# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 15:49:29 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1946M / 3000M (64.9%) |
| Step | 118760 |
| Latest loss | 2.1862 |
| Avg loss (last 30 logged) | 2.0870 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 23:26:50 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.15 -> 2.73 -> 2.20 -> 2.22 -> 2.17 -> 2.72 -> 1.68 -> 2.37 -> 2.20 -> 2.21 -> 2.07 -> 1.89

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=118650 tokens=1944.0M loss=2.1845 lr=1.06e-04 tok/s=12489
[train] step=118660 tokens=1944.1M loss=1.7991 lr=1.06e-04 tok/s=12489
[train] step=118670 tokens=1944.3M loss=1.7434 lr=1.06e-04 tok/s=12489
[train] step=118680 tokens=1944.5M loss=2.0344 lr=1.06e-04 tok/s=12489
[train] step=118690 tokens=1944.6M loss=2.0159 lr=1.06e-04 tok/s=12489
[train] step=118700 tokens=1944.8M loss=2.1342 lr=1.05e-04 tok/s=12489
[train] step=118710 tokens=1944.9M loss=1.7305 lr=1.05e-04 tok/s=12489
[train] step=118720 tokens=1945.1M loss=2.0539 lr=1.05e-04 tok/s=12489
[train] step=118730 tokens=1945.3M loss=2.1586 lr=1.05e-04 tok/s=12489
[train] step=118740 tokens=1945.4M loss=1.8877 lr=1.05e-04 tok/s=12489
[train] step=118750 tokens=1945.6M loss=1.7316 lr=1.05e-04 tok/s=12489
[train] step=118760 tokens=1945.8M loss=2.1862 lr=1.05e-04 tok/s=12489
```
