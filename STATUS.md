# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 14:02:54 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2944M / 3000M (98.1%) |
| Step | 179670 |
| Latest loss | 2.1716 |
| Avg loss (last 30 logged) | 2.0824 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1:15:09 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.05 -> 2.01 -> 1.88 -> 1.56 -> 2.17 -> 2.16 -> 2.01 -> 2.07 -> 2.13 -> 2.08 -> 2.36 -> 2.00

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
[train] step=179560 tokens=2941.9M loss=1.8756 lr=3.03e-05 tok/s=12484
[train] step=179570 tokens=2942.1M loss=2.0989 lr=3.03e-05 tok/s=12484
[train] step=179580 tokens=2942.2M loss=2.1768 lr=3.03e-05 tok/s=12484
[train] step=179590 tokens=2942.4M loss=1.9015 lr=3.02e-05 tok/s=12484
[train] step=179600 tokens=2942.6M loss=2.2490 lr=3.02e-05 tok/s=12484
[train] step=179610 tokens=2942.7M loss=1.8891 lr=3.02e-05 tok/s=12484
[train] step=179620 tokens=2942.9M loss=1.8846 lr=3.02e-05 tok/s=12484
[train] step=179630 tokens=2943.1M loss=2.0046 lr=3.02e-05 tok/s=12484
[train] step=179640 tokens=2943.2M loss=1.9941 lr=3.02e-05 tok/s=12484
[train] step=179650 tokens=2943.4M loss=2.0019 lr=3.02e-05 tok/s=12484
[train] step=179660 tokens=2943.5M loss=2.1751 lr=3.02e-05 tok/s=12484
[train] step=179670 tokens=2943.7M loss=2.1716 lr=3.02e-05 tok/s=12484
```
