# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 02:37:31 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1352M / 3000M (45.1%) |
| Step | 82520 |
| Latest loss | 2.0528 |
| Avg loss (last 30 logged) | 2.2204 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 12:39:37 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.14 -> 2.38 -> 3.00 -> 2.28 -> 2.03 -> 2.23 -> 2.16 -> 2.26 -> 2.39 -> 1.77 -> 1.90 -> 2.24

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`

## Recent log tail
```
[train] step=82410 tokens=1350.2M loss=2.2970 lr=1.88e-04 tok/s=12487
[train] step=82420 tokens=1350.4M loss=2.1840 lr=1.88e-04 tok/s=12487
[train] step=82430 tokens=1350.5M loss=2.0509 lr=1.88e-04 tok/s=12487
[train] step=82440 tokens=1350.7M loss=2.2177 lr=1.88e-04 tok/s=12487
[train] step=82450 tokens=1350.9M loss=2.2245 lr=1.88e-04 tok/s=12487
[train] step=82460 tokens=1351.0M loss=2.0652 lr=1.88e-04 tok/s=12487
[train] step=82470 tokens=1351.2M loss=2.1179 lr=1.88e-04 tok/s=12487
[train] step=82480 tokens=1351.4M loss=2.2970 lr=1.88e-04 tok/s=12487
[train] step=82490 tokens=1351.5M loss=1.9615 lr=1.88e-04 tok/s=12487
[train] step=82500 tokens=1351.7M loss=2.2371 lr=1.88e-04 tok/s=12487
[train] step=82510 tokens=1351.8M loss=2.4320 lr=1.88e-04 tok/s=12487
[train] step=82520 tokens=1352.0M loss=2.0528 lr=1.88e-04 tok/s=12487
```
