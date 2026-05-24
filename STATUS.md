# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 09:52:15 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2756M / 3000M (91.9%) |
| Step | 168210 |
| Latest loss | 1.8203 |
| Avg loss (last 30 logged) | 1.9968 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 5:25:45 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
2.48 -> 2.34 -> 2.09 -> 2.39 -> 1.87 -> 2.02 -> 2.17 -> 1.77 -> 2.28 -> 2.64 -> 1.86 -> 1.99

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
[train] step=168100 tokens=2754.2M loss=1.9584 lr=3.45e-05 tok/s=12484
[train] step=168110 tokens=2754.3M loss=2.2019 lr=3.45e-05 tok/s=12484
[train] step=168120 tokens=2754.5M loss=1.5855 lr=3.45e-05 tok/s=12484
[train] step=168130 tokens=2754.6M loss=1.7781 lr=3.45e-05 tok/s=12484
[train] step=168140 tokens=2754.8M loss=2.2720 lr=3.45e-05 tok/s=12484
[train] step=168150 tokens=2755.0M loss=2.2602 lr=3.45e-05 tok/s=12484
[train] step=168160 tokens=2755.1M loss=2.0029 lr=3.45e-05 tok/s=12484
[train] step=168170 tokens=2755.3M loss=2.2299 lr=3.45e-05 tok/s=12484
[train] step=168180 tokens=2755.5M loss=1.9738 lr=3.45e-05 tok/s=12484
[train] step=168190 tokens=2755.6M loss=1.9852 lr=3.45e-05 tok/s=12484
[train] step=168200 tokens=2755.8M loss=1.8112 lr=3.45e-05 tok/s=12484
[train] step=168210 tokens=2756.0M loss=1.8203 lr=3.45e-05 tok/s=12484
```
