# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 12:42:41 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2884M / 3000M (96.1%) |
| Step | 176010 |
| Latest loss | 2.0475 |
| Avg loss (last 30 logged) | 2.1551 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2:35:15 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.82 -> 2.10 -> 1.98 -> 2.07 -> 2.23 -> 2.30 -> 2.11 -> 2.45 -> 2.43 -> 2.03 -> 2.16 -> 2.55

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
[train] step=175900 tokens=2881.9M loss=1.6995 lr=3.10e-05 tok/s=12484
[train] step=175910 tokens=2882.1M loss=1.9116 lr=3.10e-05 tok/s=12484
[train] step=175920 tokens=2882.3M loss=2.3607 lr=3.10e-05 tok/s=12484
[train] step=175930 tokens=2882.4M loss=2.6614 lr=3.10e-05 tok/s=12484
[train] step=175940 tokens=2882.6M loss=1.7441 lr=3.10e-05 tok/s=12484
[train] step=175950 tokens=2882.8M loss=1.8329 lr=3.10e-05 tok/s=12484
[train] step=175960 tokens=2882.9M loss=2.7201 lr=3.10e-05 tok/s=12484
[train] step=175970 tokens=2883.1M loss=2.1483 lr=3.10e-05 tok/s=12484
[train] step=175980 tokens=2883.3M loss=2.5522 lr=3.10e-05 tok/s=12484
[train] step=175990 tokens=2883.4M loss=2.2123 lr=3.10e-05 tok/s=12484
[train] step=176000 tokens=2883.6M loss=1.8152 lr=3.10e-05 tok/s=12484
[train] step=176010 tokens=2883.7M loss=2.0475 lr=3.10e-05 tok/s=12484
```
