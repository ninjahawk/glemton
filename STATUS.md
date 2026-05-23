# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 01:37:22 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1307M / 3000M (43.6%) |
| Step | 79770 |
| Latest loss | 2.2075 |
| Avg loss (last 30 logged) | 2.1861 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 13:39:41 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.18 -> 2.39 -> 2.15 -> 2.04 -> 2.22 -> 2.29 -> 2.11 -> 2.54 -> 2.05 -> 2.28 -> 2.04 -> 1.99

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`

## Recent log tail
```
[train] step=79660 tokens=1305.1M loss=1.8836 lr=1.94e-04 tok/s=12487
[train] step=79670 tokens=1305.3M loss=1.9052 lr=1.94e-04 tok/s=12487
[train] step=79680 tokens=1305.5M loss=2.0811 lr=1.94e-04 tok/s=12487
[train] step=79690 tokens=1305.6M loss=2.3925 lr=1.94e-04 tok/s=12487
[train] step=79700 tokens=1305.8M loss=1.7640 lr=1.94e-04 tok/s=12487
[train] step=79710 tokens=1306.0M loss=2.8465 lr=1.94e-04 tok/s=12487
[train] step=79720 tokens=1306.1M loss=1.8799 lr=1.94e-04 tok/s=12487
[train] step=79730 tokens=1306.3M loss=2.3768 lr=1.94e-04 tok/s=12487
[train] step=79740 tokens=1306.5M loss=2.0072 lr=1.94e-04 tok/s=12487
[train] step=79750 tokens=1306.6M loss=1.9900 lr=1.94e-04 tok/s=12487
[train] step=79760 tokens=1306.8M loss=2.0264 lr=1.94e-04 tok/s=12487
[train] step=79770 tokens=1307.0M loss=2.2075 lr=1.94e-04 tok/s=12487
```
