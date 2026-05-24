# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 11:12:27 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2816M / 3000M (93.9%) |
| Step | 171880 |
| Latest loss | 2.0033 |
| Avg loss (last 30 logged) | 2.0728 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 4:05:30 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.76 -> 1.96 -> 2.18 -> 2.26 -> 2.01 -> 2.06 -> 2.00 -> 1.91 -> 2.23 -> 1.42 -> 1.90 -> 2.05

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
[train] step=171770 tokens=2814.3M loss=2.1985 lr=3.26e-05 tok/s=12484
[train] step=171780 tokens=2814.4M loss=1.9358 lr=3.26e-05 tok/s=12484
[train] step=171790 tokens=2814.6M loss=2.4198 lr=3.26e-05 tok/s=12484
[train] step=171800 tokens=2814.8M loss=1.9356 lr=3.26e-05 tok/s=12484
[train] step=171810 tokens=2814.9M loss=1.8921 lr=3.26e-05 tok/s=12484
[train] step=171820 tokens=2815.1M loss=2.6185 lr=3.26e-05 tok/s=12484
[train] step=171830 tokens=2815.3M loss=2.2197 lr=3.26e-05 tok/s=12484
[train] step=171840 tokens=2815.4M loss=2.1848 lr=3.26e-05 tok/s=12484
[train] step=171850 tokens=2815.6M loss=2.0629 lr=3.26e-05 tok/s=12484
[train] step=171860 tokens=2815.8M loss=2.0485 lr=3.25e-05 tok/s=12484
[train] step=171870 tokens=2815.9M loss=2.1291 lr=3.25e-05 tok/s=12484
[train] step=171880 tokens=2816.1M loss=2.0033 lr=3.25e-05 tok/s=12484
```
