# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 18:46:18 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 999M / 3000M (33.3%) |
| Step | 60970 |
| Latest loss | 2.1270 |
| Avg loss (last 30 logged) | 2.2679 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 20:31:20 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.37 -> 2.35 -> 2.40 -> 2.19 -> 2.04 -> 2.31 -> 2.72 -> 2.48 -> 2.62 -> 2.10 -> 2.38 -> 2.23

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=60860 tokens=997.1M loss=2.0391 lr=2.35e-04 tok/s=12485
[train] step=60870 tokens=997.3M loss=2.6196 lr=2.35e-04 tok/s=12485
[train] step=60880 tokens=997.5M loss=1.9272 lr=2.35e-04 tok/s=12485
[train] step=60890 tokens=997.6M loss=2.2025 lr=2.35e-04 tok/s=12485
[train] step=60900 tokens=997.8M loss=2.4500 lr=2.35e-04 tok/s=12485
[train] step=60910 tokens=997.9M loss=2.0818 lr=2.35e-04 tok/s=12485
[train] step=60920 tokens=998.1M loss=2.3230 lr=2.35e-04 tok/s=12485
[train] step=60930 tokens=998.3M loss=2.5592 lr=2.35e-04 tok/s=12485
[train] step=60940 tokens=998.4M loss=2.2323 lr=2.35e-04 tok/s=12485
[train] step=60950 tokens=998.6M loss=2.0299 lr=2.35e-04 tok/s=12485
[train] step=60960 tokens=998.8M loss=2.0094 lr=2.35e-04 tok/s=12485
[train] step=60970 tokens=998.9M loss=2.1270 lr=2.35e-04 tok/s=12485
```
