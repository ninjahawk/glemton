# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 00:40:50 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2344M / 3000M (78.1%) |
| Step | 143060 |
| Latest loss | 1.7780 |
| Avg loss (last 30 logged) | 2.0697 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 14:35:34 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.87 -> 2.21 -> 2.17 -> 1.77 -> 1.80 -> 2.13 -> 1.92 -> 1.97 -> 1.68 -> 2.29 -> 1.84 -> 1.89

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
[train] step=142950 tokens=2342.1M loss=1.8476 lr=6.13e-05 tok/s=12489
[train] step=142960 tokens=2342.3M loss=2.0015 lr=6.13e-05 tok/s=12489
[train] step=142970 tokens=2342.4M loss=2.0926 lr=6.13e-05 tok/s=12489
[train] step=142980 tokens=2342.6M loss=1.7471 lr=6.12e-05 tok/s=12489
[train] step=142990 tokens=2342.7M loss=1.9668 lr=6.12e-05 tok/s=12489
[train] step=143000 tokens=2342.9M loss=2.3084 lr=6.12e-05 tok/s=12489
[train] step=143010 tokens=2343.1M loss=2.2847 lr=6.12e-05 tok/s=12489
[train] step=143020 tokens=2343.2M loss=1.9615 lr=6.12e-05 tok/s=12489
[train] step=143030 tokens=2343.4M loss=1.7560 lr=6.12e-05 tok/s=12489
[train] step=143040 tokens=2343.6M loss=1.8866 lr=6.12e-05 tok/s=12489
[train] step=143050 tokens=2343.7M loss=1.9838 lr=6.11e-05 tok/s=12489
[train] step=143060 tokens=2343.9M loss=1.7780 lr=6.11e-05 tok/s=12489
```
