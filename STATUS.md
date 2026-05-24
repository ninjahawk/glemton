# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 04:51:29 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2532M / 3000M (84.4%) |
| Step | 154520 |
| Latest loss | 2.4775 |
| Avg loss (last 30 logged) | 1.9677 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 10:24:56 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.32 -> 2.20 -> 1.88 -> 2.08 -> 1.91 -> 2.29 -> 1.98 -> 2.55 -> 1.92 -> 1.85 -> 2.18 -> 2.10

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=154410 tokens=2529.9M loss=2.2539 lr=4.63e-05 tok/s=12489
[train] step=154420 tokens=2530.0M loss=1.7387 lr=4.63e-05 tok/s=12489
[train] step=154430 tokens=2530.2M loss=1.9561 lr=4.63e-05 tok/s=12489
[train] step=154440 tokens=2530.3M loss=2.2348 lr=4.63e-05 tok/s=12489
[train] step=154450 tokens=2530.5M loss=1.4212 lr=4.63e-05 tok/s=12489
[train] step=154460 tokens=2530.7M loss=1.7119 lr=4.62e-05 tok/s=12489
[train] step=154470 tokens=2530.8M loss=1.4296 lr=4.62e-05 tok/s=12489
[train] step=154480 tokens=2531.0M loss=2.2841 lr=4.62e-05 tok/s=12489
[train] step=154490 tokens=2531.2M loss=2.1187 lr=4.62e-05 tok/s=12489
[train] step=154500 tokens=2531.3M loss=2.0964 lr=4.62e-05 tok/s=12489
[train] step=154510 tokens=2531.5M loss=1.8143 lr=4.62e-05 tok/s=12489
[train] step=154520 tokens=2531.7M loss=2.4775 lr=4.62e-05 tok/s=12489
```
