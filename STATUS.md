# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 19:09:59 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2096M / 3000M (69.9%) |
| Step | 127940 |
| Latest loss | 2.4134 |
| Avg loss (last 30 logged) | 2.1150 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 20:06:01 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.96 -> 1.72 -> 2.21 -> 2.26 -> 1.51 -> 1.99 -> 2.10 -> 1.78 -> 1.50 -> 1.57 -> 1.92 -> 2.39

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
[train] step=127830 tokens=2094.4M loss=2.4854 lr=8.72e-05 tok/s=12490
[train] step=127840 tokens=2094.5M loss=2.2645 lr=8.72e-05 tok/s=12490
[train] step=127850 tokens=2094.7M loss=1.7443 lr=8.71e-05 tok/s=12490
[train] step=127860 tokens=2094.9M loss=2.2666 lr=8.71e-05 tok/s=12490
[train] step=127870 tokens=2095.0M loss=1.7581 lr=8.71e-05 tok/s=12490
[train] step=127880 tokens=2095.2M loss=2.3468 lr=8.71e-05 tok/s=12490
[train] step=127890 tokens=2095.3M loss=2.1506 lr=8.71e-05 tok/s=12490
[train] step=127900 tokens=2095.5M loss=2.2395 lr=8.70e-05 tok/s=12490
[train] step=127910 tokens=2095.7M loss=2.3915 lr=8.70e-05 tok/s=12490
[train] step=127920 tokens=2095.8M loss=1.9583 lr=8.70e-05 tok/s=12490
[train] step=127930 tokens=2096.0M loss=2.1914 lr=8.70e-05 tok/s=12490
[train] step=127940 tokens=2096.2M loss=2.4134 lr=8.70e-05 tok/s=12490
```
