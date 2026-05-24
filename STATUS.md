# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 10:32:21 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2786M / 3000M (92.9%) |
| Step | 170050 |
| Latest loss | 1.9039 |
| Avg loss (last 30 logged) | 2.0779 |
| Throughput | 12,484 tok/s |
| ETA to 3B tokens | 4:45:33 |
| Projected finish | Sun 2026-05-24 15:17 |

## Loss trajectory (sampled)
1.98 -> 2.00 -> 1.60 -> 1.84 -> 1.95 -> 1.91 -> 1.92 -> 1.97 -> 2.27 -> 2.07 -> 2.22 -> 2.36

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_146485_tokens_2400M.pt`
- `step_152588_tokens_2500M.pt`
- `step_158692_tokens_2600M.pt`
- `step_164795_tokens_2700M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=169940 tokens=2784.3M loss=1.7722 lr=3.35e-05 tok/s=12484
[train] step=169950 tokens=2784.5M loss=1.6856 lr=3.35e-05 tok/s=12484
[train] step=169960 tokens=2784.6M loss=2.3987 lr=3.35e-05 tok/s=12484
[train] step=169970 tokens=2784.8M loss=2.2724 lr=3.35e-05 tok/s=12484
[train] step=169980 tokens=2785.0M loss=1.9981 lr=3.35e-05 tok/s=12484
[train] step=169990 tokens=2785.1M loss=1.9524 lr=3.35e-05 tok/s=12484
[train] step=170000 tokens=2785.3M loss=2.1975 lr=3.35e-05 tok/s=12484
[train] step=170010 tokens=2785.4M loss=2.1475 lr=3.35e-05 tok/s=12484
[train] step=170020 tokens=2785.6M loss=2.3559 lr=3.34e-05 tok/s=12484
[train] step=170030 tokens=2785.8M loss=2.5038 lr=3.34e-05 tok/s=12484
[train] step=170040 tokens=2785.9M loss=1.9048 lr=3.34e-05 tok/s=12484
[train] step=170050 tokens=2786.1M loss=1.9039 lr=3.34e-05 tok/s=12484
```
