# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 20:00:07 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2134M / 3000M (71.1%) |
| Step | 130230 |
| Latest loss | 1.9896 |
| Avg loss (last 30 logged) | 2.1073 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 19:15:59 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.10 -> 2.03 -> 2.51 -> 1.86 -> 2.24 -> 1.77 -> 1.72 -> 2.16 -> 1.59 -> 2.55 -> 2.26 -> 2.19

## Checkpoints on disk
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=130120 tokens=2131.9M loss=2.4708 lr=8.29e-05 tok/s=12490
[train] step=130130 tokens=2132.0M loss=1.9675 lr=8.28e-05 tok/s=12490
[train] step=130140 tokens=2132.2M loss=2.2904 lr=8.28e-05 tok/s=12490
[train] step=130150 tokens=2132.4M loss=2.3852 lr=8.28e-05 tok/s=12490
[train] step=130160 tokens=2132.5M loss=2.0026 lr=8.28e-05 tok/s=12490
[train] step=130170 tokens=2132.7M loss=2.1869 lr=8.28e-05 tok/s=12490
[train] step=130180 tokens=2132.9M loss=1.8210 lr=8.28e-05 tok/s=12490
[train] step=130190 tokens=2133.0M loss=1.9127 lr=8.27e-05 tok/s=12490
[train] step=130200 tokens=2133.2M loss=2.4396 lr=8.27e-05 tok/s=12490
[train] step=130210 tokens=2133.4M loss=2.1851 lr=8.27e-05 tok/s=12490
[train] step=130220 tokens=2133.5M loss=2.1882 lr=8.27e-05 tok/s=12490
[train] step=130230 tokens=2133.7M loss=1.9896 lr=8.27e-05 tok/s=12490
```
