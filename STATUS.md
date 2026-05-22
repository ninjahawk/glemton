# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 08:34:40 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 541M / 3000M (18.0%) |
| Step | 33000 |
| Latest loss | 2.2396 |
| Avg loss (last 30 logged) | 2.3377 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 6:43:16 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.23 -> 2.41 -> 2.54 -> 2.33 -> 2.41 -> 2.23 -> 2.07 -> 2.54 -> 2.56 -> 2.31 -> 1.93 -> 2.48

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`

## Recent log tail
```
[train] step=32890 tokens=538.9M loss=2.0312 lr=2.81e-04 tok/s=12484
[train] step=32900 tokens=539.0M loss=2.2178 lr=2.81e-04 tok/s=12484
[train] step=32910 tokens=539.2M loss=2.5318 lr=2.81e-04 tok/s=12484
[train] step=32920 tokens=539.4M loss=2.4625 lr=2.81e-04 tok/s=12484
[train] step=32930 tokens=539.5M loss=2.1082 lr=2.81e-04 tok/s=12484
[train] step=32940 tokens=539.7M loss=2.1537 lr=2.81e-04 tok/s=12484
[train] step=32950 tokens=539.9M loss=2.6294 lr=2.81e-04 tok/s=12484
[train] step=32960 tokens=540.0M loss=2.4429 lr=2.81e-04 tok/s=12484
[train] step=32970 tokens=540.2M loss=2.5645 lr=2.81e-04 tok/s=12484
[train] step=32980 tokens=540.3M loss=2.4774 lr=2.80e-04 tok/s=12484
[train] step=32990 tokens=540.5M loss=2.2291 lr=2.80e-04 tok/s=12484
[train] step=33000 tokens=540.7M loss=2.2396 lr=2.80e-04 tok/s=12484
```
