# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 15:59:30 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1953M / 3000M (65.1%) |
| Step | 119220 |
| Latest loss | 1.9025 |
| Avg loss (last 30 logged) | 2.1371 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 23:16:49 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.88 -> 1.85 -> 1.95 -> 2.05 -> 1.99 -> 2.18 -> 1.83 -> 1.60 -> 1.60 -> 1.98 -> 1.93 -> 2.07

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
[train] step=119110 tokens=1951.5M loss=2.0157 lr=1.05e-04 tok/s=12489
[train] step=119120 tokens=1951.7M loss=2.3655 lr=1.05e-04 tok/s=12489
[train] step=119130 tokens=1951.8M loss=1.8397 lr=1.05e-04 tok/s=12489
[train] step=119140 tokens=1952.0M loss=2.2735 lr=1.05e-04 tok/s=12489
[train] step=119150 tokens=1952.2M loss=2.1955 lr=1.05e-04 tok/s=12489
[train] step=119160 tokens=1952.3M loss=2.1261 lr=1.05e-04 tok/s=12489
[train] step=119170 tokens=1952.5M loss=2.1316 lr=1.05e-04 tok/s=12489
[train] step=119180 tokens=1952.6M loss=2.8339 lr=1.04e-04 tok/s=12489
[train] step=119190 tokens=1952.8M loss=2.1190 lr=1.04e-04 tok/s=12489
[train] step=119200 tokens=1953.0M loss=2.0698 lr=1.04e-04 tok/s=12489
[train] step=119210 tokens=1953.1M loss=2.1069 lr=1.04e-04 tok/s=12489
[train] step=119220 tokens=1953.3M loss=1.9025 lr=1.04e-04 tok/s=12489
```
