# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 12:52:43 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2891M / 3000M (96.4%) |
| Step | 176460 |
| Latest loss | 2.3174 |
| Avg loss (last 30 logged) | 2.0387 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2:25:23 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
1.75 -> 2.25 -> 1.65 -> 2.17 -> 1.83 -> 1.86 -> 1.76 -> 1.80 -> 1.81 -> 2.26 -> 2.40 -> 2.02

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
[train] step=176350 tokens=2889.3M loss=2.0114 lr=3.09e-05 tok/s=12484
[train] step=176360 tokens=2889.5M loss=1.6199 lr=3.09e-05 tok/s=12484
[train] step=176370 tokens=2889.6M loss=1.8269 lr=3.09e-05 tok/s=12484
[train] step=176380 tokens=2889.8M loss=1.8849 lr=3.09e-05 tok/s=12484
[train] step=176390 tokens=2890.0M loss=2.2235 lr=3.09e-05 tok/s=12484
[train] step=176400 tokens=2890.1M loss=2.0743 lr=3.09e-05 tok/s=12484
[train] step=176410 tokens=2890.3M loss=2.0232 lr=3.09e-05 tok/s=12484
[train] step=176420 tokens=2890.5M loss=1.8248 lr=3.09e-05 tok/s=12484
[train] step=176430 tokens=2890.6M loss=2.0225 lr=3.09e-05 tok/s=12484
[train] step=176440 tokens=2890.8M loss=2.0283 lr=3.09e-05 tok/s=12484
[train] step=176450 tokens=2891.0M loss=2.4949 lr=3.09e-05 tok/s=12484
[train] step=176460 tokens=2891.1M loss=2.3174 lr=3.09e-05 tok/s=12484
```
