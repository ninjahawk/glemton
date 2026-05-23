# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 18:39:55 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2074M / 3000M (69.1%) |
| Step | 126560 |
| Latest loss | 2.4128 |
| Avg loss (last 30 logged) | 2.0053 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 20:36:11 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.46 -> 2.06 -> 2.07 -> 2.07 -> 2.91 -> 1.90 -> 2.32 -> 1.77 -> 2.17 -> 2.10 -> 2.74 -> 1.98

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
[train] step=126450 tokens=2071.8M loss=2.1777 lr=8.98e-05 tok/s=12490
[train] step=126460 tokens=2071.9M loss=2.1573 lr=8.98e-05 tok/s=12490
[train] step=126470 tokens=2072.1M loss=2.1190 lr=8.98e-05 tok/s=12490
[train] step=126480 tokens=2072.2M loss=1.8038 lr=8.98e-05 tok/s=12490
[train] step=126490 tokens=2072.4M loss=1.9080 lr=8.97e-05 tok/s=12490
[train] step=126500 tokens=2072.6M loss=1.8746 lr=8.97e-05 tok/s=12490
[train] step=126510 tokens=2072.7M loss=1.9932 lr=8.97e-05 tok/s=12490
[train] step=126520 tokens=2072.9M loss=2.0545 lr=8.97e-05 tok/s=12490
[train] step=126530 tokens=2073.1M loss=1.9823 lr=8.97e-05 tok/s=12490
[train] step=126540 tokens=2073.2M loss=1.8259 lr=8.97e-05 tok/s=12490
[train] step=126550 tokens=2073.4M loss=1.6554 lr=8.96e-05 tok/s=12490
[train] step=126560 tokens=2073.6M loss=2.4128 lr=8.96e-05 tok/s=12490
```
