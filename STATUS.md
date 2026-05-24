# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 14:52:58 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2981M / 3000M (99.4%) |
| Step | 181960 |
| Latest loss | 2.3990 |
| Avg loss (last 30 logged) | 2.0267 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 0:25:05 |
| Projected finish | Sun 2026-05-24 15:18 |

## Loss trajectory (sampled)
1.57 -> 1.86 -> 2.56 -> 2.05 -> 1.88 -> 2.32 -> 2.26 -> 1.93 -> 1.65 -> 2.05 -> 2.04 -> 2.03

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
[train] step=181850 tokens=2979.4M loss=1.9104 lr=3.00e-05 tok/s=12484
[train] step=181860 tokens=2979.6M loss=1.8880 lr=3.00e-05 tok/s=12484
[train] step=181870 tokens=2979.8M loss=1.9388 lr=3.00e-05 tok/s=12484
[train] step=181880 tokens=2979.9M loss=2.5400 lr=3.00e-05 tok/s=12484
[train] step=181890 tokens=2980.1M loss=2.0209 lr=3.00e-05 tok/s=12484
[train] step=181900 tokens=2980.2M loss=1.6092 lr=3.00e-05 tok/s=12484
[train] step=181910 tokens=2980.4M loss=2.1008 lr=3.00e-05 tok/s=12484
[train] step=181920 tokens=2980.6M loss=1.9509 lr=3.00e-05 tok/s=12484
[train] step=181930 tokens=2980.7M loss=2.0279 lr=3.00e-05 tok/s=12484
[train] step=181940 tokens=2980.9M loss=2.3202 lr=3.00e-05 tok/s=12484
[train] step=181950 tokens=2981.1M loss=1.5830 lr=3.00e-05 tok/s=12484
[train] step=181960 tokens=2981.2M loss=2.3990 lr=3.00e-05 tok/s=12484
```
