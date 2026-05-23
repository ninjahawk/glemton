# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 17:59:49 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2044M / 3000M (68.1%) |
| Step | 124730 |
| Latest loss | 2.5344 |
| Avg loss (last 30 logged) | 2.1138 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 21:16:13 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.03 -> 2.29 -> 2.12 -> 2.24 -> 2.11 -> 1.86 -> 2.28 -> 2.26 -> 2.10 -> 1.94 -> 2.49 -> 2.04

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
[train] step=124620 tokens=2041.8M loss=2.3626 lr=9.34e-05 tok/s=12490
[train] step=124630 tokens=2041.9M loss=2.0103 lr=9.34e-05 tok/s=12490
[train] step=124640 tokens=2042.1M loss=1.7980 lr=9.34e-05 tok/s=12490
[train] step=124650 tokens=2042.3M loss=2.2829 lr=9.34e-05 tok/s=12490
[train] step=124660 tokens=2042.4M loss=2.0892 lr=9.33e-05 tok/s=12490
[train] step=124670 tokens=2042.6M loss=2.3540 lr=9.33e-05 tok/s=12490
[train] step=124680 tokens=2042.8M loss=1.7344 lr=9.33e-05 tok/s=12490
[train] step=124690 tokens=2042.9M loss=1.7247 lr=9.33e-05 tok/s=12490
[train] step=124700 tokens=2043.1M loss=2.5791 lr=9.33e-05 tok/s=12490
[train] step=124710 tokens=2043.2M loss=2.0412 lr=9.32e-05 tok/s=12490
[train] step=124720 tokens=2043.4M loss=2.2953 lr=9.32e-05 tok/s=12490
[train] step=124730 tokens=2043.6M loss=2.5344 lr=9.32e-05 tok/s=12490
```
