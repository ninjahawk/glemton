# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-22 00:53:24 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 195M / 3000M (6.5%) |
| Step | 11920 |
| Latest loss | 2.4662 |
| Avg loss (last 30 logged) | 2.5553 |
| Throughput | 12,491 tok/s |
| ETA to 3B tokens | 2 days, 14:22:17 |
| Projected finish | Sun 2026-05-24 15:15 |

## Loss trajectory (sampled)
2.56 -> 2.49 -> 2.44 -> 2.67 -> 2.81 -> 2.53 -> 2.43 -> 2.69 -> 2.79 -> 2.76 -> 2.65 -> 2.89

## Checkpoints on disk
- `step_6104_tokens_100M.pt`

## Recent log tail
```
[train] step=11810 tokens=193.5M loss=2.3802 lr=2.98e-04 tok/s=12491
[train] step=11820 tokens=193.7M loss=2.5150 lr=2.98e-04 tok/s=12491
[train] step=11830 tokens=193.8M loss=2.5699 lr=2.98e-04 tok/s=12491
[train] step=11840 tokens=194.0M loss=3.1489 lr=2.98e-04 tok/s=12491
[train] step=11850 tokens=194.2M loss=2.6184 lr=2.98e-04 tok/s=12491
[train] step=11860 tokens=194.3M loss=2.7004 lr=2.98e-04 tok/s=12491
[train] step=11870 tokens=194.5M loss=2.4103 lr=2.98e-04 tok/s=12491
[train] step=11880 tokens=194.6M loss=2.4315 lr=2.98e-04 tok/s=12491
[train] step=11890 tokens=194.8M loss=2.8895 lr=2.98e-04 tok/s=12491
[train] step=11900 tokens=195.0M loss=2.5473 lr=2.98e-04 tok/s=12491
[train] step=11910 tokens=195.1M loss=2.3831 lr=2.98e-04 tok/s=12491
[train] step=11920 tokens=195.3M loss=2.4662 lr=2.98e-04 tok/s=12491
```
