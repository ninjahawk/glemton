# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 00:20:47 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2329M / 3000M (77.6%) |
| Step | 142150 |
| Latest loss | 2.0520 |
| Avg loss (last 30 logged) | 2.0760 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 14:55:27 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.07 -> 1.89 -> 2.80 -> 2.07 -> 2.46 -> 2.35 -> 2.04 -> 2.57 -> 2.10 -> 2.02 -> 2.42 -> 1.84

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=142040 tokens=2327.2M loss=2.5788 lr=6.27e-05 tok/s=12489
[train] step=142050 tokens=2327.3M loss=1.6761 lr=6.26e-05 tok/s=12489
[train] step=142060 tokens=2327.5M loss=2.1555 lr=6.26e-05 tok/s=12489
[train] step=142070 tokens=2327.7M loss=1.7285 lr=6.26e-05 tok/s=12489
[train] step=142080 tokens=2327.8M loss=2.0821 lr=6.26e-05 tok/s=12489
[train] step=142090 tokens=2328.0M loss=2.3947 lr=6.26e-05 tok/s=12489
[train] step=142100 tokens=2328.2M loss=1.5555 lr=6.26e-05 tok/s=12489
[train] step=142110 tokens=2328.3M loss=2.0176 lr=6.26e-05 tok/s=12489
[train] step=142120 tokens=2328.5M loss=2.1359 lr=6.25e-05 tok/s=12489
[train] step=142130 tokens=2328.7M loss=1.8391 lr=6.25e-05 tok/s=12489
[train] step=142140 tokens=2328.8M loss=1.8466 lr=6.25e-05 tok/s=12489
[train] step=142150 tokens=2329.0M loss=2.0520 lr=6.25e-05 tok/s=12489
```
