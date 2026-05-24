# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 13:32:49 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2921M / 3000M (97.4%) |
| Step | 178300 |
| Latest loss | 1.5727 |
| Avg loss (last 30 logged) | 2.0686 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 1:45:04 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.49 -> 2.43 -> 2.03 -> 1.99 -> 2.15 -> 2.06 -> 2.02 -> 2.07 -> 2.41 -> 1.74 -> 2.27 -> 1.82

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
[train] step=178190 tokens=2919.5M loss=2.7319 lr=3.05e-05 tok/s=12484
[train] step=178200 tokens=2919.6M loss=1.7394 lr=3.05e-05 tok/s=12484
[train] step=178210 tokens=2919.8M loss=2.1683 lr=3.05e-05 tok/s=12484
[train] step=178220 tokens=2920.0M loss=1.9995 lr=3.05e-05 tok/s=12484
[train] step=178230 tokens=2920.1M loss=2.0591 lr=3.05e-05 tok/s=12484
[train] step=178240 tokens=2920.3M loss=1.9377 lr=3.05e-05 tok/s=12484
[train] step=178250 tokens=2920.4M loss=1.8715 lr=3.05e-05 tok/s=12484
[train] step=178260 tokens=2920.6M loss=2.1403 lr=3.05e-05 tok/s=12484
[train] step=178270 tokens=2920.8M loss=2.0654 lr=3.05e-05 tok/s=12484
[train] step=178280 tokens=2920.9M loss=1.8214 lr=3.05e-05 tok/s=12484
[train] step=178290 tokens=2921.1M loss=1.7804 lr=3.05e-05 tok/s=12484
[train] step=178300 tokens=2921.3M loss=1.5727 lr=3.05e-05 tok/s=12484
```
