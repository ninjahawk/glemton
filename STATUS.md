# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 10:22:20 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2779M / 3000M (92.6%) |
| Step | 169590 |
| Latest loss | 2.0955 |
| Avg loss (last 30 logged) | 2.0813 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 4:55:34 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.15 -> 2.16 -> 1.69 -> 1.98 -> 2.30 -> 2.48 -> 1.95 -> 2.17 -> 1.85 -> 2.56 -> 2.49 -> 2.07

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=169480 tokens=2776.8M loss=1.7285 lr=3.37e-05 tok/s=12484
[train] step=169490 tokens=2776.9M loss=2.0439 lr=3.37e-05 tok/s=12484
[train] step=169500 tokens=2777.1M loss=2.0577 lr=3.37e-05 tok/s=12484
[train] step=169510 tokens=2777.3M loss=2.0841 lr=3.37e-05 tok/s=12484
[train] step=169520 tokens=2777.4M loss=2.1681 lr=3.37e-05 tok/s=12484
[train] step=169530 tokens=2777.6M loss=2.2911 lr=3.37e-05 tok/s=12484
[train] step=169540 tokens=2777.7M loss=2.0270 lr=3.37e-05 tok/s=12484
[train] step=169550 tokens=2777.9M loss=2.0113 lr=3.37e-05 tok/s=12484
[train] step=169560 tokens=2778.1M loss=2.0688 lr=3.37e-05 tok/s=12484
[train] step=169570 tokens=2778.2M loss=1.8246 lr=3.37e-05 tok/s=12484
[train] step=169580 tokens=2778.4M loss=2.3037 lr=3.37e-05 tok/s=12484
[train] step=169590 tokens=2778.6M loss=2.0955 lr=3.37e-05 tok/s=12484
```
