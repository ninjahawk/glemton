# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 23:40:41 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2299M / 3000M (76.6%) |
| Step | 140310 |
| Latest loss | 1.6380 |
| Avg loss (last 30 logged) | 2.1113 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 15:35:45 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.11 -> 1.94 -> 1.99 -> 2.15 -> 2.30 -> 2.16 -> 2.62 -> 1.89 -> 2.18 -> 2.38 -> 1.82 -> 2.07

## Checkpoints on disk
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=140200 tokens=2297.0M loss=2.0299 lr=6.55e-05 tok/s=12489
[train] step=140210 tokens=2297.2M loss=2.1693 lr=6.55e-05 tok/s=12489
[train] step=140220 tokens=2297.4M loss=1.5932 lr=6.55e-05 tok/s=12489
[train] step=140230 tokens=2297.5M loss=1.9466 lr=6.55e-05 tok/s=12489
[train] step=140240 tokens=2297.7M loss=1.5843 lr=6.55e-05 tok/s=12489
[train] step=140250 tokens=2297.9M loss=2.2426 lr=6.54e-05 tok/s=12489
[train] step=140260 tokens=2298.0M loss=2.0390 lr=6.54e-05 tok/s=12489
[train] step=140270 tokens=2298.2M loss=2.1965 lr=6.54e-05 tok/s=12489
[train] step=140280 tokens=2298.3M loss=2.0712 lr=6.54e-05 tok/s=12489
[train] step=140290 tokens=2298.5M loss=2.1109 lr=6.54e-05 tok/s=12489
[train] step=140300 tokens=2298.7M loss=2.0860 lr=6.54e-05 tok/s=12489
[train] step=140310 tokens=2298.8M loss=1.6380 lr=6.53e-05 tok/s=12489
```
