# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 11:58:57 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1773M / 3000M (59.1%) |
| Step | 108210 |
| Latest loss | 1.8214 |
| Avg loss (last 30 logged) | 2.1582 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 3:17:42 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.57 -> 2.34 -> 2.37 -> 2.77 -> 2.42 -> 2.00 -> 1.91 -> 2.03 -> 2.33 -> 2.17 -> 2.05 -> 2.33

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=108100 tokens=1771.1M loss=1.9149 lr=1.29e-04 tok/s=12488
[train] step=108110 tokens=1771.3M loss=2.3515 lr=1.29e-04 tok/s=12488
[train] step=108120 tokens=1771.4M loss=1.9693 lr=1.29e-04 tok/s=12488
[train] step=108130 tokens=1771.6M loss=1.8983 lr=1.29e-04 tok/s=12488
[train] step=108140 tokens=1771.8M loss=2.4713 lr=1.28e-04 tok/s=12488
[train] step=108150 tokens=1771.9M loss=2.5229 lr=1.28e-04 tok/s=12488
[train] step=108160 tokens=1772.1M loss=2.2709 lr=1.28e-04 tok/s=12488
[train] step=108170 tokens=1772.3M loss=2.3967 lr=1.28e-04 tok/s=12488
[train] step=108180 tokens=1772.4M loss=2.3323 lr=1.28e-04 tok/s=12488
[train] step=108190 tokens=1772.6M loss=2.5167 lr=1.28e-04 tok/s=12488
[train] step=108200 tokens=1772.7M loss=1.9234 lr=1.28e-04 tok/s=12488
[train] step=108210 tokens=1772.9M loss=1.8214 lr=1.28e-04 tok/s=12488
```
