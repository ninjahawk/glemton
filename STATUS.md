# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 09:22:11 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2734M / 3000M (91.1%) |
| Step | 166870 |
| Latest loss | 1.7687 |
| Avg loss (last 30 logged) | 2.0303 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 5:55:02 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.38 -> 1.98 -> 2.44 -> 2.27 -> 1.83 -> 2.50 -> 2.23 -> 2.12 -> 2.15 -> 2.11 -> 2.24 -> 2.05

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
[train] step=166760 tokens=2732.2M loss=1.9283 lr=3.54e-05 tok/s=12487
[train] step=166770 tokens=2732.4M loss=1.8770 lr=3.54e-05 tok/s=12487
[train] step=166780 tokens=2732.5M loss=1.9999 lr=3.53e-05 tok/s=12487
[train] step=166790 tokens=2732.7M loss=1.8828 lr=3.53e-05 tok/s=12487
[train] step=166800 tokens=2732.9M loss=1.9875 lr=3.53e-05 tok/s=12487
[train] step=166810 tokens=2733.0M loss=2.1053 lr=3.53e-05 tok/s=12487
[train] step=166820 tokens=2733.2M loss=1.8838 lr=3.53e-05 tok/s=12487
[train] step=166830 tokens=2733.3M loss=2.0349 lr=3.53e-05 tok/s=12487
[train] step=166840 tokens=2733.5M loss=1.9220 lr=3.53e-05 tok/s=12487
[train] step=166850 tokens=2733.7M loss=2.0544 lr=3.53e-05 tok/s=12487
[train] step=166860 tokens=2733.8M loss=2.2386 lr=3.53e-05 tok/s=12487
[train] step=166870 tokens=2734.0M loss=1.7687 lr=3.53e-05 tok/s=12487
```
