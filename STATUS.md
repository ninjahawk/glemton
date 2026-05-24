# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 21:40:22 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2209M / 3000M (73.6%) |
| Step | 134810 |
| Latest loss | 1.7791 |
| Avg loss (last 30 logged) | 1.9957 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 17:35:59 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.17 -> 2.05 -> 2.03 -> 1.89 -> 2.08 -> 2.52 -> 2.23 -> 2.38 -> 2.37 -> 2.10 -> 2.22 -> 2.39

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
[train] step=134700 tokens=2206.9M loss=2.1335 lr=7.46e-05 tok/s=12489
[train] step=134710 tokens=2207.1M loss=2.6494 lr=7.46e-05 tok/s=12489
[train] step=134720 tokens=2207.3M loss=2.4604 lr=7.46e-05 tok/s=12489
[train] step=134730 tokens=2207.4M loss=1.9979 lr=7.46e-05 tok/s=12489
[train] step=134740 tokens=2207.6M loss=2.0018 lr=7.46e-05 tok/s=12489
[train] step=134750 tokens=2207.7M loss=1.7341 lr=7.46e-05 tok/s=12489
[train] step=134760 tokens=2207.9M loss=2.2731 lr=7.45e-05 tok/s=12489
[train] step=134770 tokens=2208.1M loss=2.1076 lr=7.45e-05 tok/s=12489
[train] step=134780 tokens=2208.2M loss=1.9879 lr=7.45e-05 tok/s=12489
[train] step=134790 tokens=2208.4M loss=2.3902 lr=7.45e-05 tok/s=12489
[train] step=134800 tokens=2208.6M loss=1.9224 lr=7.45e-05 tok/s=12489
[train] step=134810 tokens=2208.7M loss=1.7791 lr=7.44e-05 tok/s=12489
```
