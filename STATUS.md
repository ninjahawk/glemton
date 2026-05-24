# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 11:22:29 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2824M / 3000M (94.1%) |
| Step | 172340 |
| Latest loss | 2.0282 |
| Avg loss (last 30 logged) | 2.0549 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 3:55:30 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.92 -> 2.13 -> 2.02 -> 2.05 -> 2.15 -> 2.20 -> 2.78 -> 1.86 -> 2.43 -> 2.41 -> 2.09 -> 2.10

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
[train] step=172230 tokens=2821.8M loss=2.1344 lr=3.24e-05 tok/s=12484
[train] step=172240 tokens=2822.0M loss=2.1054 lr=3.24e-05 tok/s=12484
[train] step=172250 tokens=2822.1M loss=2.0270 lr=3.24e-05 tok/s=12484
[train] step=172260 tokens=2822.3M loss=2.0855 lr=3.24e-05 tok/s=12484
[train] step=172270 tokens=2822.5M loss=2.1759 lr=3.24e-05 tok/s=12484
[train] step=172280 tokens=2822.6M loss=2.2325 lr=3.24e-05 tok/s=12484
[train] step=172290 tokens=2822.8M loss=1.8580 lr=3.24e-05 tok/s=12484
[train] step=172300 tokens=2823.0M loss=1.9490 lr=3.24e-05 tok/s=12484
[train] step=172310 tokens=2823.1M loss=1.7410 lr=3.23e-05 tok/s=12484
[train] step=172320 tokens=2823.3M loss=2.1012 lr=3.23e-05 tok/s=12484
[train] step=172330 tokens=2823.5M loss=1.7605 lr=3.23e-05 tok/s=12484
[train] step=172340 tokens=2823.6M loss=2.0282 lr=3.23e-05 tok/s=12484
```
