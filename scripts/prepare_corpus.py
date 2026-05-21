"""Turn raw downloaded sources into normalized text shards under data/processed/.

For each source:
- extract any archives
- normalize line endings, drop obvious junk
- format Q&A and chat into <user>/<reply> turn structure
- write `.txt` shards (one document per blank-line-separated paragraph block)

The tokenizer (`scripts/train_tokenizer.py`) and the packed-shard builder
(`scripts/pack_shards.py`) consume the output of this stage.
"""

from __future__ import annotations

import gzip
import os
import re
import sys
import tarfile
import zipfile
from html import unescape
from pathlib import Path
from typing import Iterator

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"


def _ensure(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p


def _strip_html(s: str) -> str:
    s = unescape(s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def _write_shards(dest: Path, docs: Iterator[str], docs_per_shard: int = 100_000) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    cur, idx = [], 0
    for d in docs:
        if d and d.strip():
            cur.append(d.strip())
        if len(cur) >= docs_per_shard:
            (dest / f"shard_{idx:05d}.txt").write_text(
                "\n\n".join(cur), encoding="utf-8"
            )
            print(f"  wrote shard {idx} ({len(cur)} docs)")
            cur.clear()
            idx += 1
    if cur:
        (dest / f"shard_{idx:05d}.txt").write_text("\n\n".join(cur), encoding="utf-8")
        print(f"  wrote final shard {idx} ({len(cur)} docs)")


def prepare_gutenberg_dialogue() -> None:
    src = RAW / "gutenberg_dialogue" / "source.tar.gz"
    if not src.exists():
        print(f"[gutenberg_dialogue] missing {src}; run download first")
        return
    dest = _ensure(OUT / "gutenberg_dialogue")
    tmpdir = RAW / "gutenberg_dialogue" / "_extracted"
    if not tmpdir.exists():
        print(f"[gutenberg_dialogue] extracting {src}")
        with tarfile.open(src) as tf:
            tf.extractall(tmpdir)

    def docs() -> Iterator[str]:
        for txt in tmpdir.rglob("*.txt"):
            try:
                content = txt.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            # Heuristic: dialogue files alternate lines as turns.
            lines = [ln.strip() for ln in content.splitlines() if ln.strip()]
            if not lines:
                continue
            chunks: list[str] = []
            buf: list[str] = []
            for i, ln in enumerate(lines):
                speaker = "<user>" if i % 2 == 0 else "<reply>"
                buf.append(f"{speaker} {ln}")
                if len(buf) >= 32:
                    chunks.append("\n".join(buf))
                    buf = []
            if buf:
                chunks.append("\n".join(buf))
            for c in chunks:
                yield c

    _write_shards(dest, docs(), docs_per_shard=50_000)


def prepare_stack_exchange() -> None:
    """Q&A from SE dumps becomes single-turn dialogue: <user> Q\n<reply> A."""
    src_dir = RAW / "stack_exchange"
    if not src_dir.exists():
        print(f"[stack_exchange] no archives in {src_dir}")
        return
    dest = _ensure(OUT / "stack_exchange")

    # SE dumps are 7z. Without a 7z extractor available cross-platform in Python,
    # we document this step. The user / wake-up script can run a one-time 7z extract.
    archives = list(src_dir.glob("*.7z"))
    print(f"[stack_exchange] {len(archives)} .7z archives present.")
    print("[stack_exchange] NOTE: 7z extraction requires `py7zr` (pip install py7zr) or system 7z.")
    print("[stack_exchange]   After extraction, point this function at Posts.xml + parse with bs4.")
    print("[stack_exchange]   Implementation deferred until py7zr is installed; safe to defer overnight.")


def prepare_open_subtitles() -> None:
    src_dir = RAW / "open_subtitles"
    if not src_dir.exists():
        print(f"[open_subtitles] no shards in {src_dir}")
        return
    dest = _ensure(OUT / "open_subtitles")

    def docs() -> Iterator[str]:
        for shard in sorted(src_dir.glob("shard_*.txt")):
            content = shard.read_text(encoding="utf-8", errors="ignore")
            lines = [ln.strip() for ln in content.splitlines() if ln.strip()]
            buf: list[str] = []
            for i, ln in enumerate(lines):
                speaker = "<user>" if i % 2 == 0 else "<reply>"
                buf.append(f"{speaker} {ln}")
                if len(buf) >= 24:
                    yield "\n".join(buf)
                    buf = []
            if buf:
                yield "\n".join(buf)

    _write_shards(dest, docs(), docs_per_shard=100_000)


def prepare_common_pile() -> None:
    src_dir = RAW / "common_pile"
    if not src_dir.exists():
        print(f"[common_pile] no shards in {src_dir}")
        return
    dest = _ensure(OUT / "common_pile")

    def docs() -> Iterator[str]:
        for shard in sorted(src_dir.glob("shard_*.txt")):
            content = shard.read_text(encoding="utf-8", errors="ignore")
            for d in content.split("\n\n"):
                if 200 < len(d) < 50_000:
                    yield d.strip()

    _write_shards(dest, docs(), docs_per_shard=10_000)


STAGES = {
    "gutenberg_dialogue": prepare_gutenberg_dialogue,
    "stack_exchange": prepare_stack_exchange,
    "open_subtitles": prepare_open_subtitles,
    "common_pile": prepare_common_pile,
}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python scripts/prepare_corpus.py <stage|all>")
        print("stages:", ", ".join(STAGES))
        return 2
    target = argv[1]
    if target == "all":
        for name, fn in STAGES.items():
            print(f"\n=== {name} ===")
            try:
                fn()
            except Exception as e:
                print(f"[{name}] failed: {e}")
        return 0
    if target not in STAGES:
        print(f"unknown stage: {target}")
        return 2
    STAGES[target]()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
