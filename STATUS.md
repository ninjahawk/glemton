# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 02:27:30 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1345M / 3000M (44.8%) |
| Step | 82070 |
| Latest loss | 2.3765 |
| Avg loss (last 30 logged) | 2.1948 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 12:49:29 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.79 -> 2.16 -> 2.55 -> 2.62 -> 2.01 -> 1.87 -> 2.15 -> 2.35 -> 2.33 -> 1.94 -> 2.68 -> 2.57

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`

## Recent log tail
```
[train] step=81960 tokens=1342.8M loss=1.9349 lr=1.89e-04 tok/s=12487
[train] step=81970 tokens=1343.0M loss=2.5388 lr=1.89e-04 tok/s=12487
[train] step=81980 tokens=1343.2M loss=1.7690 lr=1.89e-04 tok/s=12487
[train] step=81990 tokens=1343.3M loss=2.3310 lr=1.89e-04 tok/s=12487
[train] step=82000 tokens=1343.5M loss=2.1221 lr=1.89e-04 tok/s=12487
[train] step=82010 tokens=1343.7M loss=1.6775 lr=1.89e-04 tok/s=12487
[train] step=82020 tokens=1343.8M loss=2.2501 lr=1.89e-04 tok/s=12487
[train] step=82030 tokens=1344.0M loss=2.3792 lr=1.89e-04 tok/s=12487
[train] step=82040 tokens=1344.1M loss=1.8463 lr=1.89e-04 tok/s=12487
[train] step=82050 tokens=1344.3M loss=2.5654 lr=1.89e-04 tok/s=12487
[train] step=82060 tokens=1344.5M loss=2.0015 lr=1.89e-04 tok/s=12487
[train] step=82070 tokens=1344.6M loss=2.3765 lr=1.89e-04 tok/s=12487
```
