# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 22:56:57 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1187M / 3000M (39.6%) |
| Step | 72430 |
| Latest loss | 2.1942 |
| Avg loss (last 30 logged) | 2.2077 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 16:20:26 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.26 -> 2.69 -> 2.54 -> 2.07 -> 2.21 -> 2.11 -> 2.04 -> 2.04 -> 1.95 -> 2.57 -> 2.10 -> 2.36

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`

## Recent log tail
```
[train] step=72320 tokens=1184.9M loss=2.1004 lr=2.11e-04 tok/s=12486
[train] step=72330 tokens=1185.1M loss=2.0997 lr=2.11e-04 tok/s=12486
[train] step=72340 tokens=1185.2M loss=2.4457 lr=2.11e-04 tok/s=12486
[train] step=72350 tokens=1185.4M loss=2.4334 lr=2.11e-04 tok/s=12486
[train] step=72360 tokens=1185.5M loss=1.9325 lr=2.11e-04 tok/s=12486
[train] step=72370 tokens=1185.7M loss=1.9750 lr=2.11e-04 tok/s=12486
[train] step=72380 tokens=1185.9M loss=2.5539 lr=2.11e-04 tok/s=12486
[train] step=72390 tokens=1186.0M loss=2.3438 lr=2.11e-04 tok/s=12486
[train] step=72400 tokens=1186.2M loss=2.3558 lr=2.11e-04 tok/s=12486
[train] step=72410 tokens=1186.4M loss=2.2183 lr=2.11e-04 tok/s=12486
[train] step=72420 tokens=1186.5M loss=2.0478 lr=2.11e-04 tok/s=12486
[train] step=72430 tokens=1186.7M loss=2.1942 lr=2.11e-04 tok/s=12486
```
