# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 03:17:38 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1382M / 3000M (46.1%) |
| Step | 84360 |
| Latest loss | 1.7326 |
| Avg loss (last 30 logged) | 2.2390 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 11:59:18 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.11 -> 2.16 -> 2.69 -> 2.41 -> 2.25 -> 2.26 -> 2.03 -> 1.91 -> 1.77 -> 2.31 -> 2.56 -> 2.27

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`

## Recent log tail
```
[train] step=84250 tokens=1380.4M loss=2.9177 lr=1.84e-04 tok/s=12487
[train] step=84260 tokens=1380.5M loss=2.2505 lr=1.84e-04 tok/s=12487
[train] step=84270 tokens=1380.7M loss=2.1991 lr=1.84e-04 tok/s=12487
[train] step=84280 tokens=1380.8M loss=1.4929 lr=1.84e-04 tok/s=12487
[train] step=84290 tokens=1381.0M loss=2.4382 lr=1.84e-04 tok/s=12487
[train] step=84300 tokens=1381.2M loss=2.2228 lr=1.84e-04 tok/s=12487
[train] step=84310 tokens=1381.3M loss=2.3449 lr=1.84e-04 tok/s=12487
[train] step=84320 tokens=1381.5M loss=2.0899 lr=1.84e-04 tok/s=12487
[train] step=84330 tokens=1381.7M loss=2.2703 lr=1.84e-04 tok/s=12487
[train] step=84340 tokens=1381.8M loss=2.2979 lr=1.84e-04 tok/s=12487
[train] step=84350 tokens=1382.0M loss=1.8564 lr=1.84e-04 tok/s=12487
[train] step=84360 tokens=1382.2M loss=1.7326 lr=1.84e-04 tok/s=12487
```
