# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 20:26:34 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1074M / 3000M (35.8%) |
| Step | 65550 |
| Latest loss | 2.3028 |
| Avg loss (last 30 logged) | 2.2094 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 18:50:52 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.07 -> 2.17 -> 2.56 -> 1.80 -> 2.39 -> 2.24 -> 2.05 -> 2.38 -> 1.86 -> 2.64 -> 2.14 -> 2.28

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`

## Recent log tail
```
[train] step=65440 tokens=1072.2M loss=2.5382 lr=2.26e-04 tok/s=12486
[train] step=65450 tokens=1072.3M loss=1.9341 lr=2.26e-04 tok/s=12486
[train] step=65460 tokens=1072.5M loss=2.4184 lr=2.25e-04 tok/s=12486
[train] step=65470 tokens=1072.7M loss=2.2953 lr=2.25e-04 tok/s=12486
[train] step=65480 tokens=1072.8M loss=2.0183 lr=2.25e-04 tok/s=12486
[train] step=65490 tokens=1073.0M loss=2.0604 lr=2.25e-04 tok/s=12486
[train] step=65500 tokens=1073.2M loss=2.1117 lr=2.25e-04 tok/s=12486
[train] step=65510 tokens=1073.3M loss=2.3679 lr=2.25e-04 tok/s=12486
[train] step=65520 tokens=1073.5M loss=2.2833 lr=2.25e-04 tok/s=12486
[train] step=65530 tokens=1073.6M loss=2.0901 lr=2.25e-04 tok/s=12486
[train] step=65540 tokens=1073.8M loss=2.0869 lr=2.25e-04 tok/s=12486
[train] step=65550 tokens=1074.0M loss=2.3028 lr=2.25e-04 tok/s=12486
```
