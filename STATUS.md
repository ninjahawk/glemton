# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 09:24:49 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 578M / 3000M (19.3%) |
| Step | 35290 |
| Latest loss | 2.3883 |
| Avg loss (last 30 logged) | 2.4308 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 5:53:12 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.47 -> 2.98 -> 2.19 -> 1.94 -> 2.63 -> 2.18 -> 2.44 -> 2.42 -> 2.35 -> 2.28 -> 2.19 -> 2.84

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`

## Recent log tail
```
[train] step=35180 tokens=576.4M loss=2.3517 lr=2.78e-04 tok/s=12484
[train] step=35190 tokens=576.6M loss=2.1224 lr=2.78e-04 tok/s=12484
[train] step=35200 tokens=576.7M loss=2.5824 lr=2.78e-04 tok/s=12484
[train] step=35210 tokens=576.9M loss=2.3851 lr=2.78e-04 tok/s=12484
[train] step=35220 tokens=577.0M loss=2.3868 lr=2.78e-04 tok/s=12484
[train] step=35230 tokens=577.2M loss=2.5848 lr=2.78e-04 tok/s=12484
[train] step=35240 tokens=577.4M loss=2.3553 lr=2.78e-04 tok/s=12484
[train] step=35250 tokens=577.5M loss=2.2143 lr=2.78e-04 tok/s=12484
[train] step=35260 tokens=577.7M loss=2.8426 lr=2.78e-04 tok/s=12484
[train] step=35270 tokens=577.9M loss=2.3345 lr=2.78e-04 tok/s=12484
[train] step=35280 tokens=578.0M loss=2.2167 lr=2.78e-04 tok/s=12484
[train] step=35290 tokens=578.2M loss=2.3883 lr=2.78e-04 tok/s=12484
```
