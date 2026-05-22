# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 11:05:06 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 653M / 3000M (21.8%) |
| Step | 39870 |
| Latest loss | 2.3620 |
| Avg loss (last 30 logged) | 2.4232 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 4:13:19 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.24 -> 2.19 -> 2.34 -> 2.99 -> 2.21 -> 2.31 -> 2.37 -> 2.39 -> 2.34 -> 2.15 -> 2.34 -> 2.58

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=39760 tokens=651.4M loss=2.3995 lr=2.72e-04 tok/s=12483
[train] step=39770 tokens=651.6M loss=2.5092 lr=2.72e-04 tok/s=12483
[train] step=39780 tokens=651.8M loss=2.4489 lr=2.71e-04 tok/s=12483
[train] step=39790 tokens=651.9M loss=2.3859 lr=2.71e-04 tok/s=12483
[train] step=39800 tokens=652.1M loss=2.7943 lr=2.71e-04 tok/s=12483
[train] step=39810 tokens=652.2M loss=2.0521 lr=2.71e-04 tok/s=12483
[train] step=39820 tokens=652.4M loss=2.6966 lr=2.71e-04 tok/s=12483
[train] step=39830 tokens=652.6M loss=2.3924 lr=2.71e-04 tok/s=12483
[train] step=39840 tokens=652.7M loss=2.7182 lr=2.71e-04 tok/s=12483
[train] step=39850 tokens=652.9M loss=2.5772 lr=2.71e-04 tok/s=12483
[train] step=39860 tokens=653.1M loss=2.2005 lr=2.71e-04 tok/s=12483
[train] step=39870 tokens=653.2M loss=2.3620 lr=2.71e-04 tok/s=12483
```
