# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 11:15:08 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 661M / 3000M (22.0%) |
| Step | 40330 |
| Latest loss | 2.4499 |
| Avg loss (last 30 logged) | 2.3271 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 4:03:10 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.42 -> 2.76 -> 2.39 -> 2.10 -> 2.31 -> 2.87 -> 2.53 -> 2.37 -> 2.26 -> 2.74 -> 2.45 -> 2.50

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=40220 tokens=659.0M loss=2.1873 lr=2.71e-04 tok/s=12483
[train] step=40230 tokens=659.1M loss=2.2125 lr=2.71e-04 tok/s=12483
[train] step=40240 tokens=659.3M loss=2.3448 lr=2.71e-04 tok/s=12483
[train] step=40250 tokens=659.5M loss=2.4424 lr=2.71e-04 tok/s=12483
[train] step=40260 tokens=659.6M loss=2.4588 lr=2.71e-04 tok/s=12483
[train] step=40270 tokens=659.8M loss=2.1717 lr=2.71e-04 tok/s=12483
[train] step=40280 tokens=659.9M loss=2.1957 lr=2.71e-04 tok/s=12483
[train] step=40290 tokens=660.1M loss=2.4472 lr=2.71e-04 tok/s=12483
[train] step=40300 tokens=660.3M loss=2.3103 lr=2.71e-04 tok/s=12483
[train] step=40310 tokens=660.4M loss=2.5015 lr=2.71e-04 tok/s=12483
[train] step=40320 tokens=660.6M loss=2.5119 lr=2.71e-04 tok/s=12483
[train] step=40330 tokens=660.8M loss=2.4499 lr=2.71e-04 tok/s=12483
```
