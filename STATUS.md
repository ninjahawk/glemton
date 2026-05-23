# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 12:49:04 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1810M / 3000M (60.3%) |
| Step | 110500 |
| Latest loss | 2.2986 |
| Avg loss (last 30 logged) | 2.1176 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 2:27:39 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.23 -> 2.07 -> 2.12 -> 1.72 -> 2.40 -> 1.95 -> 1.86 -> 2.08 -> 1.76 -> 2.01 -> 2.31 -> 1.98

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=110390 tokens=1808.6M loss=2.0050 lr=1.23e-04 tok/s=12488
[train] step=110400 tokens=1808.8M loss=1.9448 lr=1.23e-04 tok/s=12488
[train] step=110410 tokens=1809.0M loss=2.0630 lr=1.23e-04 tok/s=12488
[train] step=110420 tokens=1809.1M loss=1.8175 lr=1.23e-04 tok/s=12488
[train] step=110430 tokens=1809.3M loss=2.4633 lr=1.23e-04 tok/s=12488
[train] step=110440 tokens=1809.4M loss=2.2819 lr=1.23e-04 tok/s=12488
[train] step=110450 tokens=1809.6M loss=2.3378 lr=1.23e-04 tok/s=12488
[train] step=110460 tokens=1809.8M loss=1.9964 lr=1.23e-04 tok/s=12488
[train] step=110470 tokens=1809.9M loss=2.1538 lr=1.23e-04 tok/s=12488
[train] step=110480 tokens=1810.1M loss=1.9750 lr=1.23e-04 tok/s=12488
[train] step=110490 tokens=1810.3M loss=2.0559 lr=1.23e-04 tok/s=12488
[train] step=110500 tokens=1810.4M loss=2.2986 lr=1.23e-04 tok/s=12488
```
