# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 00:17:10 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1247M / 3000M (41.6%) |
| Step | 76100 |
| Latest loss | 2.3649 |
| Avg loss (last 30 logged) | 2.1927 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 15:00:13 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.14 -> 1.94 -> 1.87 -> 2.04 -> 2.23 -> 2.08 -> 2.09 -> 2.20 -> 2.61 -> 1.84 -> 1.94 -> 2.12

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] step=75990 tokens=1245.0M loss=2.2904 lr=2.03e-04 tok/s=12486
[train] step=76000 tokens=1245.2M loss=2.2477 lr=2.03e-04 tok/s=12486
[train] step=76010 tokens=1245.3M loss=2.2390 lr=2.03e-04 tok/s=12486
[train] step=76020 tokens=1245.5M loss=1.9465 lr=2.03e-04 tok/s=12486
[train] step=76030 tokens=1245.7M loss=2.0897 lr=2.03e-04 tok/s=12486
[train] step=76040 tokens=1245.8M loss=2.1061 lr=2.03e-04 tok/s=12486
[train] step=76050 tokens=1246.0M loss=2.2545 lr=2.02e-04 tok/s=12486
[train] step=76060 tokens=1246.2M loss=2.1318 lr=2.02e-04 tok/s=12486
[train] step=76070 tokens=1246.3M loss=2.2102 lr=2.02e-04 tok/s=12486
[train] step=76080 tokens=1246.5M loss=2.1177 lr=2.02e-04 tok/s=12486
[train] step=76090 tokens=1246.7M loss=1.9964 lr=2.02e-04 tok/s=12486
[train] step=76100 tokens=1246.8M loss=2.3649 lr=2.02e-04 tok/s=12486
```
