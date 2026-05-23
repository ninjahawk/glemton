# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 09:58:38 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1683M / 3000M (56.1%) |
| Step | 102710 |
| Latest loss | 2.4104 |
| Avg loss (last 30 logged) | 2.1624 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 5:17:57 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.01 -> 2.36 -> 1.70 -> 1.91 -> 2.00 -> 2.03 -> 2.04 -> 2.40 -> 1.86 -> 2.22 -> 2.06 -> 2.90

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=102600 tokens=1681.0M loss=2.0845 lr=1.41e-04 tok/s=12488
[train] step=102610 tokens=1681.2M loss=1.8912 lr=1.41e-04 tok/s=12488
[train] step=102620 tokens=1681.3M loss=1.9939 lr=1.41e-04 tok/s=12488
[train] step=102630 tokens=1681.5M loss=2.1595 lr=1.41e-04 tok/s=12488
[train] step=102640 tokens=1681.7M loss=1.7831 lr=1.41e-04 tok/s=12488
[train] step=102650 tokens=1681.8M loss=1.7898 lr=1.41e-04 tok/s=12488
[train] step=102660 tokens=1682.0M loss=2.5046 lr=1.41e-04 tok/s=12488
[train] step=102670 tokens=1682.1M loss=2.2285 lr=1.41e-04 tok/s=12488
[train] step=102680 tokens=1682.3M loss=2.8951 lr=1.41e-04 tok/s=12488
[train] step=102690 tokens=1682.5M loss=1.9746 lr=1.41e-04 tok/s=12488
[train] step=102700 tokens=1682.6M loss=2.3133 lr=1.41e-04 tok/s=12488
[train] step=102710 tokens=1682.8M loss=2.4104 lr=1.41e-04 tok/s=12488
```
