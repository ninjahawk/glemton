# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 07:38:17 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1578M / 3000M (52.6%) |
| Step | 96280 |
| Latest loss | 2.0250 |
| Avg loss (last 30 logged) | 2.0697 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 7:38:29 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.18 -> 2.17 -> 2.15 -> 1.65 -> 1.88 -> 2.07 -> 2.09 -> 2.10 -> 2.79 -> 2.26 -> 2.15 -> 2.03

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_73243_tokens_1200M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=96170 tokens=1575.6M loss=2.1759 lr=1.56e-04 tok/s=12488
[train] step=96180 tokens=1575.8M loss=2.3025 lr=1.56e-04 tok/s=12488
[train] step=96190 tokens=1576.0M loss=2.1677 lr=1.56e-04 tok/s=12488
[train] step=96200 tokens=1576.1M loss=1.9911 lr=1.56e-04 tok/s=12488
[train] step=96210 tokens=1576.3M loss=1.7437 lr=1.56e-04 tok/s=12488
[train] step=96220 tokens=1576.5M loss=2.1753 lr=1.56e-04 tok/s=12488
[train] step=96230 tokens=1576.6M loss=2.1218 lr=1.56e-04 tok/s=12488
[train] step=96240 tokens=1576.8M loss=2.1570 lr=1.56e-04 tok/s=12488
[train] step=96250 tokens=1577.0M loss=2.0322 lr=1.56e-04 tok/s=12488
[train] step=96260 tokens=1577.1M loss=2.5825 lr=1.56e-04 tok/s=12488
[train] step=96270 tokens=1577.3M loss=1.9079 lr=1.56e-04 tok/s=12488
[train] step=96280 tokens=1577.5M loss=2.0250 lr=1.56e-04 tok/s=12488
```
