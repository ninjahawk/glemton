# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 00:43:22 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 188M / 3000M (6.3%) |
| Step | 11460 |
| Latest loss | 2.6521 |
| Avg loss (last 30 logged) | 2.6694 |
| Throughput | 12,491 tok/s |
| ETA to 3B tokens | 2 days, 14:32:18 |
| Projected finish | Sun 2026-05-24 15:15 |

## Loss trajectory (sampled)
2.29 -> 2.83 -> 2.51 -> 2.58 -> 2.48 -> 2.70 -> 2.78 -> 2.66 -> 2.58 -> 2.36 -> 2.54 -> 2.43

## Checkpoints on disk
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=11350 tokens=186.0M loss=2.7288 lr=2.98e-04 tok/s=12491
[train] step=11360 tokens=186.1M loss=2.5647 lr=2.98e-04 tok/s=12491
[train] step=11370 tokens=186.3M loss=2.4243 lr=2.98e-04 tok/s=12491
[train] step=11380 tokens=186.4M loss=2.5603 lr=2.98e-04 tok/s=12491
[train] step=11390 tokens=186.6M loss=2.5323 lr=2.98e-04 tok/s=12491
[train] step=11400 tokens=186.8M loss=2.7092 lr=2.98e-04 tok/s=12491
[train] step=11410 tokens=186.9M loss=2.3950 lr=2.98e-04 tok/s=12491
[train] step=11420 tokens=187.1M loss=2.6564 lr=2.98e-04 tok/s=12491
[train] step=11430 tokens=187.3M loss=2.4348 lr=2.98e-04 tok/s=12491
[train] step=11440 tokens=187.4M loss=2.6951 lr=2.98e-04 tok/s=12491
[train] step=11450 tokens=187.6M loss=2.9229 lr=2.98e-04 tok/s=12491
[train] step=11460 tokens=187.8M loss=2.6521 lr=2.98e-04 tok/s=12491
```
