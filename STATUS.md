# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-21 23:23:09 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 128M / 3000M (4.3%) |
| Step | 7790 |
| Latest loss | 2.5878 |
| Avg loss (last 30 logged) | 2.6797 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 2 days, 15:53:32 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.92 -> 2.56 -> 2.57 -> 2.82 -> 2.61 -> 2.76 -> 2.42 -> 2.72 -> 2.81 -> 2.44 -> 2.76 -> 2.71

## Checkpoints on disk
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=7680 tokens=125.8M loss=2.8048 lr=2.99e-04 tok/s=12488
[train] step=7690 tokens=126.0M loss=2.3842 lr=2.99e-04 tok/s=12488
[train] step=7700 tokens=126.2M loss=2.3586 lr=2.99e-04 tok/s=12488
[train] step=7710 tokens=126.3M loss=2.8993 lr=2.99e-04 tok/s=12488
[train] step=7720 tokens=126.5M loss=2.4671 lr=2.99e-04 tok/s=12488
[train] step=7730 tokens=126.6M loss=2.5325 lr=2.99e-04 tok/s=12488
[train] step=7740 tokens=126.8M loss=2.6821 lr=2.99e-04 tok/s=12488
[train] step=7750 tokens=127.0M loss=2.8354 lr=2.99e-04 tok/s=12488
[train] step=7760 tokens=127.1M loss=2.6241 lr=2.99e-04 tok/s=12488
[train] step=7770 tokens=127.3M loss=2.7122 lr=2.99e-04 tok/s=12488
[train] step=7780 tokens=127.5M loss=2.7288 lr=2.99e-04 tok/s=12488
[train] step=7790 tokens=127.6M loss=2.5878 lr=2.99e-04 tok/s=12488
```
