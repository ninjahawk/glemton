# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 09:04:45 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 563M / 3000M (18.8%) |
| Step | 34370 |
| Latest loss | 2.3267 |
| Avg loss (last 30 logged) | 2.3874 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 6:13:21 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.21 -> 2.89 -> 2.34 -> 2.53 -> 2.24 -> 2.61 -> 2.34 -> 2.14 -> 2.48 -> 2.48 -> 2.37 -> 2.48

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`

## Recent log tail
```
[train] step=34260 tokens=561.3M loss=2.3736 lr=2.79e-04 tok/s=12484
[train] step=34270 tokens=561.5M loss=2.3460 lr=2.79e-04 tok/s=12484
[train] step=34280 tokens=561.6M loss=2.4181 lr=2.79e-04 tok/s=12484
[train] step=34290 tokens=561.8M loss=2.5168 lr=2.79e-04 tok/s=12484
[train] step=34300 tokens=562.0M loss=2.0718 lr=2.79e-04 tok/s=12484
[train] step=34310 tokens=562.1M loss=2.7495 lr=2.79e-04 tok/s=12484
[train] step=34320 tokens=562.3M loss=2.3952 lr=2.79e-04 tok/s=12484
[train] step=34330 tokens=562.5M loss=2.5463 lr=2.79e-04 tok/s=12484
[train] step=34340 tokens=562.6M loss=2.6206 lr=2.79e-04 tok/s=12484
[train] step=34350 tokens=562.8M loss=2.4826 lr=2.79e-04 tok/s=12484
[train] step=34360 tokens=563.0M loss=2.1178 lr=2.79e-04 tok/s=12484
[train] step=34370 tokens=563.1M loss=2.3267 lr=2.79e-04 tok/s=12484
```
