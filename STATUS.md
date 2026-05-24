# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 10:52:24 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2801M / 3000M (93.4%) |
| Step | 170960 |
| Latest loss | 1.7252 |
| Avg loss (last 30 logged) | 2.0881 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 4:25:40 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.31 -> 1.60 -> 1.89 -> 2.04 -> 2.04 -> 1.99 -> 2.15 -> 2.27 -> 1.69 -> 1.75 -> 2.50 -> 2.33

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_170899_tokens_2800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=170860 tokens=2799.4M loss=2.0317 lr=3.30e-05 tok/s=12484
[train] step=170870 tokens=2799.5M loss=2.2316 lr=3.30e-05 tok/s=12484
[train] step=170880 tokens=2799.7M loss=1.8673 lr=3.30e-05 tok/s=12484
[train] step=170890 tokens=2799.9M loss=1.7549 lr=3.30e-05 tok/s=12484
[train] checkpoint -> checkpoints\glemton-350m\step_170899_tokens_2800M.pt
[train] step=170900 tokens=2800.0M loss=2.0556 lr=3.30e-05 tok/s=12484
[train] step=170910 tokens=2800.2M loss=2.0750 lr=3.30e-05 tok/s=12484
[train] step=170920 tokens=2800.4M loss=2.2915 lr=3.30e-05 tok/s=12484
[train] step=170930 tokens=2800.5M loss=2.1929 lr=3.30e-05 tok/s=12484
[train] step=170940 tokens=2800.7M loss=2.3278 lr=3.30e-05 tok/s=12484
[train] step=170950 tokens=2800.8M loss=1.8513 lr=3.30e-05 tok/s=12484
[train] step=170960 tokens=2801.0M loss=1.7252 lr=3.30e-05 tok/s=12484
```
