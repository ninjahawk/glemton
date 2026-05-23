# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 03:27:39 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1390M / 3000M (46.3%) |
| Step | 84820 |
| Latest loss | 2.2700 |
| Avg loss (last 30 logged) | 2.2036 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 11:49:18 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.10 -> 2.06 -> 2.16 -> 2.20 -> 2.30 -> 2.30 -> 2.37 -> 1.97 -> 2.19 -> 2.70 -> 2.27 -> 2.12

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`

## Recent log tail
```
[train] step=84710 tokens=1387.9M loss=2.5114 lr=1.83e-04 tok/s=12487
[train] step=84720 tokens=1388.1M loss=2.5520 lr=1.83e-04 tok/s=12487
[train] step=84730 tokens=1388.2M loss=2.0962 lr=1.83e-04 tok/s=12487
[train] step=84740 tokens=1388.4M loss=2.4670 lr=1.83e-04 tok/s=12487
[train] step=84750 tokens=1388.5M loss=2.4326 lr=1.83e-04 tok/s=12487
[train] step=84760 tokens=1388.7M loss=2.3513 lr=1.83e-04 tok/s=12487
[train] step=84770 tokens=1388.9M loss=2.1172 lr=1.83e-04 tok/s=12487
[train] step=84780 tokens=1389.0M loss=2.0532 lr=1.83e-04 tok/s=12487
[train] step=84790 tokens=1389.2M loss=2.1200 lr=1.83e-04 tok/s=12487
[train] step=84800 tokens=1389.4M loss=1.8435 lr=1.83e-04 tok/s=12487
[train] step=84810 tokens=1389.5M loss=2.5172 lr=1.82e-04 tok/s=12487
[train] step=84820 tokens=1389.7M loss=2.2700 lr=1.82e-04 tok/s=12487
```
