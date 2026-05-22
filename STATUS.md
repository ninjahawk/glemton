# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 18:06:12 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 969M / 3000M (32.3%) |
| Step | 59130 |
| Latest loss | 2.1302 |
| Avg loss (last 30 logged) | 2.2661 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 21:11:31 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.57 -> 2.30 -> 2.61 -> 2.57 -> 2.53 -> 2.22 -> 2.27 -> 2.60 -> 2.67 -> 2.53 -> 2.53 -> 2.02

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=59020 tokens=967.0M loss=2.1562 lr=2.39e-04 tok/s=12485
[train] step=59030 tokens=967.1M loss=2.2816 lr=2.39e-04 tok/s=12485
[train] step=59040 tokens=967.3M loss=2.4975 lr=2.38e-04 tok/s=12485
[train] step=59050 tokens=967.5M loss=2.1831 lr=2.38e-04 tok/s=12485
[train] step=59060 tokens=967.6M loss=2.0456 lr=2.38e-04 tok/s=12485
[train] step=59070 tokens=967.8M loss=2.9237 lr=2.38e-04 tok/s=12485
[train] step=59080 tokens=968.0M loss=2.0724 lr=2.38e-04 tok/s=12485
[train] step=59090 tokens=968.1M loss=2.1421 lr=2.38e-04 tok/s=12485
[train] step=59100 tokens=968.3M loss=2.0156 lr=2.38e-04 tok/s=12485
[train] step=59110 tokens=968.5M loss=2.1496 lr=2.38e-04 tok/s=12485
[train] step=59120 tokens=968.6M loss=2.3312 lr=2.38e-04 tok/s=12485
[train] step=59130 tokens=968.8M loss=2.1302 lr=2.38e-04 tok/s=12485
```
