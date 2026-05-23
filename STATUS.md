# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 16:49:38 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1991M / 3000M (66.4%) |
| Step | 121520 |
| Latest loss | 2.0054 |
| Avg loss (last 30 logged) | 2.1710 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 22:26:24 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.82 -> 2.21 -> 2.28 -> 2.06 -> 2.83 -> 2.21 -> 1.98 -> 2.06 -> 2.19 -> 2.01 -> 2.17 -> 2.47

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=121410 tokens=1989.2M loss=2.2916 lr=9.99e-05 tok/s=12490
[train] step=121420 tokens=1989.3M loss=2.4687 lr=9.99e-05 tok/s=12490
[train] step=121430 tokens=1989.5M loss=1.5857 lr=9.98e-05 tok/s=12490
[train] step=121440 tokens=1989.7M loss=2.3045 lr=9.98e-05 tok/s=12490
[train] step=121450 tokens=1989.8M loss=2.0785 lr=9.98e-05 tok/s=12490
[train] step=121460 tokens=1990.0M loss=2.3380 lr=9.98e-05 tok/s=12490
[train] step=121470 tokens=1990.2M loss=2.4619 lr=9.98e-05 tok/s=12490
[train] step=121480 tokens=1990.3M loss=2.8225 lr=9.97e-05 tok/s=12490
[train] step=121490 tokens=1990.5M loss=2.4736 lr=9.97e-05 tok/s=12490
[train] step=121500 tokens=1990.7M loss=1.9641 lr=9.97e-05 tok/s=12490
[train] step=121510 tokens=1990.8M loss=1.5722 lr=9.97e-05 tok/s=12490
[train] step=121520 tokens=1991.0M loss=2.0054 lr=9.97e-05 tok/s=12490
```
