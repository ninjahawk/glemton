# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 17:49:47 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2036M / 3000M (67.9%) |
| Step | 124270 |
| Latest loss | 2.2607 |
| Avg loss (last 30 logged) | 2.0801 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 21:26:21 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.05 -> 1.67 -> 2.02 -> 1.87 -> 1.95 -> 2.38 -> 2.34 -> 1.84 -> 1.92 -> 2.31 -> 2.21 -> 1.61

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=124160 tokens=2034.2M loss=1.9692 lr=9.43e-05 tok/s=12490
[train] step=124170 tokens=2034.4M loss=1.9274 lr=9.43e-05 tok/s=12490
[train] step=124180 tokens=2034.6M loss=2.7260 lr=9.43e-05 tok/s=12490
[train] step=124190 tokens=2034.7M loss=1.7156 lr=9.43e-05 tok/s=12490
[train] step=124200 tokens=2034.9M loss=1.9707 lr=9.42e-05 tok/s=12490
[train] step=124210 tokens=2035.1M loss=1.6358 lr=9.42e-05 tok/s=12490
[train] step=124220 tokens=2035.2M loss=2.9060 lr=9.42e-05 tok/s=12490
[train] step=124230 tokens=2035.4M loss=2.3944 lr=9.42e-05 tok/s=12490
[train] step=124240 tokens=2035.5M loss=1.6854 lr=9.42e-05 tok/s=12490
[train] step=124250 tokens=2035.7M loss=1.6103 lr=9.41e-05 tok/s=12490
[train] step=124260 tokens=2035.9M loss=2.3086 lr=9.41e-05 tok/s=12490
[train] step=124270 tokens=2036.0M loss=2.2607 lr=9.41e-05 tok/s=12490
```
