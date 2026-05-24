# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 03:01:11 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2449M / 3000M (81.6%) |
| Step | 149480 |
| Latest loss | 2.0194 |
| Avg loss (last 30 logged) | 2.0456 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 12:15:10 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.66 -> 2.40 -> 2.36 -> 2.03 -> 1.69 -> 2.15 -> 2.35 -> 2.22 -> 1.78 -> 1.75 -> 2.36 -> 2.05

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
[train] step=149370 tokens=2447.3M loss=1.9299 lr=5.24e-05 tok/s=12489
[train] step=149380 tokens=2447.4M loss=2.1330 lr=5.23e-05 tok/s=12489
[train] step=149390 tokens=2447.6M loss=2.3645 lr=5.23e-05 tok/s=12489
[train] step=149400 tokens=2447.8M loss=2.4986 lr=5.23e-05 tok/s=12489
[train] step=149410 tokens=2447.9M loss=1.6853 lr=5.23e-05 tok/s=12489
[train] step=149420 tokens=2448.1M loss=1.8031 lr=5.23e-05 tok/s=12489
[train] step=149430 tokens=2448.3M loss=1.9119 lr=5.23e-05 tok/s=12489
[train] step=149440 tokens=2448.4M loss=1.9727 lr=5.23e-05 tok/s=12489
[train] step=149450 tokens=2448.6M loss=2.2553 lr=5.22e-05 tok/s=12489
[train] step=149460 tokens=2448.8M loss=2.0517 lr=5.22e-05 tok/s=12489
[train] step=149470 tokens=2448.9M loss=2.1708 lr=5.22e-05 tok/s=12489
[train] step=149480 tokens=2449.1M loss=2.0194 lr=5.22e-05 tok/s=12489
```
