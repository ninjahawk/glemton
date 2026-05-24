# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 12:32:40 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2876M / 3000M (95.9%) |
| Step | 175550 |
| Latest loss | 1.7063 |
| Avg loss (last 30 logged) | 2.0298 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2:45:16 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.28 -> 2.12 -> 2.02 -> 2.35 -> 2.15 -> 2.21 -> 1.99 -> 1.91 -> 2.22 -> 2.30 -> 2.38 -> 2.01

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
[train] step=175440 tokens=2874.4M loss=1.8127 lr=3.12e-05 tok/s=12484
[train] step=175450 tokens=2874.6M loss=2.1553 lr=3.12e-05 tok/s=12484
[train] step=175460 tokens=2874.7M loss=2.3787 lr=3.12e-05 tok/s=12484
[train] step=175470 tokens=2874.9M loss=2.0013 lr=3.12e-05 tok/s=12484
[train] step=175480 tokens=2875.1M loss=1.9487 lr=3.12e-05 tok/s=12484
[train] step=175490 tokens=2875.2M loss=2.1968 lr=3.12e-05 tok/s=12484
[train] step=175500 tokens=2875.4M loss=2.1238 lr=3.12e-05 tok/s=12484
[train] step=175510 tokens=2875.6M loss=2.0898 lr=3.12e-05 tok/s=12484
[train] step=175520 tokens=2875.7M loss=2.0147 lr=3.12e-05 tok/s=12484
[train] step=175530 tokens=2875.9M loss=1.9728 lr=3.12e-05 tok/s=12484
[train] step=175540 tokens=2876.0M loss=2.0448 lr=3.12e-05 tok/s=12484
[train] step=175550 tokens=2876.2M loss=1.7063 lr=3.12e-05 tok/s=12484
```
