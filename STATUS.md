# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 07:21:53 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2644M / 3000M (88.1%) |
| Step | 161400 |
| Latest loss | 2.3035 |
| Avg loss (last 30 logged) | 1.9369 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 7:54:33 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.04 -> 2.35 -> 2.03 -> 2.10 -> 2.15 -> 2.42 -> 2.20 -> 2.06 -> 2.11 -> 1.79 -> 2.12 -> 1.88

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
[train] step=161290 tokens=2642.6M loss=2.3956 lr=3.95e-05 tok/s=12489
[train] step=161300 tokens=2642.7M loss=1.8061 lr=3.95e-05 tok/s=12489
[train] step=161310 tokens=2642.9M loss=1.5962 lr=3.95e-05 tok/s=12489
[train] step=161320 tokens=2643.1M loss=1.6728 lr=3.95e-05 tok/s=12489
[train] step=161330 tokens=2643.2M loss=2.0241 lr=3.95e-05 tok/s=12489
[train] step=161340 tokens=2643.4M loss=1.6712 lr=3.95e-05 tok/s=12489
[train] step=161350 tokens=2643.6M loss=2.1128 lr=3.95e-05 tok/s=12489
[train] step=161360 tokens=2643.7M loss=2.0023 lr=3.94e-05 tok/s=12489
[train] step=161370 tokens=2643.9M loss=1.8263 lr=3.94e-05 tok/s=12489
[train] step=161380 tokens=2644.0M loss=1.8839 lr=3.94e-05 tok/s=12489
[train] step=161390 tokens=2644.2M loss=2.0092 lr=3.94e-05 tok/s=12489
[train] step=161400 tokens=2644.4M loss=2.3035 lr=3.94e-05 tok/s=12489
```
