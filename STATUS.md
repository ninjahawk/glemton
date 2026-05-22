# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 17:36:07 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 946M / 3000M (31.5%) |
| Step | 57760 |
| Latest loss | 2.1860 |
| Avg loss (last 30 logged) | 2.3244 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 21:41:33 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.20 -> 2.35 -> 2.21 -> 2.16 -> 2.24 -> 2.18 -> 2.37 -> 2.17 -> 2.28 -> 2.89 -> 2.23 -> 2.08

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_36622_tokens_600M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`

## Recent log tail
```
[train] step=57650 tokens=944.5M loss=2.2464 lr=2.41e-04 tok/s=12485
[train] step=57660 tokens=944.7M loss=2.5454 lr=2.41e-04 tok/s=12485
[train] step=57670 tokens=944.9M loss=1.9654 lr=2.41e-04 tok/s=12485
[train] step=57680 tokens=945.0M loss=2.3973 lr=2.41e-04 tok/s=12485
[train] step=57690 tokens=945.2M loss=1.9952 lr=2.41e-04 tok/s=12485
[train] step=57700 tokens=945.4M loss=2.6086 lr=2.41e-04 tok/s=12485
[train] step=57710 tokens=945.5M loss=2.0883 lr=2.41e-04 tok/s=12485
[train] step=57720 tokens=945.7M loss=2.1847 lr=2.41e-04 tok/s=12485
[train] step=57730 tokens=945.8M loss=2.2678 lr=2.41e-04 tok/s=12485
[train] step=57740 tokens=946.0M loss=2.0783 lr=2.41e-04 tok/s=12485
[train] step=57750 tokens=946.2M loss=2.5069 lr=2.41e-04 tok/s=12485
[train] step=57760 tokens=946.3M loss=2.1860 lr=2.41e-04 tok/s=12485
```
