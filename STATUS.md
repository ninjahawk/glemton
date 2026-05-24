# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 12:02:35 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2854M / 3000M (95.1%) |
| Step | 174170 |
| Latest loss | 1.4166 |
| Avg loss (last 30 logged) | 2.0317 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 3:15:27 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.73 -> 2.05 -> 2.41 -> 2.24 -> 2.18 -> 2.16 -> 1.93 -> 1.81 -> 1.78 -> 1.93 -> 1.85 -> 2.00

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_170899_tokens_2800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=174060 tokens=2851.8M loss=1.6771 lr=3.16e-05 tok/s=12484
[train] step=174070 tokens=2852.0M loss=1.8809 lr=3.16e-05 tok/s=12484
[train] step=174080 tokens=2852.1M loss=1.8800 lr=3.16e-05 tok/s=12484
[train] step=174090 tokens=2852.3M loss=2.5143 lr=3.16e-05 tok/s=12484
[train] step=174100 tokens=2852.5M loss=2.4043 lr=3.16e-05 tok/s=12484
[train] step=174110 tokens=2852.6M loss=1.9795 lr=3.16e-05 tok/s=12484
[train] step=174120 tokens=2852.8M loss=1.8298 lr=3.16e-05 tok/s=12484
[train] step=174130 tokens=2852.9M loss=1.8801 lr=3.16e-05 tok/s=12484
[train] step=174140 tokens=2853.1M loss=2.2320 lr=3.16e-05 tok/s=12484
[train] step=174150 tokens=2853.3M loss=1.9970 lr=3.16e-05 tok/s=12484
[train] step=174160 tokens=2853.4M loss=2.1252 lr=3.16e-05 tok/s=12484
[train] step=174170 tokens=2853.6M loss=1.4166 lr=3.16e-05 tok/s=12484
```
