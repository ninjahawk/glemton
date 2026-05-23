# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 05:58:01 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1502M / 3000M (50.1%) |
| Step | 91700 |
| Latest loss | 2.3535 |
| Avg loss (last 30 logged) | 2.2304 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 9:18:43 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.19 -> 1.94 -> 1.99 -> 2.13 -> 1.96 -> 2.09 -> 2.15 -> 2.10 -> 2.52 -> 2.46 -> 1.54 -> 2.14

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=91590 tokens=1500.6M loss=2.2151 lr=1.67e-04 tok/s=12488
[train] step=91600 tokens=1500.8M loss=1.9468 lr=1.67e-04 tok/s=12488
[train] step=91610 tokens=1500.9M loss=2.4489 lr=1.67e-04 tok/s=12488
[train] step=91620 tokens=1501.1M loss=2.1512 lr=1.67e-04 tok/s=12488
[train] step=91630 tokens=1501.3M loss=2.3294 lr=1.67e-04 tok/s=12488
[train] step=91640 tokens=1501.4M loss=2.0946 lr=1.67e-04 tok/s=12488
[train] step=91650 tokens=1501.6M loss=2.6864 lr=1.67e-04 tok/s=12488
[train] step=91660 tokens=1501.8M loss=1.9956 lr=1.67e-04 tok/s=12488
[train] step=91670 tokens=1501.9M loss=2.5793 lr=1.67e-04 tok/s=12488
[train] step=91680 tokens=1502.1M loss=2.1386 lr=1.66e-04 tok/s=12488
[train] step=91690 tokens=1502.2M loss=2.3489 lr=1.66e-04 tok/s=12488
[train] step=91700 tokens=1502.4M loss=2.3535 lr=1.66e-04 tok/s=12488
```
