# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 23:20:38 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2284M / 3000M (76.1%) |
| Step | 139400 |
| Latest loss | 2.2118 |
| Avg loss (last 30 logged) | 2.0611 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 15:55:38 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.60 -> 1.83 -> 2.24 -> 1.95 -> 2.16 -> 1.94 -> 2.26 -> 2.01 -> 2.22 -> 2.40 -> 1.84 -> 2.34

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
[train] step=139290 tokens=2282.1M loss=2.1809 lr=6.70e-05 tok/s=12489
[train] step=139300 tokens=2282.3M loss=1.9896 lr=6.70e-05 tok/s=12489
[train] step=139310 tokens=2282.5M loss=2.2082 lr=6.69e-05 tok/s=12489
[train] step=139320 tokens=2282.6M loss=2.2502 lr=6.69e-05 tok/s=12489
[train] step=139330 tokens=2282.8M loss=1.7420 lr=6.69e-05 tok/s=12489
[train] step=139340 tokens=2282.9M loss=1.7228 lr=6.69e-05 tok/s=12489
[train] step=139350 tokens=2283.1M loss=2.4017 lr=6.69e-05 tok/s=12489
[train] step=139360 tokens=2283.3M loss=1.9394 lr=6.69e-05 tok/s=12489
[train] step=139370 tokens=2283.4M loss=2.3401 lr=6.68e-05 tok/s=12489
[train] step=139380 tokens=2283.6M loss=2.2614 lr=6.68e-05 tok/s=12489
[train] step=139390 tokens=2283.8M loss=1.8124 lr=6.68e-05 tok/s=12489
[train] step=139400 tokens=2283.9M loss=2.2118 lr=6.68e-05 tok/s=12489
```
