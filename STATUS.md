# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 11:35:11 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 676M / 3000M (22.5%) |
| Step | 41250 |
| Latest loss | 2.1218 |
| Avg loss (last 30 logged) | 2.3887 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 3:43:09 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.20 -> 2.04 -> 2.37 -> 2.42 -> 2.62 -> 2.24 -> 2.51 -> 2.27 -> 2.21 -> 2.25 -> 2.64 -> 2.08

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=41140 tokens=674.0M loss=2.0933 lr=2.70e-04 tok/s=12483
[train] step=41150 tokens=674.2M loss=2.4539 lr=2.69e-04 tok/s=12483
[train] step=41160 tokens=674.4M loss=2.7677 lr=2.69e-04 tok/s=12483
[train] step=41170 tokens=674.5M loss=2.4423 lr=2.69e-04 tok/s=12483
[train] step=41180 tokens=674.7M loss=2.1426 lr=2.69e-04 tok/s=12483
[train] step=41190 tokens=674.9M loss=2.2662 lr=2.69e-04 tok/s=12483
[train] step=41200 tokens=675.0M loss=2.4548 lr=2.69e-04 tok/s=12483
[train] step=41210 tokens=675.2M loss=2.8655 lr=2.69e-04 tok/s=12483
[train] step=41220 tokens=675.3M loss=2.0778 lr=2.69e-04 tok/s=12483
[train] step=41230 tokens=675.5M loss=2.1976 lr=2.69e-04 tok/s=12483
[train] step=41240 tokens=675.7M loss=2.6682 lr=2.69e-04 tok/s=12483
[train] step=41250 tokens=675.8M loss=2.1218 lr=2.69e-04 tok/s=12483
```
