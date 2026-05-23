# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 21:26:44 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1119M / 3000M (37.3%) |
| Step | 68300 |
| Latest loss | 2.1101 |
| Avg loss (last 30 logged) | 2.1619 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 17:50:48 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.08 -> 2.11 -> 2.15 -> 2.52 -> 2.26 -> 2.37 -> 2.39 -> 3.05 -> 2.79 -> 2.39 -> 2.24 -> 2.05

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`

## Recent log tail
```
[train] step=68190 tokens=1117.2M loss=2.1522 lr=2.20e-04 tok/s=12486
[train] step=68200 tokens=1117.4M loss=2.8275 lr=2.20e-04 tok/s=12486
[train] step=68210 tokens=1117.6M loss=2.1002 lr=2.20e-04 tok/s=12486
[train] step=68220 tokens=1117.7M loss=2.2672 lr=2.20e-04 tok/s=12486
[train] step=68230 tokens=1117.9M loss=2.2738 lr=2.20e-04 tok/s=12486
[train] step=68240 tokens=1118.0M loss=2.3501 lr=2.20e-04 tok/s=12486
[train] step=68250 tokens=1118.2M loss=2.1962 lr=2.20e-04 tok/s=12486
[train] step=68260 tokens=1118.4M loss=2.2141 lr=2.20e-04 tok/s=12486
[train] step=68270 tokens=1118.5M loss=2.3674 lr=2.20e-04 tok/s=12486
[train] step=68280 tokens=1118.7M loss=2.0504 lr=2.20e-04 tok/s=12486
[train] step=68290 tokens=1118.9M loss=1.9518 lr=2.20e-04 tok/s=12486
[train] step=68300 tokens=1119.0M loss=2.1101 lr=2.19e-04 tok/s=12486
```
