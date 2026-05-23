# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 20:06:31 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1059M / 3000M (35.3%) |
| Step | 64640 |
| Latest loss | 2.3805 |
| Avg loss (last 30 logged) | 2.2000 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 19:10:46 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.52 -> 2.92 -> 2.61 -> 2.11 -> 2.88 -> 1.98 -> 2.21 -> 2.27 -> 2.12 -> 2.34 -> 2.41 -> 2.29

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`

## Recent log tail
```
[train] step=64530 tokens=1057.3M loss=1.8603 lr=2.27e-04 tok/s=12486
[train] step=64540 tokens=1057.4M loss=2.1983 lr=2.27e-04 tok/s=12486
[train] step=64550 tokens=1057.6M loss=2.3882 lr=2.27e-04 tok/s=12486
[train] step=64560 tokens=1057.8M loss=2.2423 lr=2.27e-04 tok/s=12486
[train] step=64570 tokens=1057.9M loss=2.1890 lr=2.27e-04 tok/s=12486
[train] step=64580 tokens=1058.1M loss=2.4236 lr=2.27e-04 tok/s=12486
[train] step=64590 tokens=1058.2M loss=2.1250 lr=2.27e-04 tok/s=12486
[train] step=64600 tokens=1058.4M loss=2.4315 lr=2.27e-04 tok/s=12486
[train] step=64610 tokens=1058.6M loss=2.4480 lr=2.27e-04 tok/s=12486
[train] step=64620 tokens=1058.7M loss=2.2891 lr=2.27e-04 tok/s=12486
[train] step=64630 tokens=1058.9M loss=2.2115 lr=2.27e-04 tok/s=12486
[train] step=64640 tokens=1059.1M loss=2.3805 lr=2.27e-04 tok/s=12486
```
