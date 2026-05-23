# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 19:30:03 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2111M / 3000M (70.4%) |
| Step | 128850 |
| Latest loss | 2.2505 |
| Avg loss (last 30 logged) | 2.0639 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 19:46:08 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.16 -> 1.84 -> 2.05 -> 1.89 -> 2.05 -> 2.26 -> 2.03 -> 2.39 -> 2.26 -> 1.90 -> 1.97 -> 1.84

## Checkpoints on disk
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=128740 tokens=2109.3M loss=2.2466 lr=8.54e-05 tok/s=12490
[train] step=128750 tokens=2109.4M loss=1.8496 lr=8.54e-05 tok/s=12490
[train] step=128760 tokens=2109.6M loss=2.7974 lr=8.54e-05 tok/s=12490
[train] step=128770 tokens=2109.8M loss=1.9663 lr=8.54e-05 tok/s=12490
[train] step=128780 tokens=2109.9M loss=2.2684 lr=8.54e-05 tok/s=12490
[train] step=128790 tokens=2110.1M loss=2.5169 lr=8.53e-05 tok/s=12490
[train] step=128800 tokens=2110.3M loss=1.6448 lr=8.53e-05 tok/s=12490
[train] step=128810 tokens=2110.4M loss=2.0936 lr=8.53e-05 tok/s=12490
[train] step=128820 tokens=2110.6M loss=2.0155 lr=8.53e-05 tok/s=12490
[train] step=128830 tokens=2110.8M loss=1.8413 lr=8.53e-05 tok/s=12490
[train] step=128840 tokens=2110.9M loss=1.5483 lr=8.53e-05 tok/s=12490
[train] step=128850 tokens=2111.1M loss=2.2505 lr=8.52e-05 tok/s=12490
```
