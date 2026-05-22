# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 05:44:12 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 413M / 3000M (13.8%) |
| Step | 25210 |
| Latest loss | 2.5009 |
| Avg loss (last 30 logged) | 2.4506 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 2 days, 9:33:12 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.71 -> 2.48 -> 2.32 -> 2.54 -> 2.42 -> 2.36 -> 2.31 -> 2.11 -> 2.51 -> 2.56 -> 2.38 -> 2.59

## Checkpoints on disk
- `step_12208_tokens_200M.pt`
- `step_18311_tokens_300M.pt`
- `step_24415_tokens_400M.pt`
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=25100 tokens=411.2M loss=2.3868 lr=2.89e-04 tok/s=12486
[train] step=25110 tokens=411.4M loss=2.4397 lr=2.89e-04 tok/s=12486
[train] step=25120 tokens=411.6M loss=2.3513 lr=2.89e-04 tok/s=12486
[train] step=25130 tokens=411.7M loss=2.5305 lr=2.89e-04 tok/s=12486
[train] step=25140 tokens=411.9M loss=2.3151 lr=2.89e-04 tok/s=12486
[train] step=25150 tokens=412.1M loss=2.0256 lr=2.89e-04 tok/s=12486
[train] step=25160 tokens=412.2M loss=2.5766 lr=2.89e-04 tok/s=12486
[train] step=25170 tokens=412.4M loss=2.5082 lr=2.89e-04 tok/s=12486
[train] step=25180 tokens=412.5M loss=2.5197 lr=2.89e-04 tok/s=12486
[train] step=25190 tokens=412.7M loss=2.5939 lr=2.89e-04 tok/s=12486
[train] step=25200 tokens=412.9M loss=2.6279 lr=2.89e-04 tok/s=12486
[train] step=25210 tokens=413.0M loss=2.5009 lr=2.89e-04 tok/s=12486
```
