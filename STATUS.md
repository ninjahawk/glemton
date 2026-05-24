# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 03:41:18 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2479M / 3000M (82.6%) |
| Step | 151320 |
| Latest loss | 2.2344 |
| Avg loss (last 30 logged) | 2.1003 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 11:35:00 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.17 -> 1.93 -> 1.87 -> 1.84 -> 1.99 -> 1.93 -> 2.17 -> 2.36 -> 2.27 -> 1.56 -> 1.70 -> 1.62

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
[train] step=151210 tokens=2477.4M loss=2.0839 lr=5.00e-05 tok/s=12489
[train] step=151220 tokens=2477.6M loss=1.8892 lr=5.00e-05 tok/s=12489
[train] step=151230 tokens=2477.8M loss=2.2899 lr=5.00e-05 tok/s=12489
[train] step=151240 tokens=2477.9M loss=2.2546 lr=5.00e-05 tok/s=12489
[train] step=151250 tokens=2478.1M loss=2.0661 lr=5.00e-05 tok/s=12489
[train] step=151260 tokens=2478.2M loss=2.0338 lr=5.00e-05 tok/s=12489
[train] step=151270 tokens=2478.4M loss=2.3611 lr=5.00e-05 tok/s=12489
[train] step=151280 tokens=2478.6M loss=2.3453 lr=5.00e-05 tok/s=12489
[train] step=151290 tokens=2478.7M loss=1.6204 lr=4.99e-05 tok/s=12489
[train] step=151300 tokens=2478.9M loss=2.5621 lr=4.99e-05 tok/s=12489
[train] step=151310 tokens=2479.1M loss=2.1058 lr=4.99e-05 tok/s=12489
[train] step=151320 tokens=2479.2M loss=2.2344 lr=4.99e-05 tok/s=12489
```
