# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 15:03:00 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2989M / 3000M (99.6%) |
| Step | 182420 |
| Latest loss | 1.9706 |
| Avg loss (last 30 logged) | 2.0296 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 0:14:57 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.05 -> 2.42 -> 1.92 -> 2.15 -> 1.93 -> 1.94 -> 2.40 -> 1.67 -> 1.94 -> 2.03 -> 2.06 -> 1.83

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
[train] step=182310 tokens=2987.0M loss=1.9127 lr=3.00e-05 tok/s=12484
[train] step=182320 tokens=2987.1M loss=2.1071 lr=3.00e-05 tok/s=12484
[train] step=182330 tokens=2987.3M loss=1.5342 lr=3.00e-05 tok/s=12484
[train] step=182340 tokens=2987.5M loss=2.1874 lr=3.00e-05 tok/s=12484
[train] step=182350 tokens=2987.6M loss=2.1923 lr=3.00e-05 tok/s=12484
[train] step=182360 tokens=2987.8M loss=2.0856 lr=3.00e-05 tok/s=12484
[train] step=182370 tokens=2988.0M loss=2.5422 lr=3.00e-05 tok/s=12484
[train] step=182380 tokens=2988.1M loss=1.8068 lr=3.00e-05 tok/s=12484
[train] step=182390 tokens=2988.3M loss=1.8313 lr=3.00e-05 tok/s=12484
[train] step=182400 tokens=2988.4M loss=1.8234 lr=3.00e-05 tok/s=12484
[train] step=182410 tokens=2988.6M loss=1.8135 lr=3.00e-05 tok/s=12484
[train] step=182420 tokens=2988.8M loss=1.9706 lr=3.00e-05 tok/s=12484
```
