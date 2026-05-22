# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 10:35:01 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 631M / 3000M (21.0%) |
| Step | 38500 |
| Latest loss | 2.2596 |
| Avg loss (last 30 logged) | 2.3128 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 4:43:14 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.24 -> 2.35 -> 2.13 -> 2.11 -> 2.37 -> 2.38 -> 2.34 -> 2.04 -> 2.35 -> 2.32 -> 2.15 -> 2.44

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=38390 tokens=629.0M loss=2.2968 lr=2.73e-04 tok/s=12483
[train] step=38400 tokens=629.1M loss=2.2217 lr=2.73e-04 tok/s=12483
[train] step=38410 tokens=629.3M loss=2.3160 lr=2.73e-04 tok/s=12483
[train] step=38420 tokens=629.5M loss=2.1803 lr=2.73e-04 tok/s=12483
[train] step=38430 tokens=629.6M loss=2.0858 lr=2.73e-04 tok/s=12483
[train] step=38440 tokens=629.8M loss=2.5133 lr=2.73e-04 tok/s=12483
[train] step=38450 tokens=630.0M loss=2.1744 lr=2.73e-04 tok/s=12483
[train] step=38460 tokens=630.1M loss=2.3913 lr=2.73e-04 tok/s=12483
[train] step=38470 tokens=630.3M loss=2.1924 lr=2.73e-04 tok/s=12483
[train] step=38480 tokens=630.5M loss=2.4419 lr=2.73e-04 tok/s=12483
[train] step=38490 tokens=630.6M loss=2.2603 lr=2.73e-04 tok/s=12483
[train] step=38500 tokens=630.8M loss=2.2596 lr=2.73e-04 tok/s=12483
```
