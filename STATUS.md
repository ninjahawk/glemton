# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 00:57:16 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1277M / 3000M (42.6%) |
| Step | 77940 |
| Latest loss | 2.1624 |
| Avg loss (last 30 logged) | 2.1739 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 14:19:43 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.92 -> 2.26 -> 2.39 -> 2.42 -> 2.36 -> 1.80 -> 1.89 -> 2.68 -> 1.98 -> 2.29 -> 2.01 -> 1.89

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] step=77830 tokens=1275.2M loss=2.5422 lr=1.98e-04 tok/s=12486
[train] step=77840 tokens=1275.3M loss=2.0737 lr=1.98e-04 tok/s=12487
[train] step=77850 tokens=1275.5M loss=2.8127 lr=1.98e-04 tok/s=12487
[train] step=77860 tokens=1275.7M loss=1.9752 lr=1.98e-04 tok/s=12487
[train] step=77870 tokens=1275.8M loss=2.3476 lr=1.98e-04 tok/s=12487
[train] step=77880 tokens=1276.0M loss=2.4214 lr=1.98e-04 tok/s=12487
[train] step=77890 tokens=1276.1M loss=2.4597 lr=1.98e-04 tok/s=12487
[train] step=77900 tokens=1276.3M loss=2.0062 lr=1.98e-04 tok/s=12487
[train] step=77910 tokens=1276.5M loss=1.8943 lr=1.98e-04 tok/s=12487
[train] step=77920 tokens=1276.6M loss=2.0692 lr=1.98e-04 tok/s=12487
[train] step=77930 tokens=1276.8M loss=2.0093 lr=1.98e-04 tok/s=12487
[train] step=77940 tokens=1277.0M loss=2.1624 lr=1.98e-04 tok/s=12487
```
