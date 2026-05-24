# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 01:51:01 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2396M / 3000M (79.9%) |
| Step | 146270 |
| Latest loss | 1.6765 |
| Avg loss (last 30 logged) | 2.0913 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 13:25:22 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.93 -> 1.97 -> 2.54 -> 2.27 -> 1.66 -> 1.90 -> 2.08 -> 2.01 -> 2.27 -> 2.05 -> 1.87 -> 2.30

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
[train] step=146160 tokens=2394.7M loss=2.3969 lr=5.67e-05 tok/s=12489
[train] step=146170 tokens=2394.8M loss=2.3053 lr=5.66e-05 tok/s=12489
[train] step=146180 tokens=2395.0M loss=1.9424 lr=5.66e-05 tok/s=12489
[train] step=146190 tokens=2395.2M loss=1.9812 lr=5.66e-05 tok/s=12489
[train] step=146200 tokens=2395.3M loss=1.9885 lr=5.66e-05 tok/s=12489
[train] step=146210 tokens=2395.5M loss=2.0992 lr=5.66e-05 tok/s=12489
[train] step=146220 tokens=2395.7M loss=1.6381 lr=5.66e-05 tok/s=12489
[train] step=146230 tokens=2395.8M loss=2.1634 lr=5.66e-05 tok/s=12489
[train] step=146240 tokens=2396.0M loss=2.2971 lr=5.65e-05 tok/s=12489
[train] step=146250 tokens=2396.2M loss=1.7500 lr=5.65e-05 tok/s=12489
[train] step=146260 tokens=2396.3M loss=2.4888 lr=5.65e-05 tok/s=12489
[train] step=146270 tokens=2396.5M loss=1.6765 lr=5.65e-05 tok/s=12489
```
