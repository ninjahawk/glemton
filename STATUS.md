# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 05:01:31 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2539M / 3000M (84.6%) |
| Step | 154980 |
| Latest loss | 1.9571 |
| Avg loss (last 30 logged) | 2.1080 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 10:14:56 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.55 -> 2.24 -> 2.14 -> 2.24 -> 1.97 -> 2.34 -> 2.55 -> 1.90 -> 1.96 -> 2.14 -> 2.08 -> 2.64

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=154870 tokens=2537.4M loss=2.1080 lr=4.58e-05 tok/s=12489
[train] step=154880 tokens=2537.6M loss=1.7126 lr=4.58e-05 tok/s=12489
[train] step=154890 tokens=2537.7M loss=2.0549 lr=4.58e-05 tok/s=12489
[train] step=154900 tokens=2537.9M loss=2.0131 lr=4.58e-05 tok/s=12489
[train] step=154910 tokens=2538.0M loss=1.9226 lr=4.57e-05 tok/s=12489
[train] step=154920 tokens=2538.2M loss=1.8596 lr=4.57e-05 tok/s=12489
[train] step=154930 tokens=2538.4M loss=2.1261 lr=4.57e-05 tok/s=12489
[train] step=154940 tokens=2538.5M loss=2.1074 lr=4.57e-05 tok/s=12489
[train] step=154950 tokens=2538.7M loss=2.9315 lr=4.57e-05 tok/s=12489
[train] step=154960 tokens=2538.9M loss=2.6376 lr=4.57e-05 tok/s=12489
[train] step=154970 tokens=2539.0M loss=2.1038 lr=4.57e-05 tok/s=12489
[train] step=154980 tokens=2539.2M loss=1.9571 lr=4.57e-05 tok/s=12489
```
