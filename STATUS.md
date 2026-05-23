# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 04:47:51 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1450M / 3000M (48.3%) |
| Step | 88490 |
| Latest loss | 2.2033 |
| Avg loss (last 30 logged) | 2.2016 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 10:29:05 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.21 -> 2.90 -> 2.19 -> 2.15 -> 1.90 -> 2.21 -> 2.15 -> 2.09 -> 1.81 -> 2.19 -> 2.77 -> 1.86

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`

## Recent log tail
```
[train] step=88380 tokens=1448.0M loss=1.9392 lr=1.74e-04 tok/s=12487
[train] step=88390 tokens=1448.2M loss=2.2828 lr=1.74e-04 tok/s=12487
[train] step=88400 tokens=1448.3M loss=2.3630 lr=1.74e-04 tok/s=12487
[train] step=88410 tokens=1448.5M loss=2.1284 lr=1.74e-04 tok/s=12487
[train] step=88420 tokens=1448.7M loss=2.0246 lr=1.74e-04 tok/s=12487
[train] step=88430 tokens=1448.8M loss=2.2060 lr=1.74e-04 tok/s=12487
[train] step=88440 tokens=1449.0M loss=1.7452 lr=1.74e-04 tok/s=12487
[train] step=88450 tokens=1449.2M loss=2.7431 lr=1.74e-04 tok/s=12487
[train] step=88460 tokens=1449.3M loss=2.2053 lr=1.74e-04 tok/s=12487
[train] step=88470 tokens=1449.5M loss=1.8644 lr=1.74e-04 tok/s=12487
[train] step=88480 tokens=1449.7M loss=2.2517 lr=1.74e-04 tok/s=12487
[train] step=88490 tokens=1449.8M loss=2.2033 lr=1.74e-04 tok/s=12487
```
