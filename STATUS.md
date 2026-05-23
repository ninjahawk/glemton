# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 11:38:54 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1758M / 3000M (58.6%) |
| Step | 107290 |
| Latest loss | 1.8314 |
| Avg loss (last 30 logged) | 2.0834 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 3:37:51 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.87 -> 1.70 -> 2.02 -> 2.64 -> 1.71 -> 2.40 -> 2.04 -> 1.76 -> 2.11 -> 2.00 -> 2.44 -> 2.12

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=107180 tokens=1756.0M loss=2.0672 lr=1.31e-04 tok/s=12488
[train] step=107190 tokens=1756.2M loss=2.3287 lr=1.31e-04 tok/s=12488
[train] step=107200 tokens=1756.4M loss=1.5702 lr=1.31e-04 tok/s=12488
[train] step=107210 tokens=1756.5M loss=2.3870 lr=1.31e-04 tok/s=12488
[train] step=107220 tokens=1756.7M loss=1.7540 lr=1.31e-04 tok/s=12488
[train] step=107230 tokens=1756.9M loss=1.8464 lr=1.31e-04 tok/s=12488
[train] step=107240 tokens=1757.0M loss=2.0211 lr=1.31e-04 tok/s=12488
[train] step=107250 tokens=1757.2M loss=2.0666 lr=1.31e-04 tok/s=12488
[train] step=107260 tokens=1757.3M loss=2.4317 lr=1.30e-04 tok/s=12488
[train] step=107270 tokens=1757.5M loss=2.1249 lr=1.30e-04 tok/s=12488
[train] step=107280 tokens=1757.7M loss=2.2110 lr=1.30e-04 tok/s=12488
[train] step=107290 tokens=1757.8M loss=1.8314 lr=1.30e-04 tok/s=12488
```
