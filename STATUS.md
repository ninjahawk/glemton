# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 23:06:59 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1194M / 3000M (39.8%) |
| Step | 72890 |
| Latest loss | 2.1284 |
| Avg loss (last 30 logged) | 2.1204 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 16:10:25 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.44 -> 1.97 -> 2.22 -> 2.11 -> 2.23 -> 2.12 -> 2.48 -> 2.46 -> 2.04 -> 2.09 -> 2.60 -> 2.07

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`

## Recent log tail
```
[train] step=72780 tokens=1192.4M loss=1.9425 lr=2.10e-04 tok/s=12486
[train] step=72790 tokens=1192.6M loss=2.5112 lr=2.10e-04 tok/s=12486
[train] step=72800 tokens=1192.8M loss=2.4326 lr=2.10e-04 tok/s=12486
[train] step=72810 tokens=1192.9M loss=1.8572 lr=2.10e-04 tok/s=12486
[train] step=72820 tokens=1193.1M loss=2.1687 lr=2.10e-04 tok/s=12486
[train] step=72830 tokens=1193.2M loss=2.4442 lr=2.10e-04 tok/s=12486
[train] step=72840 tokens=1193.4M loss=2.0246 lr=2.10e-04 tok/s=12486
[train] step=72850 tokens=1193.6M loss=2.0824 lr=2.10e-04 tok/s=12486
[train] step=72860 tokens=1193.7M loss=2.0749 lr=2.10e-04 tok/s=12486
[train] step=72870 tokens=1193.9M loss=2.1605 lr=2.10e-04 tok/s=12486
[train] step=72880 tokens=1194.1M loss=1.9701 lr=2.10e-04 tok/s=12486
[train] step=72890 tokens=1194.2M loss=2.1284 lr=2.10e-04 tok/s=12486
```
