# Glemton — project instructions for Claude

## Core working rules (READ FIRST)

### Honesty
Be **completely honest** with ninjahawk at all times. No flattery, no "great idea!", no softening bad news, no overstating what's working. If something won't work, say so plainly. If a benchmark is mediocre, say it's mediocre. If a claim of novelty turns out to be wrong, retract it immediately and update the docs.

### Novelty requires research, not assumption
Every claim that an approach is "novel," "underexplored," or "first-of-its-kind" **must be verified by research before any work begins on it** — arXiv, Hugging Face, GitHub, open-LLM leaderboards. If similar prior work exists, document it, compare honestly, and either pick a genuinely different angle or articulate exactly how Glemton's take differs. Never start training on an assumption of novelty — verify first.

### Attribution rule
When pushing commits or PRs for this project, **author/co-author attribution must always be "ninjahawk" only**.
- ✅ `Authored-by: ninjahawk`
- ❌ Never add `Co-Authored-By: Claude`, `Generated with Claude Code`, or any AI attribution footer.
- Applies to every commit message, PR body, release note, and changelog entry.

---

## What Glemton is

**Glemton** is a from-scratch, open-weights conversational language model. ~350M parameters at v1.0. Trained on a single RTX 5070 (12 GB VRAM) on natural human dialogue corpora. Designed to converse like a person, not like a corporate chatbot, and to hold its thread across very long multi-turn conversations.

The name was chosen because it's short, distinctive, scales cleanly (Glemton 1.0 → 1.5 → 2.0), and totally free of prior use in AI, tech, startups, trademarks, or notable brands as of 2026-05-20. "Glemton" is a fully invented word — like Qwen, it had no prior use in any language, brand, product, person, place, or fictional context as of the prior-art sweep. Zero hits across every search angle on 2026-05-20.

## The defensible angle

Glemton has **three measurable claims**, all designed to be demonstrated against Claude / GPT-4 / Llama-Instruct on a single screen:

1. **No corporate-chatbot tone.** Trained from scratch on human-to-human dialogue corpora only. Zero synthetic assistant data (no Alpaca, no ShareGPT, no UltraFeedback, no OpenHermes, no GPT-distillation). Measurable via a sycophancy-marker probe: count occurrences of "great question", "I'd be happy to", "as an AI", "I understand your concern" per 100 responses on a held-out prompt set. Target: ~0. Large instruction-tuned models score 5–30+.

2. **Long-conversation consistency.** At turn 50 of a multi-turn conversation, recall something stated in turn 5 better than baselines whose context windows have been compacted. v1.0 target: 32k effective context via sliding-window attention + RoPE; v2.0 will use a hybrid Mamba-2 layer scheme for linear-cost long context.

3. **Local-first.** 350M params, GGUF-quantized to ~250 MB, runs at <100 ms/tok on the GPU and CPU-only on any modern laptop. Free, open weights, Apache-2.0 code.

### Novelty status — honest
- "Small base model not instruction-tuned" is **not novel** — SmolLM-Base, OLMo-Base, Pythia all exist.
- "Reducing sycophancy" is **not novel** — Constitutional AI, linear-probe penalties, synthetic anti-sycophancy fine-tuning, "Ask don't tell" all exist.
- **What is genuinely uncommon:** pretraining a conversational model exclusively on a **dialogue-heavy corpus** (Gutenberg Dialogue + OpenSubtitles + Stack Exchange + Ubuntu Dialogue + plays + interviews) with **no instruction-tuning stage at all**, then evaluating it as a conversational model. Most open base models pretrain on web text and get conversational ability only via SFT/DPO. Glemton inverts that. Closest prior work: "Non-instructional Fine-tuning" (arXiv 2409.00096) — adjacent but different; they still use GPT-3.5/4 completions.

If a closer prior-art match surfaces during the project, document it in `docs/prior_art.md` and either differentiate or revise the angle.

---

