# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 02:07:27 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1330M / 3000M (44.3%) |
| Step | 81150 |
| Latest loss | 2.2773 |
| Avg loss (last 30 logged) | 2.3142 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 13:09:31 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.73 -> 2.54 -> 2.12 -> 2.24 -> 2.38 -> 1.97 -> 1.80 -> 1.85 -> 2.47 -> 2.44 -> 1.89 -> 2.36

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`

## Recent log tail
```
[train] step=81040 tokens=1327.8M loss=2.3469 lr=1.91e-04 tok/s=12487
[train] step=81050 tokens=1327.9M loss=2.0376 lr=1.91e-04 tok/s=12487
[train] step=81060 tokens=1328.1M loss=2.3311 lr=1.91e-04 tok/s=12487
[train] step=81070 tokens=1328.3M loss=2.5612 lr=1.91e-04 tok/s=12487
[train] step=81080 tokens=1328.4M loss=2.3498 lr=1.91e-04 tok/s=12487
[train] step=81090 tokens=1328.6M loss=2.0134 lr=1.91e-04 tok/s=12487
[train] step=81100 tokens=1328.7M loss=2.3773 lr=1.91e-04 tok/s=12487
[train] step=81110 tokens=1328.9M loss=3.0102 lr=1.91e-04 tok/s=12487
[train] step=81120 tokens=1329.1M loss=2.3107 lr=1.91e-04 tok/s=12487
[train] step=81130 tokens=1329.2M loss=2.3623 lr=1.91e-04 tok/s=12487
[train] step=81140 tokens=1329.4M loss=1.9358 lr=1.91e-04 tok/s=12487
[train] step=81150 tokens=1329.6M loss=2.2773 lr=1.91e-04 tok/s=12487
```
