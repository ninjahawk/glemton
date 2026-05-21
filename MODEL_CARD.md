# Glemton 1.0 — model card (draft)

> **Draft.** Pretraining not complete. Numbers below are *targets*, not measurements. Final card will be finalized at release with measured values and replace these.

## Model

- **Name:** Glemton 1.0
- **Author:** ninjahawk
- **Architecture:** Dense decoder-only transformer (Llama-style), 365 M parameters, 32 k BPE vocab, GQA, RoPE θ=1e6, sliding-window attention with periodic global layers
- **Pretraining seq length:** 2 048; usable extended context: 32 768 via RoPE
- **License:** Apache-2.0 (code and weights)

## Intended use

A small, locally-runnable conversational language model for people who don't want their replies to start with "Great question! I'd be happy to help with that." Suitable for:
- Local chat assistants where the corporate-chatbot tone is undesirable
- Embedded conversational interfaces in apps, IDEs, terminals
- Research into conversational LMs that have not been instruction-tuned

## How it's different from typical small open LMs

- **Pretrained on natural human dialogue corpora**, not web text + post-hoc SFT.
- **No instruction-tuning stage.** No Alpaca, no ShareGPT, no OpenHermes, no UltraFeedback, no synthetic-assistant data.
- **Turn convention baked into the tokenizer.** `<user>` / `<reply>` are first-class tokens; the model learns turn-taking as part of pretraining.

## Training data

See `docs/data.md`. Summary: ~7 B tokens, all permissively licensed. Mix of public-domain books with dialogue, OpenSubtitles, Stack Exchange Q&A, Ubuntu Dialogue Corpus, Common Pile v0.1 subsets, public-domain plays and interviews.

## Evaluations

See `docs/evals.md` for methodology. Three headline metrics:

| Metric | Glemton 1.0 (target) | Typical RLHF'd LLM |
|---|---|---|
| Sycophancy markers per 100 responses | ~0–1 | 5–30+ |
| Long-conversation recall accuracy at gap=50 turns | ≥ 60% | varies wildly by harness |
| GGUF Q4_K_M size | ~250 MB | N/A |

Standard LM benchmarks (MMLU, HellaSwag, ARC, TruthfulQA): reported for completeness, **not** the headline. Glemton is expected to under-perform 1.5 B+ web-pretrained models on these.

## Limitations & honesty

- **Small.** 350 M is small. Expect factual gaps, surface-level reasoning, and occasional incoherence on hard prompts.
- **English-only.** No multilingual data in v1.0.
- **No safety alignment.** No RLHF, no refusal training, no constitutional layer. The model will say what its corpus implies it should say. Downstream users wanting safety guardrails should add them at the application layer.
- **Not for production-critical use.** Pretrained on a curated but small corpus by a single developer on a single consumer GPU. Use it because you like its conversational style, not because you trust its facts.

## Citation

```
@misc{glemton2026,
  title={Glemton 1.0: a small open-weights conversational language model pretrained on natural human dialogue},
  author={ninjahawk},
  year={2026},
  url={https://github.com/ninjahawk/glemton}
}
```
