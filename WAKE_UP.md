# WAKE_UP — overnight status report

**Session:** 2026-05-20 overnight (start ~19:00 local).
**Project:** Glemton (formerly considered BOOST, HEED, Flabby — all blocked by name conflicts).
**Repo:** https://github.com/ninjahawk/glemton.git (committed locally; ready to push).

## TL;DR — Phase 0 passed.

The full pipeline works end-to-end on your Blackwell 5070:
- **Toolchain:** PyTorch 2.12 nightly cu128 sees the 5070 (`capability=(12, 0)`, `bf16_supported=True`).
- **Architecture:** 365 M Llama-style transformer (Glemton spec) builds; 12 M debug variant trained to convergence.
- **Data pipeline:** download → prepare → tokenize → pack → train → sample → eval, every stage wired.
- **First training run completed:** 12 M params, 50 M tokens, loss 10.01 → 4.0, 160 k tok/s, 5 checkpoints saved.
- **Both evals validated end-to-end** against the trained checkpoint.

A **50 M-parameter mid-size training run on 200 M tokens** is **running on the GPU right now** as of this writing. Should finish in ~20–30 min. Check `logs/midsize_train.log` for status and `checkpoints/glemton-midsize-50m/` for output.

## What you can do *immediately* when you wake

1. **Push the repo:**
   ```powershell
   cd C:\Users\jedin\Desktop\Glemton
   git push -u origin main
   ```
   (Two commits ready: initial scaffold + Phase 0 + expanded corpus / evals.)

2. **Chat with the trained debug model:**
   ```powershell
   .venv\Scripts\python.exe scripts\chat.py
   ```
   It will be incoherent (12 M params, 50 M tokens of mostly Common Pile academic text). Useful only to confirm the chat REPL works.

3. **Re-run the evals on the new 50 M checkpoint** (after it finishes):
   ```powershell
   .venv\Scripts\python.exe scripts\run_sycophancy_eval.py --ckpt checkpoints\glemton-midsize-50m\final.pt
   .venv\Scripts\python.exe scripts\run_long_conversation_eval.py --ckpt checkpoints\glemton-midsize-50m\final.pt
   ```

4. **Inspect throughput numbers** to forecast the full 350 M run:
   ```powershell
   tail logs\midsize_train.log
   ```
   On the 12 M debug we hit ~160 k tok/s sustained. The 50 M run should land 60-90 k tok/s. Scale to 365 M and 7 B tokens to project the full pretrain wall time.

## What's on disk

```
C:\Users\jedin\Desktop\Glemton\
├── CLAUDE.md, README.md, LICENSE, pyproject.toml, requirements.txt, .gitignore
├── MODEL_CARD.md (draft), WAKE_UP.md (this file)
├── .venv\                          ← Python 3.11 + PyTorch 2.12 nightly cu128 + all deps
├── configs\
│   ├── glemton-350m.yaml           ← v1.0 full pretrain config (365 M params)
│   ├── midsize-50m.yaml            ← intermediate test (currently training)
│   └── debug-10m.yaml              ← Phase 0 scaffold-validation (passed)
├── src\glemton\
│   ├── model.py                    ← Llama-style transformer, build+forward verified
│   ├── tokenizer.py                ← BPE trainer, 32 k vocab with <user>/<reply> turn tokens
│   ├── data.py                     ← PackedDataset mmap iterator (rglob fix)
│   ├── train.py                    ← single-GPU bf16 loop, 8-bit Adam w/ fallback
│   ├── generate.py                 ← top-k + top-p sampling, checkpoint loader
│   ├── eval_sycophancy.py          ← regex marker counter
│   └── eval_long_conversation.py   ← synthetic plant/recall probe builder
├── scripts\
│   ├── download_data.py            ← v1 downloaders (HF dataset-script issues)
│   ├── download_data_v2.py         ← fallbacks for HF deprecation
│   ├── pull_more_gutenberg.py      ← list-driven Gutenberg .txt puller (79 books)
│   ├── pull_hf_dialogue.py         ← parquet-based dialogue puller
│   ├── prepare_corpus.py           ← normalize raw → processed
│   ├── prepare_gutenberg_books.py  ← heuristic dialogue extraction
│   ├── train_tokenizer.py          ← orchestrator
│   ├── pack_shards.py              ← processed .txt → tokenized .bin
│   ├── run_debug_train.py          ← wrapper for the 10 M phase-0 train
│   ├── run_sycophancy_eval.py      ← end-to-end sycophancy eval runner
│   ├── run_long_conversation_eval.py ← end-to-end long-conv eval runner
│   └── chat.py                     ← interactive REPL
├── docs\
│   ├── architecture.md, data.md, training.md, prior_art.md, evals.md
│   └── journal\2026-05-20.md
├── tests\probes\
│   └── sycophancy_probes.txt       ← 39 probes
├── data\
│   ├── raw\
│   │   ├── gutenberg_books\        ← 79 classic books (67 MB)
│   │   ├── common_pile\            ← 25 streamed shards (2.3 GB)
│   │   ├── stack_exchange\         ← philosophy + skeptics .7z (195 MB)
│   │   └── squad\                  ← 87.6 k Q&A pairs (74 MB)
│   ├── processed\
│   │   ├── common_pile\            ← 246 shards (2.3 GB)
│   │   ├── gutenberg_books\        ← 12 shards (42 MB, 58 k chunks)
│   │   └── squad\                  ← 2 shards (74 MB)
│   ├── tokenized\                  ← packed uint16 .bin shards
│   │   ├── common_pile\            ← 246 .bin (~496 M tokens)
│   │   ├── gutenberg_books\        ← 12 .bin (~12.5 M tokens)
│   │   └── squad\                  ← 2 .bin (~19.3 M tokens)
│   └── tokenizer\
│       └── glemton-bpe-32k.json    ← trained 32 k BPE
├── checkpoints\
│   └── glemton-debug-10m\          ← 5 intermediate + final (each ~47 MB)
└── logs\                           ← every install / download / prep / train log
```

