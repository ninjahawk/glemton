# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-21 22:53:04 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 105M / 3000M (3.5%) |
| Step | 6410 |
| Latest loss | 2.6072 |
| Avg loss (last 30 logged) | 2.7529 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 2 days, 16:24:19 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.77 -> 2.95 -> 3.06 -> 3.12 -> 2.73 -> 2.67 -> 2.62 -> 2.85 -> 2.69 -> 2.78 -> 2.49 -> 2.73

## Checkpoints on disk
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=6300 tokens=103.2M loss=2.6162 lr=3.00e-04 tok/s=12485
[train] step=6310 tokens=103.4M loss=2.5919 lr=3.00e-04 tok/s=12485
[train] step=6320 tokens=103.5M loss=2.8990 lr=3.00e-04 tok/s=12485
[train] step=6330 tokens=103.7M loss=2.8505 lr=3.00e-04 tok/s=12485
[train] step=6340 tokens=103.9M loss=2.6258 lr=3.00e-04 tok/s=12485
[train] step=6350 tokens=104.0M loss=2.7163 lr=3.00e-04 tok/s=12485
[train] step=6360 tokens=104.2M loss=2.4443 lr=3.00e-04 tok/s=12486
[train] step=6370 tokens=104.4M loss=2.8641 lr=3.00e-04 tok/s=12486
[train] step=6380 tokens=104.5M loss=2.8108 lr=3.00e-04 tok/s=12486
[train] step=6390 tokens=104.7M loss=2.7328 lr=3.00e-04 tok/s=12486
[train] step=6400 tokens=104.9M loss=2.7184 lr=3.00e-04 tok/s=12486
[train] step=6410 tokens=105.0M loss=2.6072 lr=3.00e-04 tok/s=12486
```
