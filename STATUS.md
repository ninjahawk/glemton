# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 15:29:26 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1931M / 3000M (64.4%) |
| Step | 117840 |
| Latest loss | 2.2937 |
| Avg loss (last 30 logged) | 2.0913 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 23:46:59 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.39 -> 2.55 -> 2.27 -> 2.32 -> 2.43 -> 2.13 -> 1.93 -> 2.21 -> 2.19 -> 2.54 -> 2.39 -> 1.67

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
[train] step=117730 tokens=1928.9M loss=1.7390 lr=1.08e-04 tok/s=12489
[train] step=117740 tokens=1929.1M loss=1.7225 lr=1.08e-04 tok/s=12489
[train] step=117750 tokens=1929.2M loss=2.1989 lr=1.07e-04 tok/s=12489
[train] step=117760 tokens=1929.4M loss=2.3415 lr=1.07e-04 tok/s=12489
[train] step=117770 tokens=1929.5M loss=2.3736 lr=1.07e-04 tok/s=12489
[train] step=117780 tokens=1929.7M loss=2.2259 lr=1.07e-04 tok/s=12489
[train] step=117790 tokens=1929.9M loss=1.7581 lr=1.07e-04 tok/s=12489
[train] step=117800 tokens=1930.0M loss=2.2180 lr=1.07e-04 tok/s=12489
[train] step=117810 tokens=1930.2M loss=2.4183 lr=1.07e-04 tok/s=12489
[train] step=117820 tokens=1930.4M loss=1.6707 lr=1.07e-04 tok/s=12489
[train] step=117830 tokens=1930.5M loss=1.9535 lr=1.07e-04 tok/s=12489
[train] step=117840 tokens=1930.7M loss=2.2937 lr=1.07e-04 tok/s=12489
```
