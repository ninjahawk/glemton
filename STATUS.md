# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 02:11:04 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2412M / 3000M (80.4%) |
| Step | 147190 |
| Latest loss | 2.0286 |
| Avg loss (last 30 logged) | 2.0152 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 13:05:13 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.34 -> 1.93 -> 1.93 -> 2.14 -> 2.53 -> 2.21 -> 1.79 -> 2.09 -> 1.94 -> 1.77 -> 1.64 -> 1.69

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=147080 tokens=2409.8M loss=1.8994 lr=5.54e-05 tok/s=12489
[train] step=147090 tokens=2409.9M loss=2.4240 lr=5.54e-05 tok/s=12489
[train] step=147100 tokens=2410.1M loss=2.3217 lr=5.54e-05 tok/s=12489
[train] step=147110 tokens=2410.3M loss=2.0926 lr=5.53e-05 tok/s=12489
[train] step=147120 tokens=2410.4M loss=1.6984 lr=5.53e-05 tok/s=12489
[train] step=147130 tokens=2410.6M loss=2.0450 lr=5.53e-05 tok/s=12489
[train] step=147140 tokens=2410.7M loss=1.9514 lr=5.53e-05 tok/s=12489
[train] step=147150 tokens=2410.9M loss=1.6926 lr=5.53e-05 tok/s=12489
[train] step=147160 tokens=2411.1M loss=2.3968 lr=5.53e-05 tok/s=12489
[train] step=147170 tokens=2411.2M loss=1.6943 lr=5.53e-05 tok/s=12489
[train] step=147180 tokens=2411.4M loss=1.5364 lr=5.52e-05 tok/s=12489
[train] step=147190 tokens=2411.6M loss=2.0286 lr=5.52e-05 tok/s=12489
```
