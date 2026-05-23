# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 20:16:33 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1067M / 3000M (35.6%) |
| Step | 65100 |
| Latest loss | 2.3371 |
| Avg loss (last 30 logged) | 2.2760 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 19:00:45 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.44 -> 2.11 -> 2.45 -> 2.30 -> 2.29 -> 2.27 -> 2.23 -> 2.49 -> 2.19 -> 2.00 -> 2.21 -> 2.34

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`

## Recent log tail
```
[train] step=64990 tokens=1064.8M loss=2.0310 lr=2.26e-04 tok/s=12486
[train] step=65000 tokens=1065.0M loss=2.1376 lr=2.26e-04 tok/s=12486
[train] step=65010 tokens=1065.1M loss=2.2817 lr=2.26e-04 tok/s=12486
[train] step=65020 tokens=1065.3M loss=1.9205 lr=2.26e-04 tok/s=12486
[train] step=65030 tokens=1065.5M loss=2.3384 lr=2.26e-04 tok/s=12486
[train] step=65040 tokens=1065.6M loss=2.1373 lr=2.26e-04 tok/s=12486
[train] step=65050 tokens=1065.8M loss=2.0519 lr=2.26e-04 tok/s=12486
[train] step=65060 tokens=1065.9M loss=2.4231 lr=2.26e-04 tok/s=12486
[train] step=65070 tokens=1066.1M loss=2.3438 lr=2.26e-04 tok/s=12486
[train] step=65080 tokens=1066.3M loss=2.6918 lr=2.26e-04 tok/s=12486
[train] step=65090 tokens=1066.4M loss=2.2754 lr=2.26e-04 tok/s=12486
[train] step=65100 tokens=1066.6M loss=2.3371 lr=2.26e-04 tok/s=12486
```
