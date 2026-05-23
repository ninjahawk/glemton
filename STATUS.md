# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 00:37:13 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1262M / 3000M (42.1%) |
| Step | 77020 |
| Latest loss | 2.4017 |
| Avg loss (last 30 logged) | 2.1814 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 14:40:03 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.85 -> 2.04 -> 2.48 -> 2.41 -> 2.25 -> 1.88 -> 1.67 -> 2.44 -> 2.24 -> 2.23 -> 2.54 -> 2.20

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] step=76910 tokens=1260.1M loss=2.0059 lr=2.01e-04 tok/s=12486
[train] step=76920 tokens=1260.3M loss=1.9751 lr=2.01e-04 tok/s=12486
[train] step=76930 tokens=1260.4M loss=2.1054 lr=2.01e-04 tok/s=12486
[train] step=76940 tokens=1260.6M loss=2.2779 lr=2.00e-04 tok/s=12486
[train] step=76950 tokens=1260.7M loss=2.1502 lr=2.00e-04 tok/s=12486
[train] step=76960 tokens=1260.9M loss=1.8323 lr=2.00e-04 tok/s=12486
[train] step=76970 tokens=1261.1M loss=2.4582 lr=2.00e-04 tok/s=12486
[train] step=76980 tokens=1261.2M loss=2.2908 lr=2.00e-04 tok/s=12486
[train] step=76990 tokens=1261.4M loss=2.1929 lr=2.00e-04 tok/s=12486
[train] step=77000 tokens=1261.6M loss=2.2005 lr=2.00e-04 tok/s=12486
[train] step=77010 tokens=1261.7M loss=2.3355 lr=2.00e-04 tok/s=12486
[train] step=77020 tokens=1261.9M loss=2.4017 lr=2.00e-04 tok/s=12486
```
