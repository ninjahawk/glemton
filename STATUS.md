# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 03:33:51 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 315M / 3000M (10.5%) |
| Step | 19250 |
| Latest loss | 2.0173 |
| Avg loss (last 30 logged) | 2.4681 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 2 days, 11:42:54 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.93 -> 2.55 -> 2.48 -> 2.37 -> 2.43 -> 2.62 -> 2.52 -> 2.42 -> 2.56 -> 2.33 -> 2.66 -> 2.44

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=19140 tokens=313.6M loss=2.7349 lr=2.94e-04 tok/s=12488
[train] step=19150 tokens=313.8M loss=2.5656 lr=2.94e-04 tok/s=12488
[train] step=19160 tokens=313.9M loss=2.1654 lr=2.94e-04 tok/s=12488
[train] step=19170 tokens=314.1M loss=2.2477 lr=2.94e-04 tok/s=12488
[train] step=19180 tokens=314.2M loss=2.3761 lr=2.94e-04 tok/s=12488
[train] step=19190 tokens=314.4M loss=2.5656 lr=2.94e-04 tok/s=12488
[train] step=19200 tokens=314.6M loss=2.2751 lr=2.94e-04 tok/s=12488
[train] step=19210 tokens=314.7M loss=2.3478 lr=2.94e-04 tok/s=12488
[train] step=19220 tokens=314.9M loss=2.2954 lr=2.94e-04 tok/s=12488
[train] step=19230 tokens=315.1M loss=2.4406 lr=2.94e-04 tok/s=12488
[train] step=19240 tokens=315.2M loss=2.4498 lr=2.94e-04 tok/s=12488
[train] step=19250 tokens=315.4M loss=2.0173 lr=2.94e-04 tok/s=12488
```
