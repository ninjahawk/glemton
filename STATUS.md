# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 00:27:11 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1254M / 3000M (41.8%) |
| Step | 76560 |
| Latest loss | 1.9520 |
| Avg loss (last 30 logged) | 2.2480 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 14:50:04 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.40 -> 2.20 -> 2.05 -> 1.93 -> 1.84 -> 2.06 -> 2.26 -> 2.40 -> 2.33 -> 2.05 -> 2.29 -> 2.22

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] step=76450 tokens=1252.6M loss=2.3854 lr=2.02e-04 tok/s=12486
[train] step=76460 tokens=1252.7M loss=2.2060 lr=2.02e-04 tok/s=12486
[train] step=76470 tokens=1252.9M loss=2.0669 lr=2.02e-04 tok/s=12486
[train] step=76480 tokens=1253.0M loss=2.1336 lr=2.02e-04 tok/s=12486
[train] step=76490 tokens=1253.2M loss=2.0748 lr=2.02e-04 tok/s=12486
[train] step=76500 tokens=1253.4M loss=2.5035 lr=2.01e-04 tok/s=12486
[train] step=76510 tokens=1253.5M loss=2.4369 lr=2.01e-04 tok/s=12486
[train] step=76520 tokens=1253.7M loss=2.1551 lr=2.01e-04 tok/s=12486
[train] step=76530 tokens=1253.9M loss=2.7172 lr=2.01e-04 tok/s=12486
[train] step=76540 tokens=1254.0M loss=2.2197 lr=2.01e-04 tok/s=12486
[train] step=76550 tokens=1254.2M loss=2.2013 lr=2.01e-04 tok/s=12486
[train] step=76560 tokens=1254.4M loss=1.9520 lr=2.01e-04 tok/s=12486
```
