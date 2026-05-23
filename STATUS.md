# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-23 01:27:20 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 1299M / 3000M (43.3%) |
| Step | 79310 |
| Latest loss | 2.2077 |
| Avg loss (last 30 logged) | 2.1702 |
| Throughput | 12,487 tok/s |
| ETA to 3B tokens | 1 day, 13:49:49 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
2.48 -> 2.33 -> 2.19 -> 2.02 -> 2.46 -> 2.06 -> 2.33 -> 2.16 -> 2.04 -> 2.03 -> 2.26 -> 2.21

## Checkpoints on disk
- `step_30518_tokens_500M.pt`
- `step_54932_tokens_900M.pt`
- `step_61036_tokens_1000M.pt`
- `step_67139_tokens_1100M.pt`
- `step_73243_tokens_1200M.pt`

## Recent log tail
```
[train] step=79200 tokens=1297.6M loss=2.3768 lr=1.95e-04 tok/s=12487
[train] step=79210 tokens=1297.8M loss=2.0095 lr=1.95e-04 tok/s=12487
[train] step=79220 tokens=1297.9M loss=2.3267 lr=1.95e-04 tok/s=12487
[train] step=79230 tokens=1298.1M loss=2.0935 lr=1.95e-04 tok/s=12487
[train] step=79240 tokens=1298.3M loss=2.1445 lr=1.95e-04 tok/s=12487
[train] step=79250 tokens=1298.4M loss=2.1331 lr=1.95e-04 tok/s=12487
[train] step=79260 tokens=1298.6M loss=2.1825 lr=1.95e-04 tok/s=12487
[train] step=79270 tokens=1298.8M loss=2.0720 lr=1.95e-04 tok/s=12487
[train] step=79280 tokens=1298.9M loss=2.2112 lr=1.95e-04 tok/s=12487
[train] step=79290 tokens=1299.1M loss=2.0708 lr=1.95e-04 tok/s=12487
[train] step=79300 tokens=1299.3M loss=1.8017 lr=1.95e-04 tok/s=12487
[train] step=79310 tokens=1299.4M loss=2.2077 lr=1.95e-04 tok/s=12487
```
