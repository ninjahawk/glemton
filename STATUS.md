# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 15:39:27 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1938M / 3000M (64.6%) |
| Step | 118300 |
| Latest loss | 2.1013 |
| Avg loss (last 30 logged) | 2.0668 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 23:36:58 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.06 -> 2.45 -> 2.16 -> 1.52 -> 1.86 -> 2.21 -> 2.37 -> 2.58 -> 2.43 -> 1.78 -> 1.71 -> 2.12

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=118190 tokens=1936.4M loss=2.2099 lr=1.07e-04 tok/s=12489
[train] step=118200 tokens=1936.6M loss=1.7195 lr=1.07e-04 tok/s=12489
[train] step=118210 tokens=1936.8M loss=1.6019 lr=1.07e-04 tok/s=12489
[train] step=118220 tokens=1936.9M loss=2.1567 lr=1.07e-04 tok/s=12489
[train] step=118230 tokens=1937.1M loss=2.4854 lr=1.06e-04 tok/s=12489
[train] step=118240 tokens=1937.2M loss=2.2113 lr=1.06e-04 tok/s=12489
[train] step=118250 tokens=1937.4M loss=2.2054 lr=1.06e-04 tok/s=12489
[train] step=118260 tokens=1937.6M loss=1.8130 lr=1.06e-04 tok/s=12489
[train] step=118270 tokens=1937.7M loss=2.1074 lr=1.06e-04 tok/s=12489
[train] step=118280 tokens=1937.9M loss=2.1242 lr=1.06e-04 tok/s=12489
[train] step=118290 tokens=1938.1M loss=2.5469 lr=1.06e-04 tok/s=12489
[train] step=118300 tokens=1938.2M loss=2.1013 lr=1.06e-04 tok/s=12489
```
