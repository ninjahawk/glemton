# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 13:59:15 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1863M / 3000M (62.1%) |
| Step | 113710 |
| Latest loss | 1.9005 |
| Avg loss (last 30 logged) | 2.1174 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 1 day, 1:17:20 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.06 -> 2.00 -> 1.72 -> 2.08 -> 2.64 -> 2.41 -> 2.07 -> 2.40 -> 2.13 -> 2.16 -> 1.96 -> 2.17

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=113600 tokens=1861.2M loss=2.5103 lr=1.16e-04 tok/s=12489
[train] step=113610 tokens=1861.4M loss=2.1803 lr=1.16e-04 tok/s=12489
[train] step=113620 tokens=1861.6M loss=2.2207 lr=1.16e-04 tok/s=12489
[train] step=113630 tokens=1861.7M loss=2.4533 lr=1.16e-04 tok/s=12489
[train] step=113640 tokens=1861.9M loss=2.0414 lr=1.16e-04 tok/s=12489
[train] step=113650 tokens=1862.0M loss=2.1827 lr=1.16e-04 tok/s=12489
[train] step=113660 tokens=1862.2M loss=2.0247 lr=1.16e-04 tok/s=12489
[train] step=113670 tokens=1862.4M loss=2.1165 lr=1.16e-04 tok/s=12489
[train] step=113680 tokens=1862.5M loss=1.6547 lr=1.16e-04 tok/s=12489
[train] step=113690 tokens=1862.7M loss=2.1692 lr=1.16e-04 tok/s=12489
[train] step=113700 tokens=1862.9M loss=2.0744 lr=1.16e-04 tok/s=12489
[train] step=113710 tokens=1863.0M loss=1.9005 lr=1.16e-04 tok/s=12489
```
