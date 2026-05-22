# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 15:05:43 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 834M / 3000M (27.8%) |
| Step | 50880 |
| Latest loss | 2.0633 |
| Avg loss (last 30 logged) | 2.2916 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 0:12:14 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.33 -> 2.24 -> 2.27 -> 2.85 -> 2.47 -> 2.60 -> 2.36 -> 2.47 -> 2.63 -> 2.01 -> 2.43 -> 2.14

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`

## Recent log tail
```
[train] step=50770 tokens=831.8M loss=2.3106 lr=2.54e-04 tok/s=12484
[train] step=50780 tokens=832.0M loss=2.2838 lr=2.54e-04 tok/s=12484
[train] step=50790 tokens=832.1M loss=2.5158 lr=2.54e-04 tok/s=12484
[train] step=50800 tokens=832.3M loss=2.3699 lr=2.54e-04 tok/s=12484
[train] step=50810 tokens=832.5M loss=2.2335 lr=2.54e-04 tok/s=12484
[train] step=50820 tokens=832.6M loss=2.0510 lr=2.54e-04 tok/s=12484
[train] step=50830 tokens=832.8M loss=2.3617 lr=2.54e-04 tok/s=12484
[train] step=50840 tokens=833.0M loss=2.1973 lr=2.54e-04 tok/s=12484
[train] step=50850 tokens=833.1M loss=2.4442 lr=2.54e-04 tok/s=12484
[train] step=50860 tokens=833.3M loss=2.1407 lr=2.54e-04 tok/s=12484
[train] step=50870 tokens=833.5M loss=2.1341 lr=2.54e-04 tok/s=12484
[train] step=50880 tokens=833.6M loss=2.0633 lr=2.54e-04 tok/s=12484
```
