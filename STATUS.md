# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 10:45:02 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 638M / 3000M (21.3%) |
| Step | 38960 |
| Latest loss | 2.6542 |
| Avg loss (last 30 logged) | 2.4101 |
| Throughput | 12,483 tok/s |
| ETA to 3B tokens | 2 days, 4:33:13 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.72 -> 2.56 -> 2.61 -> 2.28 -> 2.29 -> 2.46 -> 2.24 -> 2.50 -> 2.59 -> 2.55 -> 2.17 -> 2.11

## Checkpoints on disk
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`

## Recent log tail
```
[train] step=38850 tokens=636.5M loss=2.8307 lr=2.73e-04 tok/s=12483
[train] step=38860 tokens=636.7M loss=2.3366 lr=2.73e-04 tok/s=12483
[train] step=38870 tokens=636.8M loss=2.3545 lr=2.73e-04 tok/s=12483
[train] step=38880 tokens=637.0M loss=2.4923 lr=2.73e-04 tok/s=12483
[train] step=38890 tokens=637.2M loss=2.3778 lr=2.73e-04 tok/s=12483
[train] step=38900 tokens=637.3M loss=2.0895 lr=2.73e-04 tok/s=12483
[train] step=38910 tokens=637.5M loss=2.6184 lr=2.73e-04 tok/s=12483
[train] step=38920 tokens=637.7M loss=2.3701 lr=2.73e-04 tok/s=12483
[train] step=38930 tokens=637.8M loss=2.3029 lr=2.73e-04 tok/s=12483
[train] step=38940 tokens=638.0M loss=2.1144 lr=2.73e-04 tok/s=12483
[train] step=38950 tokens=638.2M loss=2.0527 lr=2.73e-04 tok/s=12483
[train] step=38960 tokens=638.3M loss=2.6542 lr=2.73e-04 tok/s=12483
```
