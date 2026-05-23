# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 22:26:53 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1164M / 3000M (38.8%) |
| Step | 71060 |
| Latest loss | 2.2015 |
| Avg loss (last 30 logged) | 2.2003 |
| Throughput | 12,486 tok/s |
| ETA to 3B tokens | 1 day, 16:50:28 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.54 -> 2.36 -> 2.00 -> 2.00 -> 2.79 -> 2.00 -> 1.97 -> 2.44 -> 2.28 -> 2.26 -> 2.51 -> 2.27

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_48829_tokens_800M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`

## Recent log tail
```
[train] step=70950 tokens=1162.4M loss=2.1760 lr=2.14e-04 tok/s=12486
[train] step=70960 tokens=1162.6M loss=2.3420 lr=2.14e-04 tok/s=12486
[train] step=70970 tokens=1162.8M loss=2.0825 lr=2.14e-04 tok/s=12486
[train] step=70980 tokens=1162.9M loss=2.0593 lr=2.14e-04 tok/s=12486
[train] step=70990 tokens=1163.1M loss=2.2782 lr=2.14e-04 tok/s=12486
[train] step=71000 tokens=1163.3M loss=2.5043 lr=2.14e-04 tok/s=12486
[train] step=71010 tokens=1163.4M loss=1.9708 lr=2.14e-04 tok/s=12486
[train] step=71020 tokens=1163.6M loss=1.9434 lr=2.14e-04 tok/s=12486
[train] step=71030 tokens=1163.8M loss=2.0344 lr=2.14e-04 tok/s=12486
[train] step=71040 tokens=1163.9M loss=2.2704 lr=2.14e-04 tok/s=12486
[train] step=71050 tokens=1164.1M loss=2.0934 lr=2.14e-04 tok/s=12486
[train] step=71060 tokens=1164.2M loss=2.2015 lr=2.14e-04 tok/s=12486
```
