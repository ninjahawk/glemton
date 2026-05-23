# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 23:27:02 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1209M / 3000M (40.3%) |
| Step | 73810 |
| Latest loss | 2.1164 |
| Avg loss (last 30 logged) | 2.1598 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 15:50:16 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.52 -> 2.13 -> 2.36 -> 2.26 -> 1.91 -> 2.33 -> 2.02 -> 2.25 -> 2.43 -> 1.99 -> 2.11 -> 1.83

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] step=73700 tokens=1207.5M loss=2.0383 lr=2.08e-04 tok/s=12486
[train] step=73710 tokens=1207.7M loss=1.5434 lr=2.08e-04 tok/s=12486
[train] step=73720 tokens=1207.8M loss=2.4350 lr=2.08e-04 tok/s=12486
[train] step=73730 tokens=1208.0M loss=2.4979 lr=2.08e-04 tok/s=12486
[train] step=73740 tokens=1208.2M loss=2.3836 lr=2.08e-04 tok/s=12486
[train] step=73750 tokens=1208.3M loss=2.1665 lr=2.08e-04 tok/s=12486
[train] step=73760 tokens=1208.5M loss=2.3233 lr=2.08e-04 tok/s=12486
[train] step=73770 tokens=1208.6M loss=2.2283 lr=2.08e-04 tok/s=12486
[train] step=73780 tokens=1208.8M loss=1.9683 lr=2.08e-04 tok/s=12486
[train] step=73790 tokens=1209.0M loss=1.8293 lr=2.08e-04 tok/s=12486
[train] step=73800 tokens=1209.1M loss=2.4057 lr=2.08e-04 tok/s=12486
[train] step=73810 tokens=1209.3M loss=2.1164 lr=2.07e-04 tok/s=12486
```
