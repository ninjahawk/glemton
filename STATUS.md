# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 09:48:37 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1675M / 3000M (55.8%) |
| Step | 102250 |
| Latest loss | 1.8635 |
| Avg loss (last 30 logged) | 2.1477 |
| Throughput | 12,488 tok/s |
| ETA to 3B tokens | 1 day, 5:27:57 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.88 -> 2.51 -> 1.96 -> 2.26 -> 2.16 -> 2.44 -> 2.11 -> 1.89 -> 1.97 -> 2.26 -> 2.20 -> 2.02

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_79346_tokens_1300M.pt`
- `step_85450_tokens_1400M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=102140 tokens=1673.5M loss=2.1845 lr=1.42e-04 tok/s=12488
[train] step=102150 tokens=1673.6M loss=2.1105 lr=1.42e-04 tok/s=12488
[train] step=102160 tokens=1673.8M loss=2.3238 lr=1.42e-04 tok/s=12488
[train] step=102170 tokens=1674.0M loss=2.5789 lr=1.42e-04 tok/s=12488
[train] step=102180 tokens=1674.1M loss=1.8289 lr=1.42e-04 tok/s=12488
[train] step=102190 tokens=1674.3M loss=2.3574 lr=1.42e-04 tok/s=12488
[train] step=102200 tokens=1674.4M loss=2.0966 lr=1.42e-04 tok/s=12488
[train] step=102210 tokens=1674.6M loss=2.1251 lr=1.42e-04 tok/s=12488
[train] step=102220 tokens=1674.8M loss=2.0197 lr=1.42e-04 tok/s=12488
[train] step=102230 tokens=1674.9M loss=1.9507 lr=1.42e-04 tok/s=12488
[train] step=102240 tokens=1675.1M loss=2.3236 lr=1.42e-04 tok/s=12488
[train] step=102250 tokens=1675.3M loss=1.8635 lr=1.42e-04 tok/s=12488
```
