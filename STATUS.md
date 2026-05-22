# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 06:04:16 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 428M / 3000M (14.3%) |
| Step | 26130 |
| Latest loss | 2.4977 |
| Avg loss (last 30 logged) | 2.4628 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 2 days, 9:13:19 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.46 -> 2.54 -> 2.51 -> 2.45 -> 2.08 -> 2.56 -> 2.48 -> 2.55 -> 2.35 -> 2.16 -> 2.25 -> 2.27

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=26020 tokens=426.3M loss=2.1490 lr=2.88e-04 tok/s=12485
[train] step=26030 tokens=426.5M loss=2.4503 lr=2.88e-04 tok/s=12485
[train] step=26040 tokens=426.6M loss=2.4143 lr=2.88e-04 tok/s=12485
[train] step=26050 tokens=426.8M loss=2.3045 lr=2.88e-04 tok/s=12485
[train] step=26060 tokens=427.0M loss=2.0762 lr=2.88e-04 tok/s=12485
[train] step=26070 tokens=427.1M loss=2.3695 lr=2.88e-04 tok/s=12485
[train] step=26080 tokens=427.3M loss=2.5638 lr=2.88e-04 tok/s=12485
[train] step=26090 tokens=427.5M loss=2.6067 lr=2.88e-04 tok/s=12485
[train] step=26100 tokens=427.6M loss=2.4404 lr=2.88e-04 tok/s=12485
[train] step=26110 tokens=427.8M loss=2.2719 lr=2.88e-04 tok/s=12485
[train] step=26120 tokens=428.0M loss=2.6861 lr=2.88e-04 tok/s=12485
[train] step=26130 tokens=428.1M loss=2.4977 lr=2.88e-04 tok/s=12485
```
