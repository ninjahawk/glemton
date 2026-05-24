# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 09:42:14 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2748M / 3000M (91.6%) |
| Step | 167750 |
| Latest loss | 2.6304 |
| Avg loss (last 30 logged) | 2.0884 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 5:35:53 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.22 -> 2.15 -> 2.05 -> 2.33 -> 1.80 -> 1.58 -> 1.20 -> 2.44 -> 1.75 -> 2.49 -> 2.93 -> 2.03

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
[train] step=167640 tokens=2746.6M loss=1.6035 lr=3.48e-05 tok/s=12484
[train] step=167650 tokens=2746.8M loss=2.2565 lr=3.48e-05 tok/s=12484
[train] step=167660 tokens=2746.9M loss=1.7440 lr=3.48e-05 tok/s=12484
[train] step=167670 tokens=2747.1M loss=1.9397 lr=3.48e-05 tok/s=12484
[train] step=167680 tokens=2747.3M loss=1.8796 lr=3.48e-05 tok/s=12484
[train] step=167690 tokens=2747.4M loss=2.2730 lr=3.48e-05 tok/s=12484
[train] step=167700 tokens=2747.6M loss=2.1102 lr=3.48e-05 tok/s=12484
[train] step=167710 tokens=2747.8M loss=1.9539 lr=3.48e-05 tok/s=12484
[train] step=167720 tokens=2747.9M loss=2.0850 lr=3.48e-05 tok/s=12484
[train] step=167730 tokens=2748.1M loss=2.0260 lr=3.47e-05 tok/s=12484
[train] step=167740 tokens=2748.3M loss=2.1531 lr=3.47e-05 tok/s=12484
[train] step=167750 tokens=2748.4M loss=2.6304 lr=3.47e-05 tok/s=12484
```
