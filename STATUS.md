# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 03:37:41 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1397M / 3000M (46.6%) |
| Step | 85280 |
| Latest loss | 1.9746 |
| Avg loss (last 30 logged) | 2.1976 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 11:39:17 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.94 -> 2.28 -> 2.31 -> 2.23 -> 2.06 -> 2.11 -> 2.15 -> 2.45 -> 2.25 -> 2.12 -> 2.53 -> 1.82

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`

## Recent log tail
```
[train] step=85170 tokens=1395.4M loss=2.8965 lr=1.82e-04 tok/s=12487
[train] step=85180 tokens=1395.6M loss=1.8430 lr=1.82e-04 tok/s=12487
[train] step=85190 tokens=1395.8M loss=1.9914 lr=1.82e-04 tok/s=12487
[train] step=85200 tokens=1395.9M loss=2.1861 lr=1.82e-04 tok/s=12487
[train] step=85210 tokens=1396.1M loss=1.7905 lr=1.82e-04 tok/s=12487
[train] step=85220 tokens=1396.2M loss=1.9420 lr=1.82e-04 tok/s=12487
[train] step=85230 tokens=1396.4M loss=2.2588 lr=1.82e-04 tok/s=12487
[train] step=85240 tokens=1396.6M loss=2.0041 lr=1.81e-04 tok/s=12487
[train] step=85250 tokens=1396.7M loss=1.8187 lr=1.81e-04 tok/s=12487
[train] step=85260 tokens=1396.9M loss=2.4613 lr=1.81e-04 tok/s=12487
[train] step=85270 tokens=1397.1M loss=2.2604 lr=1.81e-04 tok/s=12487
[train] step=85280 tokens=1397.2M loss=1.9746 lr=1.81e-04 tok/s=12487
```
