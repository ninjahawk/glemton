# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 09:02:08 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2719M / 3000M (90.6%) |
| Step | 165980 |
| Latest loss | 2.1524 |
| Avg loss (last 30 logged) | 2.0102 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 6:14:27 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.90 -> 2.29 -> 1.97 -> 2.48 -> 1.83 -> 1.43 -> 1.98 -> 2.19 -> 1.96 -> 2.13 -> 1.61 -> 2.27

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
[train] step=165870 tokens=2717.6M loss=1.5725 lr=3.60e-05 tok/s=12489
[train] step=165880 tokens=2717.8M loss=1.8732 lr=3.60e-05 tok/s=12489
[train] step=165890 tokens=2717.9M loss=1.7096 lr=3.59e-05 tok/s=12489
[train] step=165900 tokens=2718.1M loss=2.1467 lr=3.59e-05 tok/s=12489
[train] step=165910 tokens=2718.3M loss=2.3373 lr=3.59e-05 tok/s=12489
[train] step=165920 tokens=2718.4M loss=1.9229 lr=3.59e-05 tok/s=12489
[train] step=165930 tokens=2718.6M loss=2.1470 lr=3.59e-05 tok/s=12489
[train] step=165940 tokens=2718.8M loss=2.0074 lr=3.59e-05 tok/s=12489
[train] step=165950 tokens=2718.9M loss=1.9159 lr=3.59e-05 tok/s=12489
[train] step=165960 tokens=2719.1M loss=2.2747 lr=3.59e-05 tok/s=12489
[train] step=165970 tokens=2719.3M loss=2.2369 lr=3.59e-05 tok/s=12489
[train] step=165980 tokens=2719.4M loss=2.1524 lr=3.59e-05 tok/s=12489
```
