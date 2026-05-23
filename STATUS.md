# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 15:09:23 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1916M / 3000M (63.9%) |
| Step | 116930 |
| Latest loss | 2.0987 |
| Avg loss (last 30 logged) | 2.0915 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 1 day, 0:06:52 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.29 -> 2.18 -> 2.31 -> 2.03 -> 2.33 -> 1.87 -> 1.90 -> 2.65 -> 2.13 -> 2.18 -> 1.87 -> 1.67

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
[train] step=116820 tokens=1914.0M loss=2.0979 lr=1.09e-04 tok/s=12489
[train] step=116830 tokens=1914.1M loss=2.1861 lr=1.09e-04 tok/s=12489
[train] step=116840 tokens=1914.3M loss=1.7632 lr=1.09e-04 tok/s=12489
[train] step=116850 tokens=1914.5M loss=1.8537 lr=1.09e-04 tok/s=12489
[train] step=116860 tokens=1914.6M loss=2.1871 lr=1.09e-04 tok/s=12489
[train] step=116870 tokens=1914.8M loss=2.1786 lr=1.09e-04 tok/s=12489
[train] step=116880 tokens=1915.0M loss=2.0732 lr=1.09e-04 tok/s=12489
[train] step=116890 tokens=1915.1M loss=1.9936 lr=1.09e-04 tok/s=12489
[train] step=116900 tokens=1915.3M loss=1.9804 lr=1.09e-04 tok/s=12489
[train] step=116910 tokens=1915.5M loss=1.6701 lr=1.09e-04 tok/s=12489
[train] step=116920 tokens=1915.6M loss=2.2951 lr=1.09e-04 tok/s=12489
[train] step=116930 tokens=1915.8M loss=2.0987 lr=1.09e-04 tok/s=12489
```
