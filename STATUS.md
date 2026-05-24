# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 15:13:01 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2996M / 3000M (99.9%) |
| Step | 182880 |
| Latest loss | 2.0352 |
| Avg loss (last 30 logged) | 2.0441 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 0:04:56 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.94 -> 2.21 -> 2.08 -> 1.75 -> 2.38 -> 2.02 -> 1.65 -> 1.90 -> 1.89 -> 2.75 -> 2.01 -> 1.39

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
[train] step=182770 tokens=2994.5M loss=2.0489 lr=3.00e-05 tok/s=12484
[train] step=182780 tokens=2994.7M loss=2.5813 lr=3.00e-05 tok/s=12484
[train] step=182790 tokens=2994.8M loss=1.9467 lr=3.00e-05 tok/s=12484
[train] step=182800 tokens=2995.0M loss=1.9825 lr=3.00e-05 tok/s=12484
[train] step=182810 tokens=2995.2M loss=1.8460 lr=3.00e-05 tok/s=12484
[train] step=182820 tokens=2995.3M loss=2.6171 lr=3.00e-05 tok/s=12484
[train] step=182830 tokens=2995.5M loss=1.8868 lr=3.00e-05 tok/s=12484
[train] step=182840 tokens=2995.7M loss=2.0187 lr=3.00e-05 tok/s=12484
[train] step=182850 tokens=2995.8M loss=1.3854 lr=3.00e-05 tok/s=12484
[train] step=182860 tokens=2996.0M loss=2.0224 lr=3.00e-05 tok/s=12484
[train] step=182870 tokens=2996.1M loss=2.5512 lr=3.00e-05 tok/s=12484
[train] step=182880 tokens=2996.3M loss=2.0352 lr=3.00e-05 tok/s=12484
```
