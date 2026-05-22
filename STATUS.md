# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 17:46:09 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 954M / 3000M (31.8%) |
| Step | 58220 |
| Latest loss | 2.1706 |
| Avg loss (last 30 logged) | 2.2867 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 21:31:24 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.13 -> 2.09 -> 2.65 -> 2.35 -> 2.21 -> 2.13 -> 2.19 -> 2.08 -> 2.16 -> 2.34 -> 2.40 -> 2.02

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=58110 tokens=952.1M loss=2.6746 lr=2.40e-04 tok/s=12485
[train] step=58120 tokens=952.2M loss=2.9774 lr=2.40e-04 tok/s=12485
[train] step=58130 tokens=952.4M loss=2.1091 lr=2.40e-04 tok/s=12485
[train] step=58140 tokens=952.6M loss=2.6448 lr=2.40e-04 tok/s=12485
[train] step=58150 tokens=952.7M loss=2.0625 lr=2.40e-04 tok/s=12485
[train] step=58160 tokens=952.9M loss=1.9198 lr=2.40e-04 tok/s=12485
[train] step=58170 tokens=953.1M loss=2.1464 lr=2.40e-04 tok/s=12485
[train] step=58180 tokens=953.2M loss=2.3806 lr=2.40e-04 tok/s=12485
[train] step=58190 tokens=953.4M loss=2.1611 lr=2.40e-04 tok/s=12485
[train] step=58200 tokens=953.5M loss=2.0160 lr=2.40e-04 tok/s=12485
[train] step=58210 tokens=953.7M loss=2.2507 lr=2.40e-04 tok/s=12485
[train] step=58220 tokens=953.9M loss=2.1706 lr=2.40e-04 tok/s=12485
```
