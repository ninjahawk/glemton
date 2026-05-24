# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 01:40:59 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2389M / 3000M (79.6%) |
| Step | 145820 |
| Latest loss | 2.1291 |
| Avg loss (last 30 logged) | 2.0314 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 13:35:15 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.98 -> 1.95 -> 2.21 -> 1.95 -> 1.73 -> 2.29 -> 2.10 -> 1.87 -> 2.21 -> 2.26 -> 2.22 -> 2.10

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=145710 tokens=2387.3M loss=2.0675 lr=5.73e-05 tok/s=12489
[train] step=145720 tokens=2387.5M loss=1.7544 lr=5.73e-05 tok/s=12489
[train] step=145730 tokens=2387.6M loss=1.9199 lr=5.73e-05 tok/s=12489
[train] step=145740 tokens=2387.8M loss=2.1579 lr=5.72e-05 tok/s=12489
[train] step=145750 tokens=2388.0M loss=1.9629 lr=5.72e-05 tok/s=12489
[train] step=145760 tokens=2388.1M loss=2.2773 lr=5.72e-05 tok/s=12489
[train] step=145770 tokens=2388.3M loss=1.7896 lr=5.72e-05 tok/s=12489
[train] step=145780 tokens=2388.5M loss=2.2581 lr=5.72e-05 tok/s=12489
[train] step=145790 tokens=2388.6M loss=2.1048 lr=5.72e-05 tok/s=12489
[train] step=145800 tokens=2388.8M loss=1.8060 lr=5.72e-05 tok/s=12489
[train] step=145810 tokens=2389.0M loss=1.7110 lr=5.71e-05 tok/s=12489
[train] step=145820 tokens=2389.1M loss=2.1291 lr=5.71e-05 tok/s=12489
```
