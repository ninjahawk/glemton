# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 23:37:04 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1217M / 3000M (40.6%) |
| Step | 74270 |
| Latest loss | 2.0387 |
| Avg loss (last 30 logged) | 2.1921 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 15:40:15 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.99 -> 2.18 -> 2.16 -> 2.06 -> 2.20 -> 2.44 -> 2.16 -> 2.57 -> 1.99 -> 2.17 -> 2.29 -> 2.38

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] step=74160 tokens=1215.0M loss=2.2567 lr=2.07e-04 tok/s=12486
[train] step=74170 tokens=1215.2M loss=2.1857 lr=2.07e-04 tok/s=12486
[train] step=74180 tokens=1215.4M loss=1.8028 lr=2.07e-04 tok/s=12486
[train] step=74190 tokens=1215.5M loss=1.9596 lr=2.07e-04 tok/s=12486
[train] step=74200 tokens=1215.7M loss=2.0974 lr=2.07e-04 tok/s=12486
[train] step=74210 tokens=1215.9M loss=2.2544 lr=2.07e-04 tok/s=12486
[train] step=74220 tokens=1216.0M loss=2.0996 lr=2.07e-04 tok/s=12486
[train] step=74230 tokens=1216.2M loss=1.8414 lr=2.07e-04 tok/s=12486
[train] step=74240 tokens=1216.3M loss=2.0111 lr=2.07e-04 tok/s=12486
[train] step=74250 tokens=1216.5M loss=2.3751 lr=2.07e-04 tok/s=12486
[train] step=74260 tokens=1216.7M loss=2.1585 lr=2.06e-04 tok/s=12486
[train] step=74270 tokens=1216.8M loss=2.0387 lr=2.06e-04 tok/s=12486
```
