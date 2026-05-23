# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 10:28:43 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1705M / 3000M (56.8%) |
| Step | 104080 |
| Latest loss | 1.8013 |
| Avg loss (last 30 logged) | 2.0659 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 4:48:03 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.99 -> 2.20 -> 1.69 -> 2.13 -> 2.31 -> 1.93 -> 1.98 -> 2.53 -> 2.26 -> 2.24 -> 2.18 -> 2.25

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=103970 tokens=1703.4M loss=1.7042 lr=1.38e-04 tok/s=12488
[train] step=103980 tokens=1703.6M loss=2.2092 lr=1.38e-04 tok/s=12488
[train] step=103990 tokens=1703.8M loss=2.2241 lr=1.38e-04 tok/s=12488
[train] step=104000 tokens=1703.9M loss=1.6327 lr=1.38e-04 tok/s=12488
[train] step=104010 tokens=1704.1M loss=2.2859 lr=1.38e-04 tok/s=12488
[train] step=104020 tokens=1704.3M loss=2.0154 lr=1.38e-04 tok/s=12488
[train] step=104030 tokens=1704.4M loss=1.8495 lr=1.38e-04 tok/s=12488
[train] step=104040 tokens=1704.6M loss=1.9446 lr=1.38e-04 tok/s=12488
[train] step=104050 tokens=1704.8M loss=2.3448 lr=1.38e-04 tok/s=12488
[train] step=104060 tokens=1704.9M loss=2.2502 lr=1.38e-04 tok/s=12488
[train] step=104070 tokens=1705.1M loss=2.2546 lr=1.38e-04 tok/s=12488
[train] step=104080 tokens=1705.2M loss=1.8013 lr=1.38e-04 tok/s=12488
```
