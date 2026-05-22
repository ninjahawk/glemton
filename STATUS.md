# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 16:45:59 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 909M / 3000M (30.3%) |
| Step | 55460 |
| Latest loss | 2.4538 |
| Avg loss (last 30 logged) | 2.3330 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1 day, 22:31:58 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.20 -> 1.91 -> 2.27 -> 2.38 -> 2.60 -> 2.18 -> 2.23 -> 2.44 -> 2.58 -> 2.27 -> 2.34 -> 2.42

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=55350 tokens=906.9M loss=2.2984 lr=2.46e-04 tok/s=12484
[train] step=55360 tokens=907.0M loss=2.1914 lr=2.46e-04 tok/s=12484
[train] step=55370 tokens=907.2M loss=2.8172 lr=2.46e-04 tok/s=12484
[train] step=55380 tokens=907.3M loss=1.9614 lr=2.46e-04 tok/s=12484
[train] step=55390 tokens=907.5M loss=2.6710 lr=2.45e-04 tok/s=12484
[train] step=55400 tokens=907.7M loss=2.3903 lr=2.45e-04 tok/s=12484
[train] step=55410 tokens=907.8M loss=2.1607 lr=2.45e-04 tok/s=12484
[train] step=55420 tokens=908.0M loss=2.3412 lr=2.45e-04 tok/s=12484
[train] step=55430 tokens=908.2M loss=2.2380 lr=2.45e-04 tok/s=12484
[train] step=55440 tokens=908.3M loss=2.4218 lr=2.45e-04 tok/s=12484
[train] step=55450 tokens=908.5M loss=1.9724 lr=2.45e-04 tok/s=12484
[train] step=55460 tokens=908.7M loss=2.4538 lr=2.45e-04 tok/s=12484
```
