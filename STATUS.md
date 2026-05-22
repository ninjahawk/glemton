# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 05:54:14 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 421M / 3000M (14.0%) |
| Step | 25670 |
| Latest loss | 2.4497 |
| Avg loss (last 30 logged) | 2.4504 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 2 days, 9:23:19 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.51 -> 2.66 -> 2.54 -> 2.32 -> 2.44 -> 2.64 -> 2.54 -> 2.28 -> 2.53 -> 2.36 -> 2.33 -> 2.55

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=25560 tokens=418.8M loss=2.7069 lr=2.88e-04 tok/s=12485
[train] step=25570 tokens=418.9M loss=2.6202 lr=2.88e-04 tok/s=12485
[train] step=25580 tokens=419.1M loss=2.6223 lr=2.88e-04 tok/s=12485
[train] step=25590 tokens=419.3M loss=2.5817 lr=2.88e-04 tok/s=12485
[train] step=25600 tokens=419.4M loss=2.1760 lr=2.88e-04 tok/s=12485
[train] step=25610 tokens=419.6M loss=2.4983 lr=2.88e-04 tok/s=12485
[train] step=25620 tokens=419.8M loss=2.5630 lr=2.88e-04 tok/s=12485
[train] step=25630 tokens=419.9M loss=2.5877 lr=2.88e-04 tok/s=12485
[train] step=25640 tokens=420.1M loss=2.2952 lr=2.88e-04 tok/s=12485
[train] step=25650 tokens=420.2M loss=2.5461 lr=2.88e-04 tok/s=12485
[train] step=25660 tokens=420.4M loss=2.8464 lr=2.88e-04 tok/s=12485
[train] step=25670 tokens=420.6M loss=2.4497 lr=2.88e-04 tok/s=12485
```
