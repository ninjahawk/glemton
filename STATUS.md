# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 17:26:06 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 939M / 3000M (31.3%) |
| Step | 57300 |
| Latest loss | 2.5329 |
| Avg loss (last 30 logged) | 2.2720 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 21:51:34 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.45 -> 2.56 -> 2.18 -> 2.36 -> 2.70 -> 2.19 -> 2.01 -> 2.23 -> 2.08 -> 2.73 -> 2.43 -> 2.23

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=57190 tokens=937.0M loss=2.4545 lr=2.42e-04 tok/s=12485
[train] step=57200 tokens=937.2M loss=2.3620 lr=2.42e-04 tok/s=12485
[train] step=57210 tokens=937.3M loss=2.1573 lr=2.42e-04 tok/s=12485
[train] step=57220 tokens=937.5M loss=2.3982 lr=2.42e-04 tok/s=12485
[train] step=57230 tokens=937.7M loss=1.9828 lr=2.42e-04 tok/s=12485
[train] step=57240 tokens=937.8M loss=2.1477 lr=2.42e-04 tok/s=12485
[train] step=57250 tokens=938.0M loss=2.2219 lr=2.42e-04 tok/s=12485
[train] step=57260 tokens=938.1M loss=2.1178 lr=2.42e-04 tok/s=12485
[train] step=57270 tokens=938.3M loss=2.1276 lr=2.42e-04 tok/s=12485
[train] step=57280 tokens=938.5M loss=2.2273 lr=2.42e-04 tok/s=12485
[train] step=57290 tokens=938.6M loss=1.9328 lr=2.42e-04 tok/s=12485
[train] step=57300 tokens=938.8M loss=2.5329 lr=2.42e-04 tok/s=12485
```
