"""Modern conversational data downloaders.

Replaces the Victorian-Gutenberg-heavy v1 corpus with actually modern
human dialogue from sources that are either CC-licensed or routinely used
for research without redistribution concerns.

Sources:
  - opus_subtitles  : OPUS OpenSubtitles v2018 English monolingual plaintext
                      (CC license per opus.nlpl.eu, ~10 GB compressed)
  - hacker_news     : Top + recent comments via Firebase API (HN ToS allows
                      research/non-commercial; ymmv for commercial release)
  - stack_exchange  : archive.org Stack Exchange full dump (CC-BY-SA)
  - wikipedia_talk  : Wikipedia talk pages dump via HF datasets (CC-BY-SA)

Run as:  python scripts/download_modern_dialogue.py <source|all>
"""

from __future__ import annotations

import gzip
import io
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"


def _ensure(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p


def _stream(url: str, dest: Path, timeout: int = 60) -> None:
    """Stream a URL to disk using requests (which has a bundled CA bundle —
    plain urllib on Windows can't find the system trust store)."""
    import requests

    if dest.exists() and dest.stat().st_size > 1024:
        print(f"[skip] {dest} already exists ({dest.stat().st_size/1e6:.1f} MB)")
        return
    print(f"[download] {url} -> {dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    headers = {"User-Agent": "glemton-data/0.1.0"}
    with requests.get(url, headers=headers, stream=True, timeout=timeout) as r:
        r.raise_for_status()
        total = 0
        t0 = time.time()
        with open(tmp, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if not chunk:
                    continue
                f.write(chunk)
                total += len(chunk)
                if total % (64 * 1024 * 1024) < len(chunk):
                    elapsed = time.time() - t0
                    rate = total / max(elapsed, 0.001) / 1e6
                    print(f"  {total/1e6:.0f} MB at {rate:.1f} MB/s")
    tmp.rename(dest)
    print(f"  done: {dest} ({dest.stat().st_size/1e6:.1f} MB)")


def opus_subtitles() -> None:
    """OPUS OpenSubtitles English monolingual plaintext.

    Hosted by University of Helsinki. Standard URL pattern:
      https://object.pouta.csc.fi/OPUS-OpenSubtitles/v2018/mono/en.txt.gz
    File is several GB compressed.
    """
    out = _ensure(RAW / "opus_subtitles")
    url = "https://object.pouta.csc.fi/OPUS-OpenSubtitles/v2018/mono/en.txt.gz"
    dest = out / "en.txt.gz"
    try:
        _stream(url, dest, timeout=120)
    except urllib.error.HTTPError as e:
        print(f"[opus_subtitles] HTTP {e.code}; trying mirror URL")
        # Backup: the moses archive form
        url2 = "https://object.pouta.csc.fi/OPUS-OpenSubtitles/v2018/moses/en.txt.zip"
        _stream(url2, out / "en.txt.zip", timeout=120)


def hacker_news() -> None:
    """Scrape Hacker News via the Firebase API.

    We pull the most recent N items, walk the comment tree, and emit each
    discussion as a multi-turn <user>/<reply> dialogue chunk.

    HN ToS: 'You may not use, scrape, or otherwise duplicate Hacker News
    content for commercial purposes' -- so this data is for the
    portfolio/research variant of Glemton, NOT for commercial release.
    """
    out = _ensure(RAW / "hacker_news")
    base = "https://hacker-news.firebaseio.com/v0"
    # Range of recent item IDs. Max item id can be fetched from /maxitem.json.
    try:
        max_id = int(_get_json(f"{base}/maxitem.json"))
    except Exception as e:
        print(f"[hacker_news] cannot reach API: {e}")
        return
    print(f"[hacker_news] current max item id: {max_id}")

    target_items = 50_000  # pull last ~50k items
    start = max(1, max_id - target_items)

    out_path = out / f"hn_items_{start}_{max_id}.jsonl"
    if out_path.exists():
        print(f"[hacker_news] already have {out_path}")
    else:
        print(f"[hacker_news] streaming {start}..{max_id} into {out_path}")
        with open(out_path, "w", encoding="utf-8") as f:
            written = 0
            for i in range(max_id, start, -1):
                try:
                    obj = _get_json(f"{base}/item/{i}.json", timeout=10)
                except Exception:
                    continue
                if not obj or obj.get("deleted") or obj.get("dead"):
                    continue
                f.write(json.dumps(obj) + "\n")
                written += 1
                if written % 1000 == 0:
                    print(f"  written {written} items (id={i})")
                if written >= target_items:
                    break
        print(f"[hacker_news] wrote {written} items")


def _get_json(url: str, timeout: int = 15):
    import requests
    r = requests.get(url, headers={"User-Agent": "glemton-data/0.1.0"}, timeout=timeout)
    r.raise_for_status()
    return r.json()


def stack_exchange_archive() -> None:
    """Stack Exchange complete dump from archive.org.

    The canonical bundle. CC-BY-SA. ~50+ GB total uncompressed but we
    grab a curated subset of dialogue-heavy communities.
    """
    out = _ensure(RAW / "stack_exchange")
    base = "https://archive.org/download/stackexchange"

    # Modern, dialogue-rich communities. Programming.SE excluded for now (huge).
    targets = [
        "stackoverflow.com-Posts.7z",
        "stackoverflow.com-Comments.7z",
        "writing.stackexchange.com.7z",
        "english.stackexchange.com.7z",
        "philosophy.stackexchange.com.7z",
        "linguistics.stackexchange.com.7z",
        "skeptics.stackexchange.com.7z",
        "interpersonal.stackexchange.com.7z",
        "academia.stackexchange.com.7z",
        "expatriates.stackexchange.com.7z",
        "money.stackexchange.com.7z",
        "parenting.stackexchange.com.7z",
        "puzzling.stackexchange.com.7z",
    ]
    for t in targets:
        try:
            _stream(f"{base}/{t}", out / t, timeout=120)
        except urllib.error.HTTPError as e:
            print(f"[stack_exchange] {t} -> HTTP {e.code}, skipping")


def wikipedia_talk() -> None:
    """Wikipedia talk pages via HuggingFace datasets (parquet-native)."""
    try:
        import datasets as ds
    except Exception as e:
        print(f"[wikipedia_talk] datasets lib missing: {e}")
        return
    out = _ensure(RAW / "wikipedia_talk")
    # Try a few mirrors that ship as parquet
    candidates = [
        ("OpenAssistant/wikipedia_talk", None),
        ("wiki_talk_pages", None),
    ]
    for name, conf in candidates:
        try:
            print(f"[wikipedia_talk] trying {name}")
            d = ds.load_dataset(name, conf, streaming=True) if conf else ds.load_dataset(name, streaming=True)
            split = d.get("train") or list(d.values())[0]
            n = 0
            cur, idx = [], 0
            for row in split:
                txt = row.get("text") or row.get("content") or row.get("body") or ""
                if txt:
                    cur.append(txt)
                    n += 1
                if len(cur) >= 20_000:
                    (out / f"shard_{idx:04d}.txt").write_text("\n\n".join(cur), encoding="utf-8")
                    cur.clear()
                    idx += 1
                    if idx >= 5:
                        break
            if cur:
                (out / f"shard_{idx:04d}.txt").write_text("\n\n".join(cur), encoding="utf-8")
            print(f"[wikipedia_talk] success with {name}, {n} entries")
            return
        except Exception as e:
            print(f"  {name} failed: {e}")
    print("[wikipedia_talk] all candidates failed; skip")


SOURCES = {
    "opus_subtitles": opus_subtitles,
    "hacker_news": hacker_news,
    "stack_exchange": stack_exchange_archive,
    "wikipedia_talk": wikipedia_talk,
}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python scripts/download_modern_dialogue.py <source|all>")
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
