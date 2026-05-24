# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 13:52:52 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2936M / 3000M (97.9%) |
| Step | 179210 |
| Latest loss | 2.2692 |
| Avg loss (last 30 logged) | 2.1123 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1:25:10 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.23 -> 1.36 -> 2.32 -> 1.88 -> 1.90 -> 1.83 -> 2.67 -> 1.97 -> 1.74 -> 1.96 -> 1.68 -> 1.73

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
[train] step=179100 tokens=2934.4M loss=2.5531 lr=3.03e-05 tok/s=12484
[train] step=179110 tokens=2934.5M loss=1.8568 lr=3.03e-05 tok/s=12484
[train] step=179120 tokens=2934.7M loss=1.4824 lr=3.03e-05 tok/s=12484
[train] step=179130 tokens=2934.9M loss=2.2504 lr=3.03e-05 tok/s=12484
[train] step=179140 tokens=2935.0M loss=1.9614 lr=3.03e-05 tok/s=12484
[train] step=179150 tokens=2935.2M loss=1.9594 lr=3.03e-05 tok/s=12484
[train] step=179160 tokens=2935.4M loss=2.3256 lr=3.03e-05 tok/s=12484
[train] step=179170 tokens=2935.5M loss=2.0544 lr=3.03e-05 tok/s=12484
[train] step=179180 tokens=2935.7M loss=1.9057 lr=3.03e-05 tok/s=12484
[train] step=179190 tokens=2935.8M loss=1.7342 lr=3.03e-05 tok/s=12484
[train] step=179200 tokens=2936.0M loss=2.1712 lr=3.03e-05 tok/s=12484
[train] step=179210 tokens=2936.2M loss=2.2692 lr=3.03e-05 tok/s=12484
```
