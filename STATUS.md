# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 12:12:37 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2861M / 3000M (95.4%) |
| Step | 174630 |
| Latest loss | 2.2775 |
| Avg loss (last 30 logged) | 2.0283 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 3:05:26 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
1.53 -> 1.83 -> 2.16 -> 1.95 -> 1.95 -> 2.16 -> 1.81 -> 1.90 -> 2.52 -> 1.94 -> 2.28 -> 2.28

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_170899_tokens_2800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=174520 tokens=2859.3M loss=2.1338 lr=3.15e-05 tok/s=12484
[train] step=174530 tokens=2859.5M loss=2.2204 lr=3.15e-05 tok/s=12484
[train] step=174540 tokens=2859.7M loss=1.9626 lr=3.15e-05 tok/s=12484
[train] step=174550 tokens=2859.8M loss=2.1669 lr=3.15e-05 tok/s=12484
[train] step=174560 tokens=2860.0M loss=2.0904 lr=3.15e-05 tok/s=12484
[train] step=174570 tokens=2860.2M loss=2.2125 lr=3.15e-05 tok/s=12484
[train] step=174580 tokens=2860.3M loss=2.0047 lr=3.15e-05 tok/s=12484
[train] step=174590 tokens=2860.5M loss=1.7948 lr=3.15e-05 tok/s=12484
[train] step=174600 tokens=2860.6M loss=2.6530 lr=3.15e-05 tok/s=12484
[train] step=174610 tokens=2860.8M loss=2.2777 lr=3.15e-05 tok/s=12484
[train] step=174620 tokens=2861.0M loss=1.7377 lr=3.15e-05 tok/s=12484
[train] step=174630 tokens=2861.1M loss=2.2775 lr=3.14e-05 tok/s=12484
```
