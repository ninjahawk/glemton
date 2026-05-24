# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 08:52:06 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2712M / 3000M (90.4%) |
| Step | 165530 |
| Latest loss | 2.1189 |
| Avg loss (last 30 logged) | 2.0786 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 6:24:20 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.28 -> 2.07 -> 2.13 -> 1.85 -> 2.03 -> 2.31 -> 2.02 -> 1.74 -> 2.25 -> 1.89 -> 1.64 -> 2.65

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=165420 tokens=2710.2M loss=1.8011 lr=3.63e-05 tok/s=12489
[train] step=165430 tokens=2710.4M loss=2.2156 lr=3.63e-05 tok/s=12489
[train] step=165440 tokens=2710.6M loss=2.0399 lr=3.63e-05 tok/s=12489
[train] step=165450 tokens=2710.7M loss=1.8401 lr=3.62e-05 tok/s=12489
[train] step=165460 tokens=2710.9M loss=2.0879 lr=3.62e-05 tok/s=12489
[train] step=165470 tokens=2711.1M loss=1.5150 lr=3.62e-05 tok/s=12489
[train] step=165480 tokens=2711.2M loss=1.9732 lr=3.62e-05 tok/s=12489
[train] step=165490 tokens=2711.4M loss=1.9237 lr=3.62e-05 tok/s=12489
[train] step=165500 tokens=2711.6M loss=2.1054 lr=3.62e-05 tok/s=12489
[train] step=165510 tokens=2711.7M loss=2.6469 lr=3.62e-05 tok/s=12489
[train] step=165520 tokens=2711.9M loss=1.9181 lr=3.62e-05 tok/s=12489
[train] step=165530 tokens=2712.0M loss=2.1189 lr=3.62e-05 tok/s=12489
```
