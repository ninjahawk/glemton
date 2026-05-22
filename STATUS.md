# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 07:04:26 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 473M / 3000M (15.8%) |
| Step | 28880 |
| Latest loss | 2.4681 |
| Avg loss (last 30 logged) | 2.5000 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 2 days, 8:13:06 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.30 -> 2.45 -> 2.43 -> 2.54 -> 2.77 -> 2.45 -> 2.61 -> 2.43 -> 2.53 -> 2.54 -> 2.04 -> 2.28

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=28770 tokens=471.4M loss=2.1645 lr=2.85e-04 tok/s=12485
[train] step=28780 tokens=471.5M loss=2.1810 lr=2.85e-04 tok/s=12485
[train] step=28790 tokens=471.7M loss=3.2269 lr=2.85e-04 tok/s=12485
[train] step=28800 tokens=471.9M loss=2.4376 lr=2.85e-04 tok/s=12485
[train] step=28810 tokens=472.0M loss=2.3696 lr=2.85e-04 tok/s=12485
[train] step=28820 tokens=472.2M loss=2.8062 lr=2.85e-04 tok/s=12485
[train] step=28830 tokens=472.4M loss=2.6229 lr=2.85e-04 tok/s=12485
[train] step=28840 tokens=472.5M loss=2.3729 lr=2.85e-04 tok/s=12485
[train] step=28850 tokens=472.7M loss=2.2819 lr=2.85e-04 tok/s=12485
[train] step=28860 tokens=472.8M loss=2.7258 lr=2.85e-04 tok/s=12485
[train] step=28870 tokens=473.0M loss=2.2559 lr=2.85e-04 tok/s=12485
[train] step=28880 tokens=473.2M loss=2.4681 lr=2.85e-04 tok/s=12485
```
