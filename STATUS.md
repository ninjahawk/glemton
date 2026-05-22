# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 11:55:15 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 691M / 3000M (23.0%) |
| Step | 42170 |
| Latest loss | 2.6040 |
| Avg loss (last 30 logged) | 2.3608 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 3:22:59 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.44 -> 2.21 -> 2.27 -> 2.22 -> 2.39 -> 2.06 -> 2.52 -> 2.05 -> 2.45 -> 2.03 -> 2.27 -> 2.42

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=42060 tokens=689.1M loss=2.1188 lr=2.68e-04 tok/s=12483
[train] step=42070 tokens=689.3M loss=2.5318 lr=2.68e-04 tok/s=12483
[train] step=42080 tokens=689.4M loss=2.0570 lr=2.68e-04 tok/s=12483
[train] step=42090 tokens=689.6M loss=2.5386 lr=2.68e-04 tok/s=12483
[train] step=42100 tokens=689.8M loss=2.1981 lr=2.68e-04 tok/s=12483
[train] step=42110 tokens=689.9M loss=2.3248 lr=2.68e-04 tok/s=12483
[train] step=42120 tokens=690.1M loss=2.3897 lr=2.68e-04 tok/s=12483
[train] step=42130 tokens=690.3M loss=2.2780 lr=2.68e-04 tok/s=12483
[train] step=42140 tokens=690.4M loss=2.4235 lr=2.68e-04 tok/s=12483
[train] step=42150 tokens=690.6M loss=2.1194 lr=2.68e-04 tok/s=12483
[train] step=42160 tokens=690.7M loss=2.3389 lr=2.68e-04 tok/s=12483
[train] step=42170 tokens=690.9M loss=2.6040 lr=2.68e-04 tok/s=12483
```
