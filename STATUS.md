# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 10:55:04 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 646M / 3000M (21.5%) |
| Step | 39410 |
| Latest loss | 2.2823 |
| Avg loss (last 30 logged) | 2.4029 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 4:23:20 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.41 -> 2.62 -> 2.32 -> 2.16 -> 2.52 -> 2.49 -> 2.28 -> 2.08 -> 2.22 -> 2.42 -> 1.93 -> 2.18

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=39300 tokens=643.9M loss=2.4487 lr=2.72e-04 tok/s=12483
[train] step=39310 tokens=644.1M loss=2.5852 lr=2.72e-04 tok/s=12483
[train] step=39320 tokens=644.2M loss=2.2596 lr=2.72e-04 tok/s=12483
[train] step=39330 tokens=644.4M loss=2.3529 lr=2.72e-04 tok/s=12483
[train] step=39340 tokens=644.5M loss=2.3569 lr=2.72e-04 tok/s=12483
[train] step=39350 tokens=644.7M loss=2.6158 lr=2.72e-04 tok/s=12483
[train] step=39360 tokens=644.9M loss=2.2968 lr=2.72e-04 tok/s=12483
[train] step=39370 tokens=645.0M loss=2.3386 lr=2.72e-04 tok/s=12483
[train] step=39380 tokens=645.2M loss=2.2023 lr=2.72e-04 tok/s=12483
[train] step=39390 tokens=645.4M loss=2.1768 lr=2.72e-04 tok/s=12483
[train] step=39400 tokens=645.5M loss=2.5955 lr=2.72e-04 tok/s=12483
[train] step=39410 tokens=645.7M loss=2.2823 lr=2.72e-04 tok/s=12483
```
