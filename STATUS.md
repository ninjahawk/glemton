# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 02:13:38 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 255M / 3000M (8.5%) |
| Step | 15590 |
| Latest loss | 2.8237 |
| Avg loss (last 30 logged) | 2.5605 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 2 days, 13:02:23 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.58 -> 2.31 -> 2.53 -> 2.63 -> 2.23 -> 2.55 -> 2.54 -> 2.40 -> 2.47 -> 2.43 -> 2.71 -> 2.90

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=15480 tokens=253.6M loss=2.5559 lr=2.96e-04 tok/s=12489
[train] step=15490 tokens=253.8M loss=2.3382 lr=2.96e-04 tok/s=12489
[train] step=15500 tokens=254.0M loss=2.4647 lr=2.96e-04 tok/s=12489
[train] step=15510 tokens=254.1M loss=2.4186 lr=2.96e-04 tok/s=12490
[train] step=15520 tokens=254.3M loss=2.4046 lr=2.96e-04 tok/s=12490
[train] step=15530 tokens=254.4M loss=2.4443 lr=2.96e-04 tok/s=12490
[train] step=15540 tokens=254.6M loss=2.4170 lr=2.96e-04 tok/s=12490
[train] step=15550 tokens=254.8M loss=2.7065 lr=2.96e-04 tok/s=12490
[train] step=15560 tokens=254.9M loss=2.5515 lr=2.96e-04 tok/s=12490
[train] step=15570 tokens=255.1M loss=2.8973 lr=2.96e-04 tok/s=12490
[train] step=15580 tokens=255.3M loss=2.4306 lr=2.96e-04 tok/s=12490
[train] step=15590 tokens=255.4M loss=2.8237 lr=2.96e-04 tok/s=12490
```
