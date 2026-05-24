# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 11:02:26 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2808M / 3000M (93.6%) |
| Step | 171420 |
| Latest loss | 2.0247 |
| Avg loss (last 30 logged) | 1.9965 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 4:15:39 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.15 -> 1.96 -> 1.98 -> 2.21 -> 1.96 -> 1.78 -> 1.85 -> 2.14 -> 2.62 -> 2.37 -> 2.32 -> 2.11

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_170899_tokens_2800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=171310 tokens=2806.7M loss=1.8279 lr=3.28e-05 tok/s=12484
[train] step=171320 tokens=2806.9M loss=1.9315 lr=3.28e-05 tok/s=12484
[train] step=171330 tokens=2807.1M loss=2.4334 lr=3.28e-05 tok/s=12484
[train] step=171340 tokens=2807.2M loss=1.8119 lr=3.28e-05 tok/s=12484
[train] step=171350 tokens=2807.4M loss=2.0971 lr=3.28e-05 tok/s=12484
[train] step=171360 tokens=2807.6M loss=2.0256 lr=3.28e-05 tok/s=12484
[train] step=171370 tokens=2807.7M loss=1.9590 lr=3.28e-05 tok/s=12484
[train] step=171380 tokens=2807.9M loss=2.2531 lr=3.28e-05 tok/s=12484
[train] step=171390 tokens=2808.1M loss=2.2548 lr=3.28e-05 tok/s=12484
[train] step=171400 tokens=2808.2M loss=2.1124 lr=3.28e-05 tok/s=12484
[train] step=171410 tokens=2808.4M loss=2.0803 lr=3.28e-05 tok/s=12484
[train] step=171420 tokens=2808.5M loss=2.0247 lr=3.27e-05 tok/s=12484
```
