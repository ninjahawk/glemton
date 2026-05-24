# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 21:50:24 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2216M / 3000M (73.9%) |
| Step | 135270 |
| Latest loss | 2.4589 |
| Avg loss (last 30 logged) | 2.0268 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 17:25:51 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.89 -> 2.22 -> 1.90 -> 1.84 -> 2.24 -> 2.04 -> 2.52 -> 2.27 -> 1.96 -> 2.39 -> 2.32 -> 2.22

## Checkpoints on disk
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=135160 tokens=2214.5M loss=1.5934 lr=7.38e-05 tok/s=12489
[train] step=135170 tokens=2214.6M loss=1.8019 lr=7.38e-05 tok/s=12489
[train] step=135180 tokens=2214.8M loss=1.9728 lr=7.38e-05 tok/s=12489
[train] step=135190 tokens=2215.0M loss=1.7401 lr=7.38e-05 tok/s=12489
[train] step=135200 tokens=2215.1M loss=1.9280 lr=7.38e-05 tok/s=12489
[train] step=135210 tokens=2215.3M loss=1.9252 lr=7.38e-05 tok/s=12489
[train] step=135220 tokens=2215.4M loss=1.6434 lr=7.37e-05 tok/s=12489
[train] step=135230 tokens=2215.6M loss=1.9969 lr=7.37e-05 tok/s=12489
[train] step=135240 tokens=2215.8M loss=2.2808 lr=7.37e-05 tok/s=12489
[train] step=135250 tokens=2215.9M loss=2.2156 lr=7.37e-05 tok/s=12489
[train] step=135260 tokens=2216.1M loss=1.8786 lr=7.37e-05 tok/s=12489
[train] step=135270 tokens=2216.3M loss=2.4589 lr=7.37e-05 tok/s=12489
```
