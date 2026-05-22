# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 05:14:07 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 391M / 3000M (13.0%) |
| Step | 23840 |
| Latest loss | 2.2610 |
| Avg loss (last 30 logged) | 2.4251 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 2 days, 10:02:49 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.68 -> 2.60 -> 2.38 -> 2.87 -> 2.73 -> 2.18 -> 2.54 -> 2.51 -> 2.44 -> 2.25 -> 2.55 -> 2.24

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=23730 tokens=388.8M loss=2.4822 lr=2.90e-04 tok/s=12487
[train] step=23740 tokens=389.0M loss=2.4049 lr=2.90e-04 tok/s=12487
[train] step=23750 tokens=389.1M loss=2.5446 lr=2.90e-04 tok/s=12487
[train] step=23760 tokens=389.3M loss=2.5095 lr=2.90e-04 tok/s=12487
[train] step=23770 tokens=389.4M loss=2.1546 lr=2.90e-04 tok/s=12487
[train] step=23780 tokens=389.6M loss=2.4777 lr=2.90e-04 tok/s=12487
[train] step=23790 tokens=389.8M loss=2.2978 lr=2.90e-04 tok/s=12487
[train] step=23800 tokens=389.9M loss=2.0759 lr=2.90e-04 tok/s=12487
[train] step=23810 tokens=390.1M loss=2.2400 lr=2.90e-04 tok/s=12487
[train] step=23820 tokens=390.3M loss=2.3951 lr=2.90e-04 tok/s=12487
[train] step=23830 tokens=390.4M loss=2.4980 lr=2.90e-04 tok/s=12487
[train] step=23840 tokens=390.6M loss=2.2610 lr=2.90e-04 tok/s=12487
```
