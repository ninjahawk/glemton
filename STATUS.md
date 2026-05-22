# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 12:15:18 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 706M / 3000M (23.5%) |
| Step | 43080 |
| Latest loss | 2.1743 |
| Avg loss (last 30 logged) | 2.3117 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 3:03:05 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.31 -> 2.40 -> 2.17 -> 2.46 -> 2.27 -> 2.52 -> 2.09 -> 2.15 -> 2.53 -> 2.35 -> 2.27 -> 2.16

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`

## Recent log tail
```
[train] step=42970 tokens=704.0M loss=2.1776 lr=2.67e-04 tok/s=12483
[train] step=42980 tokens=704.2M loss=2.3237 lr=2.67e-04 tok/s=12483
[train] step=42990 tokens=704.3M loss=2.4005 lr=2.67e-04 tok/s=12483
[train] step=43000 tokens=704.5M loss=2.1240 lr=2.67e-04 tok/s=12483
[train] step=43010 tokens=704.7M loss=1.8871 lr=2.67e-04 tok/s=12483
[train] step=43020 tokens=704.8M loss=2.4358 lr=2.67e-04 tok/s=12483
[train] step=43030 tokens=705.0M loss=2.3437 lr=2.67e-04 tok/s=12483
[train] step=43040 tokens=705.2M loss=2.3438 lr=2.67e-04 tok/s=12483
[train] step=43050 tokens=705.3M loss=2.5045 lr=2.67e-04 tok/s=12483
[train] step=43060 tokens=705.5M loss=2.1553 lr=2.67e-04 tok/s=12483
[train] step=43070 tokens=705.7M loss=2.1430 lr=2.67e-04 tok/s=12483
[train] step=43080 tokens=705.8M loss=2.1743 lr=2.67e-04 tok/s=12483
```
