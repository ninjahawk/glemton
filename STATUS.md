# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 10:02:17 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2764M / 3000M (92.1%) |
| Step | 168670 |
| Latest loss | 1.7687 |
| Avg loss (last 30 logged) | 2.0769 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 5:15:44 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.23 -> 1.99 -> 1.64 -> 1.92 -> 2.24 -> 2.24 -> 2.58 -> 2.17 -> 1.74 -> 2.37 -> 2.09 -> 1.70

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
[train] step=168560 tokens=2761.7M loss=1.9633 lr=3.43e-05 tok/s=12484
[train] step=168570 tokens=2761.9M loss=1.8499 lr=3.42e-05 tok/s=12484
[train] step=168580 tokens=2762.0M loss=2.0872 lr=3.42e-05 tok/s=12484
[train] step=168590 tokens=2762.2M loss=2.1342 lr=3.42e-05 tok/s=12484
[train] step=168600 tokens=2762.3M loss=2.2308 lr=3.42e-05 tok/s=12484
[train] step=168610 tokens=2762.5M loss=2.0748 lr=3.42e-05 tok/s=12484
[train] step=168620 tokens=2762.7M loss=2.1135 lr=3.42e-05 tok/s=12484
[train] step=168630 tokens=2762.8M loss=2.0414 lr=3.42e-05 tok/s=12484
[train] step=168640 tokens=2763.0M loss=2.2792 lr=3.42e-05 tok/s=12484
[train] step=168650 tokens=2763.2M loss=1.6982 lr=3.42e-05 tok/s=12484
[train] step=168660 tokens=2763.3M loss=2.4432 lr=3.42e-05 tok/s=12484
[train] step=168670 tokens=2763.5M loss=1.7687 lr=3.42e-05 tok/s=12484
```
