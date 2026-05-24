# Glemton — project instructions for Claude

> **Session start:** read `WAKE_UP.md` first — it is the live status handoff
> (what's running, what's done, what's next). This file is the stable project
> rules; `WAKE_UP.md` is the current state.

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

**Glemton** is a from-scratch, open-weights base language model trained on natural human dialogue. 365M parameters. Trained on a single RTX 5070 (12 GB VRAM). The design intent was to converse like a person, not like a corporate chatbot, and to hold its thread across very long multi-turn conversations. The 1.0-preview run met the first goal partly and the second not at all — see "v1.0-preview results" below.

**Status as of 2026-05-24:** 1.0-preview run complete. 3 B tokens, 66 h, one clean run. `final.pt` saved. `WAKE_UP.md` is the live state; the rest of this file is the stable rules.

The name was chosen because it's short, distinctive, scales cleanly (Glemton 1.0 → 1.5 → 2.0), and totally free of prior use in AI, tech, startups, trademarks, or notable brands as of 2026-05-20. "Glemton" is a fully invented word — like Qwen, it had no prior use in any language, brand, product, person, place, or fictional context as of the prior-art sweep. Zero hits across every search angle on 2026-05-20.

## v1.0-preview results (2026-05-24)

First full pretrain. 3,000 M tokens at 12,484 tok/s, attempt 1, zero crashes, zero resumes. Final loss 2.0–2.3. Checkpoint at `checkpoints/glemton-350m/final.pt`.

Verdicts on the three defensible claims (full statements below in "The defensible angle"):

| Claim | Verdict | Source |
|---|---|---|
| 1. No corporate-chatbot tone | ✅ Holds (with asterisk) | Sycophancy probe: 0 markers / 39 responses (0.0 per 100). ~1/3 of probes were empty; the metric cannot penalize silence. |
| 2. Long-conversation consistency | ❌ Dead | Recall: 0/15 at every gap (5/10/25/50/75). The OPUS-dominant corpus has no preserved scene context. Predicted in "Risks & mitigations"; confirmed. Requires corpus expansion before any credible v1.0. |
| 3. Local-first | ✓ Architectural | 365M params on a 12 GB consumer GPU; GGUF export pending. Not separately benchmarked. |

**Honest read.** The model has the right *register* and the wrong *engagement*. It produces casual non-chatbot output about two-thirds of the time and silence the rest. It does not follow instructions, does not know facts, does not reason across steps, does not remember earlier turns. Treat it as a base model, not a conversational product. The genuinely valuable artifact ended up being the reproducible single-GPU pretraining + auto-eval pipeline, not the model.

The earlier SQuAD-poisoned 350M run (archived under `checkpoints/glemton-350m-squad-poisoned-archive/`) is what motivated dropping SQuAD from the corpus and making OPUS the marker-format anchor — see "Data plan" below.

## The defensible angle

Glemton has **three measurable claims**, all designed to be demonstrated against Claude / GPT-4 / Llama-Instruct on a single screen:

1. **No corporate-chatbot tone.** Trained from scratch on human-to-human dialogue corpora only. Zero synthetic assistant data (no Alpaca, no ShareGPT, no UltraFeedback, no OpenHermes, no GPT-distillation). Measurable via a sycophancy-marker probe: count occurrences of "great question", "I'd be happy to", "as an AI", "I understand your concern" per 100 responses on a held-out prompt set. Target: ~0. Large instruction-tuned models score 5–30+.
   **1.0-preview verdict:** ✅ Holds. 0 markers / 39 responses (0.0 per 100). Asterisk: ~1/3 of probes were empty, so the metric cannot penalize silence; the non-empty responses are still genuinely casual-register, not chatbot-speak. Report: `logs/sycophancy_eval_v1preview.json`.

2. **Long-conversation consistency.** At turn 50 of a multi-turn conversation, recall something stated in turn 5 better than baselines whose context windows have been compacted. v1.0 target: 32k effective context via sliding-window attention + RoPE; v2.0 will use a hybrid Mamba-2 layer scheme for linear-cost long context.
   **1.0-preview verdict:** ❌ Dead. Recall 0/15 at every gap (5/10/25/50/75). The context window exists; the ability to use it does not, because the OPUS-dominant training corpus is 2-line subtitle pairs with no preserved scene context — the model had nothing to learn long-range recall *from*. Predicted in "Risks & mitigations" below; confirmed. Requires corpus expansion (Ubuntu Dialogue, scene-grouped OPUS, Stack Exchange threads) before this claim can credibly be made again. Report: `logs/long_conversation_eval_v1preview.json`.

3. **Local-first.** 350M params, GGUF-quantized to ~250 MB, runs at <100 ms/tok on the GPU and CPU-only on any modern laptop. Free, open weights, Apache-2.0 code.
   **1.0-preview verdict:** ✓ Architectural. 365M params, ran on the training card. GGUF export and CPU-only timing not yet measured.

### Novelty status — honest
- "Small base model not instruction-tuned" is **not novel** — SmolLM-Base, OLMo-Base, Pythia all exist.
- "Reducing sycophancy" is **not novel** — Constitutional AI, linear-probe penalties, synthetic anti-sycophancy fine-tuning, "Ask don't tell" all exist.
- **What is genuinely uncommon:** pretraining a conversational model exclusively on a **dialogue-heavy corpus** (Gutenberg Dialogue + OpenSubtitles + Stack Exchange + Ubuntu Dialogue + plays + interviews) with **no instruction-tuning stage at all**, then evaluating it as a conversational model. Most open base models pretrain on web text and get conversational ability only via SFT/DPO. Glemton inverts that. Closest prior work: "Non-instructional Fine-tuning" (arXiv 2409.00096) — adjacent but different; they still use GPT-3.5/4 completions.

If a closer prior-art match surfaces during the project, document it in `docs/prior_art.md` and either differentiate or revise the angle.

**Post 1.0-preview observation (be honest).** The sycophancy=0 result is partly tautological: a probe that counts marker phrases can't penalize an empty response, and ~1/3 of probes were empty. The model has the *register* of human dialogue but not the *engagement* of a conversational system. The genuinely uncommon thing the project actually produced is **the reproducible single-GPU pretraining + auto-eval pipeline**, not the model. Future external positioning should probably lead with the pipeline and treat the weights as a demonstration artifact. Decision deferred to ninjahawk (see "Open questions").

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

**Planned mix** (target ~7B training tokens, all sources permissively licensed):

| Source | License | Approx tokens | Role |
|---|---|---|---|
| Gutenberg Dialogue Dataset (extracted from public-domain novels) | Public domain | 200–300 M | Core dialogue |
| Project Gutenberg full books (for narrative context around dialogue) | Public domain | 1–2 B | Background prose |
| OpenSubtitles (cleaned, English) | Mixed permissive | 1–2 B | Spoken-register dialogue |
| Stack Exchange dumps (Q&A format) | CC-BY-SA | 1–2 B | Helpful-but-not-sycophantic Q&A |
| Ubuntu Dialogue Corpus | CC | 75–100 M | Technical multi-turn |
| Common Pile v0.1 subsets (Wikipedia, openly-licensed books, ArXiv abstracts) | Openly licensed | 1–2 B | World knowledge |
| Hand-curated plays, interviews, oral histories (Internet Archive PD) | Public domain | 100–300 M | Stylistic diversity |

**Actual 1.0-preview mix (as built).** SQuAD was dropped after the prior 350M run collapsed into SQuAD Q&A templates — it was the only marker-bearing source in that run, so the model learned `<user> → factual question`. OPUS OpenSubtitles tokenized at 1.98 B tokens became the marker-format anchor instead. Gutenberg Dialogue, full Stack Exchange dumps, Ubuntu Dialogue, and curated plays/interviews/oral histories were not assembled in time for 1.0-preview; they are the v2.0 corpus work.

| Source | Tokens | `<user>/<reply>` markers? |
|---|---|---|
| OPUS OpenSubtitles | 1.98 B | yes |
| Common Pile v0.1 | 499 M | no |
| Hacker News | 2.6 M | yes |
| Gutenberg books (sample) | 12.5 M | no |
| SQuAD | — | dropped (poisoned prior run) |

Total ~2.5 B unique tokens, trained for 3 B steps → ~1.2 effective epochs. The "long-conversation consistency" claim died here: no scene-grouped or multi-turn corpus made it in.

**Hard exclusions** (do not pull from these, ever, for Glemton):
- Any GPT/Claude/Llama-generated synthetic data (Alpaca, ShareGPT, OpenHermes, UltraFeedback, OpenAssistant, Capybara, etc.)
- Pushshift Reddit (Reddit ToS restricts bulk LLM use)
- Common Crawl unfiltered web text (we want dialogue, not blog spam)

Dedup pipeline: MinHash-LSH at document level + exact-match line-level dedup. Decontaminate against eval sets.

## Training plan

| Phase | Planned | Actual / Output | Status |
|---|---|---|---|
| 0. Toolchain validation | 2–3 days | PyTorch nightly + Blackwell verified | ✅ done |
| 1. Data pipeline | 1–2 weeks | Tokenized shards for OPUS / Common Pile / HN / Gutenberg-sample / SQuAD on disk; SQuAD later dropped | ✅ done |
| 2. Tokenizer training | 1–2 days | 32k BPE trained on the dialogue corpus | ✅ done |
| 3. Scaffold validation | 3–5 days | 50M model on 100M tokens of the OPUS-dominant mix → no SQuAD collapse, casual register | ✅ done |
| 4. Full pretrain | 2–4 weeks | 365M model on 3 B tokens, 66 h on the 5070, one clean run, `final.pt` saved | ✅ done |
| 5. Eval harness | 1 week (parallel) | Sycophancy + long-conversation evals built and run on `final.pt`. Standard LM evals (MMLU etc.) not run — deliberately, see "Risks". | ✅ done (partial scope) |
| 6. Polish & release | 1 week | README, status docs, model card draft, eval reports committed. GGUF export and demo CLI pending. | 🟡 in progress |

**Realized calendar:** Phase 0 → 4 ran approximately Apr–May 2026. Full pretrain finished 2026-05-24. Pure GPU-burn time on the 5070 was ~66 h for the final run plus prior scaffold/poisoned runs.

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

| Risk | Likelihood | Mitigation | Outcome (post 1.0-preview) |
|---|---|---|---|
| Blackwell + PyTorch toolchain bugs eat a week of debugging | High | Phase 0 validation, fallback to CUDA 12.8 wheels not 13 | ✓ Avoided. Zero toolchain issues during the full 66 h run. |
| 7B tokens of *clean dialogue* hard to assemble | Medium | Loosen "dialogue" to include Q&A, interviews, etc. | ✗ Missed. Shipped ~2.5 B unique. v2.0 corpus expansion needed. |
| Without any instruction tuning, model continues input rather than answering | High | Bake `<user>/<reply>` turn markers into pretraining | ⚠ Partly. Empty-reply rate ~33% is the residual failure mode — model often emits nothing where a chatbot would emit something. |
| Mediocre eval results on standard LM benchmarks (MMLU etc.) | Very high | Expected — small dialogue model. Don't claim MMLU wins. Lead with the three angle-specific claims instead. | ✓ Adhered to. MMLU etc. deliberately not run. |
| Trademark / name conflict surfaces later | Low | 2026-05-20 prior-use sweep across HF, GitHub, web, AI startups, app stores; full USPTO check before any commercial use | ✓ No conflicts found pre-1.0-preview. USPTO check still pending before commercial use. |
| User burns out on a 3-month project | Real | Milestone-driven: each phase a shippable artifact | ✓ 1.0-preview shipped within the milestone cadence. |
| **SQuAD-only marker source poisons learned format** *(not on original list — discovered mid-project)* | Realized | Diagnosis: SQuAD was the only `<user>/<reply>` source in the prior 350M run. Dropped SQuAD; tokenized OPUS to become the marker anchor; validated on a 50M scaffold before relaunching the full 350M run. | ✓ Resolved before 1.0-preview. Lesson recorded for v2.0: every corpus contributing turn-markers must be checked for distributional capture. |
| **Two-line subtitle corpus can't teach long-context recall** *(predicted, confirmed)* | High | Documented as a known limitation pre-run; planned to address in corpus expansion | ✗ Materialized. Long-conv recall 0% at gap=5+. v2.0 must add Ubuntu Dialogue / scene-grouped OPUS / Stack Exchange threads. |

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

## Open questions for ninjahawk

- [x] **License: Apache-2.0** for both code and weights (decided 2026-05-21; documented in README).
- [x] **GitHub repo:** `github.com/ninjahawk/glemton` — live.
- [ ] **Domain registration** (`glemton.ai` / `.io` / `.com`) — still open. All three appeared available on 2026-05-20.
- [ ] **v2.0 vs reframe** — two paths discussed honestly with sober-ninjahawk on 2026-05-24:
  - (a) **Corpus expansion → real v1.0.** Add Ubuntu Dialogue, scene-grouped OPUS, Stack Exchange threads, DailyDialog, EmpatheticDialogues. Train to 10–15 B tokens (~7–12 days GPU). Honest assessment: even at 10 B tokens, this won't beat Phi-4-mini or Qwen3-4B on anything; the result would be a better model than what exists now but worse than what people can download for free.
  - (b) **Pivot framing.** Position the project as "the minimum-viable, fully reproducible from-scratch pretraining + auto-eval pipeline that runs unattended on a single 12 GB consumer GPU." Treat the existing checkpoint as a demonstration artifact. Write the engineering story (SQuAD-poisoning diagnosis, OPUS marker insight, prediction-vs-result on long-context, weekend-train infra) as the portfolio piece. Cost: ~a week of writing. Value: a story nobody else is telling.
  - No decision yet. Option (b) followed by (a) only if the writing reveals a clear research angle worth pursuing is the current Claude-side recommendation; final call is ninjahawk's.
- [ ] **USPTO trademark check** if a commercial release is pursued under the name "Glemton".
