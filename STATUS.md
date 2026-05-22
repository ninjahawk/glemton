# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 16:05:53 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 879M / 3000M (29.3%) |
| Step | 53630 |
| Latest loss | 2.4138 |
| Avg loss (last 30 logged) | 2.2178 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1 day, 23:12:01 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.37 -> 2.62 -> 2.28 -> 2.46 -> 2.48 -> 2.07 -> 2.31 -> 2.11 -> 2.37 -> 2.18 -> 2.42 -> 2.36

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`

## Recent log tail
```
[train] step=53520 tokens=876.9M loss=2.1968 lr=2.49e-04 tok/s=12484
[train] step=53530 tokens=877.0M loss=2.4470 lr=2.49e-04 tok/s=12484
[train] step=53540 tokens=877.2M loss=2.1181 lr=2.49e-04 tok/s=12484
[train] step=53550 tokens=877.4M loss=2.2131 lr=2.49e-04 tok/s=12484
[train] step=53560 tokens=877.5M loss=2.1071 lr=2.49e-04 tok/s=12484
[train] step=53570 tokens=877.7M loss=1.9280 lr=2.49e-04 tok/s=12484
[train] step=53580 tokens=877.9M loss=3.0482 lr=2.49e-04 tok/s=12484
[train] step=53590 tokens=878.0M loss=2.1982 lr=2.49e-04 tok/s=12484
[train] step=53600 tokens=878.2M loss=2.3644 lr=2.49e-04 tok/s=12484
[train] step=53610 tokens=878.3M loss=2.2247 lr=2.49e-04 tok/s=12484
[train] step=53620 tokens=878.5M loss=2.0176 lr=2.49e-04 tok/s=12484
[train] step=53630 tokens=878.7M loss=2.4138 lr=2.49e-04 tok/s=12484
```
