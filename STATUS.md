# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 08:14:37 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 526M / 3000M (17.5%) |
| Step | 32080 |
| Latest loss | 2.2422 |
| Avg loss (last 30 logged) | 2.4208 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 7:03:25 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.33 -> 2.41 -> 2.88 -> 2.26 -> 2.22 -> 2.03 -> 2.26 -> 2.61 -> 2.16 -> 2.19 -> 2.20 -> 2.17

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`

## Recent log tail
```
[train] step=31970 tokens=523.8M loss=2.4811 lr=2.82e-04 tok/s=12484
[train] step=31980 tokens=524.0M loss=2.4885 lr=2.82e-04 tok/s=12484
[train] step=31990 tokens=524.1M loss=2.5569 lr=2.82e-04 tok/s=12484
[train] step=32000 tokens=524.3M loss=2.1939 lr=2.82e-04 tok/s=12484
[train] step=32010 tokens=524.5M loss=2.7046 lr=2.82e-04 tok/s=12484
[train] step=32020 tokens=524.6M loss=2.4805 lr=2.82e-04 tok/s=12484
[train] step=32030 tokens=524.8M loss=2.1393 lr=2.82e-04 tok/s=12484
[train] step=32040 tokens=524.9M loss=2.2386 lr=2.82e-04 tok/s=12484
[train] step=32050 tokens=525.1M loss=2.8695 lr=2.82e-04 tok/s=12484
[train] step=32060 tokens=525.3M loss=2.1681 lr=2.82e-04 tok/s=12484
[train] step=32070 tokens=525.4M loss=2.4160 lr=2.82e-04 tok/s=12484
[train] step=32080 tokens=525.6M loss=2.2422 lr=2.82e-04 tok/s=12484
```
