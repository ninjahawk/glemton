# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 21:00:16 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2179M / 3000M (72.6%) |
| Step | 132980 |
| Latest loss | 1.9166 |
| Avg loss (last 30 logged) | 2.0650 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 18:16:01 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.89 -> 1.84 -> 1.72 -> 2.26 -> 1.79 -> 2.14 -> 2.21 -> 2.30 -> 2.13 -> 2.06 -> 1.83 -> 2.17

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
[train] step=132870 tokens=2176.9M loss=1.6889 lr=7.79e-05 tok/s=12489
[train] step=132880 tokens=2177.1M loss=1.9037 lr=7.78e-05 tok/s=12489
[train] step=132890 tokens=2177.3M loss=2.1310 lr=7.78e-05 tok/s=12489
[train] step=132900 tokens=2177.4M loss=2.2908 lr=7.78e-05 tok/s=12489
[train] step=132910 tokens=2177.6M loss=2.1435 lr=7.78e-05 tok/s=12489
[train] step=132920 tokens=2177.8M loss=2.2515 lr=7.78e-05 tok/s=12489
[train] step=132930 tokens=2177.9M loss=2.2767 lr=7.78e-05 tok/s=12489
[train] step=132940 tokens=2178.1M loss=2.2375 lr=7.77e-05 tok/s=12489
[train] step=132950 tokens=2178.3M loss=2.1659 lr=7.77e-05 tok/s=12489
[train] step=132960 tokens=2178.4M loss=2.0858 lr=7.77e-05 tok/s=12489
[train] step=132970 tokens=2178.6M loss=2.0761 lr=7.77e-05 tok/s=12489
[train] step=132980 tokens=2178.7M loss=1.9166 lr=7.77e-05 tok/s=12489
```
