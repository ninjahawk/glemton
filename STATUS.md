# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 08:54:44 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 556M / 3000M (18.5%) |
| Step | 33920 |
| Latest loss | 2.1468 |
| Avg loss (last 30 logged) | 2.4364 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 6:23:14 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.72 -> 2.39 -> 2.41 -> 2.33 -> 2.34 -> 2.31 -> 2.25 -> 2.51 -> 2.53 -> 2.44 -> 2.22 -> 2.37

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`

## Recent log tail
```
[train] step=33810 tokens=553.9M loss=2.1277 lr=2.79e-04 tok/s=12484
[train] step=33820 tokens=554.1M loss=2.7048 lr=2.79e-04 tok/s=12484
[train] step=33830 tokens=554.3M loss=2.5371 lr=2.79e-04 tok/s=12484
[train] step=33840 tokens=554.4M loss=2.1539 lr=2.79e-04 tok/s=12484
[train] step=33850 tokens=554.6M loss=2.6487 lr=2.79e-04 tok/s=12484
[train] step=33860 tokens=554.8M loss=2.5007 lr=2.79e-04 tok/s=12484
[train] step=33870 tokens=554.9M loss=2.2728 lr=2.79e-04 tok/s=12484
[train] step=33880 tokens=555.1M loss=2.3505 lr=2.79e-04 tok/s=12484
[train] step=33890 tokens=555.3M loss=2.1818 lr=2.79e-04 tok/s=12484
[train] step=33900 tokens=555.4M loss=2.3706 lr=2.79e-04 tok/s=12484
[train] step=33910 tokens=555.6M loss=2.3234 lr=2.79e-04 tok/s=12484
[train] step=33920 tokens=555.7M loss=2.1468 lr=2.79e-04 tok/s=12484
```
