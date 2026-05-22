# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 14:35:38 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 811M / 3000M (27.0%) |
| Step | 49500 |
| Latest loss | 1.9948 |
| Avg loss (last 30 logged) | 2.2938 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 0:42:24 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
1.98 -> 2.08 -> 2.04 -> 2.18 -> 2.02 -> 2.22 -> 2.10 -> 2.19 -> 2.29 -> 2.02 -> 2.51 -> 2.18

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`

## Recent log tail
```
[train] step=49390 tokens=809.2M loss=1.9568 lr=2.56e-04 tok/s=12484
[train] step=49400 tokens=809.4M loss=2.1752 lr=2.56e-04 tok/s=12484
[train] step=49410 tokens=809.5M loss=2.3667 lr=2.56e-04 tok/s=12484
[train] step=49420 tokens=809.7M loss=2.3686 lr=2.56e-04 tok/s=12484
[train] step=49430 tokens=809.9M loss=1.9932 lr=2.56e-04 tok/s=12484
[train] step=49440 tokens=810.0M loss=1.9597 lr=2.56e-04 tok/s=12484
[train] step=49450 tokens=810.2M loss=2.1573 lr=2.56e-04 tok/s=12484
[train] step=49460 tokens=810.4M loss=2.2451 lr=2.56e-04 tok/s=12484
[train] step=49470 tokens=810.5M loss=2.0790 lr=2.56e-04 tok/s=12484
[train] step=49480 tokens=810.7M loss=2.1838 lr=2.56e-04 tok/s=12484
[train] step=49490 tokens=810.8M loss=2.3411 lr=2.56e-04 tok/s=12484
[train] step=49500 tokens=811.0M loss=1.9948 lr=2.56e-04 tok/s=12484
```
