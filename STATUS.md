# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 16:59:40 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1998M / 3000M (66.6%) |
| Step | 121970 |
| Latest loss | 1.8026 |
| Avg loss (last 30 logged) | 2.0744 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 22:16:32 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.74 -> 1.86 -> 2.46 -> 2.33 -> 2.47 -> 2.40 -> 1.99 -> 2.05 -> 1.67 -> 2.02 -> 1.87 -> 1.95

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=121860 tokens=1996.6M loss=2.7955 lr=9.90e-05 tok/s=12490
[train] step=121870 tokens=1996.7M loss=2.0515 lr=9.89e-05 tok/s=12490
[train] step=121880 tokens=1996.9M loss=2.1883 lr=9.89e-05 tok/s=12490
[train] step=121890 tokens=1997.0M loss=2.1958 lr=9.89e-05 tok/s=12490
[train] step=121900 tokens=1997.2M loss=1.9024 lr=9.89e-05 tok/s=12490
[train] step=121910 tokens=1997.4M loss=2.2409 lr=9.89e-05 tok/s=12490
[train] step=121920 tokens=1997.5M loss=1.9764 lr=9.88e-05 tok/s=12490
[train] step=121930 tokens=1997.7M loss=2.1944 lr=9.88e-05 tok/s=12490
[train] step=121940 tokens=1997.9M loss=1.9457 lr=9.88e-05 tok/s=12490
[train] step=121950 tokens=1998.0M loss=1.6459 lr=9.88e-05 tok/s=12490
[train] step=121960 tokens=1998.2M loss=1.9375 lr=9.88e-05 tok/s=12490
[train] step=121970 tokens=1998.4M loss=1.8026 lr=9.87e-05 tok/s=12490
```
