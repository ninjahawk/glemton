# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 21:30:21 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2201M / 3000M (73.4%) |
| Step | 134350 |
| Latest loss | 2.6516 |
| Avg loss (last 30 logged) | 2.0893 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 17:46:00 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.63 -> 2.00 -> 1.78 -> 1.93 -> 2.01 -> 2.19 -> 2.23 -> 1.87 -> 2.24 -> 2.22 -> 2.35 -> 2.31

## Checkpoints on disk
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=134250 tokens=2199.6M loss=2.4317 lr=7.54e-05 tok/s=12489
[train] step=134260 tokens=2199.7M loss=1.9578 lr=7.54e-05 tok/s=12489
[train] step=134270 tokens=2199.9M loss=1.8857 lr=7.54e-05 tok/s=12489
[train] checkpoint -> checkpoints\glemton-350m\step_134278_tokens_2200M.pt
[train] step=134280 tokens=2200.0M loss=1.6297 lr=7.54e-05 tok/s=12489
[train] step=134290 tokens=2200.2M loss=2.0275 lr=7.54e-05 tok/s=12489
[train] step=134300 tokens=2200.4M loss=2.3854 lr=7.53e-05 tok/s=12489
[train] step=134310 tokens=2200.5M loss=1.5882 lr=7.53e-05 tok/s=12489
[train] step=134320 tokens=2200.7M loss=1.9791 lr=7.53e-05 tok/s=12489
[train] step=134330 tokens=2200.9M loss=2.3072 lr=7.53e-05 tok/s=12489
[train] step=134340 tokens=2201.0M loss=2.5302 lr=7.53e-05 tok/s=12489
[train] step=134350 tokens=2201.2M loss=2.6516 lr=7.52e-05 tok/s=12489
```
