# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 05:41:37 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2569M / 3000M (85.6%) |
| Step | 156820 |
| Latest loss | 2.1996 |
| Avg loss (last 30 logged) | 2.1053 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 9:34:46 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.22 -> 1.55 -> 2.27 -> 2.06 -> 2.28 -> 2.35 -> 2.03 -> 1.75 -> 1.93 -> 2.03 -> 2.26 -> 2.28

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
[train] step=156710 tokens=2567.5M loss=2.0333 lr=4.38e-05 tok/s=12489
[train] step=156720 tokens=2567.7M loss=1.9730 lr=4.38e-05 tok/s=12489
[train] step=156730 tokens=2567.9M loss=1.7288 lr=4.38e-05 tok/s=12489
[train] step=156740 tokens=2568.0M loss=2.1191 lr=4.38e-05 tok/s=12489
[train] step=156750 tokens=2568.2M loss=2.1675 lr=4.38e-05 tok/s=12489
[train] step=156760 tokens=2568.4M loss=1.8373 lr=4.38e-05 tok/s=12489
[train] step=156770 tokens=2568.5M loss=2.7561 lr=4.38e-05 tok/s=12489
[train] step=156780 tokens=2568.7M loss=2.1317 lr=4.38e-05 tok/s=12489
[train] step=156790 tokens=2568.8M loss=2.2815 lr=4.38e-05 tok/s=12489
[train] step=156800 tokens=2569.0M loss=2.0226 lr=4.37e-05 tok/s=12489
[train] step=156810 tokens=2569.2M loss=2.3164 lr=4.37e-05 tok/s=12489
[train] step=156820 tokens=2569.3M loss=2.1996 lr=4.37e-05 tok/s=12489
```
