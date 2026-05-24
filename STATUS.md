# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 23:30:39 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2291M / 3000M (76.4%) |
| Step | 139850 |
| Latest loss | 2.1066 |
| Avg loss (last 30 logged) | 2.0725 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 15:45:45 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.04 -> 1.85 -> 1.72 -> 2.00 -> 2.05 -> 2.42 -> 2.32 -> 2.07 -> 1.89 -> 2.80 -> 2.07 -> 2.46

## Checkpoints on disk
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=139740 tokens=2289.5M loss=2.2073 lr=6.62e-05 tok/s=12489
[train] step=139750 tokens=2289.7M loss=1.9253 lr=6.62e-05 tok/s=12489
[train] step=139760 tokens=2289.8M loss=1.5824 lr=6.62e-05 tok/s=12489
[train] step=139770 tokens=2290.0M loss=1.8156 lr=6.62e-05 tok/s=12489
[train] step=139780 tokens=2290.2M loss=1.9629 lr=6.62e-05 tok/s=12489
[train] step=139790 tokens=2290.3M loss=2.0883 lr=6.62e-05 tok/s=12489
[train] step=139800 tokens=2290.5M loss=2.0441 lr=6.62e-05 tok/s=12489
[train] step=139810 tokens=2290.6M loss=2.2091 lr=6.61e-05 tok/s=12489
[train] step=139820 tokens=2290.8M loss=2.4562 lr=6.61e-05 tok/s=12489
[train] step=139830 tokens=2291.0M loss=2.1394 lr=6.61e-05 tok/s=12489
[train] step=139840 tokens=2291.1M loss=2.2691 lr=6.61e-05 tok/s=12489
[train] step=139850 tokens=2291.3M loss=2.1066 lr=6.61e-05 tok/s=12489
```
