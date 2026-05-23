# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 03:47:42 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1405M / 3000M (46.8%) |
| Step | 85730 |
| Latest loss | 2.2329 |
| Avg loss (last 30 logged) | 2.1519 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 11:29:24 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.25 -> 2.30 -> 2.48 -> 1.96 -> 1.88 -> 2.54 -> 2.34 -> 1.86 -> 2.55 -> 2.13 -> 1.96 -> 2.52

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`

## Recent log tail
```
[train] step=85620 tokens=1402.8M loss=2.1001 lr=1.81e-04 tok/s=12487
[train] step=85630 tokens=1403.0M loss=1.7314 lr=1.81e-04 tok/s=12487
[train] step=85640 tokens=1403.1M loss=1.9925 lr=1.81e-04 tok/s=12487
[train] step=85650 tokens=1403.3M loss=2.0065 lr=1.81e-04 tok/s=12487
[train] step=85660 tokens=1403.5M loss=2.1023 lr=1.81e-04 tok/s=12487
[train] step=85670 tokens=1403.6M loss=2.1975 lr=1.80e-04 tok/s=12487
[train] step=85680 tokens=1403.8M loss=2.3010 lr=1.80e-04 tok/s=12487
[train] step=85690 tokens=1403.9M loss=2.6137 lr=1.80e-04 tok/s=12487
[train] step=85700 tokens=1404.1M loss=2.0056 lr=1.80e-04 tok/s=12487
[train] step=85710 tokens=1404.3M loss=2.5229 lr=1.80e-04 tok/s=12487
[train] step=85720 tokens=1404.4M loss=1.9314 lr=1.80e-04 tok/s=12487
[train] step=85730 tokens=1404.6M loss=2.2329 lr=1.80e-04 tok/s=12487
```
