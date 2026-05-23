# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 03:57:43 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1412M / 3000M (47.1%) |
| Step | 86190 |
| Latest loss | 2.3469 |
| Avg loss (last 30 logged) | 2.2020 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 11:19:24 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.06 -> 2.49 -> 2.45 -> 1.93 -> 2.23 -> 2.16 -> 2.14 -> 2.05 -> 1.84 -> 2.13 -> 2.20 -> 2.03

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`

## Recent log tail
```
[train] step=86080 tokens=1410.3M loss=2.4729 lr=1.80e-04 tok/s=12487
[train] step=86090 tokens=1410.5M loss=2.3570 lr=1.80e-04 tok/s=12487
[train] step=86100 tokens=1410.7M loss=2.4006 lr=1.79e-04 tok/s=12487
[train] step=86110 tokens=1410.8M loss=2.5847 lr=1.79e-04 tok/s=12487
[train] step=86120 tokens=1411.0M loss=2.4797 lr=1.79e-04 tok/s=12487
[train] step=86130 tokens=1411.2M loss=2.2344 lr=1.79e-04 tok/s=12487
[train] step=86140 tokens=1411.3M loss=1.8594 lr=1.79e-04 tok/s=12487
[train] step=86150 tokens=1411.5M loss=1.7340 lr=1.79e-04 tok/s=12487
[train] step=86160 tokens=1411.6M loss=1.8994 lr=1.79e-04 tok/s=12487
[train] step=86170 tokens=1411.8M loss=2.0310 lr=1.79e-04 tok/s=12487
[train] step=86180 tokens=1412.0M loss=2.3978 lr=1.79e-04 tok/s=12487
[train] step=86190 tokens=1412.1M loss=2.3469 lr=1.79e-04 tok/s=12487
```
