# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 05:24:09 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 398M / 3000M (13.3%) |
| Step | 24290 |
| Latest loss | 2.2576 |
| Avg loss (last 30 logged) | 2.4679 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 2 days, 9:52:56 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.53 -> 2.62 -> 2.50 -> 2.25 -> 2.31 -> 3.00 -> 2.26 -> 2.57 -> 2.48 -> 2.51 -> 2.13 -> 2.28

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=24180 tokens=396.2M loss=2.3965 lr=2.90e-04 tok/s=12487
[train] step=24190 tokens=396.3M loss=2.2931 lr=2.90e-04 tok/s=12487
[train] step=24200 tokens=396.5M loss=2.5120 lr=2.90e-04 tok/s=12487
[train] step=24210 tokens=396.7M loss=2.4112 lr=2.90e-04 tok/s=12487
[train] step=24220 tokens=396.8M loss=2.4844 lr=2.90e-04 tok/s=12487
[train] step=24230 tokens=397.0M loss=2.1982 lr=2.90e-04 tok/s=12487
[train] step=24240 tokens=397.1M loss=2.4569 lr=2.90e-04 tok/s=12487
[train] step=24250 tokens=397.3M loss=2.5613 lr=2.90e-04 tok/s=12487
[train] step=24260 tokens=397.5M loss=2.2838 lr=2.90e-04 tok/s=12487
[train] step=24270 tokens=397.6M loss=2.7136 lr=2.90e-04 tok/s=12487
[train] step=24280 tokens=397.8M loss=2.1783 lr=2.90e-04 tok/s=12487
[train] step=24290 tokens=398.0M loss=2.2576 lr=2.90e-04 tok/s=12487
```
