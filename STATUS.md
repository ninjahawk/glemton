# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 05:51:39 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2577M / 3000M (85.9%) |
| Step | 157270 |
| Latest loss | 2.1280 |
| Avg loss (last 30 logged) | 2.0566 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 9:24:53 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.39 -> 2.06 -> 1.76 -> 1.99 -> 2.13 -> 2.58 -> 2.26 -> 2.46 -> 2.09 -> 2.31 -> 2.37 -> 2.30

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
[train] step=157160 tokens=2574.9M loss=1.7892 lr=4.34e-05 tok/s=12489
[train] step=157170 tokens=2575.1M loss=1.8655 lr=4.34e-05 tok/s=12489
[train] step=157180 tokens=2575.2M loss=2.2001 lr=4.34e-05 tok/s=12489
[train] step=157190 tokens=2575.4M loss=2.0940 lr=4.33e-05 tok/s=12489
[train] step=157200 tokens=2575.6M loss=2.6232 lr=4.33e-05 tok/s=12489
[train] step=157210 tokens=2575.7M loss=1.7748 lr=4.33e-05 tok/s=12489
[train] step=157220 tokens=2575.9M loss=2.1032 lr=4.33e-05 tok/s=12489
[train] step=157230 tokens=2576.1M loss=1.7916 lr=4.33e-05 tok/s=12489
[train] step=157240 tokens=2576.2M loss=2.2981 lr=4.33e-05 tok/s=12489
[train] step=157250 tokens=2576.4M loss=2.0957 lr=4.33e-05 tok/s=12489
[train] step=157260 tokens=2576.5M loss=2.2144 lr=4.33e-05 tok/s=12489
[train] step=157270 tokens=2576.7M loss=2.1280 lr=4.33e-05 tok/s=12489
```
