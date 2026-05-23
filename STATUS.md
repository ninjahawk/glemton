# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 17:19:43 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2013M / 3000M (67.1%) |
| Step | 122890 |
| Latest loss | 1.8677 |
| Avg loss (last 30 logged) | 2.1309 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 21:56:37 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.82 -> 2.42 -> 2.38 -> 1.91 -> 1.77 -> 2.66 -> 2.33 -> 1.89 -> 2.19 -> 2.10 -> 2.08 -> 2.07

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=122780 tokens=2011.6M loss=2.0732 lr=9.71e-05 tok/s=12489
[train] step=122790 tokens=2011.8M loss=2.0545 lr=9.71e-05 tok/s=12489
[train] step=122800 tokens=2012.0M loss=1.9838 lr=9.71e-05 tok/s=12489
[train] step=122810 tokens=2012.1M loss=2.1184 lr=9.70e-05 tok/s=12489
[train] step=122820 tokens=2012.3M loss=2.4898 lr=9.70e-05 tok/s=12489
[train] step=122830 tokens=2012.4M loss=2.2230 lr=9.70e-05 tok/s=12489
[train] step=122840 tokens=2012.6M loss=2.3516 lr=9.70e-05 tok/s=12489
[train] step=122850 tokens=2012.8M loss=1.8106 lr=9.70e-05 tok/s=12489
[train] step=122860 tokens=2012.9M loss=2.3914 lr=9.69e-05 tok/s=12489
[train] step=122870 tokens=2013.1M loss=2.0740 lr=9.69e-05 tok/s=12489
[train] step=122880 tokens=2013.3M loss=2.0632 lr=9.69e-05 tok/s=12489
[train] step=122890 tokens=2013.4M loss=1.8677 lr=9.69e-05 tok/s=12489
```
