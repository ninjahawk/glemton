# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 02:17:28 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1337M / 3000M (44.6%) |
| Step | 81610 |
| Latest loss | 2.3294 |
| Avg loss (last 30 logged) | 2.1753 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 12:59:30 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.16 -> 2.04 -> 2.03 -> 2.26 -> 2.21 -> 2.36 -> 1.92 -> 2.28 -> 2.16 -> 1.99 -> 2.38 -> 1.84

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`

## Recent log tail
```
[train] step=81500 tokens=1335.3M loss=2.0034 lr=1.90e-04 tok/s=12487
[train] step=81510 tokens=1335.5M loss=2.3947 lr=1.90e-04 tok/s=12487
[train] step=81520 tokens=1335.6M loss=2.1898 lr=1.90e-04 tok/s=12487
[train] step=81530 tokens=1335.8M loss=2.1539 lr=1.90e-04 tok/s=12487
[train] step=81540 tokens=1336.0M loss=2.0841 lr=1.90e-04 tok/s=12487
[train] step=81550 tokens=1336.1M loss=1.9996 lr=1.90e-04 tok/s=12487
[train] step=81560 tokens=1336.3M loss=1.8022 lr=1.90e-04 tok/s=12487
[train] step=81570 tokens=1336.4M loss=2.2442 lr=1.90e-04 tok/s=12487
[train] step=81580 tokens=1336.6M loss=2.5038 lr=1.90e-04 tok/s=12487
[train] step=81590 tokens=1336.8M loss=1.8436 lr=1.90e-04 tok/s=12487
[train] step=81600 tokens=1336.9M loss=2.1240 lr=1.90e-04 tok/s=12487
[train] step=81610 tokens=1337.1M loss=2.3294 lr=1.90e-04 tok/s=12487
```
