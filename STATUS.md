# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 15:29:15 local. Updated every ~10 min by `weekend_run.ps1`._

## State: COMPLETE - final.pt saved

| Metric | Value |
|---|---|
| Tokens seen | 3000M / 3000M (100.0%) |
| Step | 183100 |
| Latest loss | 2.3336 |
| Avg loss (last 30 logged) | 2.0576 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 0:00:08 |
| Projected finish | Sun 2026-05-24 15:29 |

## Loss trajectory (sampled)
2.24 -> 2.31 -> 1.98 -> 2.24 -> 2.09 -> 1.74 -> 2.00 -> 2.01 -> 1.44 -> 2.02 -> 2.00 -> 2.19

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_170899_tokens_2800M.pt`
- `step_177002_tokens_2900M.pt`
- `step_183106_tokens_3000M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=183010 tokens=2998.4M loss=2.1832 lr=3.00e-05 tok/s=12484
[train] step=183020 tokens=2998.6M loss=2.0383 lr=3.00e-05 tok/s=12484
[train] step=183030 tokens=2998.8M loss=1.7800 lr=3.00e-05 tok/s=12484
[train] step=183040 tokens=2998.9M loss=2.2469 lr=3.00e-05 tok/s=12484
[train] step=183050 tokens=2999.1M loss=1.8952 lr=3.00e-05 tok/s=12484
[train] step=183060 tokens=2999.3M loss=2.2748 lr=3.00e-05 tok/s=12484
[train] step=183070 tokens=2999.4M loss=2.3000 lr=3.00e-05 tok/s=12484
[train] step=183080 tokens=2999.6M loss=2.2164 lr=3.00e-05 tok/s=12484
[train] step=183090 tokens=2999.7M loss=2.1854 lr=3.00e-05 tok/s=12484
[train] step=183100 tokens=2999.9M loss=2.3336 lr=3.00e-05 tok/s=12484
[train] checkpoint -> checkpoints\glemton-350m\step_183106_tokens_3000M.pt
[train] final checkpoint -> checkpoints\glemton-350m\final.pt
```
