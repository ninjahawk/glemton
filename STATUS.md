# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 05:31:35 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2562M / 3000M (85.4%) |
| Step | 156360 |
| Latest loss | 1.3965 |
| Avg loss (last 30 logged) | 2.0274 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 9:44:46 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.24 -> 1.91 -> 2.10 -> 2.28 -> 2.00 -> 2.32 -> 2.51 -> 1.68 -> 1.89 -> 1.77 -> 1.91 -> 2.22

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=156250 tokens=2560.0M loss=2.0867 lr=4.43e-05 tok/s=12489
[train] step=156260 tokens=2560.2M loss=2.1349 lr=4.43e-05 tok/s=12489
[train] step=156270 tokens=2560.3M loss=2.0827 lr=4.43e-05 tok/s=12489
[train] step=156280 tokens=2560.5M loss=1.8183 lr=4.43e-05 tok/s=12489
[train] step=156290 tokens=2560.7M loss=1.7267 lr=4.43e-05 tok/s=12489
[train] step=156300 tokens=2560.8M loss=2.6309 lr=4.43e-05 tok/s=12489
[train] step=156310 tokens=2561.0M loss=2.1123 lr=4.42e-05 tok/s=12489
[train] step=156320 tokens=2561.1M loss=2.2709 lr=4.42e-05 tok/s=12489
[train] step=156330 tokens=2561.3M loss=1.9299 lr=4.42e-05 tok/s=12489
[train] step=156340 tokens=2561.5M loss=2.2204 lr=4.42e-05 tok/s=12489
[train] step=156350 tokens=2561.6M loss=2.3713 lr=4.42e-05 tok/s=12489
[train] step=156360 tokens=2561.8M loss=1.3965 lr=4.42e-05 tok/s=12489
```
