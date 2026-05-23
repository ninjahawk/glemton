# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 18:49:56 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2081M / 3000M (69.4%) |
| Step | 127020 |
| Latest loss | 1.9429 |
| Avg loss (last 30 logged) | 2.0746 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 20:26:10 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
1.97 -> 2.20 -> 2.57 -> 1.86 -> 1.73 -> 2.14 -> 2.21 -> 2.27 -> 1.97 -> 1.89 -> 2.10 -> 1.96

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_115967_tokens_1900M.pt`
- `step_122071_tokens_2000M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=126910 tokens=2079.3M loss=2.0268 lr=8.89e-05 tok/s=12490
[train] step=126920 tokens=2079.5M loss=1.5036 lr=8.89e-05 tok/s=12490
[train] step=126930 tokens=2079.6M loss=2.3080 lr=8.89e-05 tok/s=12490
[train] step=126940 tokens=2079.8M loss=2.2103 lr=8.89e-05 tok/s=12490
[train] step=126950 tokens=2079.9M loss=2.5831 lr=8.89e-05 tok/s=12490
[train] step=126960 tokens=2080.1M loss=1.9127 lr=8.88e-05 tok/s=12490
[train] step=126970 tokens=2080.3M loss=2.5935 lr=8.88e-05 tok/s=12490
[train] step=126980 tokens=2080.4M loss=2.2714 lr=8.88e-05 tok/s=12490
[train] step=126990 tokens=2080.6M loss=1.9603 lr=8.88e-05 tok/s=12490
[train] step=127000 tokens=2080.8M loss=2.5927 lr=8.88e-05 tok/s=12490
[train] step=127010 tokens=2080.9M loss=1.9922 lr=8.87e-05 tok/s=12490
[train] step=127020 tokens=2081.1M loss=1.9429 lr=8.87e-05 tok/s=12490
```
