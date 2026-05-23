# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 17:39:46 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2028M / 3000M (67.6%) |
| Step | 123810 |
| Latest loss | 2.6155 |
| Avg loss (last 30 logged) | 2.0713 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 21:36:22 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.14 -> 2.03 -> 1.90 -> 1.81 -> 2.82 -> 1.97 -> 2.48 -> 2.22 -> 1.98 -> 1.94 -> 1.82 -> 2.18

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=123700 tokens=2026.7M loss=2.1029 lr=9.52e-05 tok/s=12490
[train] step=123710 tokens=2026.9M loss=2.0721 lr=9.52e-05 tok/s=12490
[train] step=123720 tokens=2027.0M loss=2.1027 lr=9.52e-05 tok/s=12490
[train] step=123730 tokens=2027.2M loss=1.9880 lr=9.52e-05 tok/s=12490
[train] step=123740 tokens=2027.4M loss=2.2484 lr=9.52e-05 tok/s=12490
[train] step=123750 tokens=2027.5M loss=1.7774 lr=9.51e-05 tok/s=12490
[train] step=123760 tokens=2027.7M loss=2.0438 lr=9.51e-05 tok/s=12490
[train] step=123770 tokens=2027.8M loss=1.7989 lr=9.51e-05 tok/s=12490
[train] step=123780 tokens=2028.0M loss=1.3838 lr=9.51e-05 tok/s=12490
[train] step=123790 tokens=2028.2M loss=2.1824 lr=9.51e-05 tok/s=12490
[train] step=123800 tokens=2028.3M loss=2.3879 lr=9.50e-05 tok/s=12490
[train] step=123810 tokens=2028.5M loss=2.6155 lr=9.50e-05 tok/s=12490
```
