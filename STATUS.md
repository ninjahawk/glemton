# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 01:00:53 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2359M / 3000M (78.6%) |
| Step | 143980 |
| Latest loss | 1.7818 |
| Avg loss (last 30 logged) | 2.0919 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 14:15:25 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.07 -> 1.96 -> 1.85 -> 1.88 -> 1.82 -> 2.02 -> 1.57 -> 2.53 -> 2.09 -> 2.45 -> 2.94 -> 2.15

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=143870 tokens=2357.2M loss=1.9298 lr=5.99e-05 tok/s=12489
[train] step=143880 tokens=2357.3M loss=2.4097 lr=5.99e-05 tok/s=12489
[train] step=143890 tokens=2357.5M loss=2.3388 lr=5.99e-05 tok/s=12489
[train] step=143900 tokens=2357.7M loss=2.0183 lr=5.99e-05 tok/s=12489
[train] step=143910 tokens=2357.8M loss=2.1410 lr=5.99e-05 tok/s=12489
[train] step=143920 tokens=2358.0M loss=1.9252 lr=5.99e-05 tok/s=12489
[train] step=143930 tokens=2358.1M loss=1.6594 lr=5.98e-05 tok/s=12489
[train] step=143940 tokens=2358.3M loss=2.1045 lr=5.98e-05 tok/s=12489
[train] step=143950 tokens=2358.5M loss=1.9960 lr=5.98e-05 tok/s=12489
[train] step=143960 tokens=2358.6M loss=2.1464 lr=5.98e-05 tok/s=12489
[train] step=143970 tokens=2358.8M loss=1.7766 lr=5.98e-05 tok/s=12489
[train] step=143980 tokens=2359.0M loss=1.7818 lr=5.98e-05 tok/s=12489
```
