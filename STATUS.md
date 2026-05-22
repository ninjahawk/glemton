# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 04:23:59 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 353M / 3000M (11.8%) |
| Step | 21540 |
| Latest loss | 2.3330 |
| Avg loss (last 30 logged) | 2.4928 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 2 days, 10:52:51 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.22 -> 3.18 -> 2.53 -> 2.52 -> 2.35 -> 2.32 -> 2.55 -> 2.22 -> 2.44 -> 2.52 -> 2.15 -> 2.50

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=21430 tokens=351.1M loss=2.4531 lr=2.92e-04 tok/s=12488
[train] step=21440 tokens=351.3M loss=2.1183 lr=2.92e-04 tok/s=12488
[train] step=21450 tokens=351.4M loss=2.6859 lr=2.92e-04 tok/s=12488
[train] step=21460 tokens=351.6M loss=2.1791 lr=2.92e-04 tok/s=12488
[train] step=21470 tokens=351.8M loss=2.3208 lr=2.92e-04 tok/s=12488
[train] step=21480 tokens=351.9M loss=2.7552 lr=2.92e-04 tok/s=12488
[train] step=21490 tokens=352.1M loss=2.6595 lr=2.92e-04 tok/s=12488
[train] step=21500 tokens=352.3M loss=2.7342 lr=2.92e-04 tok/s=12488
[train] step=21510 tokens=352.4M loss=2.7166 lr=2.92e-04 tok/s=12488
[train] step=21520 tokens=352.6M loss=2.4989 lr=2.92e-04 tok/s=12488
[train] step=21530 tokens=352.7M loss=2.5702 lr=2.92e-04 tok/s=12488
[train] step=21540 tokens=352.9M loss=2.3330 lr=2.92e-04 tok/s=12488
```
