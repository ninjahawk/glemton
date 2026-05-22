# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 07:44:32 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 503M / 3000M (16.8%) |
| Step | 30710 |
| Latest loss | 2.6649 |
| Avg loss (last 30 logged) | 2.4065 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 7:33:20 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.88 -> 2.46 -> 2.23 -> 2.31 -> 2.27 -> 2.65 -> 2.57 -> 2.80 -> 2.31 -> 2.77 -> 2.42 -> 2.56

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=30600 tokens=501.4M loss=2.3931 lr=2.83e-04 tok/s=12484
[train] step=30610 tokens=501.5M loss=2.4222 lr=2.83e-04 tok/s=12484
[train] step=30620 tokens=501.7M loss=2.4406 lr=2.83e-04 tok/s=12484
[train] step=30630 tokens=501.8M loss=2.8002 lr=2.83e-04 tok/s=12484
[train] step=30640 tokens=502.0M loss=2.2311 lr=2.83e-04 tok/s=12484
[train] step=30650 tokens=502.2M loss=2.6452 lr=2.83e-04 tok/s=12484
[train] step=30660 tokens=502.3M loss=2.2089 lr=2.83e-04 tok/s=12484
[train] step=30670 tokens=502.5M loss=2.4117 lr=2.83e-04 tok/s=12484
[train] step=30680 tokens=502.7M loss=2.4712 lr=2.83e-04 tok/s=12484
[train] step=30690 tokens=502.8M loss=2.5611 lr=2.83e-04 tok/s=12484
[train] step=30700 tokens=503.0M loss=3.0470 lr=2.83e-04 tok/s=12484
[train] step=30710 tokens=503.2M loss=2.6649 lr=2.83e-04 tok/s=12484
```
