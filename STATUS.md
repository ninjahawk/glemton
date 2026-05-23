# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 11:08:49 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1735M / 3000M (57.8%) |
| Step | 105920 |
| Latest loss | 2.0344 |
| Avg loss (last 30 logged) | 2.1493 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 4:07:45 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.87 -> 2.08 -> 2.51 -> 2.09 -> 1.94 -> 2.36 -> 1.64 -> 1.95 -> 1.98 -> 2.11 -> 2.29 -> 2.01

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=105810 tokens=1733.6M loss=2.2748 lr=1.34e-04 tok/s=12488
[train] step=105820 tokens=1733.8M loss=1.8809 lr=1.34e-04 tok/s=12488
[train] step=105830 tokens=1733.9M loss=2.0194 lr=1.34e-04 tok/s=12488
[train] step=105840 tokens=1734.1M loss=2.0026 lr=1.34e-04 tok/s=12488
[train] step=105850 tokens=1734.2M loss=2.0722 lr=1.34e-04 tok/s=12488
[train] step=105860 tokens=1734.4M loss=1.9544 lr=1.34e-04 tok/s=12488
[train] step=105870 tokens=1734.6M loss=2.4159 lr=1.34e-04 tok/s=12488
[train] step=105880 tokens=1734.7M loss=2.4380 lr=1.34e-04 tok/s=12488
[train] step=105890 tokens=1734.9M loss=2.1129 lr=1.34e-04 tok/s=12488
[train] step=105900 tokens=1735.1M loss=2.0121 lr=1.34e-04 tok/s=12488
[train] step=105910 tokens=1735.2M loss=1.7338 lr=1.34e-04 tok/s=12488
[train] step=105920 tokens=1735.4M loss=2.0344 lr=1.34e-04 tok/s=12488
```
