# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 17:09:41 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2006M / 3000M (66.9%) |
| Step | 122430 |
| Latest loss | 2.1722 |
| Avg loss (last 30 logged) | 2.1814 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 22:06:38 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.21 -> 2.02 -> 1.96 -> 1.90 -> 2.25 -> 1.79 -> 2.15 -> 1.91 -> 2.47 -> 2.00 -> 1.90 -> 2.21

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=122320 tokens=2004.1M loss=2.1228 lr=9.80e-05 tok/s=12489
[train] step=122330 tokens=2004.3M loss=2.4160 lr=9.80e-05 tok/s=12489
[train] step=122340 tokens=2004.4M loss=2.5322 lr=9.80e-05 tok/s=12489
[train] step=122350 tokens=2004.6M loss=2.6905 lr=9.80e-05 tok/s=12489
[train] step=122360 tokens=2004.7M loss=2.1890 lr=9.79e-05 tok/s=12489
[train] step=122370 tokens=2004.9M loss=1.9802 lr=9.79e-05 tok/s=12489
[train] step=122380 tokens=2005.1M loss=1.8804 lr=9.79e-05 tok/s=12489
[train] step=122390 tokens=2005.2M loss=1.5208 lr=9.79e-05 tok/s=12489
[train] step=122400 tokens=2005.4M loss=2.1111 lr=9.79e-05 tok/s=12489
[train] step=122410 tokens=2005.6M loss=2.2099 lr=9.78e-05 tok/s=12489
[train] step=122420 tokens=2005.7M loss=2.1475 lr=9.78e-05 tok/s=12489
[train] step=122430 tokens=2005.9M loss=2.1722 lr=9.78e-05 tok/s=12489
```
