# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 13:42:50 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2929M / 3000M (97.6%) |
| Step | 178760 |
| Latest loss | 2.0507 |
| Avg loss (last 30 logged) | 2.0352 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1:35:03 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.80 -> 1.81 -> 2.26 -> 2.40 -> 2.02 -> 2.08 -> 2.17 -> 2.22 -> 1.86 -> 2.20 -> 2.27 -> 1.55

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_170899_tokens_2800M.pt`
- `step_177002_tokens_2900M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=178650 tokens=2927.0M loss=1.6867 lr=3.04e-05 tok/s=12484
[train] step=178660 tokens=2927.2M loss=2.1256 lr=3.04e-05 tok/s=12484
[train] step=178670 tokens=2927.3M loss=1.8597 lr=3.04e-05 tok/s=12484
[train] step=178680 tokens=2927.5M loss=2.7351 lr=3.04e-05 tok/s=12484
[train] step=178690 tokens=2927.7M loss=1.5484 lr=3.04e-05 tok/s=12484
[train] step=178700 tokens=2927.8M loss=2.0186 lr=3.04e-05 tok/s=12484
[train] step=178710 tokens=2928.0M loss=2.0226 lr=3.04e-05 tok/s=12484
[train] step=178720 tokens=2928.1M loss=2.0954 lr=3.04e-05 tok/s=12484
[train] step=178730 tokens=2928.3M loss=2.0952 lr=3.04e-05 tok/s=12484
[train] step=178740 tokens=2928.5M loss=1.5516 lr=3.04e-05 tok/s=12484
[train] step=178750 tokens=2928.6M loss=1.8008 lr=3.04e-05 tok/s=12484
[train] step=178760 tokens=2928.8M loss=2.0507 lr=3.04e-05 tok/s=12484
```
