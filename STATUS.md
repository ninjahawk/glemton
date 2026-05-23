# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 17:29:44 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2021M / 3000M (67.4%) |
| Step | 123350 |
| Latest loss | 1.5939 |
| Avg loss (last 30 logged) | 2.1312 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 21:46:28 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.42 -> 1.94 -> 1.75 -> 2.20 -> 1.87 -> 1.99 -> 1.93 -> 2.08 -> 2.53 -> 2.04 -> 2.10 -> 2.08

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=123240 tokens=2019.2M loss=2.2772 lr=9.62e-05 tok/s=12489
[train] step=123250 tokens=2019.3M loss=2.1385 lr=9.61e-05 tok/s=12489
[train] step=123260 tokens=2019.5M loss=1.9249 lr=9.61e-05 tok/s=12489
[train] step=123270 tokens=2019.7M loss=2.2253 lr=9.61e-05 tok/s=12489
[train] step=123280 tokens=2019.8M loss=2.0635 lr=9.61e-05 tok/s=12489
[train] step=123290 tokens=2020.0M loss=2.1092 lr=9.61e-05 tok/s=12489
[train] step=123300 tokens=2020.1M loss=2.4131 lr=9.60e-05 tok/s=12489
[train] step=123310 tokens=2020.3M loss=2.2510 lr=9.60e-05 tok/s=12489
[train] step=123320 tokens=2020.5M loss=2.5009 lr=9.60e-05 tok/s=12489
[train] step=123330 tokens=2020.6M loss=2.0831 lr=9.60e-05 tok/s=12489
[train] step=123340 tokens=2020.8M loss=2.4092 lr=9.60e-05 tok/s=12489
[train] step=123350 tokens=2021.0M loss=1.5939 lr=9.59e-05 tok/s=12489
```