**Corpus inventory:** ~ 528 M training tokens total, all permissively licensed.
- Common Pile v0.1 subsets — academic / books / reference (~ 496 M, 94 % of corpus)
- Project Gutenberg classics — dialogue-rich novels and plays (~ 12.5 M, 2.4 %)
- SQuAD — Q&A pairs as single-turn dialogue (~ 19.3 M, 3.6 %)

## What worked

| | Status |
|---|---|
| Project scaffold + .venv + Apache-2.0 license | done |
| PyTorch 2.12 nightly cu128 + transformers + tokenizers + datasets + wandb + utilities | done |
| Verified PyTorch sees the 5070 with bf16 + sm_120 | done |
| Model code (350 M target, 12 M debug, 50 M mid) — all build + forward | done |
| Training loop with bf16 + grad accum + cosine LR + checkpoints | done |
| BPE tokenizer trained from scratch (32 k vocab, turn markers as special tokens) | done |
| Shard packing pipeline (uint16 mmap) | done |
| **Phase 0 — 12 M model trained on 50 M tokens to loss 4.0** | done |
| Inference + chat tooling + sampling | done |
| Sycophancy probe + long-conversation probe **eval pipelines both validated end-to-end** | done |
| 79-book Gutenberg corpus + SQuAD added | done |
| Two git commits attributed to ninjahawk only (no Claude footer) | done |
| Midsize 50 M training launched | running |

## What didn't work — and the workarounds

1. **OpenSubtitles, DailyDialog, EmpatheticDialogues** — every HF mirror still uses Python loader scripts, which `datasets >= 4.x` no longer supports. We could not pull any of these in the overnight session.
   - **Workaround:** SQuAD (which *is* parquet-native) was substituted as a Q&A dialogue surrogate. For the full v1.0 corpus you'll either need to source OpenSubtitles directly from the OPUS project's plain-text dumps (opus.nlpl.eu) or find a hand-converted parquet mirror.

2. **Most Stack Exchange .7z dumps 404'd on archive.org.** Only philosophy + skeptics arrived (195 MB). The archive bundle paths have apparently shifted.
   - **Workaround:** check https://archive.org/details/stackexchange directly; the file naming changed. Also `py7zr` is needed to actually extract these — not installed.

3. **bitsandbytes 8-bit Adam on Windows + Blackwell** — installed without erroring but its native CUDA kernels may not load at runtime. `train.py` falls back to plain `AdamW` automatically. The 12 M debug train used plain AdamW; no degradation observed.

4. **Corpus is far smaller than the 7 B Chinchilla-optimal target.** Current ~528 M tokens is ~7.5 % of the budget. With a 350 M model trained on 528 M tokens, you'd be training "wide and shallow" — the result wouldn't show the angle as clearly as a fully Chinchilla-trained run.

## What needs your decisions

1. **Push the repo.** I set `user.name = ninjahawk` and `user.email = ninjahawk@users.noreply.github.com`. Two commits ready. Just `git push -u origin main`.

2. **Corpus shortfall.** Three reasonable v1.0 paths:
   - **(a) Source more dialogue data manually.** OPUS OpenSubtitles plain text, more Stack Exchange archives, additional CC-licensed conversational corpora.
   - **(b) Pull more from Common Pile.** It's 8 TB total; the 2.3 GB I streamed is a tiny slice. Expanding this is the lowest-friction path, but increases the academic-text dominance further.
   - **(c) Accept a "data-limited" v1.0** and train on ~500 M tokens, labeling the model honestly as undertrained.
   - **My honest pick: (b) + accept (c) for v1.0.** Common Pile expansion is one script-edit away (raise the streaming cap in `download_data.py`). Ship Glemton 1.0 at ~500 M-1 B tokens, call it "Glemton 1.0 — data-limited preview," document the limitation clearly in the model card, and use the lessons + the eval baselines to budget a Glemton 2.0 with proper data.

3. **bitsandbytes on Windows / Blackwell.** If you want the 8-bit Adam memory savings for the full 350 M run, this needs verification. The workaround (plain AdamW) costs roughly 4 GB extra VRAM at our config — uncomfortable but fits in 12 GB.

## Honest summary

Everything that the *toolchain* could block, isn't blocking. PyTorch sees the 5070, training works, sampling works, the eval pipelines run end-to-end. The architecture's correct, the tokenizer's trained, the data pipeline mmaps. Phase 0 actually trained a working tiny model with a clean loss curve.

The remaining hard problem is **data**. The HuggingFace `datasets` library deprecating loader scripts in v4.x meaningfully changed what's reachable overnight — three of the planned dialogue sources became out-of-reach without manual sourcing. We pivoted to SQuAD + many more Gutenberg books to compensate.

You have a working open-source small LM project skeleton, a Phase 0 validation, two interesting eval pipelines, and a reasonable starting corpus. The next two weeks of work are mostly: (1) decide on the data path above, (2) bring the corpus to a defensible token budget, (3) launch the actual 350 M pretrain run for 1–4 weeks of GPU time, (4) measure the headline claims, (5) ship Glemton 1.0.
