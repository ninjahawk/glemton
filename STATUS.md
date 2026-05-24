# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 11:42:32 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2839M / 3000M (94.6%) |
| Step | 173260 |
| Latest loss | 2.4571 |
| Avg loss (last 30 logged) | 2.0630 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 3:35:20 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.32 -> 1.77 -> 1.94 -> 2.40 -> 2.19 -> 1.95 -> 2.31 -> 2.20 -> 2.03 -> 1.85 -> 2.04 -> 1.72

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
[train] step=173150 tokens=2836.9M loss=2.0096 lr=3.20e-05 tok/s=12484
[train] step=173160 tokens=2837.1M loss=1.7773 lr=3.20e-05 tok/s=12484
[train] step=173170 tokens=2837.2M loss=1.8348 lr=3.20e-05 tok/s=12484
[train] step=173180 tokens=2837.4M loss=1.9835 lr=3.20e-05 tok/s=12484
[train] step=173190 tokens=2837.5M loss=2.2158 lr=3.20e-05 tok/s=12484
[train] step=173200 tokens=2837.7M loss=2.3240 lr=3.20e-05 tok/s=12484
[train] step=173210 tokens=2837.9M loss=2.1455 lr=3.20e-05 tok/s=12484
[train] step=173220 tokens=2838.0M loss=1.9187 lr=3.20e-05 tok/s=12484
[train] step=173230 tokens=2838.2M loss=1.9370 lr=3.20e-05 tok/s=12484
[train] step=173240 tokens=2838.4M loss=1.7191 lr=3.20e-05 tok/s=12484
[train] step=173250 tokens=2838.5M loss=2.0761 lr=3.20e-05 tok/s=12484
[train] step=173260 tokens=2838.7M loss=2.4571 lr=3.20e-05 tok/s=12484
```
