# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 20:56:39 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1097M / 3000M (36.6%) |
| Step | 66930 |
| Latest loss | 2.3702 |
| Avg loss (last 30 logged) | 2.2515 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 18:20:42 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.20 -> 2.21 -> 2.16 -> 2.16 -> 2.12 -> 2.86 -> 2.59 -> 2.13 -> 2.10 -> 2.07 -> 2.69 -> 2.55

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`

## Recent log tail
```
[train] step=66820 tokens=1094.8M loss=2.1079 lr=2.23e-04 tok/s=12486
[train] step=66830 tokens=1094.9M loss=2.2033 lr=2.23e-04 tok/s=12486
[train] step=66840 tokens=1095.1M loss=2.1510 lr=2.23e-04 tok/s=12486
[train] step=66850 tokens=1095.3M loss=1.9674 lr=2.23e-04 tok/s=12486
[train] step=66860 tokens=1095.4M loss=2.3094 lr=2.23e-04 tok/s=12486
[train] step=66870 tokens=1095.6M loss=2.3795 lr=2.23e-04 tok/s=12486
[train] step=66880 tokens=1095.8M loss=2.3532 lr=2.23e-04 tok/s=12486
[train] step=66890 tokens=1095.9M loss=2.0736 lr=2.22e-04 tok/s=12486
[train] step=66900 tokens=1096.1M loss=2.5526 lr=2.22e-04 tok/s=12486
[train] step=66910 tokens=1096.3M loss=2.0141 lr=2.22e-04 tok/s=12486
[train] step=66920 tokens=1096.4M loss=2.3938 lr=2.22e-04 tok/s=12486
[train] step=66930 tokens=1096.6M loss=2.3702 lr=2.22e-04 tok/s=12486
```
