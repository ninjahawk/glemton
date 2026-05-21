"""Fallback / alternative downloaders that route around HF dataset-script deprecation.

The v1 download_data.py uses some datasets that relied on Python loader scripts.
HuggingFace dropped support for those, so this v2 script pulls everything via
parquet files / direct URLs. Run after v1 has its failures.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"


def _ensure(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p


def daily_dialog() -> None:
    """DailyDialog — small but clean multi-turn human dialogue, manually labelled.

    Hub: `daily_dialog` (parquet-native).
    """
    import datasets as ds

    out = _ensure(DATA_RAW / "daily_dialog")
    d = ds.load_dataset("daily_dialog", trust_remote_code=False, cache_dir=str(out))
    print(f"[daily_dialog] splits: {list(d.keys())}, train rows: {len(d['train'])}")
    # Write a simple text dump.
    lines: list[str] = []
    for row in d["train"]:
        turns = row["dialog"]
        block = []
        for i, t in enumerate(turns):
            speaker = "<user>" if i % 2 == 0 else "<reply>"
            block.append(f"{speaker} {t.strip()}")
        lines.append("\n".join(block))
    (out / "daily_dialog_train.txt").write_text("\n\n".join(lines), encoding="utf-8")
    print(f"[daily_dialog] wrote {len(lines)} dialogues")


def wikiquote() -> None:
    """Wikiquote dump — quotes are mostly clean dialogue snippets.

    A small but high-quality bonus dialogue source.
    """
    import datasets as ds

    out = _ensure(DATA_RAW / "wikiquote")
    try:
        d = ds.load_dataset("nthngdy/oscar-mini", split="train", streaming=True)
        # placeholder — wikiquote canonical dump path varies; user can swap.
        cur, idx = [], 0
        for row in d:
            txt = row.get("text", "")
            if "—" in txt and 50 < len(txt) < 2000:
                cur.append(txt)
            if len(cur) >= 20_000:
                (out / f"shard_{idx:05d}.txt").write_text("\n\n".join(cur), encoding="utf-8")
                cur.clear()
                idx += 1
                if idx >= 5:
                    break
        if cur:
            (out / f"shard_{idx:05d}.txt").write_text("\n\n".join(cur), encoding="utf-8")
        print(f"[wikiquote] approximate dialogue-y snippets written")
    except Exception as e:
        print(f"[wikiquote] failed (non-critical, skip): {e}")


def gutenberg_books_raw() -> None:
    """Download a Gutenberg books mirror tarball for narrative + dialogue.

    The standalone `gutenberg-dialog` repo gives us extraction code only;
    we need the raw books to feed through it. Standard Gutenberg mirror is
    rsync-only for the canonical bulk dump, but Project Gutenberg also offers
    monthly catalogs and selected dumps via archive.org.

    For overnight, we pull a curated small set of public-domain books known
    to be dialogue-rich (Austen, Doyle, Dickens, Twain, Hawthorne, etc.).
    Bulk fetch is deferred to the user since rsync is the recommended path.
    """
    import urllib.request

    out = _ensure(DATA_RAW / "gutenberg_books")
    # Plain-text URLs from gutenberg.org (these IDs are stable, classic books).
    # Pride and Prejudice, Sherlock Holmes (Adv), Tale of Two Cities,
    # Huck Finn, Scarlet Letter, Heart of Darkness, Picture of Dorian Gray,
    # Frankenstein, Moby-Dick, War and Peace, Anna Karenina, Wuthering Heights,
    # Crime and Punishment, Dracula, Treasure Island.
    ids = [1342, 1661, 98, 76, 33, 219, 174, 84, 2701, 2600, 1399, 768, 2554, 345, 120]
    for i in ids:
        url = f"https://www.gutenberg.org/files/{i}/{i}-0.txt"
        dest = out / f"book_{i}.txt"
        if dest.exists():
            continue
        try:
            print(f"[gutenberg_books] {url}")
            req = urllib.request.Request(url, headers={"User-Agent": "glemton-data/0.0.1"})
            with urllib.request.urlopen(req, timeout=30) as r:
                dest.write_bytes(r.read())
            print(f"  -> {dest} ({dest.stat().st_size/1024:.1f} KB)")
        except Exception as e:
            print(f"  failed: {e}")
    print(f"[gutenberg_books] {len(list(out.glob('book_*.txt')))} books in {out}")


def opus_subtitles_parquet() -> None:
    """Open-Subtitles via a parquet-hosted community mirror.

    The original Helsinki-NLP/open_subtitles uses a deprecated dataset script.
    Several community mirrors expose the same data as parquet. We try a few.
    """
    import datasets as ds

    out = _ensure(DATA_RAW / "open_subtitles")
    candidates = [
        ("open_subtitles", None),  # fallback in case it ever works
        ("Helsinki-NLP/opus-100", "en-fi"),  # has English subtitle-like text
        ("sentence-transformers/parallel-sentences-opensubtitles", None),
    ]
    for name, conf in candidates:
        try:
            print(f"[opus_subtitles_parquet] trying {name} (conf={conf})")
            if conf:
                d = ds.load_dataset(name, conf, split="train", streaming=True)
            else:
                d = ds.load_dataset(name, split="train", streaming=True)
            cur, idx = [], 0
            for row in d:
                en = row.get("translation", {}).get("en") if "translation" in row else None
                if not en:
                    en = row.get("english") or row.get("text")
                if en:
                    cur.append(en.strip())
                if len(cur) >= 50_000:
                    (out / f"shard_{idx:05d}.txt").write_text("\n".join(cur), encoding="utf-8")
                    print(f"  wrote shard {idx}")
                    cur.clear()
                    idx += 1
                    if idx >= 10:
                        break
            if cur:
                (out / f"shard_{idx:05d}.txt").write_text("\n".join(cur), encoding="utf-8")
            print(f"[opus_subtitles_parquet] success with {name}, shards: {idx+1}")
            return
        except Exception as e:
            print(f"  {name} failed: {e}")
    print("[opus_subtitles_parquet] all candidates failed — leave for user to source manually")


SOURCES = {
    "daily_dialog": daily_dialog,
    "wikiquote": wikiquote,
    "gutenberg_books": gutenberg_books_raw,
    "opus_subtitles_parquet": opus_subtitles_parquet,
}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python scripts/download_data_v2.py <source|all>")
        print("sources:", ", ".join(SOURCES))
        return 2
    target = argv[1]
    if target == "all":
        for name, fn in SOURCES.items():
            print(f"\n=== {name} ===")
            try:
                fn()
            except Exception as e:
                print(f"[{name}] failed: {e}")
        return 0
    if target not in SOURCES:
        print(f"unknown source: {target}")
        return 2
    SOURCES[target]()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
