# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 08:04:35 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 518M / 3000M (17.3%) |
| Step | 31630 |
| Latest loss | 2.4694 |
| Avg loss (last 30 logged) | 2.4108 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 7:13:18 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.43 -> 2.17 -> 2.49 -> 2.29 -> 2.63 -> 2.32 -> 2.61 -> 2.68 -> 2.44 -> 2.23 -> 2.47 -> 2.62

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`

## Recent log tail
```
[train] step=31520 tokens=516.4M loss=2.3716 lr=2.82e-04 tok/s=12484
[train] step=31530 tokens=516.6M loss=2.0156 lr=2.82e-04 tok/s=12484
[train] step=31540 tokens=516.8M loss=2.4935 lr=2.82e-04 tok/s=12484
[train] step=31550 tokens=516.9M loss=2.3852 lr=2.82e-04 tok/s=12484
[train] step=31560 tokens=517.1M loss=2.5172 lr=2.82e-04 tok/s=12484
[train] step=31570 tokens=517.2M loss=2.2974 lr=2.82e-04 tok/s=12484
[train] step=31580 tokens=517.4M loss=2.3030 lr=2.82e-04 tok/s=12484
[train] step=31590 tokens=517.6M loss=2.3405 lr=2.82e-04 tok/s=12484
[train] step=31600 tokens=517.7M loss=2.3157 lr=2.82e-04 tok/s=12484
[train] step=31610 tokens=517.9M loss=2.6227 lr=2.82e-04 tok/s=12484
[train] step=31620 tokens=518.1M loss=2.2788 lr=2.82e-04 tok/s=12484
[train] step=31630 tokens=518.2M loss=2.4694 lr=2.82e-04 tok/s=12484
```
