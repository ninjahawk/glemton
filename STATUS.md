# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 03:07:36 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1375M / 3000M (45.8%) |
| Step | 83900 |
| Latest loss | 2.3565 |
| Avg loss (last 30 logged) | 2.1907 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 12:09:27 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.94 -> 2.14 -> 2.62 -> 1.71 -> 1.80 -> 1.91 -> 2.17 -> 2.68 -> 2.43 -> 2.25 -> 2.40 -> 2.20

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`

## Recent log tail
```
[train] step=83790 tokens=1372.8M loss=2.0722 lr=1.85e-04 tok/s=12487
[train] step=83800 tokens=1373.0M loss=2.1942 lr=1.85e-04 tok/s=12487
[train] step=83810 tokens=1373.1M loss=1.7186 lr=1.85e-04 tok/s=12487
[train] step=83820 tokens=1373.3M loss=2.4010 lr=1.85e-04 tok/s=12487
[train] step=83830 tokens=1373.5M loss=2.0960 lr=1.85e-04 tok/s=12487
[train] step=83840 tokens=1373.6M loss=1.9310 lr=1.85e-04 tok/s=12487
[train] step=83850 tokens=1373.8M loss=2.0276 lr=1.85e-04 tok/s=12487
[train] step=83860 tokens=1374.0M loss=2.2326 lr=1.85e-04 tok/s=12487
[train] step=83870 tokens=1374.1M loss=2.2049 lr=1.85e-04 tok/s=12487
[train] step=83880 tokens=1374.3M loss=1.9383 lr=1.85e-04 tok/s=12487
[train] step=83890 tokens=1374.5M loss=2.1423 lr=1.85e-04 tok/s=12487
[train] step=83900 tokens=1374.6M loss=2.3565 lr=1.85e-04 tok/s=12487
```
