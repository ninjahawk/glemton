# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 17:06:03 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 924M / 3000M (30.8%) |
| Step | 56380 |
| Latest loss | 2.4904 |
| Avg loss (last 30 logged) | 2.2868 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 22:11:43 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.04 -> 2.95 -> 2.09 -> 2.10 -> 2.09 -> 2.41 -> 2.46 -> 2.19 -> 2.82 -> 2.25 -> 2.34 -> 1.97

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=56270 tokens=921.9M loss=2.3419 lr=2.44e-04 tok/s=12485
[train] step=56280 tokens=922.1M loss=2.6587 lr=2.44e-04 tok/s=12485
[train] step=56290 tokens=922.3M loss=2.0817 lr=2.44e-04 tok/s=12485
[train] step=56300 tokens=922.4M loss=2.5103 lr=2.44e-04 tok/s=12485
[train] step=56310 tokens=922.6M loss=1.9715 lr=2.44e-04 tok/s=12485
[train] step=56320 tokens=922.7M loss=2.2671 lr=2.44e-04 tok/s=12485
[train] step=56330 tokens=922.9M loss=2.1881 lr=2.44e-04 tok/s=12485
[train] step=56340 tokens=923.1M loss=2.1308 lr=2.44e-04 tok/s=12485
[train] step=56350 tokens=923.2M loss=2.3320 lr=2.44e-04 tok/s=12485
[train] step=56360 tokens=923.4M loss=1.9706 lr=2.44e-04 tok/s=12485
[train] step=56370 tokens=923.6M loss=2.0711 lr=2.44e-04 tok/s=12485
[train] step=56380 tokens=923.7M loss=2.4904 lr=2.44e-04 tok/s=12485
```