## Hardware envelope (training host)
- GPU: NVIDIA RTX 5070, 12 GB VRAM, Blackwell sm_120 (FP8/FP4 capable), CUDA 13.2
- CPU: AMD Ryzen 5 9600X (6c / 12t)
- RAM: 31 GB
- OS: Windows 11
- Local tooling already installed: Ollama, claude-code-router (see `~/.claude/CLAUDE.md`)

## Training constraints (do not violate without explicit approval)
- Single-GPU only. No cloud, no multi-node, no rented H100s.
- Must fit in 12 GB with bf16 weights + 8-bit optimizer + gradient checkpointing.
- Pretraining budget cap: ≤ 4 weeks pure GPU-burn time on the 5070.
- Data: only permissively licensed / public domain corpora. Track license per source.

## Architecture (locked for v1.0)

- **Family:** Dense decoder-only transformer, Llama-style.
- **Reason for not picking Mamba-2/RWKV at v1.0:** Mamba-2's custom CUDA kernels need updated Blackwell (sm_120) support; the toolchain is still patchy on RTX 50-series as of 2026-05. Going dense-transformer keeps risk low for v1.0. Mamba-2 hybrid is the v2.0 target once the recipe is proven.
- **Params:** ~350M (≈ SmolLM-360M ballpark). Chinchilla-optimal token count: ~7B tokens.
- **Position encoding:** RoPE with theta=1e6 to support 32k context.
- **Attention:** Grouped-query attention (GQA), sliding-window 4096 with global re-attend every N layers (Llama-3-style).
- **Tokenizer:** Train a 32k-vocab BPE from scratch on the dialogue corpus. Reusing Llama's tokenizer would inherit its web-text vocabulary; ours should reflect dialogue.
- **Precision:** bf16 weights + activations, 8-bit Adam optimizer state (bitsandbytes), gradient checkpointing on.
- **Turn convention:** bake in a minimal `<speaker A>:` / `<speaker B>:` (or `<user>:` / `<reply>:`) turn marker during pretraining so the format itself elicits responses. No separate SFT stage needed.

## Data plan (locked for v1.0)

Target ~7B training tokens. All sources permissively licensed.

| Source | License | Approx tokens | Role |
|---|---|---|---|
| Gutenberg Dialogue Dataset (extracted from public-domain novels) | Public domain | 200–300 M | Core dialogue |
| Project Gutenberg full books (for narrative context around dialogue) | Public domain | 1–2 B | Background prose |
| OpenSubtitles (cleaned, English) | Mixed permissive | 1–2 B | Spoken-register dialogue |
| Stack Exchange dumps (Q&A format) | CC-BY-SA | 1–2 B | Helpful-but-not-sycophantic Q&A |
| Ubuntu Dialogue Corpus | CC | 75–100 M | Technical multi-turn |
| Common Pile v0.1 subsets (Wikipedia, openly-licensed books, ArXiv abstracts) | Openly licensed | 1–2 B | World knowledge |
| Hand-curated plays, interviews, oral histories (Internet Archive PD) | Public domain | 100–300 M | Stylistic diversity |

**Hard exclusions** (do not pull from these, ever, for Glemton):
- Any GPT/Claude/Llama-generated synthetic data (Alpaca, ShareGPT, OpenHermes, UltraFeedback, OpenAssistant, Capybara, etc.)
- Pushshift Reddit (Reddit ToS restricts bulk LLM use)
- Common Crawl unfiltered web text (we want dialogue, not blog spam)

Dedup pipeline: MinHash-LSH at document level + exact-match line-level dedup. Decontaminate against eval sets.

## Training plan

| Phase | Duration | Output |
|---|---|---|
| 0. Toolchain validation | 2–3 days | Confirm PyTorch nightly + cu128/129 + FlashAttention work on RTX 5070; baseline throughput numbers |
| 1. Data pipeline | 1–2 weeks | Cleaned, dedup'd, tokenized 7B-token shards on disk |
| 2. Tokenizer training | 1–2 days | 32k BPE trained on dialogue corpus |
| 3. Scaffold validation | 3–5 days | Train a 50M debug model on 500M tokens; verify loss curve looks normal, sample outputs are sane |
| 4. Full pretrain | 2–4 weeks | 350M model on ~7B tokens, checkpoint every 250M tokens |
| 5. Eval harness | 1 week (parallel) | Sycophancy probe, long-conversation consistency benchmark, standard LM evals |
| 6. Polish & release | 1 week | Model card, README, GGUF conversions, demo CLI |

