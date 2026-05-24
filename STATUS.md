# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 13:12:46 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2906M / 3000M (96.9%) |
| Step | 177380 |
| Latest loss | 2.3141 |
| Avg loss (last 30 logged) | 2.0827 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2:05:13 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.24 -> 1.68 -> 1.98 -> 2.07 -> 1.89 -> 1.87 -> 1.86 -> 1.68 -> 1.83 -> 1.84 -> 1.87 -> 2.01

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
[train] step=177270 tokens=2904.4M loss=2.3582 lr=3.07e-05 tok/s=12484
[train] step=177280 tokens=2904.6M loss=1.6437 lr=3.07e-05 tok/s=12484
[train] step=177290 tokens=2904.7M loss=2.4132 lr=3.07e-05 tok/s=12484
[train] step=177300 tokens=2904.9M loss=1.7552 lr=3.07e-05 tok/s=12484
[train] step=177310 tokens=2905.0M loss=1.8175 lr=3.07e-05 tok/s=12484
[train] step=177320 tokens=2905.2M loss=1.9651 lr=3.07e-05 tok/s=12484
[train] step=177330 tokens=2905.4M loss=2.2646 lr=3.07e-05 tok/s=12484
[train] step=177340 tokens=2905.5M loss=2.1737 lr=3.07e-05 tok/s=12484
[train] step=177350 tokens=2905.7M loss=2.2180 lr=3.07e-05 tok/s=12484
[train] step=177360 tokens=2905.9M loss=2.0095 lr=3.07e-05 tok/s=12484
[train] step=177370 tokens=2906.0M loss=1.8291 lr=3.07e-05 tok/s=12484
[train] step=177380 tokens=2906.2M loss=2.3141 lr=3.07e-05 tok/s=12484
```
