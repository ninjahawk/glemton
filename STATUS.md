# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 13:05:27 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 744M / 3000M (24.8%) |
| Step | 45380 |
| Latest loss | 2.7057 |
| Avg loss (last 30 logged) | 2.3119 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 2:12:45 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.24 -> 2.12 -> 2.58 -> 2.56 -> 2.50 -> 2.52 -> 2.53 -> 2.86 -> 2.66 -> 2.57 -> 2.12 -> 2.26

## Checkpoints on disk
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`

## Recent log tail
```
[train] step=45270 tokens=741.7M loss=2.3438 lr=2.63e-04 tok/s=12483
[train] step=45280 tokens=741.9M loss=2.0942 lr=2.63e-04 tok/s=12483
[train] step=45290 tokens=742.0M loss=2.4340 lr=2.63e-04 tok/s=12483
[train] step=45300 tokens=742.2M loss=2.1581 lr=2.63e-04 tok/s=12483
[train] step=45310 tokens=742.4M loss=2.3478 lr=2.63e-04 tok/s=12483
[train] step=45320 tokens=742.5M loss=2.4103 lr=2.63e-04 tok/s=12483
[train] step=45330 tokens=742.7M loss=2.0034 lr=2.63e-04 tok/s=12483
[train] step=45340 tokens=742.9M loss=2.6864 lr=2.63e-04 tok/s=12483
[train] step=45350 tokens=743.0M loss=2.2973 lr=2.63e-04 tok/s=12483
[train] step=45360 tokens=743.2M loss=2.2570 lr=2.63e-04 tok/s=12483
[train] step=45370 tokens=743.3M loss=2.1595 lr=2.63e-04 tok/s=12483
[train] step=45380 tokens=743.5M loss=2.7057 lr=2.63e-04 tok/s=12483
```
