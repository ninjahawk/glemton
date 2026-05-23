# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 22:46:56 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1179M / 3000M (39.3%) |
| Step | 71970 |
| Latest loss | 1.9238 |
| Avg loss (last 30 logged) | 2.1493 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 16:30:27 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.09 -> 2.09 -> 2.12 -> 2.39 -> 2.50 -> 1.89 -> 2.05 -> 1.99 -> 2.18 -> 2.16 -> 2.06 -> 2.20

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`

## Recent log tail
```
[train] step=71860 tokens=1177.4M loss=2.1289 lr=2.12e-04 tok/s=12486
[train] step=71870 tokens=1177.5M loss=2.0411 lr=2.12e-04 tok/s=12486
[train] step=71880 tokens=1177.7M loss=1.8650 lr=2.12e-04 tok/s=12486
[train] step=71890 tokens=1177.8M loss=2.5573 lr=2.12e-04 tok/s=12486
[train] step=71900 tokens=1178.0M loss=1.9393 lr=2.12e-04 tok/s=12486
[train] step=71910 tokens=1178.2M loss=2.4812 lr=2.12e-04 tok/s=12486
[train] step=71920 tokens=1178.3M loss=2.1143 lr=2.12e-04 tok/s=12486
[train] step=71930 tokens=1178.5M loss=1.9275 lr=2.12e-04 tok/s=12486
[train] step=71940 tokens=1178.7M loss=2.1975 lr=2.12e-04 tok/s=12486
[train] step=71950 tokens=1178.8M loss=2.1355 lr=2.12e-04 tok/s=12486
[train] step=71960 tokens=1179.0M loss=2.2320 lr=2.12e-04 tok/s=12486
[train] step=71970 tokens=1179.2M loss=1.9238 lr=2.12e-04 tok/s=12486
```
