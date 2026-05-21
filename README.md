# Glemton

A small open-weights language model that talks like a person.

Glemton is trained from scratch on natural human dialogue — books, plays, interviews, transcripts, Q&A threads. It has never seen synthetic assistant data, never been RLHF'd to be polite, never been told it's a helpful AI. It learned to converse by reading how humans actually converse.

## What's different

| | Typical small open LLM | Glemton |
|---|---|---|
| Pretraining corpus | Web text (FineWeb, RefinedWeb, C4) | Human dialogue corpora |
| Instruction tuning | SFT on GPT-distilled data (Alpaca, OpenHermes) | None |
| Tone | "Certainly! I'd be happy to help with that great question!" | Whatever the conversation calls for |
| Long conversations | Context window or compaction harness | Native 32k context, trained on long dialogues |
| Size | 1.5–7B common | 350M |
| Runs on | A GPU | Anything with a CPU |

## Status

Pre-release. v1.0 target: late 2026.

## License

Apache-2.0 (code + weights). Free for any use including commercial.

---

*Author: ninjahawk*