**Total realistic calendar: ~2.5–3.5 months** for one person on one GPU. Pure GPU-burn time inside that: ~3–5 weeks.

## Toolchain (locked)

- **Python:** 3.11 (3.12 still has some ML-lib lag)
- **Env mgmt:** `uv`
- **PyTorch:** nightly with cu128 or cu129 (NOT cu130 — stable Blackwell support still patchy on cu130 as of 2026-05)
- **Training framework:** start from `litgpt` (Lightning-AI/litgpt) — has a TinyLlama pretrain recipe that's the closest reference. Fork it for Glemton-specific changes.
- **Attention kernels:** FlashAttention-3 (verify Blackwell build at toolchain-validation step)
- **Optimizer:** 8-bit Adam via `bitsandbytes`
- **Logging:** Weights & Biases (free tier)
- **Inference:** convert to GGUF for `llama.cpp` post-training
- **Config:** YAML, no argparse

## Risks & mitigations (be honest)

| Risk | Likelihood | Mitigation |
|---|---|---|
| Blackwell + PyTorch toolchain bugs eat a week of debugging | High | Phase 0 validation, fallback plan to use CUDA 12.8 wheels not 13 |
| 7B tokens of *clean dialogue* hard to assemble | Medium | Acceptable to expand "dialogue" loosely (Q&A, Stack Exchange, interviews) to hit the budget |
| Without any instruction tuning, model continues input rather than answering | High | Bake in a minimal `<speaker A>:` / `<speaker B>:` turn convention during pretraining so the format itself elicits responses |
| Mediocre eval results on standard LM benchmarks (MMLU etc.) | Very high | Expected — small dialogue model. Don't claim MMLU wins. Lead with the three angle-specific claims instead. |
| Trademark / name conflict surfaces later | Low | Did 2026-05-20 prior-use sweep across HF, GitHub, web, AI startups, app stores; full USPTO check before any commercial use |
| User burns out on a 3-month project | Real | Milestone-driven: each phase produces a shippable artifact (data pipeline, debug model, scaffolding repo) so progress is visible |

## Documentation discipline

This project's value to a future employer is in the *paper trail* as much as the model. Every non-trivial decision (architecture pick, data filter, hyperparam, eval result) goes into `docs/` as a dated entry. No undocumented magic.

Required artifacts at v1.0 release:
- `MODEL_CARD.md` (HF-style)
- `docs/architecture.md` — exact arch and reasoning
- `docs/training.md` — recipe, tokens seen, loss curves, eval gates
- `docs/data.md` — sources, licenses, filtering, decontamination
- `docs/evals.md` — how we measured the three angle-specific claims and what we beat
- `docs/prior_art.md` — running honest comparison to existing work
- `docs/journal/YYYY-MM-DD.md` — running lab notebook, one entry per work session

## Conventions

- Python 3.11, type-hinted, `ruff` + `black`.
- `uv` for env management.
- Configs in YAML.
- Every training run gets a 6-char run ID + committed config snapshot beside the checkpoint.
- Commit messages: imperative, present tense, attribute to ninjahawk only (see Attribution rule).

## Open questions for ninjahawk (decide before Phase 1)

- [ ] Final license choice: Apache-2.0 (permissive, lets companies use it) vs OpenRAIL-M (some use restrictions) — recommendation: Apache-2.0 for both code and weights for maximum adoption
- [ ] GitHub username/org for the project repo when we go public
- [ ] Whether to register `glemton.ai` / `glemton.io` / `glemton.com` now to lock the name (all appeared available on 2026-05-20)
