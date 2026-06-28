# RESTORE — rebuilding pruned local artifacts

On **2026-06-27** the large **git-ignored** working files were pruned from this
machine to reclaim disk (~42 GB). Nothing tracked by git was touched — the
pruned files were all in `.gitignore` and never lived in the repo. This file
documents how to rebuild what was removed and how to use what was kept.

## What was pruned (and how it's recovered)

| Removed | Approx size | Recover by |
|---|---|---|
| `checkpoints/**/step_*.pt` (intermediate snapshots) | ~21 GB | retrain — or just use `final.pt`, which was kept |
| `data/raw/`, `data/processed/`, `data/tokenized/` | ~16 GB | re-run the data pipeline (§4) |
| `.venv/` | ~5 GB | recreate the env (§1) |

**Kept on disk:** every `final.pt` (the trained models), the BPE tokenizer
(`data/tokenizer/`, also tracked in git), and all code, configs, docs, and logs.

Pruning intermediate `step_*.pt` is already normal operation — the watcher in
`scripts/weekend_run.ps1` prunes them *during* training (keep newest 4 + each
500M-token milestone). The v1.0-preview run is complete (`final.pt` saved), so
there is nothing to resume and nothing was lost by removing them.

## 1. Rebuild the environment (`.venv`)

Python 3.11, PyTorch nightly cu128 (see `CLAUDE.md`). From the repo root in PowerShell:

```powershell
uv venv --python 3.11                 # or, without uv:  py -3.11 -m venv .venv
.venv\Scripts\python.exe -m pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu128
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

`bitsandbytes` (8-bit Adam) is skipped on Windows by design; `train.py` falls
back to plain AdamW automatically.

## 2. Talk to the model

The kept checkpoint is `checkpoints\glemton-350m\final.pt`:

```powershell
$env:PYTHONPATH = "src"
.venv\Scripts\python.exe scripts\chat.py --ckpt checkpoints\glemton-350m\final.pt
```

Useful knobs: `--temperature 1.1` (more talkative), `--temperature 0.6` (more
focused), `--max-new-tokens 200`. For a quick non-interactive sample use
`scripts\sample_ckpt.py`.

## 3. Re-run the evals (on the kept checkpoint)

```powershell
$env:PYTHONPATH = "src"
.venv\Scripts\python.exe scripts\run_sycophancy_eval.py --ckpt checkpoints\glemton-350m\final.pt
.venv\Scripts\python.exe scripts\run_long_conversation_eval.py --ckpt checkpoints\glemton-350m\final.pt
```

The tokenizer defaults to `data/tokenizer/glemton-bpe-32k.json` (kept); reports
are written under `logs/`.

## 4. Regenerate the training data (only needed to retrain)

The corpus is re-downloadable / re-derivable. Run from the repo root with
`$env:PYTHONPATH = "src"`, in order — each stage produces the next `data/` folder:

1. **Download raw** → `data/raw/`: `scripts\download_data_v2.py` (OPUS
   OpenSubtitles, Common Pile, Hacker News, Gutenberg sample). The older
   `download_data.py` and the `pull_*` / `download_*` helpers cover the other
   planned sources.
2. **Prepare / clean** → `data/processed/`: `scripts\prepare_corpus.py` (plus
   `prepare_gutenberg_books.py` for the book prose).
3. **Tokenize + pack shards** → `data/tokenized/`: `scripts\pack_shards.py`,
   using the kept tokenizer in `data/tokenizer/`.

The tokenizer is already kept, so `scripts\train_tokenizer.py` does **not** need
to run. Corpus mix / source weights live in `configs/glemton-350m.yaml` under
`data.source_weights`. Each script takes its options as CLI args — run it with no
args (or read its `main()`) for the exact flags.

## 5. Retrain from scratch (optional)

Training reads a YAML config and writes to `checkpoints/<name>/`:

```powershell
$env:PYTHONPATH = "src"
.venv\Scripts\python.exe -m glemton.train configs\glemton-350m.yaml
# resume from a checkpoint:
.venv\Scripts\python.exe -m glemton.train configs\glemton-350m.yaml --resume checkpoints\glemton-350m\step_XXXX.pt
```

For the full unattended 3 B-token run use `scripts\weekend_run.ps1` (headless,
auto-resume, auto-eval) — see its header for the scheduled-task launch. The
v1.0-preview run was ~66 h on a single RTX 5070.
