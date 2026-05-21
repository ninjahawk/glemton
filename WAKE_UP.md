# WAKE_UP — overnight status report

**Session:** 2026-05-20 overnight (start ~19:00 local).
**Project:** Glemton (formerly considered BOOST, HEED, Flabby — see git history / journal).
**Repo:** https://github.com/ninjahawk/glemton.git (not yet pushed; needs your git auth)

## TL;DR

The hardest non-data risk is killed: **PyTorch nightly cu128 sees your RTX 5070 with capability (12, 0) and bf16_supported = True.** All the model + training + eval code is written, tested at the import + forward-pass level, and lives under `src/glemton/`. The full architecture (350M Llama-style with GQA + RoPE θ=1e6 + sliding-window 4096) builds at **365M parameters** as configured.

The corpus is partially assembled. Common Pile v0.1 streamed cleanly (~2.3 GB processed). 15 classic Project Gutenberg books were pulled and dialogue-extracted (~9 MB, 11k chunks). OpenSubtitles, DailyDialog, Ubuntu Dialogue, and most of Stack Exchange failed — see "What didn't work".

You will need to make a few decisions before any real training (see "What needs you" at the bottom).

## What's on disk

```
C:\Users\jedin\Desktop\Glemton\
├── CLAUDE.md, README.md, LICENSE, pyproject.toml, requirements.txt, .gitignore
├── MODEL_CARD.md (draft)
├── WAKE_UP.md (this file)
├── .venv\                     ← Python 3.11 + PyTorch 2.12 nightly cu128 + deps
├── configs\
│   ├── glemton-350m.yaml      ← v1.0 full pretrain config
│   └── debug-10m.yaml         ← Phase 0 scaffold-validation config
├── src\glemton\
│   ├── model.py               ← Llama-style 365M transformer, build+forward verified
│   ├── tokenizer.py           ← BPE trainer (32k vocab, <user>/<reply> turn markers)
│   ├── data.py                ← PackedDataset mmap iterator
│   ├── train.py               ← single-GPU bf16 loop, 8bit-Adam fallback
│   ├── eval_sycophancy.py     ← regex marker counter
│   └── eval_long_conversation.py  ← synthetic plant/recall probe builder
├── scripts\
│   ├── download_data.py       ← v1 downloaders
│   ├── download_data_v2.py    ← fallbacks for HF deprecated scripts
│   ├── prepare_corpus.py      ← normalize raw → processed
│   ├── prepare_gutenberg_books.py ← extract dialogue from Gutenberg .txt
│   ├── train_tokenizer.py     ← orchestrator
│   ├── pack_shards.py         ← processed .txt → tokenized .bin
│   └── run_debug_train.py     ← wrapper around train.py with debug config
├── docs\
│   ├── architecture.md, data.md, training.md, prior_art.md, evals.md
│   └── journal\2026-05-20.md  ← detailed session log
├── tests\probes\
│   └── sycophancy_probes.txt  ← 39 prompts for the sycophancy eval
├── data\
│   ├── raw\
│   │   ├── gutenberg_books\         ← 15 classic books (14 MB)
│   │   ├── gutenberg_dialogue\      ← repo extractor code only (no data)
│   │   ├── common_pile\             ← 25 streamed shards (2.3 GB)
│   │   └── stack_exchange\          ← philosophy + skeptics .7z (195 MB)
│   ├── processed\
│   │   ├── common_pile\             ← 246 shards (2.3 GB)
│   │   └── gutenberg_books\         ← 3 shards (11k dialogue chunks)
│   └── tokenizer\                   ← tokenizer training output (may be in progress)
├── checkpoints\
└── logs\                            ← every install/download/prep log lives here
```

## What worked

| Phase | Status | Notes |
|---|---|---|
| Project scaffold | done | All dirs + base files |
| Python 3.11 venv | done | At `.venv` |
| PyTorch 2.12 nightly cu128 install | done | bf16 supported, sm_120 detected |
| transformers / tokenizers / datasets / wandb / etc. | done | All importing OK |
| Model code (Llama-style 365M) | done | Forward pass verified on CPU, debug-10m at 12.3M |
| Training loop | done | Untested on GPU |
| Eval skeletons (sycophancy + long-conversation) | done | Sycophancy probe set committed |
| Docs (architecture, data, training, prior_art, evals, journal, model card draft) | done | |
| Sycophancy probe prompts | done | 39 prompts in tests/probes/ |
| git init + remote | done | Not pushed — needs your auth |
| Common Pile v0.1 download | done | 246 processed shards, 2.3 GB |
| Gutenberg books (15 classics) | done | 11k dialogue chunks extracted |
| BPE tokenizer training | in progress / queued | See `logs/train_tokenizer.log` |
| Pack tokenized shards | not yet | Needs tokenizer to finish first |
| Debug 10M training run | not yet | Gated on tokenizer + shards |

