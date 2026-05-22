# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 12:55:25 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 736M / 3000M (24.5%) |
| Step | 44920 |
| Latest loss | 2.1246 |
| Avg loss (last 30 logged) | 2.3972 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 2:22:46 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.21 -> 2.49 -> 2.35 -> 2.81 -> 2.47 -> 2.31 -> 2.40 -> 2.14 -> 2.53 -> 2.29 -> 2.34 -> 2.42

## Checkpoints on disk
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`

## Recent log tail
```
[train] step=44810 tokens=734.2M loss=2.8300 lr=2.64e-04 tok/s=12483
[train] step=44820 tokens=734.3M loss=2.1330 lr=2.64e-04 tok/s=12483
[train] step=44830 tokens=734.5M loss=2.6480 lr=2.64e-04 tok/s=12483
[train] step=44840 tokens=734.7M loss=2.4645 lr=2.64e-04 tok/s=12483
[train] step=44850 tokens=734.8M loss=2.1141 lr=2.64e-04 tok/s=12483
[train] step=44860 tokens=735.0M loss=2.2028 lr=2.64e-04 tok/s=12483
[train] step=44870 tokens=735.2M loss=2.3340 lr=2.64e-04 tok/s=12483
[train] step=44880 tokens=735.3M loss=3.0520 lr=2.64e-04 tok/s=12483
[train] step=44890 tokens=735.5M loss=2.2066 lr=2.64e-04 tok/s=12483
[train] step=44900 tokens=735.6M loss=2.4204 lr=2.64e-04 tok/s=12483
[train] step=44910 tokens=735.8M loss=2.3751 lr=2.64e-04 tok/s=12483
[train] step=44920 tokens=736.0M loss=2.1246 lr=2.64e-04 tok/s=12483
```
