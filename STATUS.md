# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 14:22:57 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2959M / 3000M (98.6%) |
| Step | 180590 |
| Latest loss | 1.8840 |
| Avg loss (last 30 logged) | 2.0532 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 0:55:00 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.85 -> 2.36 -> 1.97 -> 2.21 -> 2.14 -> 2.11 -> 1.39 -> 2.09 -> 2.18 -> 2.08 -> 2.52 -> 2.15

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
[train] step=180480 tokens=2957.0M loss=2.2237 lr=3.01e-05 tok/s=12484
[train] step=180490 tokens=2957.1M loss=2.6051 lr=3.01e-05 tok/s=12484
[train] step=180500 tokens=2957.3M loss=1.8915 lr=3.01e-05 tok/s=12484
[train] step=180510 tokens=2957.5M loss=2.0489 lr=3.01e-05 tok/s=12484
[train] step=180520 tokens=2957.6M loss=1.7285 lr=3.01e-05 tok/s=12484
[train] step=180530 tokens=2957.8M loss=1.8169 lr=3.01e-05 tok/s=12484
[train] step=180540 tokens=2958.0M loss=2.3792 lr=3.01e-05 tok/s=12484
[train] step=180550 tokens=2958.1M loss=1.9115 lr=3.01e-05 tok/s=12484
[train] step=180560 tokens=2958.3M loss=1.6837 lr=3.01e-05 tok/s=12484
[train] step=180570 tokens=2958.5M loss=2.1516 lr=3.01e-05 tok/s=12484
[train] step=180580 tokens=2958.6M loss=2.5600 lr=3.01e-05 tok/s=12484
[train] step=180590 tokens=2958.8M loss=1.8840 lr=3.01e-05 tok/s=12484
```
