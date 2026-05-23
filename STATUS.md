# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 14:49:20 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1901M / 3000M (63.4%) |
| Step | 116010 |
| Latest loss | 2.1210 |
| Avg loss (last 30 logged) | 2.0717 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 1 day, 0:27:01 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.15 -> 2.28 -> 2.00 -> 1.77 -> 1.65 -> 1.59 -> 2.15 -> 1.96 -> 2.02 -> 1.80 -> 2.59 -> 2.02

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
[train] step=115910 tokens=1899.1M loss=2.0353 lr=1.11e-04 tok/s=12489
[train] step=115920 tokens=1899.2M loss=2.1338 lr=1.11e-04 tok/s=12489
[train] step=115930 tokens=1899.4M loss=2.0643 lr=1.11e-04 tok/s=12489
[train] step=115940 tokens=1899.6M loss=2.0741 lr=1.11e-04 tok/s=12489
[train] step=115950 tokens=1899.7M loss=1.7581 lr=1.11e-04 tok/s=12489
[train] step=115960 tokens=1899.9M loss=2.0514 lr=1.11e-04 tok/s=12489
[train] checkpoint -> checkpoints\glemton-350m\step_115967_tokens_1900M.pt
[train] step=115970 tokens=1900.1M loss=1.8570 lr=1.11e-04 tok/s=12489
[train] step=115980 tokens=1900.2M loss=2.0586 lr=1.11e-04 tok/s=12489
[train] step=115990 tokens=1900.4M loss=2.0246 lr=1.11e-04 tok/s=12489
[train] step=116000 tokens=1900.5M loss=2.2370 lr=1.11e-04 tok/s=12489
[train] step=116010 tokens=1900.7M loss=2.1210 lr=1.11e-04 tok/s=12489
```
