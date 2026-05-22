# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 19:16:23 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1021M / 3000M (34.0%) |
| Step | 62340 |
| Latest loss | 2.7721 |
| Avg loss (last 30 logged) | 2.2670 |
| Throughput | 12,485 tok/s |
| ETA to 3B tokens | 1 day, 20:01:18 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.06 -> 2.16 -> 2.38 -> 2.23 -> 2.25 -> 2.42 -> 2.13 -> 2.25 -> 2.13 -> 2.22 -> 2.28 -> 2.22

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_42725_tokens_700M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`

## Recent log tail
```
[train] step=62230 tokens=1019.6M loss=2.2217 lr=2.32e-04 tok/s=12485
[train] step=62240 tokens=1019.7M loss=2.2236 lr=2.32e-04 tok/s=12485
[train] step=62250 tokens=1019.9M loss=2.1945 lr=2.32e-04 tok/s=12485
[train] step=62260 tokens=1020.1M loss=2.5381 lr=2.32e-04 tok/s=12485
[train] step=62270 tokens=1020.2M loss=2.2249 lr=2.32e-04 tok/s=12485
[train] step=62280 tokens=1020.4M loss=2.1863 lr=2.32e-04 tok/s=12485
[train] step=62290 tokens=1020.6M loss=2.1524 lr=2.32e-04 tok/s=12485
[train] step=62300 tokens=1020.7M loss=2.1664 lr=2.32e-04 tok/s=12485
[train] step=62310 tokens=1020.9M loss=2.8760 lr=2.32e-04 tok/s=12485
[train] step=62320 tokens=1021.1M loss=2.2183 lr=2.32e-04 tok/s=12485
[train] step=62330 tokens=1021.2M loss=2.3775 lr=2.32e-04 tok/s=12485
[train] step=62340 tokens=1021.4M loss=2.7721 lr=2.32e-04 tok/s=12485
```
