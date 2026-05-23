# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 05:48:00 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1495M / 3000M (49.8%) |
| Step | 91240 |
| Latest loss | 1.9565 |
| Avg loss (last 30 logged) | 2.2218 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 9:28:43 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.59 -> 2.21 -> 2.26 -> 2.00 -> 2.41 -> 1.74 -> 2.32 -> 2.09 -> 2.47 -> 2.04 -> 1.80 -> 1.99

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`

## Recent log tail
```
[train] step=91130 tokens=1493.1M loss=2.1662 lr=1.68e-04 tok/s=12488
[train] step=91140 tokens=1493.2M loss=2.2980 lr=1.68e-04 tok/s=12488
[train] step=91150 tokens=1493.4M loss=1.9756 lr=1.68e-04 tok/s=12488
[train] step=91160 tokens=1493.6M loss=2.0250 lr=1.68e-04 tok/s=12488
[train] step=91170 tokens=1493.7M loss=2.0838 lr=1.68e-04 tok/s=12488
[train] step=91180 tokens=1493.9M loss=2.5867 lr=1.68e-04 tok/s=12488
[train] step=91190 tokens=1494.1M loss=2.0114 lr=1.68e-04 tok/s=12488
[train] step=91200 tokens=1494.2M loss=1.9165 lr=1.68e-04 tok/s=12488
[train] step=91210 tokens=1494.4M loss=1.9885 lr=1.68e-04 tok/s=12488
[train] step=91220 tokens=1494.5M loss=2.4020 lr=1.68e-04 tok/s=12488
[train] step=91230 tokens=1494.7M loss=2.1377 lr=1.68e-04 tok/s=12488
[train] step=91240 tokens=1494.9M loss=1.9565 lr=1.68e-04 tok/s=12488
```