## What didn't work

1. **OpenSubtitles via `Helsinki-NLP/open_subtitles`** — HF deprecated dataset loader scripts in `datasets >= 4.x`, this dataset still uses a script. Tried fallback parquet mirrors in `download_data_v2.py`; none of the candidates worked end-to-end in the overnight session.
   - **Workaround:** download OpenSubtitles plaintext directly from OPUS (opus.nlpl.eu); they offer per-language `.txt.gz` mono dumps. Pull manually when convenient.

2. **DailyDialog** — same HF deprecation issue.
   - **Workaround:** there's likely a community parquet mirror under a different namespace; quick search at https://huggingface.co/datasets?search=daily_dialog should find one.

3. **Stack Exchange dumps** — most of the targeted `archive.org/download/stackexchange/*.7z` URLs 404'd. Only `philosophy.stackexchange.com.7z` and `skeptics.stackexchange.com.7z` made it (195 MB total).
   - **Workaround:** the canonical Stack Exchange data dump index has moved; check https://archive.org/details/stackexchange for the current bundle naming. Also the SE dumps are `.7z`, so `pip install py7zr` will be needed to extract them.

4. **Ubuntu Dialogue Corpus** — wasn't actually attempted this session beyond the v1 script; same `datasets`-script risk applies.

5. **bitsandbytes 8-bit Adam on Windows + Blackwell** — installed without erroring, but its native CUDA kernels may not load at runtime on sm_120. `train.py` already wraps the import in `try/except` and falls back to plain `AdamW` if so. Will only be confirmed when we run the debug train.

## What's next, in priority order

1. **Confirm the tokenizer finished.** Check `logs/train_tokenizer.log`. Output should be at `data/tokenizer/glemton-bpe-32k.json`.
2. **Pack shards:** `.venv\Scripts\python.exe scripts/pack_shards.py` — this turns `data/processed/**/*.txt` into `data/tokenized/**/*.bin`.
3. **Run the debug train:** `.venv\Scripts\python.exe scripts/run_debug_train.py` — 12M model on the available tokens. Should converge to ~3–4 loss in <30 min on the 5070 if the pipeline is healthy.
4. **Decide on remaining data:** with current data alone (~2.3 GB raw text, maybe ~600M tokens after tokenization) we're well under the 7B-token Chinchilla target for 350M. Three options:
   - (a) Track down OpenSubtitles + DailyDialog + more Stack Exchange to expand toward 7B
   - (b) Shrink v1.0 to a "data-limited" run on what we have (label it that way, train for fewer tokens, ship and iterate)
   - (c) Pull more from Common Pile (it's 8TB total; we only pulled a small streaming slice)
   - Honest recommendation: **(c) plus (a)**. Common Pile is the cleanest license-wise; expanding our pull there is low-friction.

## What needs you (decisions, not work)

1. **GitHub push.** Run from `C:\Users\jedin\Desktop\Glemton`:
   ```powershell
   git add -A
   git commit -m "Initial scaffold: model, training, eval, docs, partial corpus"
   git push -u origin main
   ```
   (Note: the CLAUDE.md attribution rule means no Co-Authored-By footer on any commit. The commit above is unsigned and authored by ninjahawk per the local git config I set.)

2. **Pick one of (a)/(b)/(c) above** for the data shortfall.

3. **OpenSubtitles or skip?** If you'd rather skip rather than chase parquet mirrors, that's a defensible v1.0 choice — Gutenberg-extracted dialogue + Stack Exchange + Common Pile is a coherent corpus on its own.

## Honest summary

This is real, working scaffolding. Code is sound, toolchain is verified, ~2.3 GB of clean openly-licensed text is on disk. The remaining ~5 GB of dialogue data is the main thing standing between us and a full pretrain. There's no actual training done — the debug 10M scaffold validation is queued behind the tokenizer.

Total wall time, this session: roughly 1.5–2 hours of active work (everything else is downloads + tokenizer training in background).
