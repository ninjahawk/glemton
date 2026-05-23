# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 14:59:21 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1908M / 3000M (63.6%) |
| Step | 116470 |
| Latest loss | 1.9665 |
| Avg loss (last 30 logged) | 2.0589 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 1 day, 0:17:00 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.00 -> 1.84 -> 2.29 -> 2.27 -> 2.10 -> 2.34 -> 2.28 -> 2.32 -> 1.99 -> 2.14 -> 1.52 -> 2.25

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
[train] step=116360 tokens=1906.4M loss=1.5527 lr=1.10e-04 tok/s=12489
[train] step=116370 tokens=1906.6M loss=1.9768 lr=1.10e-04 tok/s=12489
[train] step=116380 tokens=1906.8M loss=1.7154 lr=1.10e-04 tok/s=12489
[train] step=116390 tokens=1906.9M loss=2.0025 lr=1.10e-04 tok/s=12489
[train] step=116400 tokens=1907.1M loss=2.1446 lr=1.10e-04 tok/s=12489
[train] step=116410 tokens=1907.3M loss=2.3289 lr=1.10e-04 tok/s=12489
[train] step=116420 tokens=1907.4M loss=1.5021 lr=1.10e-04 tok/s=12489
[train] step=116430 tokens=1907.6M loss=2.1748 lr=1.10e-04 tok/s=12489
[train] step=116440 tokens=1907.8M loss=2.2053 lr=1.10e-04 tok/s=12489
[train] step=116450 tokens=1907.9M loss=2.2489 lr=1.10e-04 tok/s=12489
[train] step=116460 tokens=1908.1M loss=2.3867 lr=1.10e-04 tok/s=12489
[train] step=116470 tokens=1908.2M loss=1.9665 lr=1.10e-04 tok/s=12489
```
