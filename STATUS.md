# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 10:12:18 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2771M / 3000M (92.4%) |
| Step | 169130 |
| Latest loss | 2.4885 |
| Avg loss (last 30 logged) | 2.0778 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 5:05:43 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
1.51 -> 1.47 -> 1.97 -> 2.01 -> 1.88 -> 2.39 -> 2.36 -> 2.08 -> 2.20 -> 2.02 -> 2.28 -> 1.88

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
[train] step=169020 tokens=2769.2M loss=2.1311 lr=3.40e-05 tok/s=12484
[train] step=169030 tokens=2769.4M loss=2.2714 lr=3.40e-05 tok/s=12484
[train] step=169040 tokens=2769.6M loss=2.3225 lr=3.40e-05 tok/s=12484
[train] step=169050 tokens=2769.7M loss=2.2734 lr=3.40e-05 tok/s=12484
[train] step=169060 tokens=2769.9M loss=1.7998 lr=3.40e-05 tok/s=12484
[train] step=169070 tokens=2770.0M loss=1.8202 lr=3.40e-05 tok/s=12484
[train] step=169080 tokens=2770.2M loss=2.3890 lr=3.40e-05 tok/s=12484
[train] step=169090 tokens=2770.4M loss=1.9591 lr=3.39e-05 tok/s=12484
[train] step=169100 tokens=2770.5M loss=1.8784 lr=3.39e-05 tok/s=12484
[train] step=169110 tokens=2770.7M loss=2.1303 lr=3.39e-05 tok/s=12484
[train] step=169120 tokens=2770.9M loss=1.8270 lr=3.39e-05 tok/s=12484
[train] step=169130 tokens=2771.0M loss=2.4885 lr=3.39e-05 tok/s=12484
```
