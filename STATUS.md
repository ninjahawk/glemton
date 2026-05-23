# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 04:17:47 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1427M / 3000M (47.6%) |
| Step | 87110 |
| Latest loss | 2.1525 |
| Avg loss (last 30 logged) | 2.1939 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 10:59:14 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.33 -> 2.07 -> 2.18 -> 1.94 -> 2.05 -> 2.44 -> 2.00 -> 2.33 -> 2.40 -> 2.21 -> 2.47 -> 2.51

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`

## Recent log tail
```
[train] step=87000 tokens=1425.4M loss=2.1346 lr=1.77e-04 tok/s=12487
[train] step=87010 tokens=1425.6M loss=2.1089 lr=1.77e-04 tok/s=12487
[train] step=87020 tokens=1425.7M loss=2.7352 lr=1.77e-04 tok/s=12487
[train] step=87030 tokens=1425.9M loss=2.0142 lr=1.77e-04 tok/s=12487
[train] step=87040 tokens=1426.1M loss=2.1723 lr=1.77e-04 tok/s=12487
[train] step=87050 tokens=1426.2M loss=2.2529 lr=1.77e-04 tok/s=12487
[train] step=87060 tokens=1426.4M loss=2.2314 lr=1.77e-04 tok/s=12487
[train] step=87070 tokens=1426.6M loss=1.7800 lr=1.77e-04 tok/s=12487
[train] step=87080 tokens=1426.7M loss=2.1536 lr=1.77e-04 tok/s=12487
[train] step=87090 tokens=1426.9M loss=2.5094 lr=1.77e-04 tok/s=12487
[train] step=87100 tokens=1427.0M loss=2.1593 lr=1.77e-04 tok/s=12487
[train] step=87110 tokens=1427.2M loss=2.1525 lr=1.77e-04 tok/s=12487
```
