# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 08:22:02 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2689M / 3000M (89.6%) |
| Step | 164150 |
| Latest loss | 2.3424 |
| Avg loss (last 30 logged) | 2.0516 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 6:54:29 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.02 -> 2.51 -> 1.96 -> 2.07 -> 2.11 -> 1.93 -> 1.82 -> 2.02 -> 1.82 -> 2.11 -> 2.09 -> 2.35

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=164040 tokens=2687.6M loss=2.3660 lr=3.73e-05 tok/s=12489
[train] step=164050 tokens=2687.8M loss=2.2550 lr=3.73e-05 tok/s=12489
[train] step=164060 tokens=2688.0M loss=1.5737 lr=3.73e-05 tok/s=12489
[train] step=164070 tokens=2688.1M loss=1.9319 lr=3.73e-05 tok/s=12489
[train] step=164080 tokens=2688.3M loss=1.7626 lr=3.72e-05 tok/s=12489
[train] step=164090 tokens=2688.5M loss=2.0903 lr=3.72e-05 tok/s=12489
[train] step=164100 tokens=2688.6M loss=2.2174 lr=3.72e-05 tok/s=12489
[train] step=164110 tokens=2688.8M loss=1.9918 lr=3.72e-05 tok/s=12489
[train] step=164120 tokens=2688.9M loss=2.3465 lr=3.72e-05 tok/s=12489
[train] step=164130 tokens=2689.1M loss=1.8398 lr=3.72e-05 tok/s=12489
[train] step=164140 tokens=2689.3M loss=2.0985 lr=3.72e-05 tok/s=12489
[train] step=164150 tokens=2689.4M loss=2.3424 lr=3.72e-05 tok/s=12489
```
