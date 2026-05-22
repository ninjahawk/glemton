# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 16:35:58 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 901M / 3000M (30.0%) |
| Step | 55000 |
| Latest loss | 1.9769 |
| Avg loss (last 30 logged) | 2.2547 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1 day, 22:42:07 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.12 -> 2.24 -> 1.99 -> 2.44 -> 2.18 -> 2.15 -> 2.35 -> 2.32 -> 2.49 -> 2.37 -> 2.29 -> 2.13

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=54900 tokens=899.5M loss=2.0947 lr=2.46e-04 tok/s=12485
[train] step=54910 tokens=899.6M loss=2.4949 lr=2.46e-04 tok/s=12485
[train] step=54920 tokens=899.8M loss=2.2048 lr=2.46e-04 tok/s=12485
[train] step=54930 tokens=900.0M loss=2.2834 lr=2.46e-04 tok/s=12485
[train] checkpoint -> checkpoints\glemton-350m\step_54932_tokens_900M.pt
[train] step=54940 tokens=900.1M loss=1.9692 lr=2.46e-04 tok/s=12484
[train] step=54950 tokens=900.3M loss=2.4458 lr=2.46e-04 tok/s=12484
[train] step=54960 tokens=900.5M loss=2.1611 lr=2.46e-04 tok/s=12484
[train] step=54970 tokens=900.6M loss=2.6967 lr=2.46e-04 tok/s=12484
[train] step=54980 tokens=900.8M loss=2.1268 lr=2.46e-04 tok/s=12484
[train] step=54990 tokens=901.0M loss=2.3139 lr=2.46e-04 tok/s=12484
[train] step=55000 tokens=901.1M loss=1.9769 lr=2.46e-04 tok/s=12484
```
