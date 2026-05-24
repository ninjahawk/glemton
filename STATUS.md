# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 13:22:47 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2914M / 3000M (97.1%) |
| Step | 177840 |
| Latest loss | 1.6268 |
| Avg loss (last 30 logged) | 1.9928 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1:55:12 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.25 -> 2.13 -> 2.31 -> 1.95 -> 2.09 -> 2.44 -> 2.00 -> 1.71 -> 2.35 -> 2.15 -> 2.18 -> 1.96

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_170899_tokens_2800M.pt`
- `step_177002_tokens_2900M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=177730 tokens=2911.9M loss=1.6864 lr=3.06e-05 tok/s=12484
[train] step=177740 tokens=2912.1M loss=2.2118 lr=3.06e-05 tok/s=12484
[train] step=177750 tokens=2912.3M loss=1.8600 lr=3.06e-05 tok/s=12484
[train] step=177760 tokens=2912.4M loss=2.3364 lr=3.06e-05 tok/s=12484
[train] step=177770 tokens=2912.6M loss=2.2758 lr=3.06e-05 tok/s=12484
[train] step=177780 tokens=2912.7M loss=2.2547 lr=3.06e-05 tok/s=12484
[train] step=177790 tokens=2912.9M loss=2.1973 lr=3.06e-05 tok/s=12484
[train] step=177800 tokens=2913.1M loss=2.0687 lr=3.06e-05 tok/s=12484
[train] step=177810 tokens=2913.2M loss=1.5638 lr=3.06e-05 tok/s=12484
[train] step=177820 tokens=2913.4M loss=1.9640 lr=3.06e-05 tok/s=12484
[train] step=177830 tokens=2913.6M loss=2.2222 lr=3.06e-05 tok/s=12484
[train] step=177840 tokens=2913.7M loss=1.6268 lr=3.06e-05 tok/s=12484
```
