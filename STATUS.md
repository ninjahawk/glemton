# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 09:12:09 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2727M / 3000M (90.9%) |
| Step | 166440 |
| Latest loss | 2.3185 |
| Avg loss (last 30 logged) | 2.1170 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 6:04:19 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.95 -> 1.68 -> 2.26 -> 2.07 -> 1.99 -> 2.44 -> 2.03 -> 2.28 -> 2.22 -> 1.95 -> 1.76 -> 1.55

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
[train] step=166330 tokens=2725.2M loss=2.4150 lr=3.56e-05 tok/s=12489
[train] step=166340 tokens=2725.3M loss=2.2391 lr=3.56e-05 tok/s=12489
[train] step=166350 tokens=2725.5M loss=2.7305 lr=3.56e-05 tok/s=12489
[train] step=166360 tokens=2725.6M loss=2.3436 lr=3.56e-05 tok/s=12489
[train] step=166370 tokens=2725.8M loss=2.2358 lr=3.56e-05 tok/s=12489
[train] step=166380 tokens=2726.0M loss=1.8396 lr=3.56e-05 tok/s=12489
[train] step=166390 tokens=2726.1M loss=1.9841 lr=3.56e-05 tok/s=12489
[train] step=166400 tokens=2726.3M loss=1.8024 lr=3.56e-05 tok/s=12489
[train] step=166410 tokens=2726.5M loss=2.4432 lr=3.56e-05 tok/s=12489
[train] step=166420 tokens=2726.6M loss=1.5539 lr=3.56e-05 tok/s=12489
[train] step=166430 tokens=2726.8M loss=2.0112 lr=3.56e-05 tok/s=12489
[train] step=166440 tokens=2727.0M loss=2.3185 lr=3.56e-05 tok/s=12489
```
