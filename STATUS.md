# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 06:44:22 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 458M / 3000M (15.3%) |
| Step | 27960 |
| Latest loss | 2.7216 |
| Avg loss (last 30 logged) | 2.4414 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 2 days, 8:33:16 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.34 -> 2.45 -> 2.22 -> 2.27 -> 2.59 -> 2.26 -> 2.35 -> 2.40 -> 2.38 -> 2.58 -> 2.09 -> 2.06

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=27850 tokens=456.3M loss=2.5397 lr=2.86e-04 tok/s=12485
[train] step=27860 tokens=456.5M loss=2.5338 lr=2.86e-04 tok/s=12485
[train] step=27870 tokens=456.6M loss=2.3916 lr=2.86e-04 tok/s=12485
[train] step=27880 tokens=456.8M loss=2.7137 lr=2.86e-04 tok/s=12485
[train] step=27890 tokens=456.9M loss=2.7038 lr=2.86e-04 tok/s=12485
[train] step=27900 tokens=457.1M loss=2.9222 lr=2.86e-04 tok/s=12485
[train] step=27910 tokens=457.3M loss=2.3723 lr=2.86e-04 tok/s=12485
[train] step=27920 tokens=457.4M loss=2.5313 lr=2.86e-04 tok/s=12485
[train] step=27930 tokens=457.6M loss=2.2063 lr=2.86e-04 tok/s=12485
[train] step=27940 tokens=457.8M loss=2.0649 lr=2.86e-04 tok/s=12485
[train] step=27950 tokens=457.9M loss=2.5483 lr=2.86e-04 tok/s=12485
[train] step=27960 tokens=458.1M loss=2.7216 lr=2.86e-04 tok/s=12485
```
