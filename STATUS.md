# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 16:39:36 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1983M / 3000M (66.1%) |
| Step | 121060 |
| Latest loss | 1.9619 |
| Avg loss (last 30 logged) | 2.1022 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 22:36:39 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.82 -> 1.74 -> 2.15 -> 2.33 -> 2.05 -> 1.86 -> 2.04 -> 1.91 -> 2.11 -> 2.09 -> 1.81 -> 2.39

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
[train] step=120950 tokens=1981.6M loss=1.6690 lr=1.01e-04 tok/s=12489
[train] step=120960 tokens=1981.8M loss=2.1450 lr=1.01e-04 tok/s=12489
[train] step=120970 tokens=1982.0M loss=2.0269 lr=1.01e-04 tok/s=12489
[train] step=120980 tokens=1982.1M loss=2.2341 lr=1.01e-04 tok/s=12489
[train] step=120990 tokens=1982.3M loss=2.2543 lr=1.01e-04 tok/s=12489
[train] step=121000 tokens=1982.5M loss=2.3042 lr=1.01e-04 tok/s=12489
[train] step=121010 tokens=1982.6M loss=2.5423 lr=1.01e-04 tok/s=12489
[train] step=121020 tokens=1982.8M loss=1.8707 lr=1.01e-04 tok/s=12489
[train] step=121030 tokens=1983.0M loss=2.3920 lr=1.01e-04 tok/s=12489
[train] step=121040 tokens=1983.1M loss=2.1444 lr=1.01e-04 tok/s=12489
[train] step=121050 tokens=1983.3M loss=2.1516 lr=1.01e-04 tok/s=12489
[train] step=121060 tokens=1983.4M loss=1.9619 lr=1.01e-04 tok/s=12489
```
