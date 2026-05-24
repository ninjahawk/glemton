# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 00:50:52 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2351M / 3000M (78.4%) |
| Step | 143520 |
| Latest loss | 1.8619 |
| Avg loss (last 30 logged) | 2.1237 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 14:25:33 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.23 -> 2.03 -> 2.15 -> 1.89 -> 1.78 -> 2.41 -> 2.27 -> 2.08 -> 2.15 -> 3.08 -> 1.89 -> 2.13

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
[train] step=143410 tokens=2349.6M loss=2.0371 lr=6.06e-05 tok/s=12489
[train] step=143420 tokens=2349.8M loss=2.1111 lr=6.06e-05 tok/s=12489
[train] step=143430 tokens=2350.0M loss=2.5123 lr=6.06e-05 tok/s=12489
[train] step=143440 tokens=2350.1M loss=1.8443 lr=6.06e-05 tok/s=12489
[train] step=143450 tokens=2350.3M loss=2.1483 lr=6.05e-05 tok/s=12489
[train] step=143460 tokens=2350.4M loss=2.4553 lr=6.05e-05 tok/s=12489
[train] step=143470 tokens=2350.6M loss=2.2242 lr=6.05e-05 tok/s=12489
[train] step=143480 tokens=2350.8M loss=1.7348 lr=6.05e-05 tok/s=12489
[train] step=143490 tokens=2350.9M loss=1.8949 lr=6.05e-05 tok/s=12489
[train] step=143500 tokens=2351.1M loss=2.1311 lr=6.05e-05 tok/s=12489
[train] step=143510 tokens=2351.3M loss=2.3159 lr=6.05e-05 tok/s=12489
[train] step=143520 tokens=2351.4M loss=1.8619 lr=6.04e-05 tok/s=12489
```
