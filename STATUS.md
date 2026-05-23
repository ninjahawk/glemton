# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 04:57:52 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1457M / 3000M (48.6%) |
| Step | 88950 |
| Latest loss | 2.6878 |
| Avg loss (last 30 logged) | 2.1311 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 10:18:56 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.19 -> 1.73 -> 1.83 -> 2.15 -> 2.23 -> 2.41 -> 1.91 -> 2.00 -> 2.46 -> 1.99 -> 1.83 -> 2.53

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`

## Recent log tail
```
[train] step=88840 tokens=1455.6M loss=2.4419 lr=1.73e-04 tok/s=12487
[train] step=88850 tokens=1455.7M loss=2.2037 lr=1.73e-04 tok/s=12487
[train] step=88860 tokens=1455.9M loss=1.8270 lr=1.73e-04 tok/s=12487
[train] step=88870 tokens=1456.0M loss=2.2972 lr=1.73e-04 tok/s=12487
[train] step=88880 tokens=1456.2M loss=1.9862 lr=1.73e-04 tok/s=12487
[train] step=88890 tokens=1456.4M loss=1.9878 lr=1.73e-04 tok/s=12487
[train] step=88900 tokens=1456.5M loss=2.4115 lr=1.73e-04 tok/s=12487
[train] step=88910 tokens=1456.7M loss=1.9132 lr=1.73e-04 tok/s=12487
[train] step=88920 tokens=1456.9M loss=1.8745 lr=1.73e-04 tok/s=12487
[train] step=88930 tokens=1457.0M loss=2.5349 lr=1.73e-04 tok/s=12487
[train] step=88940 tokens=1457.2M loss=2.0251 lr=1.73e-04 tok/s=12487
[train] step=88950 tokens=1457.4M loss=2.6878 lr=1.73e-04 tok/s=12487
```
