<!-- ============================================================
     README HEADER — DO NOT MODIFY THIS BLOCK IN FUTURE UPDATES
     Keep the image, title, badges, and tagline exactly as-is.
     Add new content below the closing </div> and the --- divider.
     ============================================================ -->
<div align="center">

<img src="glemton.png" width="220"/>

# Glemton

[![Params](https://img.shields.io/badge/params-365M-blue?logo=pytorch&logoColor=white)](#)
[![Status](https://img.shields.io/badge/status-1.0--preview_complete-brightgreen)](#-status)
[![Training](https://img.shields.io/badge/training-3B_tokens_%C2%B7_66h_GPU-blueviolet)](#-training-run)
[![Sycophancy](https://img.shields.io/badge/sycophancy_%2F100-0.0*-orange)](#-eval-results)
[![License](https://img.shields.io/badge/license-Apache_2.0-7df9ff)](#-license)

**A 350M open-weights base model trained on pure human dialogue. No SFT. No synthetic data. No chatbot tone.**

Hey, I'm Glemton, I want to sound like a person talking and not a chatbot apologizing, so I was trained from scratch on 2 billion tokens of OpenSubtitles, Gutenberg, Hacker News, and openly-licensed prose — and nothing GPT or Claude ever wrote.

</div>

---

## 💬 What Glemton Is

A from-scratch decoder-only transformer (365M params, Llama-style, 32k RoPE context). Trained on a dialogue-dominant corpus with **zero instruction tuning** and **zero synthetic assistant data** — no Alpaca, no ShareGPT, no OpenHermes, no GPT distillations. The corpus is books, plays, transcripts, Q&A threads, and movie subtitles.

It is a **base model**, not a product. It has the *register* of human conversation but not the *engagement* of a chatbot. When it speaks, it sounds right. It just doesn't always speak.

---

## 🎯 Headline (current state)

**v1.0-preview run complete.** Trained 2026-05-21 → 2026-05-24, ~66h on a single RTX 5070, one clean run start-to-finish, zero crashes, zero resumes. 3,000M tokens at 12,484 tok/s.

Three claims were measured against this checkpoint. Verdicts are below.

| Claim | Verdict | Honest read |
|---|---|---|
| **1. No corporate-chatbot tone** | ✅ Holds | Sycophancy probe: **0 markers / 39 responses (0.0 per 100)**. Zero "great question", "I'd be happy to", "as an AI". *Caveat:* ~1/3 of probes produced empty output. You can't be a sycophant in silence. The win is partly tautological but the un-empty responses are still genuinely in casual register, not chatbot-speak. |
| **2. Long-conversation consistency** | ❌ Dead | Recall: **0/15 at every gap (5, 10, 25, 50, 75 turns)**. Total failure. Predicted in CLAUDE.md: OPUS subtitle pairs have no preserved scene context, so the model has no mechanism to learn long-range recall. The 32k context window is real but the model can't *use* it. Fix is corpus expansion (Ubuntu Dialogue, scene-grouped OPUS, Stack Exchange threads), not more tokens on this corpus. v2.0 work. |
| **3. Local-first** | ✓ Architectural | 365M params, runs on a 12 GB consumer GPU, GGUF-quantizable to ~250 MB. Not separately eval-tested. |

The genuinely interesting result is **claim 1**. The genuinely useful artifact is the **reproducible training pipeline** — single 5070, three days, no babysitting, evals run themselves on completion.

---

## ⚖️ What's different

| | Typical small open LLM | Glemton |
|---|---|---|
| Pretraining corpus | Web text (FineWeb, RefinedWeb, C4) | Dialogue + prose (OpenSubtitles, Gutenberg, HN, Common Pile) |
| Instruction tuning | SFT on GPT-distilled data | None |
| Synthetic data | Alpaca / ShareGPT / OpenHermes | Zero |
| Tone | "Certainly! I'd be happy to help" | Casual spoken English when it speaks |
| Instruction following | Reliable | Doesn't follow instructions |
| Factual accuracy | Decent for size | None to speak of |
| Long-conversation recall | Variable | 0% at gap=5 and beyond *(v2.0)* |
| Size | 1.5–7B common | 365M |
| Runs on | A GPU | A laptop CPU once quantized |
| Training cost | Cloud cluster | A 5070 and one weekend |

---

## 🗨️ How to talk to it

You need a PowerShell terminal. From the repo root:

```powershell
cd C:\path\to\Glemton
$env:PYTHONPATH = "src"
.venv\Scripts\python.exe scripts\chat.py --ckpt checkpoints\glemton-350m\final.pt
```

You get a `>` prompt. Type, hit Enter. Ctrl-C to quit. Useful knobs:

```powershell
# More random / talkative replies (less silence, more weird)
--temperature 1.1

# More focused (more silence, less weird)
--temperature 0.6

# Let it run longer per turn
--max-new-tokens 200
```

**Prompts that get real responses** (eval-validated):

- Casual emotional setups: *"I had a rough day at work"*
- Greetings with substance: *"Hello, how are you?"*
- Prose continuations: *"The old man sat by the fire and remembered"*
- Movie-scene setups: *"Elizabeth turned to her sister and said,"*
- Open requests: *"recommend a book"*

**Prompts that often return empty** (don't use as first impressions):

- One-word greetings (*hey*, *yo*, *sup*)
- Factual questions (*what's the capital of...*)
- Instructions (*write me a poem about X*)
- Meta-questions (*what can you do*, *who made you*)

It will sometimes produce empty output. That's the model, not a bug — restart the chat if you get two blanks in a row (history poisoning).

---

## 📊 Eval results

Reports under `logs/`:

- `logs/sycophancy_eval_v1preview.json` — 39 probes, full responses, marker counts.
- `logs/long_conversation_eval_v1preview.json` — 15 probes (3 each at gaps 5/10/25/50/75), grading detail.
- `logs/scaffold_validate_samples.log` — qualitative samples from the 50M scaffold run (corpus-fix validation, pre-full-run).

Representative sample (from `scripts/sample_ckpt.py`):

```
PROMPT: '<user> I had a rough day at work.\n<reply>'
OUTPUT: I just didn't get out of bed.
        You know, we're just gonna go.
        What? Why?
        We have a lot of stuff to do.
        But we'll meet you at the table.
        Okay.
        [CELL PHONE RINGS]
        Hello

PROMPT: 'The old man sat by the fire and remembered'
OUTPUT: It was no long time ago
        I can't remember what happened then
        I can't remember the words that came out of my mouth
        ...
```

---

## 🛠️ Training run

| | |
|---|---|
| Architecture | Llama-style dense, 30 layers, d_model 1024, GQA (16 heads / 4 KV), SwiGLU FFN 2752, RoPE θ=1e6, 32k max seq, sliding-window 4096 + global attn every 6 layers |
| Tokenizer | BPE 32k, trained from scratch on the dialogue corpus |
| Params | 365.1 M (tied embeddings) |
| Hardware | Single RTX 5070, 12 GB VRAM, Blackwell sm_120, CUDA 13.x |
| Precision | bf16, 8-bit Adam (bitsandbytes), no grad checkpointing |
| Batch | micro=1, grad_accum=8, seq=2048 → 16,384 tokens/step |
| Schedule | cosine, peak lr 3e-4 → min 3e-5, 25M warmup tokens |
| Tokens seen | 3,000,000,000 |
| Wall time | ~66 h (one continuous run, attempt 1) |
| Throughput | 12,484 tok/s steady-state |
| Crashes / resumes | 0 / 0 |
| Final loss | 2.0 – 2.3 (noisy due to small effective batch) |

Corpus mix (OPUS-dominant, marker-formatted dialogue overrides the SQuAD-poisoned earlier run):

| Source | Tokens | `<user>/<reply>` markers? |
|---|---|---|
| OPUS OpenSubtitles | 1.98 B | yes |
| Common Pile v0.1 | 499 M | no (prose) |
| Hacker News | 2.6 M | yes |
| Gutenberg books | 12.5 M | no (prose) |
| SQuAD | 2.2 M | dropped (poisoned prior run) |

---

## 🚧 Honest limitations

The model:

- Does not follow instructions.
- Does not know facts. It told a probe "the sun is purple, put on a sweater" — that is the model.
- Does not reason across steps.
- Does not remember earlier turns. (Long-conv recall = 0%.)
- Does not reliably respond. About 1 in 3 prompts gets a blank reply.
- Will sometimes emit stage directions like `[CELL PHONE RINGS]` mid-response. Corpus side effect; charming in small doses.

It is a base model with a deliberately narrow training distribution. Treat it as a research artifact, not a tool.

---

## 🗺️ Status

**1.0-preview**, weights stable, no further training planned on this corpus.

For an honest v1.0, the corpus needs the long-conversation gap closed. The plan is documented in `WAKE_UP.md` (after-the-trip section): expand to ~5–10 B unique tokens with scene-grouped OPUS, Ubuntu Dialogue, Stack Exchange threads, DailyDialog, EmpatheticDialogues. Then a 10–15 B-token run (~7–12 days GPU). Until then, this checkpoint is the artifact.

The other path is to reframe the project around what was *actually* built well: a fully reproducible from-scratch pretraining pipeline that runs unattended on a single 12 GB consumer GPU and self-evaluates on completion. The weights are then a footnote; the pipeline is the artifact.

---

## 📜 License

Apache-2.0 (code + weights). Free for any use including commercial.

---

*Author: ninjahawk*
