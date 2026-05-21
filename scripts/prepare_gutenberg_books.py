"""Normalize raw Project Gutenberg book texts into dialogue-marked shards.

The book files at data/raw/gutenberg_books/book_NNN.txt are full novels;
they have Gutenberg headers/footers we need to strip, and contain dialogue
in quotation marks that we want to surface as `<user>` / `<reply>` turns.

Heuristic extraction: lines that start with `"` (or are inside paired
quotes that span lines) are taken as utterances. Surrounding narrative
becomes context blocks. We alternate `<user>` / `<reply>` per consecutive
utterance.

This isn't perfect dialogue extraction — that's what the full
`ricsinaruto/gutenberg-dialog` pipeline does — but it gives us a solid
chunk of usable training text out of the 15 books we have on disk.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "raw" / "gutenberg_books"
DST = ROOT / "data" / "processed" / "gutenberg_books"


HEADER_RE = re.compile(r"\*\*\* START OF (THIS|THE) PROJECT GUTENBERG.*?\*\*\*", re.IGNORECASE | re.DOTALL)
FOOTER_RE = re.compile(r"\*\*\* END OF (THIS|THE) PROJECT GUTENBERG", re.IGNORECASE)
UTTERANCE_RE = re.compile(r'["“]([^"”]+)["”]')


def strip_gutenberg_boilerplate(text: str) -> str:
    m = HEADER_RE.search(text)
    if m:
        text = text[m.end():]
    m = FOOTER_RE.search(text)
    if m:
        text = text[: m.start()]
    return text


def extract_dialogue_chunks(text: str) -> list[str]:
    paragraphs = re.split(r"\n\s*\n", text)
    chunks: list[str] = []
    turn_buf: list[str] = []
    turn_idx = 0
    for para in paragraphs:
        utts = UTTERANCE_RE.findall(para)
        for u in utts:
            u = u.strip()
            if len(u) < 4:
                continue
            speaker = "<user>" if turn_idx % 2 == 0 else "<reply>"
            turn_buf.append(f"{speaker} {u}")
            turn_idx += 1
            if len(turn_buf) >= 40:
                chunks.append("\n".join(turn_buf))
                turn_buf = []
                turn_idx = 0
        # Also keep some narrative-only paragraphs to preserve prose register
        if not utts and 200 < len(para) < 1500:
            chunks.append(para.strip())
    if turn_buf:
        chunks.append("\n".join(turn_buf))
    return chunks


def main() -> int:
    DST.mkdir(parents=True, exist_ok=True)
    all_chunks: list[str] = []
    for book in sorted(SRC.glob("book_*.txt")):
        raw = book.read_text(encoding="utf-8", errors="ignore")
        clean = strip_gutenberg_boilerplate(raw)
        chunks = extract_dialogue_chunks(clean)
        print(f"[gutenberg_books] {book.name}: {len(chunks)} chunks from {len(clean)//1024} KB clean")
        all_chunks.extend(chunks)
    # Write in shards of 5000 chunks each
    shard_size = 5000
    for idx in range(0, len(all_chunks), shard_size):
        out = DST / f"shard_{idx // shard_size:05d}.txt"
        out.write_text("\n\n".join(all_chunks[idx : idx + shard_size]), encoding="utf-8")
        print(f"  wrote {out} ({len(all_chunks[idx : idx + shard_size])} chunks)")
    print(f"[gutenberg_books] total {len(all_chunks)} chunks, ~{sum(len(c) for c in all_chunks)//1024} KB text")
    return 0


if __name__ == "__main__":
    sys.exit(main())
