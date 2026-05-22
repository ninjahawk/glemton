# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 07:34:31 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 496M / 3000M (16.5%) |
| Step | 30250 |
| Latest loss | 2.5437 |
| Avg loss (last 30 logged) | 2.4651 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 2 days, 7:43:12 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.30 -> 2.29 -> 2.45 -> 2.40 -> 2.37 -> 2.31 -> 2.59 -> 2.22 -> 2.39 -> 2.47 -> 2.46 -> 2.35

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=30140 tokens=493.8M loss=2.8035 lr=2.84e-04 tok/s=12485
[train] step=30150 tokens=494.0M loss=2.5166 lr=2.84e-04 tok/s=12485
[train] step=30160 tokens=494.1M loss=2.1894 lr=2.84e-04 tok/s=12485
[train] step=30170 tokens=494.3M loss=2.6289 lr=2.84e-04 tok/s=12485
[train] step=30180 tokens=494.5M loss=2.3390 lr=2.84e-04 tok/s=12485
[train] step=30190 tokens=494.6M loss=2.0789 lr=2.84e-04 tok/s=12485
[train] step=30200 tokens=494.8M loss=2.2553 lr=2.84e-04 tok/s=12485
[train] step=30210 tokens=495.0M loss=2.5698 lr=2.84e-04 tok/s=12485
[train] step=30220 tokens=495.1M loss=2.3494 lr=2.84e-04 tok/s=12485
[train] step=30230 tokens=495.3M loss=2.9729 lr=2.84e-04 tok/s=12485
[train] step=30240 tokens=495.5M loss=2.5624 lr=2.84e-04 tok/s=12485
[train] step=30250 tokens=495.6M loss=2.5437 lr=2.84e-04 tok/s=12485
```
