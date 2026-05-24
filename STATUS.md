# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 14:42:57 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2974M / 3000M (99.1%) |
| Step | 181510 |
| Latest loss | 1.8714 |
| Avg loss (last 30 logged) | 2.1099 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 0:34:50 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.70 -> 2.44 -> 1.97 -> 2.08 -> 2.05 -> 2.19 -> 2.11 -> 2.30 -> 2.61 -> 1.86 -> 2.41 -> 1.86

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_170899_tokens_2800M.pt`
- `step_177002_tokens_2900M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=181400 tokens=2972.1M loss=1.9367 lr=3.01e-05 tok/s=12484
[train] step=181410 tokens=2972.2M loss=2.3369 lr=3.01e-05 tok/s=12484
[train] step=181420 tokens=2972.4M loss=2.1741 lr=3.01e-05 tok/s=12484
[train] step=181430 tokens=2972.5M loss=2.4905 lr=3.01e-05 tok/s=12484
[train] step=181440 tokens=2972.7M loss=1.9983 lr=3.01e-05 tok/s=12484
[train] step=181450 tokens=2972.9M loss=2.0034 lr=3.01e-05 tok/s=12484
[train] step=181460 tokens=2973.0M loss=2.3362 lr=3.01e-05 tok/s=12484
[train] step=181470 tokens=2973.2M loss=2.1088 lr=3.01e-05 tok/s=12484
[train] step=181480 tokens=2973.4M loss=1.8560 lr=3.01e-05 tok/s=12484
[train] step=181490 tokens=2973.5M loss=2.9160 lr=3.01e-05 tok/s=12484
[train] step=181500 tokens=2973.7M loss=1.8451 lr=3.01e-05 tok/s=12484
[train] step=181510 tokens=2973.9M loss=1.8714 lr=3.01e-05 tok/s=12484
```
