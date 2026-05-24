# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 22:50:33 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2261M / 3000M (75.4%) |
| Step | 138020 |
| Latest loss | 2.1345 |
| Avg loss (last 30 logged) | 2.2059 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 16:25:48 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.75 -> 2.13 -> 2.25 -> 2.22 -> 2.07 -> 2.45 -> 2.09 -> 2.21 -> 2.21 -> 2.43 -> 2.40 -> 2.13

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
[train] step=137910 tokens=2259.5M loss=2.3862 lr=6.92e-05 tok/s=12489
[train] step=137920 tokens=2259.7M loss=2.6757 lr=6.92e-05 tok/s=12489
[train] step=137930 tokens=2259.8M loss=2.3765 lr=6.92e-05 tok/s=12489
[train] step=137940 tokens=2260.0M loss=2.0027 lr=6.92e-05 tok/s=12489
[train] step=137950 tokens=2260.2M loss=2.2413 lr=6.91e-05 tok/s=12489
[train] step=137960 tokens=2260.3M loss=2.3050 lr=6.91e-05 tok/s=12489
[train] step=137970 tokens=2260.5M loss=2.2959 lr=6.91e-05 tok/s=12489
[train] step=137980 tokens=2260.7M loss=2.1292 lr=6.91e-05 tok/s=12489
[train] step=137990 tokens=2260.8M loss=2.7270 lr=6.91e-05 tok/s=12489
[train] step=138000 tokens=2261.0M loss=2.1328 lr=6.91e-05 tok/s=12489
[train] step=138010 tokens=2261.2M loss=2.1801 lr=6.90e-05 tok/s=12489
[train] step=138020 tokens=2261.3M loss=2.1345 lr=6.90e-05 tok/s=12489
```
