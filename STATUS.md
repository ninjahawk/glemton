# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 12:19:00 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1788M / 3000M (59.6%) |
| Step | 109130 |
| Latest loss | 2.2945 |
| Avg loss (last 30 logged) | 2.1502 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 2:57:33 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.68 -> 1.95 -> 1.40 -> 2.73 -> 1.58 -> 1.82 -> 2.49 -> 2.36 -> 2.35 -> 2.10 -> 2.94 -> 1.77

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=109020 tokens=1786.2M loss=1.6837 lr=1.27e-04 tok/s=12488
[train] step=109030 tokens=1786.3M loss=2.3740 lr=1.27e-04 tok/s=12488
[train] step=109040 tokens=1786.5M loss=2.3102 lr=1.26e-04 tok/s=12488
[train] step=109050 tokens=1786.7M loss=2.2078 lr=1.26e-04 tok/s=12488
[train] step=109060 tokens=1786.8M loss=2.0595 lr=1.26e-04 tok/s=12488
[train] step=109070 tokens=1787.0M loss=1.9869 lr=1.26e-04 tok/s=12488
[train] step=109080 tokens=1787.2M loss=1.9893 lr=1.26e-04 tok/s=12488
[train] step=109090 tokens=1787.3M loss=2.4313 lr=1.26e-04 tok/s=12488
[train] step=109100 tokens=1787.5M loss=1.7731 lr=1.26e-04 tok/s=12488
[train] step=109110 tokens=1787.7M loss=2.1436 lr=1.26e-04 tok/s=12488
[train] step=109120 tokens=1787.8M loss=2.6083 lr=1.26e-04 tok/s=12488
[train] step=109130 tokens=1788.0M loss=2.2945 lr=1.26e-04 tok/s=12488
```
