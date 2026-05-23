# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 06:58:11 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1548M / 3000M (51.6%) |
| Step | 94450 |
| Latest loss | 2.0638 |
| Avg loss (last 30 logged) | 2.1351 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 8:18:31 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.20 -> 2.17 -> 2.26 -> 2.11 -> 2.04 -> 2.24 -> 1.71 -> 1.84 -> 2.45 -> 2.04 -> 2.02 -> 2.06

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=94340 tokens=1545.7M loss=2.2685 lr=1.60e-04 tok/s=12488
[train] step=94350 tokens=1545.8M loss=2.4275 lr=1.60e-04 tok/s=12488
[train] step=94360 tokens=1546.0M loss=1.8184 lr=1.60e-04 tok/s=12488
[train] step=94370 tokens=1546.2M loss=2.4064 lr=1.60e-04 tok/s=12488
[train] step=94380 tokens=1546.3M loss=2.0759 lr=1.60e-04 tok/s=12488
[train] step=94390 tokens=1546.5M loss=2.1316 lr=1.60e-04 tok/s=12488
[train] step=94400 tokens=1546.6M loss=2.0290 lr=1.60e-04 tok/s=12488
[train] step=94410 tokens=1546.8M loss=2.0353 lr=1.60e-04 tok/s=12488
[train] step=94420 tokens=1547.0M loss=2.2392 lr=1.60e-04 tok/s=12488
[train] step=94430 tokens=1547.1M loss=2.0645 lr=1.60e-04 tok/s=12488
[train] step=94440 tokens=1547.3M loss=2.1453 lr=1.60e-04 tok/s=12488
[train] step=94450 tokens=1547.5M loss=2.0638 lr=1.60e-04 tok/s=12488
```
