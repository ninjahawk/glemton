# Prior art — honest comparison

This file is the public, running comparison between Glemton and the existing work that shares any axis with it. If a closer prior-art match surfaces during the project, **update this file before claiming novelty anywhere else**.

## On "small base model without instruction tuning"

**Not novel.** Plenty of base models ship without instruction tuning:

| Model | Size | Notes |
|---|---|---|
| `HuggingFaceTB/SmolLM2-360M` (base) | 360 M | Trained on FineWeb-Edu (web text). Has an `-Instruct` variant. |
| `allenai/OLMo-1B` | 1 B | Fully open base model, web text + code. |
| `EleutherAI/pythia-410m` | 410 M | The Pile, no instruction tuning. |
| `bigscience/bloom-560m` | 560 M | Multilingual, no instruction tuning. |

These all exist, all have open weights. None of them are conversational by design — they're general LM bases whose conversational ability comes after later instruction tuning.

## On "anti-sycophancy"

**Not novel.** Mitigation literature:

| Paper / project | Mechanism |
|---|---|
| Constitutional AI (Anthropic, 2022) | Principle-based RLHF, includes anti-sycophancy as an explicit principle |
| "Towards Understanding Sycophancy" (Sharma et al., arXiv 2310.13548) | Characterizes sycophancy in RLHF'd models |
| Linear Probe Penalties (arXiv 2412.00967) | Quantifies sycophancy via a linear probe in the reward model, penalizes it |
| "Ask don't tell" (arXiv 2602.23971) | Reduce sycophancy via prompting |
| Measuring Sycophancy in Multi-turn (arXiv 2505.23840) | Benchmark + measurement |

These all start from a model that has *already been* instruction-tuned, and try to undo or counter the sycophancy. Glemton's approach is upstream: don't train on the data that introduces the sycophancy in the first place.

## On "exclude synthetic assistant data from pretraining"

**Mostly uncommon, but adjacent work exists.** Closest:

- **"Non-instructional Fine-tuning"** (arXiv 2409.00096) — uses random web-text completions instead of explicit instructions. Adjacent, but they still use GPT-3.5/4 completions to *generate* the targets, which re-introduces the contamination we're avoiding.
- **Various "raw"/"uncensored" community finetunes on HuggingFace** — these typically strip refusals from datasets like Alpaca/ShareGPT but still train on the underlying synthetic assistant turns. Different goal.

What Glemton claims that does appear uncommon:
> Pretrain a *conversational* model exclusively on a curated **dialogue-heavy human corpus** (Gutenberg Dialogue + OpenSubtitles + Stack Exchange + Ubuntu Dialogue + plays + interviews + public-domain books) with **zero instruction-tuning stage**, then **evaluate it as a conversational model** under multi-turn conditions.

If that claim turns out to overlap with something we missed, update this file and re-cast the angle as a **scale + accessibility + measurement** story rather than a novelty story.

## On "from-scratch small models on consumer GPUs"

**Established practice.** TinyLlama (1.1 B, 1 T tokens, 16× A100 × 90 days), SmolLM family (135 M / 360 M / 1.7 B), Pythia (70 M – 12 B), MicroLLaMA, BabyLM submissions. The recipe is open and well-documented; what Glemton inherits from this body of work is mostly the *training stack*, not the angle.

## On architecture choices

The dense-transformer-with-GQA-and-sliding-window choice is the modern default: it's what Llama-3, Qwen-3, Mistral-Small, and SmolLM-2 use. Nothing novel here, and that's deliberate — the architecture is the boring part. The interesting part is the corpus + the missing SFT stage.

## What the project does NOT need to be novel about, even if employer-pitched

- Tokenizer (BPE, 32 k vocab is standard).
- Optimizer (AdamW 8-bit, gradient accumulation).
- Precision (bf16 mixed).
- Eval methodology (the *probe* designs in `eval_sycophancy.py` and `eval_long_conversation.py` are simple and easy to copy — that's fine; the value is in the model that scores well on them).
