# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 07:11:51 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2637M / 3000M (87.9%) |
| Step | 160940 |
| Latest loss | 1.8285 |
| Avg loss (last 30 logged) | 2.1262 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 8:04:41 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.05 -> 2.06 -> 2.26 -> 1.56 -> 2.08 -> 1.89 -> 1.91 -> 2.17 -> 1.80 -> 1.82 -> 2.48 -> 2.12

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
[train] step=160830 tokens=2635.0M loss=2.1100 lr=3.99e-05 tok/s=12489
[train] step=160840 tokens=2635.2M loss=1.4380 lr=3.99e-05 tok/s=12489
[train] step=160850 tokens=2635.4M loss=2.6238 lr=3.99e-05 tok/s=12489
[train] step=160860 tokens=2635.5M loss=1.8262 lr=3.99e-05 tok/s=12489
[train] step=160870 tokens=2635.7M loss=1.9849 lr=3.99e-05 tok/s=12489
[train] step=160880 tokens=2635.9M loss=1.9239 lr=3.99e-05 tok/s=12489
[train] step=160890 tokens=2636.0M loss=2.1743 lr=3.98e-05 tok/s=12489
[train] step=160900 tokens=2636.2M loss=2.0218 lr=3.98e-05 tok/s=12489
[train] step=160910 tokens=2636.3M loss=2.6385 lr=3.98e-05 tok/s=12489
[train] step=160920 tokens=2636.5M loss=2.1215 lr=3.98e-05 tok/s=12489
[train] step=160930 tokens=2636.7M loss=2.5586 lr=3.98e-05 tok/s=12489
[train] step=160940 tokens=2636.8M loss=1.8285 lr=3.98e-05 tok/s=12489
```
