# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 12:05:16 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 698M / 3000M (23.3%) |
| Step | 42620 |
| Latest loss | 2.3575 |
| Avg loss (last 30 logged) | 2.4178 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 3:13:06 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.65 -> 2.43 -> 2.36 -> 2.40 -> 2.20 -> 2.28 -> 2.28 -> 2.21 -> 2.49 -> 2.35 -> 2.81 -> 2.47

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=42510 tokens=696.5M loss=2.1956 lr=2.67e-04 tok/s=12483
[train] step=42520 tokens=696.6M loss=2.4065 lr=2.67e-04 tok/s=12483
[train] step=42530 tokens=696.8M loss=2.0716 lr=2.67e-04 tok/s=12483
[train] step=42540 tokens=697.0M loss=2.3752 lr=2.67e-04 tok/s=12483
[train] step=42550 tokens=697.1M loss=2.3915 lr=2.67e-04 tok/s=12483
[train] step=42560 tokens=697.3M loss=2.1705 lr=2.67e-04 tok/s=12483
[train] step=42570 tokens=697.5M loss=2.1889 lr=2.67e-04 tok/s=12483
[train] step=42580 tokens=697.6M loss=2.2565 lr=2.67e-04 tok/s=12483
[train] step=42590 tokens=697.8M loss=2.4740 lr=2.67e-04 tok/s=12483
[train] step=42600 tokens=698.0M loss=2.4438 lr=2.67e-04 tok/s=12483
[train] step=42610 tokens=698.1M loss=2.3574 lr=2.67e-04 tok/s=12483
[train] step=42620 tokens=698.3M loss=2.3575 lr=2.67e-04 tok/s=12483
```
