# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 09:54:54 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 601M / 3000M (20.0%) |
| Step | 36660 |
| Latest loss | 2.3667 |
| Avg loss (last 30 logged) | 2.4005 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 5:23:33 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.57 -> 2.32 -> 2.28 -> 2.26 -> 2.55 -> 2.27 -> 2.17 -> 2.28 -> 2.12 -> 2.43 -> 2.63 -> 2.58

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=36560 tokens=599.0M loss=2.0085 lr=2.76e-04 tok/s=12483
[train] step=36570 tokens=599.2M loss=2.4548 lr=2.76e-04 tok/s=12483
[train] step=36580 tokens=599.3M loss=2.3324 lr=2.76e-04 tok/s=12483
[train] step=36590 tokens=599.5M loss=2.3232 lr=2.76e-04 tok/s=12483
[train] step=36600 tokens=599.7M loss=2.2967 lr=2.76e-04 tok/s=12483
[train] step=36610 tokens=599.8M loss=2.3207 lr=2.76e-04 tok/s=12483
[train] step=36620 tokens=600.0M loss=2.3990 lr=2.76e-04 tok/s=12483
[train] checkpoint -> checkpoints\glemton-350m\step_36622_tokens_600M.pt
[train] step=36630 tokens=600.1M loss=2.2894 lr=2.76e-04 tok/s=12483
[train] step=36640 tokens=600.3M loss=2.5810 lr=2.76e-04 tok/s=12483
[train] step=36650 tokens=600.5M loss=3.0994 lr=2.76e-04 tok/s=12483
[train] step=36660 tokens=600.6M loss=2.3667 lr=2.76e-04 tok/s=12483
```
