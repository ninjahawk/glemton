# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 07:41:56 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2660M / 3000M (88.7%) |
| Step | 162320 |
| Latest loss | 1.7474 |
| Avg loss (last 30 logged) | 2.0037 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 7:34:23 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.91 -> 2.47 -> 1.52 -> 2.15 -> 2.20 -> 2.45 -> 2.08 -> 2.11 -> 1.60 -> 2.01 -> 1.87 -> 1.91

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=162210 tokens=2657.6M loss=2.0713 lr=3.87e-05 tok/s=12489
[train] step=162220 tokens=2657.8M loss=1.9578 lr=3.87e-05 tok/s=12489
[train] step=162230 tokens=2658.0M loss=1.6826 lr=3.87e-05 tok/s=12489
[train] step=162240 tokens=2658.1M loss=1.8429 lr=3.87e-05 tok/s=12489
[train] step=162250 tokens=2658.3M loss=1.9836 lr=3.87e-05 tok/s=12489
[train] step=162260 tokens=2658.5M loss=2.2595 lr=3.87e-05 tok/s=12489
[train] step=162270 tokens=2658.6M loss=2.2429 lr=3.87e-05 tok/s=12489
[train] step=162280 tokens=2658.8M loss=2.4943 lr=3.87e-05 tok/s=12489
[train] step=162290 tokens=2659.0M loss=1.6856 lr=3.87e-05 tok/s=12489
[train] step=162300 tokens=2659.1M loss=1.9141 lr=3.87e-05 tok/s=12489
[train] step=162310 tokens=2659.3M loss=1.7386 lr=3.86e-05 tok/s=12489
[train] step=162320 tokens=2659.5M loss=1.7474 lr=3.86e-05 tok/s=12489
```
