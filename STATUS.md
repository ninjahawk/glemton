# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 19:26:25 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1029M / 3000M (34.3%) |
| Step | 62800 |
| Latest loss | 2.5136 |
| Avg loss (last 30 logged) | 2.3003 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 19:51:17 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.20 -> 2.57 -> 2.30 -> 2.48 -> 2.29 -> 2.24 -> 2.37 -> 2.56 -> 2.02 -> 2.41 -> 2.32 -> 1.86

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`

## Recent log tail
```
[train] step=62690 tokens=1027.1M loss=2.4477 lr=2.31e-04 tok/s=12485
[train] step=62700 tokens=1027.3M loss=2.3803 lr=2.31e-04 tok/s=12485
[train] step=62710 tokens=1027.4M loss=2.1943 lr=2.31e-04 tok/s=12485
[train] step=62720 tokens=1027.6M loss=2.2213 lr=2.31e-04 tok/s=12485
[train] step=62730 tokens=1027.8M loss=2.4487 lr=2.31e-04 tok/s=12485
[train] step=62740 tokens=1027.9M loss=2.2449 lr=2.31e-04 tok/s=12485
[train] step=62750 tokens=1028.1M loss=1.8490 lr=2.31e-04 tok/s=12485
[train] step=62760 tokens=1028.3M loss=2.2924 lr=2.31e-04 tok/s=12485
[train] step=62770 tokens=1028.4M loss=2.4705 lr=2.31e-04 tok/s=12485
[train] step=62780 tokens=1028.6M loss=1.8576 lr=2.31e-04 tok/s=12485
[train] step=62790 tokens=1028.8M loss=1.9930 lr=2.31e-04 tok/s=12485
[train] step=62800 tokens=1028.9M loss=2.5136 lr=2.31e-04 tok/s=12485
```
