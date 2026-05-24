# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 23:00:35 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2269M / 3000M (75.6%) |
| Step | 138480 |
| Latest loss | 2.6038 |
| Avg loss (last 30 logged) | 2.1068 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 16:15:39 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.47 -> 2.22 -> 2.04 -> 1.98 -> 2.40 -> 1.84 -> 2.05 -> 2.11 -> 2.20 -> 2.52 -> 2.16 -> 2.04

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
[train] step=138370 tokens=2267.1M loss=2.0012 lr=6.85e-05 tok/s=12489
[train] step=138380 tokens=2267.2M loss=2.2217 lr=6.84e-05 tok/s=12489
[train] step=138390 tokens=2267.4M loss=2.1113 lr=6.84e-05 tok/s=12489
[train] step=138400 tokens=2267.5M loss=2.0643 lr=6.84e-05 tok/s=12489
[train] step=138410 tokens=2267.7M loss=1.8914 lr=6.84e-05 tok/s=12489
[train] step=138420 tokens=2267.9M loss=2.0166 lr=6.84e-05 tok/s=12489
[train] step=138430 tokens=2268.0M loss=2.0134 lr=6.84e-05 tok/s=12489
[train] step=138440 tokens=2268.2M loss=1.7299 lr=6.83e-05 tok/s=12489
[train] step=138450 tokens=2268.4M loss=2.0413 lr=6.83e-05 tok/s=12489
[train] step=138460 tokens=2268.5M loss=2.3271 lr=6.83e-05 tok/s=12489
[train] step=138470 tokens=2268.7M loss=1.5038 lr=6.83e-05 tok/s=12489
[train] step=138480 tokens=2268.9M loss=2.6038 lr=6.83e-05 tok/s=12489
```
