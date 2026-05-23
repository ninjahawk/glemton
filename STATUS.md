# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 23:17:00 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1202M / 3000M (40.1%) |
| Step | 73350 |
| Latest loss | 2.3479 |
| Avg loss (last 30 logged) | 2.2325 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 16:00:17 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.61 -> 1.88 -> 2.06 -> 2.04 -> 1.94 -> 2.16 -> 2.07 -> 1.77 -> 2.45 -> 2.08 -> 1.88 -> 2.18

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] checkpoint -> checkpoints\glemton-350m\step_73243_tokens_1200M.pt
[train] step=73250 tokens=1200.1M loss=1.8419 lr=2.09e-04 tok/s=12486
[train] step=73260 tokens=1200.3M loss=1.9850 lr=2.09e-04 tok/s=12486
[train] step=73270 tokens=1200.5M loss=1.9686 lr=2.09e-04 tok/s=12486
[train] step=73280 tokens=1200.6M loss=2.3142 lr=2.09e-04 tok/s=12486
[train] step=73290 tokens=1200.8M loss=2.4969 lr=2.09e-04 tok/s=12486
[train] step=73300 tokens=1200.9M loss=2.1019 lr=2.09e-04 tok/s=12486
[train] step=73310 tokens=1201.1M loss=2.3824 lr=2.09e-04 tok/s=12486
[train] step=73320 tokens=1201.3M loss=2.3130 lr=2.09e-04 tok/s=12486
[train] step=73330 tokens=1201.4M loss=2.1837 lr=2.09e-04 tok/s=12486
[train] step=73340 tokens=1201.6M loss=2.1170 lr=2.09e-04 tok/s=12486
[train] step=73350 tokens=1201.8M loss=2.3479 lr=2.09e-04 tok/s=12486
```
