# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 03:11:13 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2457M / 3000M (81.9%) |
| Step | 149940 |
| Latest loss | 2.7974 |
| Avg loss (last 30 logged) | 2.0602 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 12:05:10 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.66 -> 1.98 -> 1.51 -> 2.32 -> 1.75 -> 2.15 -> 2.28 -> 2.34 -> 1.84 -> 2.01 -> 2.12 -> 1.88

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=149830 tokens=2454.8M loss=1.8021 lr=5.18e-05 tok/s=12489
[train] step=149840 tokens=2455.0M loss=2.2212 lr=5.17e-05 tok/s=12489
[train] step=149850 tokens=2455.1M loss=2.3563 lr=5.17e-05 tok/s=12489
[train] step=149860 tokens=2455.3M loss=2.1142 lr=5.17e-05 tok/s=12489
[train] step=149870 tokens=2455.5M loss=2.3927 lr=5.17e-05 tok/s=12489
[train] step=149880 tokens=2455.6M loss=1.8260 lr=5.17e-05 tok/s=12489
[train] step=149890 tokens=2455.8M loss=2.1282 lr=5.17e-05 tok/s=12489
[train] step=149900 tokens=2456.0M loss=1.6663 lr=5.17e-05 tok/s=12489
[train] step=149910 tokens=2456.1M loss=1.9684 lr=5.17e-05 tok/s=12489
[train] step=149920 tokens=2456.3M loss=1.8763 lr=5.16e-05 tok/s=12489
[train] step=149930 tokens=2456.5M loss=2.0096 lr=5.16e-05 tok/s=12489
[train] step=149940 tokens=2456.6M loss=2.7974 lr=5.16e-05 tok/s=12489
```
