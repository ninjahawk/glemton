# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 07:24:29 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 488M / 3000M (16.3%) |
| Step | 29790 |
| Latest loss | 2.3644 |
| Avg loss (last 30 logged) | 2.4561 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 2 days, 7:53:13 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.50 -> 2.39 -> 2.15 -> 2.23 -> 2.57 -> 2.29 -> 2.26 -> 3.24 -> 2.16 -> 2.69 -> 2.19 -> 2.36

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=29680 tokens=486.3M loss=2.4142 lr=2.84e-04 tok/s=12485
[train] step=29690 tokens=486.4M loss=2.5530 lr=2.84e-04 tok/s=12485
[train] step=29700 tokens=486.6M loss=2.3146 lr=2.84e-04 tok/s=12485
[train] step=29710 tokens=486.8M loss=2.5830 lr=2.84e-04 tok/s=12485
[train] step=29720 tokens=486.9M loss=2.0064 lr=2.84e-04 tok/s=12485
[train] step=29730 tokens=487.1M loss=2.9286 lr=2.84e-04 tok/s=12485
[train] step=29740 tokens=487.3M loss=2.5245 lr=2.84e-04 tok/s=12485
[train] step=29750 tokens=487.4M loss=2.2168 lr=2.84e-04 tok/s=12485
[train] step=29760 tokens=487.6M loss=2.3612 lr=2.84e-04 tok/s=12485
[train] step=29770 tokens=487.8M loss=2.3633 lr=2.84e-04 tok/s=12485
[train] step=29780 tokens=487.9M loss=2.3304 lr=2.84e-04 tok/s=12485
[train] step=29790 tokens=488.1M loss=2.3644 lr=2.84e-04 tok/s=12485
```
