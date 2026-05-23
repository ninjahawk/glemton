# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 04:07:45 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1420M / 3000M (47.3%) |
| Step | 86650 |
| Latest loss | 2.0835 |
| Avg loss (last 30 logged) | 2.1387 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 11:09:15 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.30 -> 2.42 -> 2.65 -> 2.15 -> 2.09 -> 2.54 -> 2.20 -> 1.99 -> 1.99 -> 1.99 -> 2.35 -> 1.91

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`

## Recent log tail
```
[train] step=86540 tokens=1417.9M loss=2.1975 lr=1.78e-04 tok/s=12487
[train] step=86550 tokens=1418.0M loss=1.9618 lr=1.78e-04 tok/s=12487
[train] step=86560 tokens=1418.2M loss=1.7828 lr=1.78e-04 tok/s=12487
[train] step=86570 tokens=1418.4M loss=2.1320 lr=1.78e-04 tok/s=12487
[train] step=86580 tokens=1418.5M loss=2.1378 lr=1.78e-04 tok/s=12487
[train] step=86590 tokens=1418.7M loss=1.9509 lr=1.78e-04 tok/s=12487
[train] step=86600 tokens=1418.9M loss=2.4859 lr=1.78e-04 tok/s=12487
[train] step=86610 tokens=1419.0M loss=2.0276 lr=1.78e-04 tok/s=12487
[train] step=86620 tokens=1419.2M loss=2.2268 lr=1.78e-04 tok/s=12487
[train] step=86630 tokens=1419.3M loss=1.9116 lr=1.78e-04 tok/s=12487
[train] step=86640 tokens=1419.5M loss=2.2300 lr=1.78e-04 tok/s=12487
[train] step=86650 tokens=1419.7M loss=2.0835 lr=1.78e-04 tok/s=12487
```
