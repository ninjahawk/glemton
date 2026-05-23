# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 05:27:57 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1480M / 3000M (49.3%) |
| Step | 90320 |
| Latest loss | 2.1898 |
| Avg loss (last 30 logged) | 2.0514 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 9:48:52 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.76 -> 1.72 -> 2.04 -> 1.96 -> 1.84 -> 2.01 -> 2.26 -> 1.87 -> 2.32 -> 2.23 -> 2.34 -> 2.21

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`

## Recent log tail
```
[train] step=90210 tokens=1478.0M loss=1.8839 lr=1.70e-04 tok/s=12488
[train] step=90220 tokens=1478.2M loss=2.4703 lr=1.70e-04 tok/s=12488
[train] step=90230 tokens=1478.3M loss=2.2281 lr=1.70e-04 tok/s=12488
[train] step=90240 tokens=1478.5M loss=2.0873 lr=1.70e-04 tok/s=12488
[train] step=90250 tokens=1478.7M loss=2.0108 lr=1.70e-04 tok/s=12488
[train] step=90260 tokens=1478.8M loss=2.0028 lr=1.70e-04 tok/s=12488
[train] step=90270 tokens=1479.0M loss=1.8310 lr=1.70e-04 tok/s=12488
[train] step=90280 tokens=1479.1M loss=1.6904 lr=1.70e-04 tok/s=12488
[train] step=90290 tokens=1479.3M loss=2.2056 lr=1.70e-04 tok/s=12488
[train] step=90300 tokens=1479.5M loss=2.3440 lr=1.70e-04 tok/s=12488
[train] step=90310 tokens=1479.6M loss=2.1279 lr=1.70e-04 tok/s=12488
[train] step=90320 tokens=1479.8M loss=2.1898 lr=1.70e-04 tok/s=12488
```
