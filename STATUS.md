# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 20:10:09 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2141M / 3000M (71.4%) |
| Step | 130690 |
| Latest loss | 2.0444 |
| Avg loss (last 30 logged) | 2.0068 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 19:05:59 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.47 -> 2.14 -> 2.21 -> 2.23 -> 1.95 -> 2.27 -> 1.76 -> 2.08 -> 2.20 -> 1.94 -> 2.08 -> 1.72

## Checkpoints on disk
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=130580 tokens=2139.4M loss=1.6147 lr=8.20e-05 tok/s=12490
[train] step=130590 tokens=2139.6M loss=2.1125 lr=8.20e-05 tok/s=12490
[train] step=130600 tokens=2139.8M loss=2.0016 lr=8.20e-05 tok/s=12490
[train] step=130610 tokens=2139.9M loss=1.9288 lr=8.20e-05 tok/s=12490
[train] step=130620 tokens=2140.1M loss=2.1507 lr=8.19e-05 tok/s=12490
[train] step=130630 tokens=2140.2M loss=1.7605 lr=8.19e-05 tok/s=12490
[train] step=130640 tokens=2140.4M loss=1.7852 lr=8.19e-05 tok/s=12490
[train] step=130650 tokens=2140.6M loss=2.2616 lr=8.19e-05 tok/s=12490
[train] step=130660 tokens=2140.7M loss=1.7993 lr=8.19e-05 tok/s=12490
[train] step=130670 tokens=2140.9M loss=1.7150 lr=8.18e-05 tok/s=12490
[train] step=130680 tokens=2141.1M loss=2.2537 lr=8.18e-05 tok/s=12490
[train] step=130690 tokens=2141.2M loss=2.0444 lr=8.18e-05 tok/s=12490
```
