# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 01:47:24 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1314M / 3000M (43.8%) |
| Step | 80230 |
| Latest loss | 2.8051 |
| Avg loss (last 30 logged) | 2.1440 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 13:29:40 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.40 -> 2.01 -> 2.18 -> 2.04 -> 2.01 -> 2.13 -> 1.98 -> 2.05 -> 2.33 -> 2.26 -> 2.20 -> 1.96

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`

## Recent log tail
```
[train] step=80120 tokens=1312.7M loss=2.2675 lr=1.93e-04 tok/s=12487
[train] step=80130 tokens=1312.8M loss=1.9897 lr=1.93e-04 tok/s=12487
[train] step=80140 tokens=1313.0M loss=2.4741 lr=1.93e-04 tok/s=12487
[train] step=80150 tokens=1313.2M loss=2.0124 lr=1.93e-04 tok/s=12487
[train] step=80160 tokens=1313.3M loss=2.0832 lr=1.93e-04 tok/s=12487
[train] step=80170 tokens=1313.5M loss=2.0214 lr=1.93e-04 tok/s=12487
[train] step=80180 tokens=1313.7M loss=1.9597 lr=1.93e-04 tok/s=12487
[train] step=80190 tokens=1313.8M loss=2.0265 lr=1.93e-04 tok/s=12487
[train] step=80200 tokens=1314.0M loss=2.1410 lr=1.93e-04 tok/s=12487
[train] step=80210 tokens=1314.2M loss=1.9647 lr=1.93e-04 tok/s=12487
[train] step=80220 tokens=1314.3M loss=2.1185 lr=1.93e-04 tok/s=12487
[train] step=80230 tokens=1314.5M loss=2.8051 lr=1.93e-04 tok/s=12487
```
