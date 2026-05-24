# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 09:32:12 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2741M / 3000M (91.4%) |
| Step | 167320 |
| Latest loss | 1.9931 |
| Avg loss (last 30 logged) | 2.0798 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 5:45:11 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.10 -> 2.08 -> 2.17 -> 1.84 -> 2.05 -> 2.11 -> 1.53 -> 2.15 -> 1.96 -> 1.74 -> 2.11 -> 2.18

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=167210 tokens=2739.6M loss=2.1051 lr=3.51e-05 tok/s=12486
[train] step=167220 tokens=2739.7M loss=2.0148 lr=3.51e-05 tok/s=12486
[train] step=167230 tokens=2739.9M loss=1.8903 lr=3.51e-05 tok/s=12486
[train] step=167240 tokens=2740.1M loss=1.9252 lr=3.51e-05 tok/s=12486
[train] step=167250 tokens=2740.2M loss=2.2960 lr=3.50e-05 tok/s=12486
[train] step=167260 tokens=2740.4M loss=2.0243 lr=3.50e-05 tok/s=12486
[train] step=167270 tokens=2740.6M loss=2.3630 lr=3.50e-05 tok/s=12486
[train] step=167280 tokens=2740.7M loss=1.8583 lr=3.50e-05 tok/s=12486
[train] step=167290 tokens=2740.9M loss=1.9145 lr=3.50e-05 tok/s=12486
[train] step=167300 tokens=2741.0M loss=2.1815 lr=3.50e-05 tok/s=12486
[train] step=167310 tokens=2741.2M loss=2.3078 lr=3.50e-05 tok/s=12486
[train] step=167320 tokens=2741.4M loss=1.9931 lr=3.50e-05 tok/s=12486
```
