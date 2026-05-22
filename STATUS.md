# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 10:14:57 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 616M / 3000M (20.5%) |
| Step | 37580 |
| Latest loss | 2.4261 |
| Avg loss (last 30 logged) | 2.3969 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 5:03:23 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.33 -> 2.37 -> 2.50 -> 2.50 -> 2.21 -> 2.47 -> 2.33 -> 2.45 -> 2.45 -> 2.63 -> 2.43 -> 2.40

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=37470 tokens=613.9M loss=2.2544 lr=2.75e-04 tok/s=12483
[train] step=37480 tokens=614.1M loss=2.4064 lr=2.75e-04 tok/s=12483
[train] step=37490 tokens=614.2M loss=2.3498 lr=2.75e-04 tok/s=12483
[train] step=37500 tokens=614.4M loss=2.3620 lr=2.75e-04 tok/s=12483
[train] step=37510 tokens=614.6M loss=2.0807 lr=2.75e-04 tok/s=12483
[train] step=37520 tokens=614.7M loss=2.8177 lr=2.75e-04 tok/s=12483
[train] step=37530 tokens=614.9M loss=2.3925 lr=2.75e-04 tok/s=12483
[train] step=37540 tokens=615.1M loss=2.2131 lr=2.75e-04 tok/s=12483
[train] step=37550 tokens=615.2M loss=2.0117 lr=2.75e-04 tok/s=12483
[train] step=37560 tokens=615.4M loss=2.4045 lr=2.75e-04 tok/s=12483
[train] step=37570 tokens=615.5M loss=2.3295 lr=2.75e-04 tok/s=12483
[train] step=37580 tokens=615.7M loss=2.4261 lr=2.75e-04 tok/s=12483
```
