# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 20:30:12 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2156M / 3000M (71.9%) |
| Step | 131600 |
| Latest loss | 2.4349 |
| Avg loss (last 30 logged) | 2.0698 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 18:46:06 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.05 -> 1.90 -> 1.76 -> 2.34 -> 2.49 -> 1.99 -> 1.61 -> 2.03 -> 2.11 -> 1.96 -> 1.75 -> 2.47

## Checkpoints on disk
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=131490 tokens=2154.3M loss=2.0464 lr=8.03e-05 tok/s=12490
[train] step=131500 tokens=2154.5M loss=2.3888 lr=8.03e-05 tok/s=12490
[train] step=131510 tokens=2154.7M loss=2.2222 lr=8.03e-05 tok/s=12490
[train] step=131520 tokens=2154.8M loss=1.6982 lr=8.03e-05 tok/s=12490
[train] step=131530 tokens=2155.0M loss=1.6457 lr=8.03e-05 tok/s=12490
[train] step=131540 tokens=2155.2M loss=1.9069 lr=8.03e-05 tok/s=12490
[train] step=131550 tokens=2155.3M loss=2.1801 lr=8.02e-05 tok/s=12490
[train] step=131560 tokens=2155.5M loss=2.0683 lr=8.02e-05 tok/s=12490
[train] step=131570 tokens=2155.6M loss=1.8076 lr=8.02e-05 tok/s=12490
[train] step=131580 tokens=2155.8M loss=2.4655 lr=8.02e-05 tok/s=12490
[train] step=131590 tokens=2156.0M loss=2.0684 lr=8.02e-05 tok/s=12490
[train] step=131600 tokens=2156.1M loss=2.4349 lr=8.01e-05 tok/s=12490
```
