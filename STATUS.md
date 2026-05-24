# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 08:42:05 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2704M / 3000M (90.2%) |
| Step | 165070 |
| Latest loss | 2.1582 |
| Avg loss (last 30 logged) | 2.1488 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 6:34:20 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.85 -> 1.95 -> 1.88 -> 2.33 -> 2.28 -> 1.68 -> 1.85 -> 2.18 -> 1.57 -> 1.73 -> 2.33 -> 2.06

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_140381_tokens_2300M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=164960 tokens=2702.7M loss=1.9181 lr=3.66e-05 tok/s=12489
[train] step=164970 tokens=2702.9M loss=1.9598 lr=3.66e-05 tok/s=12489
[train] step=164980 tokens=2703.0M loss=1.9776 lr=3.66e-05 tok/s=12489
[train] step=164990 tokens=2703.2M loss=2.0496 lr=3.66e-05 tok/s=12489
[train] step=165000 tokens=2703.4M loss=1.9676 lr=3.66e-05 tok/s=12489
[train] step=165010 tokens=2703.5M loss=1.9845 lr=3.66e-05 tok/s=12489
[train] step=165020 tokens=2703.7M loss=2.2325 lr=3.66e-05 tok/s=12489
[train] step=165030 tokens=2703.9M loss=1.8386 lr=3.65e-05 tok/s=12489
[train] step=165040 tokens=2704.0M loss=2.3487 lr=3.65e-05 tok/s=12489
[train] step=165050 tokens=2704.2M loss=2.0627 lr=3.65e-05 tok/s=12489
[train] step=165060 tokens=2704.3M loss=2.1912 lr=3.65e-05 tok/s=12489
[train] step=165070 tokens=2704.5M loss=2.1582 lr=3.65e-05 tok/s=12489
```
