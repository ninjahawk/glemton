# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 06:24:19 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 443M / 3000M (14.8%) |
| Step | 27040 |
| Latest loss | 2.2103 |
| Avg loss (last 30 logged) | 2.3742 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 2 days, 8:53:25 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.51 -> 2.46 -> 2.79 -> 2.08 -> 2.35 -> 2.22 -> 2.42 -> 2.27 -> 2.45 -> 2.67 -> 2.19 -> 2.71

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=26930 tokens=441.2M loss=2.1536 lr=2.87e-04 tok/s=12485
[train] step=26940 tokens=441.4M loss=2.5431 lr=2.87e-04 tok/s=12485
[train] step=26950 tokens=441.5M loss=2.3815 lr=2.87e-04 tok/s=12485
[train] step=26960 tokens=441.7M loss=2.4213 lr=2.87e-04 tok/s=12485
[train] step=26970 tokens=441.9M loss=2.2978 lr=2.87e-04 tok/s=12485
[train] step=26980 tokens=442.0M loss=2.5121 lr=2.87e-04 tok/s=12485
[train] step=26990 tokens=442.2M loss=2.2674 lr=2.87e-04 tok/s=12485
[train] step=27000 tokens=442.4M loss=2.3928 lr=2.87e-04 tok/s=12485
[train] step=27010 tokens=442.5M loss=2.3375 lr=2.87e-04 tok/s=12485
[train] step=27020 tokens=442.7M loss=2.7103 lr=2.87e-04 tok/s=12485
[train] step=27030 tokens=442.9M loss=2.4446 lr=2.87e-04 tok/s=12485
[train] step=27040 tokens=443.0M loss=2.2103 lr=2.87e-04 tok/s=12485
```
