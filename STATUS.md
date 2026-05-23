# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 01:07:17 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1284M / 3000M (42.8%) |
| Step | 78400 |
| Latest loss | 2.4404 |
| Avg loss (last 30 logged) | 2.1970 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 14:09:42 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.00 -> 2.25 -> 1.97 -> 1.96 -> 2.13 -> 2.24 -> 2.30 -> 2.19 -> 2.50 -> 2.57 -> 2.18 -> 2.14

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] step=78290 tokens=1282.7M loss=2.0442 lr=1.97e-04 tok/s=12487
[train] step=78300 tokens=1282.9M loss=2.3503 lr=1.97e-04 tok/s=12487
[train] step=78310 tokens=1283.0M loss=2.3477 lr=1.97e-04 tok/s=12487
[train] step=78320 tokens=1283.2M loss=2.1815 lr=1.97e-04 tok/s=12487
[train] step=78330 tokens=1283.4M loss=2.0218 lr=1.97e-04 tok/s=12487
[train] step=78340 tokens=1283.5M loss=2.1801 lr=1.97e-04 tok/s=12487
[train] step=78350 tokens=1283.7M loss=2.2383 lr=1.97e-04 tok/s=12487
[train] step=78360 tokens=1283.9M loss=2.0775 lr=1.97e-04 tok/s=12487
[train] step=78370 tokens=1284.0M loss=2.1362 lr=1.97e-04 tok/s=12487
[train] step=78380 tokens=1284.2M loss=2.2684 lr=1.97e-04 tok/s=12487
[train] step=78390 tokens=1284.3M loss=2.5145 lr=1.97e-04 tok/s=12487
[train] step=78400 tokens=1284.5M loss=2.4404 lr=1.97e-04 tok/s=12487
```
