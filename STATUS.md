# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 15:15:45 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 841M / 3000M (28.0%) |
| Step | 51340 |
| Latest loss | 3.0640 |
| Avg loss (last 30 logged) | 2.2929 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 0:02:05 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.49 -> 2.45 -> 2.45 -> 2.52 -> 2.44 -> 1.98 -> 2.10 -> 2.71 -> 2.41 -> 2.48 -> 2.43 -> 2.48

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`

## Recent log tail
```
[train] step=51230 tokens=839.4M loss=1.9531 lr=2.53e-04 tok/s=12484
[train] step=51240 tokens=839.5M loss=2.1503 lr=2.53e-04 tok/s=12484
[train] step=51250 tokens=839.7M loss=2.5310 lr=2.53e-04 tok/s=12484
[train] step=51260 tokens=839.8M loss=2.2078 lr=2.53e-04 tok/s=12484
[train] step=51270 tokens=840.0M loss=2.1747 lr=2.53e-04 tok/s=12484
[train] step=51280 tokens=840.2M loss=2.6340 lr=2.53e-04 tok/s=12484
[train] step=51290 tokens=840.3M loss=2.4795 lr=2.53e-04 tok/s=12484
[train] step=51300 tokens=840.5M loss=2.4144 lr=2.53e-04 tok/s=12484
[train] step=51310 tokens=840.7M loss=2.2054 lr=2.53e-04 tok/s=12484
[train] step=51320 tokens=840.8M loss=2.4797 lr=2.53e-04 tok/s=12484
[train] step=51330 tokens=841.0M loss=2.1428 lr=2.53e-04 tok/s=12484
[train] step=51340 tokens=841.2M loss=3.0640 lr=2.53e-04 tok/s=12484
```
