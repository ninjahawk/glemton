# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 09:44:52 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 593M / 3000M (19.8%) |
| Step | 36210 |
| Latest loss | 2.7092 |
| Avg loss (last 30 logged) | 2.4391 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 5:33:18 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.53 -> 2.19 -> 2.45 -> 2.42 -> 2.27 -> 2.18 -> 2.77 -> 2.18 -> 2.12 -> 2.38 -> 2.23 -> 2.34

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`

## Recent log tail
```
[train] step=36100 tokens=591.5M loss=2.1872 lr=2.77e-04 tok/s=12483
[train] step=36110 tokens=591.6M loss=2.4935 lr=2.77e-04 tok/s=12483
[train] step=36120 tokens=591.8M loss=2.1833 lr=2.77e-04 tok/s=12483
[train] step=36130 tokens=592.0M loss=2.3671 lr=2.77e-04 tok/s=12483
[train] step=36140 tokens=592.1M loss=2.6674 lr=2.77e-04 tok/s=12483
[train] step=36150 tokens=592.3M loss=2.5238 lr=2.76e-04 tok/s=12483
[train] step=36160 tokens=592.4M loss=2.7039 lr=2.76e-04 tok/s=12483
[train] step=36170 tokens=592.6M loss=2.3660 lr=2.76e-04 tok/s=12483
[train] step=36180 tokens=592.8M loss=2.3418 lr=2.76e-04 tok/s=12483
[train] step=36190 tokens=592.9M loss=2.2270 lr=2.76e-04 tok/s=12483
[train] step=36200 tokens=593.1M loss=2.3436 lr=2.76e-04 tok/s=12483
[train] step=36210 tokens=593.3M loss=2.7092 lr=2.76e-04 tok/s=12483
```
