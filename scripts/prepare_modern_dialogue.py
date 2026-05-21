"""Normalize the modern-dialogue raw downloads into processed shards.

Inputs (data/raw/...):
  opus_subtitles/en.txt.gz     — OPUS OpenSubtitles English mono plaintext
  hacker_news/hn_items_*.jsonl — Hacker News items pulled via API
  stack_exchange/*.7z          — already on disk (philosophy + skeptics)

Outputs (data/processed/...):
  opus_subtitles/shard_*.txt   — pseudo-dialogue chunks
  hacker_news/shard_*.txt      — comment threads as <user>/<reply>

Run as:  python scripts/prepare_modern_dialogue.py <stage|all>
"""

from __future__ import annotations

import gzip
import json
import re
import sys
from collections import defaultdict
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
    s = unescape(s or "")
    s = re.sub(r"<p>", "\n\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def _write_shards(dest: Path, docs: Iterator[str], docs_per_shard: int = 50_000) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    cur, idx = [], 0
    for d in docs:
        if d and d.strip():
            cur.append(d.strip())
        if len(cur) >= docs_per_shard:
            (dest / f"shard_{idx:05d}.txt").write_text("\n\n".join(cur), encoding="utf-8")
            print(f"  wrote shard {idx} ({len(cur)} docs)")
            cur.clear()
            idx += 1
    if cur:
        (dest / f"shard_{idx:05d}.txt").write_text("\n\n".join(cur), encoding="utf-8")
        print(f"  wrote final shard {idx} ({len(cur)} docs)")


def prepare_opus_subtitles() -> None:
    """OPUS mono English: each line is one subtitle utterance.

    We don't have proper turn ordering (it's a mono dump), so we chunk
    consecutive lines into pseudo-dialogue blocks alternating <user>/<reply>.
    The register transfers even if true turn-taking doesn't.
    """
    # Accept either the complete .gz or a recovered plaintext .partial.
    src_gz = RAW / "opus_subtitles" / "en.txt.gz"
    src_partial = RAW / "opus_subtitles" / "en.txt.partial"
    src = src_gz if src_gz.exists() else src_partial
    if not src.exists():
        print(f"[opus_subtitles] missing OPUS source (looked for {src_gz} and {src_partial})")
        return
    print(f"[opus_subtitles] using {src}")
    dest = _ensure(OUT / "opus_subtitles")

    def open_src():
        if str(src).endswith(".gz"):
            return gzip.open(src, "rt", encoding="utf-8", errors="ignore")
        return open(src, "r", encoding="utf-8", errors="ignore")

    def docs() -> Iterator[str]:
        buf: list[str] = []
        turn = 0
        with open_src() as f:
            for line in f:
                line = line.strip()
                if not line or len(line) < 3:
                    continue
                speaker = "<user>" if turn % 2 == 0 else "<reply>"
                buf.append(f"{speaker} {line}")
                turn += 1
                if len(buf) >= 12:  # ~6-turn dialogue chunks
                    yield "\n".join(buf)
                    buf = []
                    turn = 0
        if buf:
            yield "\n".join(buf)

    _write_shards(dest, docs(), docs_per_shard=100_000)


def prepare_hacker_news() -> None:
    """Hacker News: reconstruct comment threads from the flat item dump.

    Each item has 'kids' (child comment ids). We build the tree by parent,
    then walk each thread depth-first, emitting <user>/<reply> chunks.
    """
    src_dir = RAW / "hacker_news"
    items_files = sorted(src_dir.glob("hn_items_*.jsonl"))
    if not items_files:
        print(f"[hacker_news] no items files in {src_dir}")
        return
    dest = _ensure(OUT / "hacker_news")

    # Load all items into a dict.
    items: dict[int, dict] = {}
    for f in items_files:
        with open(f, "r", encoding="utf-8") as fh:
            for ln in fh:
                try:
                    obj = json.loads(ln)
                except Exception:
                    continue
                if "id" in obj:
                    items[obj["id"]] = obj
    print(f"[hacker_news] loaded {len(items)} items")

    # Walk subtree from any item id. Returns list of (depth, text) pairs.
    visited: set[int] = set()

    def walk(node_id: int, depth: int = 0) -> list[tuple[int, str]]:
        out: list[tuple[int, str]] = []
        if node_id in visited:
            return out
        visited.add(node_id)
        n = items.get(node_id)
        if not n:
            return out
        text = n.get("text") or n.get("title")
        if text:
            out.append((depth, _strip_html(text)))
        for kid in n.get("kids", []) or []:
            out.extend(walk(kid, depth + 1))
        return out

    def docs() -> Iterator[str]:
        # First: stories with their entire comment trees.
        for sid, st in items.items():
            if st.get("type") != "story":
                continue
            thread = walk(sid)
            if len(thread) < 2:
                continue
            chunks: list[str] = []
            for i, (_, text) in enumerate(thread):
                speaker = "<user>" if i % 2 == 0 else "<reply>"
                chunks.append(f"{speaker} {text}")
            if chunks:
                yield "\n".join(chunks)

        # Then: any subtree we haven't visited yet (orphan threads where we
        # don't have the parent story but we do have a comment subtree).
        for cid, c in items.items():
            if cid in visited:
                continue
            if c.get("type") != "comment":
                continue
            thread = walk(cid)
            if len(thread) < 2:
                continue
            chunks: list[str] = []
            for i, (_, text) in enumerate(thread):
                speaker = "<user>" if i % 2 == 0 else "<reply>"
                chunks.append(f"{speaker} {text}")
            if chunks:
                yield "\n".join(chunks)

    _write_shards(dest, docs(), docs_per_shard=10_000)


STAGES = {
    "opus_subtitles": prepare_opus_subtitles,
    "hacker_news": prepare_hacker_news,
}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python scripts/prepare_modern_dialogue.py <stage|all>")
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
