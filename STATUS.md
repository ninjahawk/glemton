# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 10:42:23 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2794M / 3000M (93.1%) |
| Step | 170510 |
| Latest loss | 2.2398 |
| Avg loss (last 30 logged) | 2.0341 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 4:35:33 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.05 -> 1.94 -> 2.16 -> 2.19 -> 2.23 -> 2.21 -> 1.95 -> 2.57 -> 2.04 -> 1.84 -> 1.85 -> 1.67

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=170400 tokens=2791.8M loss=2.5180 lr=3.32e-05 tok/s=12484
[train] step=170410 tokens=2792.0M loss=2.6227 lr=3.32e-05 tok/s=12484
[train] step=170420 tokens=2792.2M loss=2.2345 lr=3.32e-05 tok/s=12484
[train] step=170430 tokens=2792.3M loss=2.2120 lr=3.32e-05 tok/s=12484
[train] step=170440 tokens=2792.5M loss=1.7720 lr=3.32e-05 tok/s=12484
[train] step=170450 tokens=2792.7M loss=1.9939 lr=3.32e-05 tok/s=12484
[train] step=170460 tokens=2792.8M loss=2.3972 lr=3.32e-05 tok/s=12484
[train] step=170470 tokens=2793.0M loss=1.9909 lr=3.32e-05 tok/s=12484
[train] step=170480 tokens=2793.1M loss=1.6651 lr=3.32e-05 tok/s=12484
[train] step=170490 tokens=2793.3M loss=2.3219 lr=3.32e-05 tok/s=12484
[train] step=170500 tokens=2793.5M loss=1.4727 lr=3.32e-05 tok/s=12484
[train] step=170510 tokens=2793.6M loss=2.2398 lr=3.32e-05 tok/s=12484
```
