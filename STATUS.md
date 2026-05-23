# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 02:47:33 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1360M / 3000M (45.3%) |
| Step | 82980 |
| Latest loss | 2.2373 |
| Avg loss (last 30 logged) | 2.2111 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 12:29:36 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.90 -> 1.88 -> 2.39 -> 2.05 -> 2.14 -> 1.90 -> 2.50 -> 2.07 -> 2.54 -> 2.03 -> 1.83 -> 2.32

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`

## Recent log tail
```
[train] step=82870 tokens=1357.7M loss=2.4909 lr=1.87e-04 tok/s=12487
[train] step=82880 tokens=1357.9M loss=2.4271 lr=1.87e-04 tok/s=12487
[train] step=82890 tokens=1358.1M loss=2.4262 lr=1.87e-04 tok/s=12487
[train] step=82900 tokens=1358.2M loss=2.5489 lr=1.87e-04 tok/s=12487
[train] step=82910 tokens=1358.4M loss=2.0846 lr=1.87e-04 tok/s=12487
[train] step=82920 tokens=1358.6M loss=2.3785 lr=1.87e-04 tok/s=12487
[train] step=82930 tokens=1358.7M loss=2.9881 lr=1.87e-04 tok/s=12487
[train] step=82940 tokens=1358.9M loss=2.0647 lr=1.87e-04 tok/s=12487
[train] step=82950 tokens=1359.1M loss=2.2838 lr=1.87e-04 tok/s=12487
[train] step=82960 tokens=1359.2M loss=2.3190 lr=1.87e-04 tok/s=12487
[train] step=82970 tokens=1359.4M loss=2.1803 lr=1.87e-04 tok/s=12487
[train] step=82980 tokens=1359.5M loss=2.2373 lr=1.87e-04 tok/s=12487
```
