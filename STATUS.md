# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 12:22:38 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2869M / 3000M (95.6%) |
| Step | 175090 |
| Latest loss | 1.8724 |
| Avg loss (last 30 logged) | 2.0581 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 2:55:17 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.42 -> 1.97 -> 1.86 -> 2.51 -> 2.24 -> 1.67 -> 2.00 -> 2.15 -> 1.88 -> 1.89 -> 1.65 -> 2.15

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
[train] step=174980 tokens=2866.9M loss=2.4285 lr=3.13e-05 tok/s=12484
[train] step=174990 tokens=2867.0M loss=2.4294 lr=3.13e-05 tok/s=12484
[train] step=175000 tokens=2867.2M loss=2.0272 lr=3.13e-05 tok/s=12484
[train] step=175010 tokens=2867.4M loss=2.2236 lr=3.13e-05 tok/s=12484
[train] step=175020 tokens=2867.5M loss=1.7548 lr=3.13e-05 tok/s=12484
[train] step=175030 tokens=2867.7M loss=2.0659 lr=3.13e-05 tok/s=12484
[train] step=175040 tokens=2867.9M loss=1.9511 lr=3.13e-05 tok/s=12484
[train] step=175050 tokens=2868.0M loss=1.8941 lr=3.13e-05 tok/s=12484
[train] step=175060 tokens=2868.2M loss=2.1475 lr=3.13e-05 tok/s=12484
[train] step=175070 tokens=2868.3M loss=2.0429 lr=3.13e-05 tok/s=12484
[train] step=175080 tokens=2868.5M loss=2.2128 lr=3.13e-05 tok/s=12484
[train] step=175090 tokens=2868.7M loss=1.8724 lr=3.13e-05 tok/s=12484
```
