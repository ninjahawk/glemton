# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 16:19:33 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1968M / 3000M (65.6%) |
| Step | 120140 |
| Latest loss | 2.0430 |
| Avg loss (last 30 logged) | 2.0673 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 22:56:40 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.04 -> 2.08 -> 2.05 -> 1.85 -> 2.22 -> 1.80 -> 1.75 -> 1.92 -> 2.37 -> 2.22 -> 2.08 -> 1.62

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=120030 tokens=1966.6M loss=1.9415 lr=1.03e-04 tok/s=12489
[train] step=120040 tokens=1966.7M loss=2.1133 lr=1.03e-04 tok/s=12489
[train] step=120050 tokens=1966.9M loss=2.3213 lr=1.03e-04 tok/s=12489
[train] step=120060 tokens=1967.1M loss=2.0734 lr=1.03e-04 tok/s=12489
[train] step=120070 tokens=1967.2M loss=2.2937 lr=1.03e-04 tok/s=12489
[train] step=120080 tokens=1967.4M loss=2.1475 lr=1.03e-04 tok/s=12489
[train] step=120090 tokens=1967.6M loss=1.7846 lr=1.03e-04 tok/s=12489
[train] step=120100 tokens=1967.7M loss=2.2500 lr=1.03e-04 tok/s=12489
[train] step=120110 tokens=1967.9M loss=1.6178 lr=1.03e-04 tok/s=12489
[train] step=120120 tokens=1968.0M loss=1.7631 lr=1.03e-04 tok/s=12489
[train] step=120130 tokens=1968.2M loss=1.8756 lr=1.03e-04 tok/s=12489
[train] step=120140 tokens=1968.4M loss=2.0430 lr=1.02e-04 tok/s=12489
```
