# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 07:54:34 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 511M / 3000M (17.0%) |
| Step | 31170 |
| Latest loss | 2.6082 |
| Avg loss (last 30 logged) | 2.4004 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2 days, 7:23:19 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.38 -> 2.54 -> 2.21 -> 2.30 -> 2.37 -> 2.40 -> 2.52 -> 2.42 -> 2.19 -> 2.32 -> 2.42 -> 2.69

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_30518_tokens_500M.pt`

## Recent log tail
```
[train] step=31060 tokens=508.9M loss=2.0729 lr=2.83e-04 tok/s=12484
[train] step=31070 tokens=509.1M loss=2.1641 lr=2.83e-04 tok/s=12484
[train] step=31080 tokens=509.2M loss=2.3842 lr=2.83e-04 tok/s=12484
[train] step=31090 tokens=509.4M loss=2.5475 lr=2.83e-04 tok/s=12484
[train] step=31100 tokens=509.5M loss=2.4174 lr=2.83e-04 tok/s=12484
[train] step=31110 tokens=509.7M loss=2.7377 lr=2.83e-04 tok/s=12484
[train] step=31120 tokens=509.9M loss=2.1795 lr=2.83e-04 tok/s=12484
[train] step=31130 tokens=510.0M loss=2.9601 lr=2.83e-04 tok/s=12484
[train] step=31140 tokens=510.2M loss=2.5183 lr=2.83e-04 tok/s=12484
[train] step=31150 tokens=510.4M loss=2.6888 lr=2.83e-04 tok/s=12484
[train] step=31160 tokens=510.5M loss=2.1892 lr=2.83e-04 tok/s=12484
[train] step=31170 tokens=510.7M loss=2.6082 lr=2.83e-04 tok/s=12484
```
