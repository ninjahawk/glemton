# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 19:40:04 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2119M / 3000M (70.6%) |
| Step | 129310 |
| Latest loss | 2.2207 |
| Avg loss (last 30 logged) | 1.9822 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 19:36:08 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.91 -> 2.15 -> 2.15 -> 1.99 -> 2.27 -> 1.92 -> 1.86 -> 1.93 -> 2.14 -> 2.35 -> 2.06 -> 2.07

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
[train] step=129200 tokens=2116.8M loss=2.1041 lr=8.46e-05 tok/s=12490
[train] step=129210 tokens=2117.0M loss=2.0252 lr=8.46e-05 tok/s=12490
[train] step=129220 tokens=2117.1M loss=1.5889 lr=8.45e-05 tok/s=12490
[train] step=129230 tokens=2117.3M loss=1.9581 lr=8.45e-05 tok/s=12490
[train] step=129240 tokens=2117.5M loss=2.1423 lr=8.45e-05 tok/s=12490
[train] step=129250 tokens=2117.6M loss=1.9012 lr=8.45e-05 tok/s=12490
[train] step=129260 tokens=2117.8M loss=1.8097 lr=8.45e-05 tok/s=12490
[train] step=129270 tokens=2118.0M loss=2.4891 lr=8.44e-05 tok/s=12490
[train] step=129280 tokens=2118.1M loss=2.1237 lr=8.44e-05 tok/s=12490
[train] step=129290 tokens=2118.3M loss=2.0705 lr=8.44e-05 tok/s=12490
[train] step=129300 tokens=2118.5M loss=1.9986 lr=8.44e-05 tok/s=12490
[train] step=129310 tokens=2118.6M loss=2.2207 lr=8.44e-05 tok/s=12490
```
