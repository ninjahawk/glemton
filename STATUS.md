# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 21:20:19 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2194M / 3000M (73.1%) |
| Step | 133890 |
| Latest loss | 1.9639 |
| Avg loss (last 30 logged) | 2.0804 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 17:56:00 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.99 -> 2.55 -> 2.31 -> 2.17 -> 2.18 -> 2.09 -> 2.05 -> 1.89 -> 1.69 -> 2.04 -> 1.72 -> 1.98

## Checkpoints on disk
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=133780 tokens=2191.9M loss=2.0803 lr=7.62e-05 tok/s=12489
[train] step=133790 tokens=2192.0M loss=1.7205 lr=7.62e-05 tok/s=12489
[train] step=133800 tokens=2192.2M loss=2.3707 lr=7.62e-05 tok/s=12489
[train] step=133810 tokens=2192.3M loss=1.6255 lr=7.62e-05 tok/s=12489
[train] step=133820 tokens=2192.5M loss=2.0238 lr=7.62e-05 tok/s=12489
[train] step=133830 tokens=2192.7M loss=1.8454 lr=7.62e-05 tok/s=12489
[train] step=133840 tokens=2192.8M loss=1.8451 lr=7.61e-05 tok/s=12489
[train] step=133850 tokens=2193.0M loss=1.6314 lr=7.61e-05 tok/s=12489
[train] step=133860 tokens=2193.2M loss=1.9783 lr=7.61e-05 tok/s=12489
[train] step=133870 tokens=2193.3M loss=2.6890 lr=7.61e-05 tok/s=12489
[train] step=133880 tokens=2193.5M loss=2.2996 lr=7.61e-05 tok/s=12489
[train] step=133890 tokens=2193.7M loss=1.9639 lr=7.61e-05 tok/s=12489
```
