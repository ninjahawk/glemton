# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 09:14:47 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 571M / 3000M (19.0%) |
| Step | 34830 |
| Latest loss | 2.6307 |
| Avg loss (last 30 logged) | 2.4095 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 6:03:13 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.61 -> 2.71 -> 3.17 -> 2.46 -> 2.32 -> 2.43 -> 2.17 -> 2.10 -> 2.13 -> 2.55 -> 2.49 -> 2.20

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`

## Recent log tail
```
[train] step=34720 tokens=568.9M loss=2.7383 lr=2.78e-04 tok/s=12484
[train] step=34730 tokens=569.0M loss=2.1569 lr=2.78e-04 tok/s=12484
[train] step=34740 tokens=569.2M loss=2.0313 lr=2.78e-04 tok/s=12484
[train] step=34750 tokens=569.3M loss=2.7241 lr=2.78e-04 tok/s=12484
[train] step=34760 tokens=569.5M loss=2.3120 lr=2.78e-04 tok/s=12484
[train] step=34770 tokens=569.7M loss=2.5525 lr=2.78e-04 tok/s=12484
[train] step=34780 tokens=569.8M loss=2.5126 lr=2.78e-04 tok/s=12484
[train] step=34790 tokens=570.0M loss=2.4590 lr=2.78e-04 tok/s=12484
[train] step=34800 tokens=570.2M loss=2.2001 lr=2.78e-04 tok/s=12484
[train] step=34810 tokens=570.3M loss=1.9916 lr=2.78e-04 tok/s=12484
[train] step=34820 tokens=570.5M loss=2.1775 lr=2.78e-04 tok/s=12484
[train] step=34830 tokens=570.7M loss=2.6307 lr=2.78e-04 tok/s=12484
```
