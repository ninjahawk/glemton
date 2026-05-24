# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 20:40:13 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2164M / 3000M (72.1%) |
| Step | 132060 |
| Latest loss | 2.4197 |
| Avg loss (last 30 logged) | 2.1268 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 18:35:57 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.93 -> 2.25 -> 2.25 -> 2.00 -> 2.07 -> 2.16 -> 2.36 -> 2.36 -> 2.13 -> 2.12 -> 1.97 -> 1.65

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
[train] step=131950 tokens=2161.9M loss=2.2244 lr=7.95e-05 tok/s=12490
[train] step=131960 tokens=2162.0M loss=2.1337 lr=7.95e-05 tok/s=12490
[train] step=131970 tokens=2162.2M loss=2.1964 lr=7.95e-05 tok/s=12490
[train] step=131980 tokens=2162.4M loss=2.1703 lr=7.95e-05 tok/s=12490
[train] step=131990 tokens=2162.5M loss=2.0330 lr=7.94e-05 tok/s=12490
[train] step=132000 tokens=2162.7M loss=2.1964 lr=7.94e-05 tok/s=12490
[train] step=132010 tokens=2162.9M loss=1.9648 lr=7.94e-05 tok/s=12490
[train] step=132020 tokens=2163.0M loss=2.0144 lr=7.94e-05 tok/s=12490
[train] step=132030 tokens=2163.2M loss=2.4762 lr=7.94e-05 tok/s=12490
[train] step=132040 tokens=2163.3M loss=1.6540 lr=7.94e-05 tok/s=12490
[train] step=132050 tokens=2163.5M loss=2.1032 lr=7.93e-05 tok/s=12490
[train] step=132060 tokens=2163.7M loss=2.4197 lr=7.93e-05 tok/s=12490
```
