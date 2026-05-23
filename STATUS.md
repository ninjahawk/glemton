# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 12:59:06 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1818M / 3000M (60.6%) |
| Step | 110960 |
| Latest loss | 2.1925 |
| Avg loss (last 30 logged) | 2.1065 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 2:17:30 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.02 -> 1.87 -> 2.08 -> 1.84 -> 1.74 -> 2.18 -> 1.66 -> 2.31 -> 1.97 -> 2.32 -> 2.31 -> 2.07

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=110850 tokens=1816.2M loss=2.0260 lr=1.22e-04 tok/s=12488
[train] step=110860 tokens=1816.3M loss=1.7635 lr=1.22e-04 tok/s=12488
[train] step=110870 tokens=1816.5M loss=2.2724 lr=1.22e-04 tok/s=12488
[train] step=110880 tokens=1816.7M loss=2.5229 lr=1.22e-04 tok/s=12488
[train] step=110890 tokens=1816.8M loss=2.2676 lr=1.22e-04 tok/s=12488
[train] step=110900 tokens=1817.0M loss=2.0853 lr=1.22e-04 tok/s=12488
[train] step=110910 tokens=1817.1M loss=2.1003 lr=1.22e-04 tok/s=12488
[train] step=110920 tokens=1817.3M loss=2.0860 lr=1.22e-04 tok/s=12488
[train] step=110930 tokens=1817.5M loss=2.0144 lr=1.22e-04 tok/s=12488
[train] step=110940 tokens=1817.6M loss=2.0734 lr=1.22e-04 tok/s=12488
[train] step=110950 tokens=1817.8M loss=1.7964 lr=1.22e-04 tok/s=12488
[train] step=110960 tokens=1818.0M loss=2.1925 lr=1.22e-04 tok/s=12488
```
