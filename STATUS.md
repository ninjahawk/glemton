# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 00:10:46 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2321M / 3000M (77.4%) |
| Step | 141690 |
| Latest loss | 2.2640 |
| Avg loss (last 30 logged) | 2.0566 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 15:05:35 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.17 -> 2.00 -> 2.03 -> 2.15 -> 1.94 -> 2.05 -> 2.14 -> 1.80 -> 1.62 -> 2.20 -> 1.73 -> 1.52

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=141580 tokens=2319.6M loss=1.8969 lr=6.34e-05 tok/s=12489
[train] step=141590 tokens=2319.8M loss=2.0721 lr=6.34e-05 tok/s=12489
[train] step=141600 tokens=2320.0M loss=1.7852 lr=6.33e-05 tok/s=12489
[train] step=141610 tokens=2320.1M loss=1.8712 lr=6.33e-05 tok/s=12489
[train] step=141620 tokens=2320.3M loss=1.7205 lr=6.33e-05 tok/s=12489
[train] step=141630 tokens=2320.5M loss=2.0161 lr=6.33e-05 tok/s=12489
[train] step=141640 tokens=2320.6M loss=1.7447 lr=6.33e-05 tok/s=12489
[train] step=141650 tokens=2320.8M loss=1.8204 lr=6.33e-05 tok/s=12489
[train] step=141660 tokens=2321.0M loss=2.5074 lr=6.32e-05 tok/s=12489
[train] step=141670 tokens=2321.1M loss=1.5237 lr=6.32e-05 tok/s=12489
[train] step=141680 tokens=2321.3M loss=2.3778 lr=6.32e-05 tok/s=12489
[train] step=141690 tokens=2321.4M loss=2.2640 lr=6.32e-05 tok/s=12489
```
