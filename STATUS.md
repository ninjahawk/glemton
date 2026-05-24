# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 11:52:33 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2846M / 3000M (94.9%) |
| Step | 173710 |
| Latest loss | 2.0889 |
| Avg loss (last 30 logged) | 2.2212 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 3:25:27 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
1.69 -> 1.85 -> 2.11 -> 2.09 -> 2.25 -> 2.32 -> 2.24 -> 2.32 -> 1.68 -> 2.28 -> 2.02 -> 2.61

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
[train] step=173600 tokens=2844.3M loss=2.1526 lr=3.18e-05 tok/s=12484
[train] step=173610 tokens=2844.4M loss=2.4671 lr=3.18e-05 tok/s=12484
[train] step=173620 tokens=2844.6M loss=2.5244 lr=3.18e-05 tok/s=12484
[train] step=173630 tokens=2844.8M loss=2.1087 lr=3.18e-05 tok/s=12484
[train] step=173640 tokens=2844.9M loss=2.1060 lr=3.18e-05 tok/s=12484
[train] step=173650 tokens=2845.1M loss=2.3592 lr=3.18e-05 tok/s=12484
[train] step=173660 tokens=2845.2M loss=2.7751 lr=3.18e-05 tok/s=12484
[train] step=173670 tokens=2845.4M loss=2.2314 lr=3.18e-05 tok/s=12484
[train] step=173680 tokens=2845.6M loss=2.3826 lr=3.18e-05 tok/s=12484
[train] step=173690 tokens=2845.7M loss=2.6148 lr=3.18e-05 tok/s=12484
[train] step=173700 tokens=2845.9M loss=2.4019 lr=3.18e-05 tok/s=12484
[train] step=173710 tokens=2846.1M loss=2.0889 lr=3.18e-05 tok/s=12484
```
