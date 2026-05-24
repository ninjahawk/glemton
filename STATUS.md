# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 13:02:44 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2899M / 3000M (96.6%) |
| Step | 176920 |
| Latest loss | 2.3896 |
| Avg loss (last 30 logged) | 2.0840 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2:15:14 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.46 -> 2.21 -> 2.06 -> 2.29 -> 2.00 -> 1.66 -> 1.93 -> 1.90 -> 1.70 -> 2.22 -> 2.17 -> 2.03

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_170899_tokens_2800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=176810 tokens=2896.9M loss=2.1843 lr=3.08e-05 tok/s=12484
[train] step=176820 tokens=2897.0M loss=2.1160 lr=3.08e-05 tok/s=12484
[train] step=176830 tokens=2897.2M loss=2.3490 lr=3.08e-05 tok/s=12484
[train] step=176840 tokens=2897.3M loss=2.0127 lr=3.08e-05 tok/s=12484
[train] step=176850 tokens=2897.5M loss=2.1307 lr=3.08e-05 tok/s=12484
[train] step=176860 tokens=2897.7M loss=2.0111 lr=3.08e-05 tok/s=12484
[train] step=176870 tokens=2897.8M loss=2.2580 lr=3.08e-05 tok/s=12484
[train] step=176880 tokens=2898.0M loss=1.9024 lr=3.08e-05 tok/s=12484
[train] step=176890 tokens=2898.2M loss=2.0279 lr=3.08e-05 tok/s=12484
[train] step=176900 tokens=2898.3M loss=2.1138 lr=3.08e-05 tok/s=12484
[train] step=176910 tokens=2898.5M loss=2.3517 lr=3.08e-05 tok/s=12484
[train] step=176920 tokens=2898.7M loss=2.3896 lr=3.08e-05 tok/s=12484
```
