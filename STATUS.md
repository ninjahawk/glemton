# Glemton 350M v1.0-preview - training status

_Auto-generated 2026-05-24 00:00:44 local. Updated every ~10 min by `weekend_run.ps1`._

## State: TRAINING

| Metric | Value |
|---|---|
| Tokens seen | 2314M / 3000M (77.1%) |
| Step | 141230 |
| Latest loss | 2.3781 |
| Avg loss (last 30 logged) | 1.9852 |
| Throughput | 12,489 tok/s |
| ETA to 3B tokens | 15:15:36 |
| Projected finish | Sun 2026-05-24 15:16 |

## Loss trajectory (sampled)
2.16 -> 2.39 -> 2.30 -> 2.23 -> 2.05 -> 2.05 -> 2.27 -> 1.86 -> 1.59 -> 2.15 -> 2.21 -> 2.07

## Checkpoints on disk
- `step_122071_tokens_2000M.pt`
- `step_128174_tokens_2100M.pt`
- `step_134278_tokens_2200M.pt`
- `step_140381_tokens_2300M.pt`
- `step_30518_tokens_500M.pt`
- `step_61036_tokens_1000M.pt`
- `step_91553_tokens_1500M.pt`

## Recent log tail
```
[train] step=141120 tokens=2312.1M loss=1.7912 lr=6.41e-05 tok/s=12489
[train] step=141130 tokens=2312.3M loss=1.8825 lr=6.41e-05 tok/s=12489
[train] step=141140 tokens=2312.4M loss=2.0954 lr=6.40e-05 tok/s=12489
[train] step=141150 tokens=2312.6M loss=1.8088 lr=6.40e-05 tok/s=12489
[train] step=141160 tokens=2312.8M loss=2.0719 lr=6.40e-05 tok/s=12489
[train] step=141170 tokens=2312.9M loss=1.6379 lr=6.40e-05 tok/s=12489
[train] step=141180 tokens=2313.1M loss=2.3321 lr=6.40e-05 tok/s=12489
[train] step=141190 tokens=2313.3M loss=1.7825 lr=6.40e-05 tok/s=12489
[train] step=141200 tokens=2313.4M loss=2.0720 lr=6.40e-05 tok/s=12489
[train] step=141210 tokens=2313.6M loss=2.0673 lr=6.39e-05 tok/s=12489
[train] step=141220 tokens=2313.7M loss=1.7534 lr=6.39e-05 tok/s=12489
[train] step=141230 tokens=2313.9M loss=2.3781 lr=6.39e-05 tok/s=12489
```
