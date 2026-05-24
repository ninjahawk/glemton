# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 06:51:48 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2622M / 3000M (87.4%) |
| Step | 160020 |
| Latest loss | 1.8443 |
| Avg loss (last 30 logged) | 2.0665 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 8:24:42 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.10 -> 1.90 -> 2.29 -> 2.25 -> 2.21 -> 2.31 -> 1.96 -> 2.04 -> 2.17 -> 2.41 -> 1.80 -> 1.60

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=159910 tokens=2620.0M loss=2.1113 lr=4.07e-05 tok/s=12489
[train] step=159920 tokens=2620.1M loss=1.7243 lr=4.07e-05 tok/s=12489
[train] step=159930 tokens=2620.3M loss=1.8003 lr=4.07e-05 tok/s=12489
[train] step=159940 tokens=2620.5M loss=2.4851 lr=4.07e-05 tok/s=12489
[train] step=159950 tokens=2620.6M loss=2.2867 lr=4.07e-05 tok/s=12489
[train] step=159960 tokens=2620.8M loss=2.3316 lr=4.07e-05 tok/s=12489
[train] step=159970 tokens=2620.9M loss=2.4670 lr=4.07e-05 tok/s=12489
[train] step=159980 tokens=2621.1M loss=2.2794 lr=4.07e-05 tok/s=12489
[train] step=159990 tokens=2621.3M loss=2.1992 lr=4.07e-05 tok/s=12489
[train] step=160000 tokens=2621.4M loss=1.5957 lr=4.06e-05 tok/s=12489
[train] step=160010 tokens=2621.6M loss=2.2511 lr=4.06e-05 tok/s=12489
[train] step=160020 tokens=2621.8M loss=1.8443 lr=4.06e-05 tok/s=12489
```
