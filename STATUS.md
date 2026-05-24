# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 03:31:16 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2472M / 3000M (82.4%) |
| Step | 150860 |
| Latest loss | 1.2351 |
| Avg loss (last 30 logged) | 2.0246 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 11:45:01 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.85 -> 1.56 -> 1.78 -> 2.04 -> 1.97 -> 2.05 -> 1.95 -> 2.39 -> 2.22 -> 1.97 -> 1.98 -> 1.96

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=150750 tokens=2469.9M loss=2.3666 lr=5.06e-05 tok/s=12489
[train] step=150760 tokens=2470.1M loss=2.2844 lr=5.06e-05 tok/s=12489
[train] step=150770 tokens=2470.2M loss=1.8085 lr=5.06e-05 tok/s=12489
[train] step=150780 tokens=2470.4M loss=2.5228 lr=5.06e-05 tok/s=12489
[train] step=150790 tokens=2470.5M loss=1.7017 lr=5.06e-05 tok/s=12489
[train] step=150800 tokens=2470.7M loss=1.7666 lr=5.05e-05 tok/s=12489
[train] step=150810 tokens=2470.9M loss=2.2064 lr=5.05e-05 tok/s=12489
[train] step=150820 tokens=2471.0M loss=2.1771 lr=5.05e-05 tok/s=12489
[train] step=150830 tokens=2471.2M loss=1.9607 lr=5.05e-05 tok/s=12489
[train] step=150840 tokens=2471.4M loss=2.2340 lr=5.05e-05 tok/s=12489
[train] step=150850 tokens=2471.5M loss=2.6398 lr=5.05e-05 tok/s=12489
[train] step=150860 tokens=2471.7M loss=1.2351 lr=5.05e-05 tok/s=12489
```
