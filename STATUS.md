# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 14:32:55 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2966M / 3000M (98.9%) |
| Step | 181050 |
| Latest loss | 2.0327 |
| Avg loss (last 30 logged) | 2.0427 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 0:44:59 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.50 -> 2.31 -> 2.22 -> 1.95 -> 2.02 -> 2.31 -> 2.48 -> 2.45 -> 1.95 -> 1.92 -> 2.44 -> 2.04

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
[train] step=180940 tokens=2964.5M loss=1.6489 lr=3.01e-05 tok/s=12484
[train] step=180950 tokens=2964.7M loss=2.0866 lr=3.01e-05 tok/s=12484
[train] step=180960 tokens=2964.8M loss=1.8624 lr=3.01e-05 tok/s=12484
[train] step=180970 tokens=2965.0M loss=2.4249 lr=3.01e-05 tok/s=12484
[train] step=180980 tokens=2965.2M loss=2.2600 lr=3.01e-05 tok/s=12484
[train] step=180990 tokens=2965.3M loss=2.0801 lr=3.01e-05 tok/s=12484
[train] step=181000 tokens=2965.5M loss=1.8972 lr=3.01e-05 tok/s=12484
[train] step=181010 tokens=2965.7M loss=1.9894 lr=3.01e-05 tok/s=12484
[train] step=181020 tokens=2965.8M loss=2.0449 lr=3.01e-05 tok/s=12484
[train] step=181030 tokens=2966.0M loss=1.9204 lr=3.01e-05 tok/s=12484
[train] step=181040 tokens=2966.2M loss=2.4780 lr=3.01e-05 tok/s=12484
[train] step=181050 tokens=2966.3M loss=2.0327 lr=3.01e-05 tok/s=12484
```
