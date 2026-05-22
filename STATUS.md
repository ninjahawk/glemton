# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 11:25:10 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 668M / 3000M (22.3%) |
| Step | 40790 |
| Latest loss | 2.3762 |
| Avg loss (last 30 logged) | 2.2713 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 3:53:10 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.11 -> 2.53 -> 2.39 -> 2.30 -> 2.17 -> 2.34 -> 2.13 -> 2.90 -> 2.51 -> 2.30 -> 2.16 -> 2.54

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=40680 tokens=666.5M loss=2.0956 lr=2.70e-04 tok/s=12483
[train] step=40690 tokens=666.7M loss=2.0596 lr=2.70e-04 tok/s=12483
[train] step=40700 tokens=666.8M loss=2.4814 lr=2.70e-04 tok/s=12483
[train] step=40710 tokens=667.0M loss=2.1225 lr=2.70e-04 tok/s=12483
[train] step=40720 tokens=667.2M loss=2.1222 lr=2.70e-04 tok/s=12483
[train] step=40730 tokens=667.3M loss=2.2725 lr=2.70e-04 tok/s=12483
[train] step=40740 tokens=667.5M loss=2.1450 lr=2.70e-04 tok/s=12483
[train] step=40750 tokens=667.6M loss=2.2659 lr=2.70e-04 tok/s=12483
[train] step=40760 tokens=667.8M loss=2.5408 lr=2.70e-04 tok/s=12483
[train] step=40770 tokens=668.0M loss=2.1769 lr=2.70e-04 tok/s=12483
[train] step=40780 tokens=668.1M loss=2.2641 lr=2.70e-04 tok/s=12483
[train] step=40790 tokens=668.3M loss=2.3762 lr=2.70e-04 tok/s=12483
```
