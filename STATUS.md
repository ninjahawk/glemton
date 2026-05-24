# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 14:12:55 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2951M / 3000M (98.4%) |
| Step | 180130 |
| Latest loss | 2.0347 |
| Avg loss (last 30 logged) | 2.1033 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1:05:09 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.44 -> 2.18 -> 2.39 -> 2.16 -> 2.07 -> 2.09 -> 2.49 -> 2.43 -> 1.48 -> 2.11 -> 2.16 -> 2.17

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
[train] step=180020 tokens=2949.4M loss=2.0719 lr=3.02e-05 tok/s=12484
[train] step=180030 tokens=2949.6M loss=1.9520 lr=3.02e-05 tok/s=12484
[train] step=180040 tokens=2949.8M loss=1.9769 lr=3.02e-05 tok/s=12484
[train] step=180050 tokens=2949.9M loss=1.8928 lr=3.02e-05 tok/s=12484
[train] step=180060 tokens=2950.1M loss=2.3690 lr=3.02e-05 tok/s=12484
[train] step=180070 tokens=2950.3M loss=2.2681 lr=3.02e-05 tok/s=12484
[train] step=180080 tokens=2950.4M loss=1.9279 lr=3.02e-05 tok/s=12484
[train] step=180090 tokens=2950.6M loss=1.6639 lr=3.02e-05 tok/s=12484
[train] step=180100 tokens=2950.8M loss=1.9509 lr=3.02e-05 tok/s=12484
[train] step=180110 tokens=2950.9M loss=2.1679 lr=3.02e-05 tok/s=12484
[train] step=180120 tokens=2951.1M loss=1.9778 lr=3.02e-05 tok/s=12484
[train] step=180130 tokens=2951.2M loss=2.0347 lr=3.02e-05 tok/s=12484
```
