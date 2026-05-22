# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 11:45:13 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 683M / 3000M (22.8%) |
| Step | 41710 |
| Latest loss | 2.4191 |
| Avg loss (last 30 logged) | 2.3989 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 3:33:00 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.08 -> 2.28 -> 2.43 -> 2.29 -> 2.34 -> 2.15 -> 2.07 -> 2.19 -> 2.06 -> 2.23 -> 2.31 -> 2.41

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=41600 tokens=681.6M loss=2.4855 lr=2.69e-04 tok/s=12483
[train] step=41610 tokens=681.7M loss=2.2153 lr=2.69e-04 tok/s=12483
[train] step=41620 tokens=681.9M loss=2.5501 lr=2.69e-04 tok/s=12483
[train] step=41630 tokens=682.1M loss=2.5847 lr=2.69e-04 tok/s=12483
[train] step=41640 tokens=682.2M loss=2.6279 lr=2.69e-04 tok/s=12483
[train] step=41650 tokens=682.4M loss=1.9910 lr=2.69e-04 tok/s=12483
[train] step=41660 tokens=682.6M loss=2.0324 lr=2.69e-04 tok/s=12483
[train] step=41670 tokens=682.7M loss=2.7128 lr=2.69e-04 tok/s=12483
[train] step=41680 tokens=682.9M loss=2.4091 lr=2.69e-04 tok/s=12483
[train] step=41690 tokens=683.0M loss=2.3053 lr=2.69e-04 tok/s=12483
[train] step=41700 tokens=683.2M loss=2.3348 lr=2.69e-04 tok/s=12483
[train] step=41710 tokens=683.4M loss=2.4191 lr=2.69e-04 tok/s=12483
```
