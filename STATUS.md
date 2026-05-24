# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 22:40:32 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2254M / 3000M (75.1%) |
| Step | 137560 |
| Latest loss | 1.6146 |
| Avg loss (last 30 logged) | 2.0687 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 16:35:48 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.27 -> 1.82 -> 1.50 -> 2.35 -> 2.00 -> 2.04 -> 1.75 -> 2.23 -> 1.88 -> 2.46 -> 2.01 -> 2.02

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
[train] step=137450 tokens=2252.0M loss=2.0647 lr=7.00e-05 tok/s=12489
[train] step=137460 tokens=2252.1M loss=2.1998 lr=7.00e-05 tok/s=12489
[train] step=137470 tokens=2252.3M loss=1.8966 lr=6.99e-05 tok/s=12489
[train] step=137480 tokens=2252.5M loss=2.0290 lr=6.99e-05 tok/s=12489
[train] step=137490 tokens=2252.6M loss=2.6106 lr=6.99e-05 tok/s=12489
[train] step=137500 tokens=2252.8M loss=2.5182 lr=6.99e-05 tok/s=12489
[train] step=137510 tokens=2253.0M loss=2.0499 lr=6.99e-05 tok/s=12489
[train] step=137520 tokens=2253.1M loss=2.2129 lr=6.99e-05 tok/s=12489
[train] step=137530 tokens=2253.3M loss=1.9905 lr=6.98e-05 tok/s=12489
[train] step=137540 tokens=2253.5M loss=2.0178 lr=6.98e-05 tok/s=12489
[train] step=137550 tokens=2253.6M loss=2.0244 lr=6.98e-05 tok/s=12489
[train] step=137560 tokens=2253.8M loss=1.6146 lr=6.98e-05 tok/s=12489
```
