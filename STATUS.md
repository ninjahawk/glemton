# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 09:34:50 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 586M / 3000M (19.5%) |
| Step | 35750 |
| Latest loss | 2.4489 |
| Avg loss (last 30 logged) | 2.3551 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 5:43:27 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.48 -> 2.51 -> 2.31 -> 2.33 -> 2.31 -> 2.72 -> 2.47 -> 2.40 -> 2.16 -> 2.26 -> 2.45 -> 2.26

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`

## Recent log tail
```
[train] step=35640 tokens=583.9M loss=2.5588 lr=2.77e-04 tok/s=12483
[train] step=35650 tokens=584.1M loss=2.1213 lr=2.77e-04 tok/s=12483
[train] step=35660 tokens=584.3M loss=2.1539 lr=2.77e-04 tok/s=12483
[train] step=35670 tokens=584.4M loss=2.2266 lr=2.77e-04 tok/s=12483
[train] step=35680 tokens=584.6M loss=2.5057 lr=2.77e-04 tok/s=12483
[train] step=35690 tokens=584.7M loss=2.7778 lr=2.77e-04 tok/s=12483
[train] step=35700 tokens=584.9M loss=2.3160 lr=2.77e-04 tok/s=12483
[train] step=35710 tokens=585.1M loss=2.2021 lr=2.77e-04 tok/s=12483
[train] step=35720 tokens=585.2M loss=2.2562 lr=2.77e-04 tok/s=12483
[train] step=35730 tokens=585.4M loss=2.1747 lr=2.77e-04 tok/s=12483
[train] step=35740 tokens=585.6M loss=2.2448 lr=2.77e-04 tok/s=12483
[train] step=35750 tokens=585.7M loss=2.4489 lr=2.77e-04 tok/s=12483
```
