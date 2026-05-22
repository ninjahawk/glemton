# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 08:44:42 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 548M / 3000M (18.3%) |
| Step | 33460 |
| Latest loss | 3.2855 |
| Avg loss (last 30 logged) | 2.4128 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 6:33:15 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.43 -> 2.80 -> 2.15 -> 2.45 -> 2.96 -> 2.55 -> 2.55 -> 2.18 -> 2.62 -> 2.26 -> 2.15 -> 2.09

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`

## Recent log tail
```
[train] step=33350 tokens=546.4M loss=2.3054 lr=2.80e-04 tok/s=12484
[train] step=33360 tokens=546.6M loss=2.4772 lr=2.80e-04 tok/s=12484
[train] step=33370 tokens=546.7M loss=2.1990 lr=2.80e-04 tok/s=12484
[train] step=33380 tokens=546.9M loss=2.2276 lr=2.80e-04 tok/s=12484
[train] step=33390 tokens=547.1M loss=2.8474 lr=2.80e-04 tok/s=12484
[train] step=33400 tokens=547.2M loss=2.4601 lr=2.80e-04 tok/s=12484
[train] step=33410 tokens=547.4M loss=2.3062 lr=2.80e-04 tok/s=12484
[train] step=33420 tokens=547.6M loss=2.4929 lr=2.80e-04 tok/s=12484
[train] step=33430 tokens=547.7M loss=2.8640 lr=2.80e-04 tok/s=12484
[train] step=33440 tokens=547.9M loss=2.0916 lr=2.80e-04 tok/s=12484
[train] step=33450 tokens=548.0M loss=2.6096 lr=2.80e-04 tok/s=12484
[train] step=33460 tokens=548.2M loss=3.2855 lr=2.80e-04 tok/s=12484
```
