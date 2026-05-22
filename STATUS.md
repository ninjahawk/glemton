# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 01:23:29 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 218M / 3000M (7.3%) |
| Step | 13290 |
| Latest loss | 2.3879 |
| Avg loss (last 30 logged) | 2.5636 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 2 days, 13:52:42 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.54 -> 2.87 -> 2.49 -> 2.41 -> 2.47 -> 2.67 -> 2.32 -> 2.45 -> 2.51 -> 2.59 -> 2.59 -> 2.29

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=13180 tokens=215.9M loss=2.6252 lr=2.97e-04 tok/s=12490
[train] step=13190 tokens=216.1M loss=2.4585 lr=2.97e-04 tok/s=12490
[train] step=13200 tokens=216.3M loss=2.4940 lr=2.97e-04 tok/s=12490
[train] step=13210 tokens=216.4M loss=2.6485 lr=2.97e-04 tok/s=12490
[train] step=13220 tokens=216.6M loss=2.2295 lr=2.97e-04 tok/s=12490
[train] step=13230 tokens=216.8M loss=2.5699 lr=2.97e-04 tok/s=12490
[train] step=13240 tokens=216.9M loss=2.2960 lr=2.97e-04 tok/s=12490
[train] step=13250 tokens=217.1M loss=2.9679 lr=2.97e-04 tok/s=12490
[train] step=13260 tokens=217.3M loss=2.2263 lr=2.97e-04 tok/s=12490
[train] step=13270 tokens=217.4M loss=2.2919 lr=2.97e-04 tok/s=12490
[train] step=13280 tokens=217.6M loss=2.7369 lr=2.97e-04 tok/s=12490
[train] step=13290 tokens=217.7M loss=2.3879 lr=2.97e-04 tok/s=12490
```
