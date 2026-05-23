# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 00:47:14 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1269M / 3000M (42.3%) |
| Step | 77480 |
| Latest loss | 2.2722 |
| Avg loss (last 30 logged) | 2.2164 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 14:30:03 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.46 -> 2.13 -> 2.32 -> 2.00 -> 2.11 -> 2.58 -> 2.12 -> 2.50 -> 2.21 -> 2.09 -> 2.03 -> 2.27

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] step=77370 tokens=1267.6M loss=2.4188 lr=2.00e-04 tok/s=12486
[train] step=77380 tokens=1267.8M loss=2.4968 lr=1.99e-04 tok/s=12486
[train] step=77390 tokens=1268.0M loss=2.0219 lr=1.99e-04 tok/s=12486
[train] step=77400 tokens=1268.1M loss=2.0097 lr=1.99e-04 tok/s=12486
[train] step=77410 tokens=1268.3M loss=2.3905 lr=1.99e-04 tok/s=12486
[train] step=77420 tokens=1268.4M loss=2.0555 lr=1.99e-04 tok/s=12486
[train] step=77430 tokens=1268.6M loss=2.3970 lr=1.99e-04 tok/s=12486
[train] step=77440 tokens=1268.8M loss=2.2231 lr=1.99e-04 tok/s=12486
[train] step=77450 tokens=1268.9M loss=2.2737 lr=1.99e-04 tok/s=12486
[train] step=77460 tokens=1269.1M loss=1.7052 lr=1.99e-04 tok/s=12486
[train] step=77470 tokens=1269.3M loss=2.6938 lr=1.99e-04 tok/s=12486
[train] step=77480 tokens=1269.4M loss=2.2722 lr=1.99e-04 tok/s=12486
```
