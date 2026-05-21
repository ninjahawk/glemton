"""Download the Glemton corpus.

Each function pulls one source, writes raw text shards into data/raw/<source>/.
All sources are permissively licensed. See docs/data.md for the canonical
license + source table.

Run as:
    python scripts/download_data.py <source>
    python scripts/download_data.py all
"""

from __future__ import annotations

import gzip
import io
import os
import sys
import tarfile
import time
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"


def _ensure(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p


def _stream_to_disk(url: str, dest: Path) -> None:
    print(f"[download] {url} -> {dest}")
    if dest.exists():
        print(f"  skip (exists, {dest.stat().st_size/1e6:.1f} MB)")
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    req = urllib.request.Request(url, headers={"User-Agent": "glemton-data/0.0.1"})
    with urllib.request.urlopen(req) as r, open(tmp, "wb") as f:
        total = 0
        t0 = time.time()
        while True:
            chunk = r.read(1024 * 1024)
            if not chunk:
                break
            f.write(chunk)
            total += len(chunk)
            if total % (32 * 1024 * 1024) < len(chunk):
                elapsed = time.time() - t0
                print(f"  {total/1e6:.1f} MB at {total/elapsed/1e6:.2f} MB/s")
    tmp.rename(dest)


def gutenberg_dialogue() -> None:
    """Gutenberg Dialogue Dataset — public-domain extracted dialogue from novels.

    Source: https://github.com/ricsinaruto/gutenberg-dialog (arXiv 2004.12752)
    """
    out = _ensure(DATA_RAW / "gutenberg_dialogue")
    url = "https://github.com/ricsinaruto/gutenberg-dialog/archive/refs/heads/master.tar.gz"
    archive = out / "source.tar.gz"
    _stream_to_disk(url, archive)
    print(f"[gutenberg_dialogue] archive at {archive}; extraction pipeline lives in scripts/prepare_corpus.py")


def ubuntu_dialogue() -> None:
    """Ubuntu Dialogue Corpus — Creative Commons, technical multi-turn chat logs.

    Hosted on HuggingFace datasets; we use the `datasets` library to pull it.
    """
    import datasets as ds

    out = _ensure(DATA_RAW / "ubuntu_dialogue")
    print("[ubuntu_dialogue] loading via HuggingFace datasets")
    d = ds.load_dataset("ubuntu_dialogs_corpus", "train", cache_dir=str(out))
    print(f"  loaded {len(d['train'])} rows")


def common_pile_subsets() -> None:
    """Common Pile v0.1 — 8TB openly licensed text. We pull a few subsets.

    We deliberately do not pull all 8TB. The relevant subsets for Glemton are
    Wikipedia and openly-licensed books (background prose) and ArXiv abstracts
    (for some technical vocabulary). Documented in docs/data.md.
    """
    import datasets as ds

    out = _ensure(DATA_RAW / "common_pile")
    print("[common_pile] streaming the wikimedia subset")
    # Common Pile is large — we stream the wiki subset and write text shards as we go.
    try:
        d = ds.load_dataset(
            "common-pile/comma_v0.1_training_dataset",
            split="train",
            streaming=True,
        )
    except Exception as e:
        print(f"[common_pile] dataset name may have changed: {e}")
        print("  see https://huggingface.co/papers/2506.05209 — update this loader if needed")
        return
    n_written = 0
    cur_shard_lines: list[str] = []
    cur_shard_idx = 0
    target_lines_per_shard = 100_000
    for ex in d:
        text = ex.get("text") or ex.get("content") or ""
        if text:
            cur_shard_lines.append(text)
            n_written += 1
        if len(cur_shard_lines) >= target_lines_per_shard:
            path = out / f"shard_{cur_shard_idx:05d}.txt"
            path.write_text("\n\n".join(cur_shard_lines), encoding="utf-8")
            print(f"  wrote {path} ({len(cur_shard_lines)} docs)")
            cur_shard_lines.clear()
            cur_shard_idx += 1
            if cur_shard_idx >= 50:  # cap at ~5M docs for v0.1
                break
    if cur_shard_lines:
        (out / f"shard_{cur_shard_idx:05d}.txt").write_text(
            "\n\n".join(cur_shard_lines), encoding="utf-8"
        )
    print(f"[common_pile] total docs written: {n_written}")


def stack_exchange() -> None:
    """Stack Exchange data dump — CC-BY-SA Q&A dialogue format.

    We focus on smaller communities first (skeptics, philosophy, writing,
    cooking) to keep download manageable; programming.SE is huge.
    """
    out = _ensure(DATA_RAW / "stack_exchange")
    base = "https://archive.org/download/stackexchange"
    targets = [
        "skeptics.stackexchange.com.7z",
        "philosophy.stackexchange.com.7z",
        "writing.stackexchange.com.7z",
        "cooking.stackexchange.com.7z",
        "english.stackexchange.com.7z",
        "linguistics.stackexchange.com.7z",
        "anime.stackexchange.com.7z",
    ]
    for t in targets:
        _stream_to_disk(f"{base}/{t}", out / t)


def open_subtitles() -> None:
    """OpenSubtitles via HuggingFace datasets — spoken-register dialogue.

    Hub path: Helsinki-NLP/open_subtitles
    """
    import datasets as ds

    out = _ensure(DATA_RAW / "open_subtitles")
    print("[open_subtitles] streaming english subset via HuggingFace datasets")
    try:
        d = ds.load_dataset("Helsinki-NLP/open_subtitles", lang1="en", lang2="en", split="train", streaming=True)
    except Exception as e:
        print(f"[open_subtitles] could not load: {e}")
        print("  try lang1/lang2 with different pair; see https://huggingface.co/datasets/Helsinki-NLP/open_subtitles")
        return
    cur, idx = [], 0
    for ex in d:
        # Each row is a translation pair; for English mono we just want one side.
        line = ex.get("translation", {}).get("en") or ex.get("en") or ""
        if line:
            cur.append(line)
        if len(cur) >= 200_000:
            (out / f"shard_{idx:05d}.txt").write_text("\n".join(cur), encoding="utf-8")
            print(f"  wrote shard {idx} ({len(cur)} lines)")
            cur.clear()
            idx += 1
            if idx >= 20:
                break
    if cur:
        (out / f"shard_{idx:05d}.txt").write_text("\n".join(cur), encoding="utf-8")


SOURCES = {
    "gutenberg_dialogue": gutenberg_dialogue,
    "ubuntu_dialogue": ubuntu_dialogue,
    "common_pile": common_pile_subsets,
    "stack_exchange": stack_exchange,
    "open_subtitles": open_subtitles,
}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python scripts/download_data.py <source|all>")
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
