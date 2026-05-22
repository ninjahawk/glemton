# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 06:54:24 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 466M / 3000M (15.5%) |
| Step | 28420 |
| Latest loss | 2.3356 |
| Avg loss (last 30 logged) | 2.4003 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 2 days, 8:23:15 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.27 -> 2.43 -> 2.60 -> 2.32 -> 2.56 -> 2.38 -> 2.32 -> 2.82 -> 2.53 -> 2.22 -> 2.40 -> 2.54

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=28310 tokens=463.8M loss=2.1738 lr=2.86e-04 tok/s=12485
[train] step=28320 tokens=464.0M loss=2.4032 lr=2.86e-04 tok/s=12485
[train] step=28330 tokens=464.2M loss=2.1982 lr=2.86e-04 tok/s=12485
[train] step=28340 tokens=464.3M loss=2.6693 lr=2.86e-04 tok/s=12485
[train] step=28350 tokens=464.5M loss=2.3222 lr=2.86e-04 tok/s=12485
[train] step=28360 tokens=464.7M loss=2.2067 lr=2.86e-04 tok/s=12485
[train] step=28370 tokens=464.8M loss=2.5346 lr=2.86e-04 tok/s=12485
[train] step=28380 tokens=465.0M loss=2.2730 lr=2.86e-04 tok/s=12485
[train] step=28390 tokens=465.1M loss=2.5391 lr=2.86e-04 tok/s=12485
[train] step=28400 tokens=465.3M loss=2.2432 lr=2.86e-04 tok/s=12485
[train] step=28410 tokens=465.5M loss=2.5373 lr=2.86e-04 tok/s=12485
[train] step=28420 tokens=465.6M loss=2.3356 lr=2.86e-04 tok/s=12485
```
