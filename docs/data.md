# Data plan

Glemton's corpus is the project. The architecture is borrowed; the data choices are what make it different.

## Principles

1. **Permissively licensed only.** Public domain, CC, Apache, or explicit open-data licenses. No "scraped because we could." If the user couldn't legally redistribute a derived model, the source is out.
2. **Dialogue-heavy.** Most open base models pretrain on web text and bolt conversational ability on with SFT. We invert that — the *pretraining* objective is conversation.
3. **No synthetic assistant data.** Hard rule. No Alpaca, ShareGPT, OpenHermes, UltraFeedback, OpenAssistant, Capybara — none of the GPT/Claude/Llama-distilled SFT corpora. Doing so would defeat the whole point of the project: those datasets are *exactly* where the "Great question! I'd be happy to help!" tone comes from.

## Target mix (~7 B tokens, Chinchilla-optimal for 350 M)

| Source | License | Approx tokens (target) | Role |
|---|---|---|---|
| Gutenberg Dialogue (extracted from public-domain novels) | Public domain | 200–300 M | Core dialogue |
| Project Gutenberg full books (around the dialogue) | Public domain | 1–2 B | Background prose |
| OpenSubtitles (cleaned English) | CC / mixed permissive | 1–2 B | Spoken-register |
| Stack Exchange dumps | CC-BY-SA | 1–2 B | Helpful-but-not-sycophantic Q&A |
| Ubuntu Dialogue Corpus | CC | 75–100 M | Technical multi-turn |
| Common Pile v0.1 subsets (Wikipedia, openly-licensed books, ArXiv abstracts) | Openly licensed | 1–2 B | World knowledge |
| Hand-curated plays, interviews, oral histories (Internet Archive PD) | Public domain | 100–300 M | Stylistic diversity |
| DailyDialog | CC | a few M | Small clean dialogue sanity-check |

## Hard exclusions

| Source | Why excluded |
|---|---|
| Alpaca / ShareGPT / OpenHermes / UltraFeedback / OpenAssistant / Capybara | Synthetic assistant data — the exact thing we're trying to escape |
| Pushshift Reddit | Reddit ToS restricts bulk LLM use |
| Common Crawl raw | Want dialogue, not blog-spam noise |
| Any GPT/Claude/Llama distillation | Re-introduces sycophancy via the back door |

## Pipeline

```
data/raw/<source>/...     ← downloaded archives, parquet shards, etc.
   ↓ scripts/prepare_corpus.py
data/processed/<source>/shard_NNNNN.txt   ← normalized text, blank-line doc separators,
                                            turn markers ((<user>/<reply>) where applicable
   ↓ scripts/train_tokenizer.py
data/tokenizer/glemton-bpe-32k.json       ← 32 k BPE trained on the whole corpus
   ↓ scripts/pack_shards.py
data/tokenized/<source>/shard_NNNNN.bin   ← uint16 packed token streams
   ↓ src/glemton/data.py (PackedDataset)
trainer mmap reads
```

All shard sizes are chosen so a single shard fits in RAM; the trainer mmaps for cheap random access.

## Dedup

MinHash-LSH at document level + exact-match line-level dedup before packing. Decontamination against eval probe sets (sycophancy probes + long-conversation probes) happens at the same stage.

## Honest status as of overnight scaffold

The download script (`scripts/download_data.py` and its v2 fallback) is in place. Two issues hit during overnight:

- **OpenSubtitles**: the `Helsinki-NLP/open_subtitles` Hub dataset uses a deprecated loader script and the `datasets` library no longer runs those. v2 tries community parquet mirrors. If they all fail, the user needs to source OpenSubtitles directly (the OPUS project hosts plain text).
- **Gutenberg Dialogue Dataset**: the GitHub repo at `ricsinaruto/gutenberg-dialog` provides the *extraction code*, not pre-extracted data. To get the actual dialogue corpus we either (a) run their extraction pipeline against a raw Gutenberg mirror, or (b) use the 15 hand-picked classic books that v2's `gutenberg_books` downloader pulls and extract dialogue from those.

The v1.0 budget assumes 7 B tokens; if open dialogue sources fall short, **expand the Common Pile share and the Project Gutenberg books share** rather than introduce any synthetic assistant data.
