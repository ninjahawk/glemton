# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 13:49:13 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1856M / 3000M (61.9%) |
| Step | 113260 |
| Latest loss | 2.3014 |
| Avg loss (last 30 logged) | 2.1189 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 1 day, 1:27:04 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.18 -> 2.16 -> 1.98 -> 2.28 -> 2.01 -> 2.07 -> 2.33 -> 1.71 -> 2.40 -> 2.16 -> 1.77 -> 2.42

## Checkpoints on disk
- `step_103760_tokens_1700M.pt`
- `step_109864_tokens_1800M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`
- `step_97657_tokens_1600M.pt`

## Recent log tail
```
[train] step=113150 tokens=1853.8M loss=1.8374 lr=1.17e-04 tok/s=12489
[train] step=113160 tokens=1854.0M loss=2.0559 lr=1.17e-04 tok/s=12489
[train] step=113170 tokens=1854.2M loss=2.2086 lr=1.17e-04 tok/s=12489
[train] step=113180 tokens=1854.3M loss=1.7242 lr=1.17e-04 tok/s=12489
[train] step=113190 tokens=1854.5M loss=1.9957 lr=1.17e-04 tok/s=12489
[train] step=113200 tokens=1854.7M loss=2.4077 lr=1.17e-04 tok/s=12489
[train] step=113210 tokens=1854.8M loss=2.1304 lr=1.17e-04 tok/s=12489
[train] step=113220 tokens=1855.0M loss=2.2339 lr=1.17e-04 tok/s=12489
[train] step=113230 tokens=1855.2M loss=2.5711 lr=1.17e-04 tok/s=12489
[train] step=113240 tokens=1855.3M loss=2.4232 lr=1.17e-04 tok/s=12489
[train] step=113250 tokens=1855.5M loss=2.3882 lr=1.17e-04 tok/s=12489
[train] step=113260 tokens=1855.7M loss=2.3014 lr=1.17e-04 tok/s=12489
```
