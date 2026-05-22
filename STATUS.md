# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 04:44:02 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 368M / 3000M (12.3%) |
| Step | 22460 |
| Latest loss | 2.6216 |
| Avg loss (last 30 logged) | 2.4743 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 2 days, 10:32:59 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.29 -> 2.18 -> 2.55 -> 2.66 -> 2.56 -> 2.46 -> 2.51 -> 2.22 -> 2.12 -> 2.29 -> 2.66 -> 2.24

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=22350 tokens=366.2M loss=2.6616 lr=2.91e-04 tok/s=12487
[train] step=22360 tokens=366.3M loss=2.6626 lr=2.91e-04 tok/s=12487
[train] step=22370 tokens=366.5M loss=2.8070 lr=2.91e-04 tok/s=12487
[train] step=22380 tokens=366.7M loss=2.2434 lr=2.91e-04 tok/s=12487
[train] step=22390 tokens=366.8M loss=2.2883 lr=2.91e-04 tok/s=12487
[train] step=22400 tokens=367.0M loss=2.7233 lr=2.91e-04 tok/s=12487
[train] step=22410 tokens=367.2M loss=2.4936 lr=2.91e-04 tok/s=12487
[train] step=22420 tokens=367.3M loss=2.9493 lr=2.91e-04 tok/s=12487
[train] step=22430 tokens=367.5M loss=2.2427 lr=2.91e-04 tok/s=12487
[train] step=22440 tokens=367.7M loss=2.5911 lr=2.91e-04 tok/s=12487
[train] step=22450 tokens=367.8M loss=2.4444 lr=2.91e-04 tok/s=12487
[train] step=22460 tokens=368.0M loss=2.6216 lr=2.91e-04 tok/s=12487
```
