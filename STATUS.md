# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 01:13:27 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 210M / 3000M (7.0%) |
| Step | 12830 |
| Latest loss | 2.2915 |
| Avg loss (last 30 logged) | 2.5929 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 2 days, 14:02:42 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.43 -> 2.67 -> 2.50 -> 2.79 -> 2.40 -> 2.29 -> 2.77 -> 2.68 -> 2.52 -> 3.01 -> 2.42 -> 2.36

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=12720 tokens=208.4M loss=2.3385 lr=2.97e-04 tok/s=12490
[train] step=12730 tokens=208.6M loss=2.4385 lr=2.97e-04 tok/s=12490
[train] step=12740 tokens=208.7M loss=2.6214 lr=2.97e-04 tok/s=12490
[train] step=12750 tokens=208.9M loss=2.5669 lr=2.97e-04 tok/s=12490
[train] step=12760 tokens=209.1M loss=2.6522 lr=2.97e-04 tok/s=12490
[train] step=12770 tokens=209.2M loss=2.6912 lr=2.97e-04 tok/s=12490
[train] step=12780 tokens=209.4M loss=2.6719 lr=2.97e-04 tok/s=12490
[train] step=12790 tokens=209.6M loss=2.4052 lr=2.97e-04 tok/s=12490
[train] step=12800 tokens=209.7M loss=2.8523 lr=2.97e-04 tok/s=12490
[train] step=12810 tokens=209.9M loss=2.3588 lr=2.97e-04 tok/s=12490
[train] step=12820 tokens=210.0M loss=2.3818 lr=2.97e-04 tok/s=12490
[train] step=12830 tokens=210.2M loss=2.2915 lr=2.97e-04 tok/s=12490
```
