# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 06:34:21 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 451M / 3000M (15.0%) |
| Step | 27500 |
| Latest loss | 2.9061 |
| Avg loss (last 30 logged) | 2.3892 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 2 days, 8:43:17 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.17 -> 2.40 -> 2.88 -> 2.57 -> 2.51 -> 2.28 -> 2.06 -> 2.37 -> 2.65 -> 2.35 -> 2.33 -> 2.23

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=27390 tokens=448.8M loss=2.4574 lr=2.87e-04 tok/s=12485
[train] step=27400 tokens=448.9M loss=2.5322 lr=2.87e-04 tok/s=12485
[train] step=27410 tokens=449.1M loss=2.2406 lr=2.87e-04 tok/s=12485
[train] step=27420 tokens=449.2M loss=2.4273 lr=2.87e-04 tok/s=12485
[train] step=27430 tokens=449.4M loss=2.3076 lr=2.87e-04 tok/s=12485
[train] step=27440 tokens=449.6M loss=2.1483 lr=2.87e-04 tok/s=12485
[train] step=27450 tokens=449.7M loss=2.5709 lr=2.87e-04 tok/s=12485
[train] step=27460 tokens=449.9M loss=2.2576 lr=2.87e-04 tok/s=12485
[train] step=27470 tokens=450.1M loss=2.5080 lr=2.87e-04 tok/s=12485
[train] step=27480 tokens=450.2M loss=2.2258 lr=2.87e-04 tok/s=12485
[train] step=27490 tokens=450.4M loss=2.2364 lr=2.87e-04 tok/s=12485
[train] step=27500 tokens=450.6M loss=2.9061 lr=2.87e-04 tok/s=12485
```
