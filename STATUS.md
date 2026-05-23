# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 05:07:54 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1465M / 3000M (48.8%) |
| Step | 89400 |
| Latest loss | 1.9251 |
| Avg loss (last 30 logged) | 2.0917 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 10:09:11 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.08 -> 2.47 -> 2.11 -> 2.18 -> 1.78 -> 1.91 -> 2.50 -> 2.28 -> 2.28 -> 2.11 -> 2.14 -> 1.89

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`

## Recent log tail
```
[train] step=89290 tokens=1462.9M loss=2.3693 lr=1.72e-04 tok/s=12487
[train] step=89300 tokens=1463.1M loss=2.3217 lr=1.72e-04 tok/s=12487
[train] step=89310 tokens=1463.3M loss=2.0328 lr=1.72e-04 tok/s=12487
[train] step=89320 tokens=1463.4M loss=2.2046 lr=1.72e-04 tok/s=12487
[train] step=89330 tokens=1463.6M loss=2.1219 lr=1.72e-04 tok/s=12487
[train] step=89340 tokens=1463.7M loss=1.9896 lr=1.72e-04 tok/s=12487
[train] step=89350 tokens=1463.9M loss=2.2134 lr=1.72e-04 tok/s=12487
[train] step=89360 tokens=1464.1M loss=2.4111 lr=1.72e-04 tok/s=12487
[train] step=89370 tokens=1464.2M loss=1.9602 lr=1.72e-04 tok/s=12487
[train] step=89380 tokens=1464.4M loss=1.8891 lr=1.72e-04 tok/s=12487
[train] step=89390 tokens=1464.6M loss=2.2359 lr=1.72e-04 tok/s=12487
[train] step=89400 tokens=1464.7M loss=1.9251 lr=1.72e-04 tok/s=12487
```
