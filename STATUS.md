# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 01:17:19 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1292M / 3000M (43.1%) |
| Step | 78850 |
| Latest loss | 2.1455 |
| Avg loss (last 30 logged) | 2.1127 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 13:59:50 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.32 -> 2.15 -> 2.29 -> 2.38 -> 2.44 -> 2.52 -> 2.03 -> 1.73 -> 2.54 -> 2.12 -> 2.24 -> 2.38

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] step=78740 tokens=1290.1M loss=1.9460 lr=1.96e-04 tok/s=12487
[train] step=78750 tokens=1290.2M loss=2.1617 lr=1.96e-04 tok/s=12487
[train] step=78760 tokens=1290.4M loss=2.0537 lr=1.96e-04 tok/s=12487
[train] step=78770 tokens=1290.6M loss=2.2155 lr=1.96e-04 tok/s=12487
[train] step=78780 tokens=1290.7M loss=2.0144 lr=1.96e-04 tok/s=12487
[train] step=78790 tokens=1290.9M loss=2.2159 lr=1.96e-04 tok/s=12487
[train] step=78800 tokens=1291.1M loss=2.2127 lr=1.96e-04 tok/s=12487
[train] step=78810 tokens=1291.2M loss=1.9667 lr=1.96e-04 tok/s=12487
[train] step=78820 tokens=1291.4M loss=2.3785 lr=1.96e-04 tok/s=12487
[train] step=78830 tokens=1291.6M loss=2.3516 lr=1.96e-04 tok/s=12487
[train] step=78840 tokens=1291.7M loss=2.0662 lr=1.96e-04 tok/s=12487
[train] step=78850 tokens=1291.9M loss=2.1455 lr=1.96e-04 tok/s=12487
```
