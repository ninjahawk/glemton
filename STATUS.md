# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 18:29:53 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2066M / 3000M (68.9%) |
| Step | 126100 |
| Latest loss | 2.0160 |
| Avg loss (last 30 logged) | 2.0437 |
| Throughput | 12,490 tok/s |
| ETA to 3B tokens | 20:46:19 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.05 -> 1.98 -> 2.09 -> 1.66 -> 2.04 -> 1.76 -> 2.07 -> 2.12 -> 1.93 -> 2.13 -> 2.03 -> 2.12

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
[train] step=125990 tokens=2064.2M loss=2.1461 lr=9.07e-05 tok/s=12490
[train] step=126000 tokens=2064.4M loss=1.9689 lr=9.07e-05 tok/s=12490
[train] step=126010 tokens=2064.5M loss=2.1945 lr=9.07e-05 tok/s=12490
[train] step=126020 tokens=2064.7M loss=2.4611 lr=9.07e-05 tok/s=12490
[train] step=126030 tokens=2064.9M loss=1.7981 lr=9.06e-05 tok/s=12490
[train] step=126040 tokens=2065.0M loss=2.5580 lr=9.06e-05 tok/s=12490
[train] step=126050 tokens=2065.2M loss=2.0052 lr=9.06e-05 tok/s=12490
[train] step=126060 tokens=2065.4M loss=1.9158 lr=9.06e-05 tok/s=12490
[train] step=126070 tokens=2065.5M loss=2.1250 lr=9.06e-05 tok/s=12490
[train] step=126080 tokens=2065.7M loss=2.0949 lr=9.05e-05 tok/s=12490
[train] step=126090 tokens=2065.9M loss=1.7880 lr=9.05e-05 tok/s=12490
[train] step=126100 tokens=2066.0M loss=2.0160 lr=9.05e-05 tok/s=12490
```
