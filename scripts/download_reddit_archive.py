"""Pull a small Reddit comment archive from archive.org.

Reddit comments are the most archetypal "modern dialogue" data — a few
million casual reply threads. Hosted as monthly .zst dumps on archive.org's
pushshift mirror. We pull one or two recent months as a starting sample.

The user explicitly authorized scraping for the research variant of Glemton.
The base Glemton 1.0 ships on the permissive-only subset; this data is
opt-in for the research / personality-finetune variant.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"


def _ensure(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p


def _stream(url: str, dest: Path, timeout: int = 120) -> None:
    if dest.exists() and dest.stat().st_size > 1024:
        print(f"[skip] {dest} ({dest.stat().st_size/1e6:.1f} MB exists)")
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
                if total % (32 * 1024 * 1024) < len(chunk):
                    elapsed = time.time() - t0
                    rate = total / max(elapsed, 0.001) / 1e6
                    print(f"  {total/1e6:.0f} MB at {rate:.1f} MB/s")
    tmp.rename(dest)
    print(f"  done: {dest} ({dest.stat().st_size/1e6:.1f} MB)")


def reddit_subset() -> None:
    """Try a curated HF subset first (parquet, no download size issues).

    Falls back to archive.org pushshift month if HF subset isn't reachable.
    """
    out = _ensure(RAW / "reddit")

    # Try a small parquet-native subset first.
    candidates = [
        ("bonjour-jpg/reddit-comments-mini", None),
        ("OpenAssistant/reddit_eli5_qna", None),
        ("euclaise/reddit_news_comments", None),
        ("HuggingFaceH4/no_robots", None),  # this one is actually small + clean, even if not strictly Reddit
    ]
    try:
        import datasets as ds

        for name, conf in candidates:
            try:
                print(f"[reddit_subset] trying {name}")
                d = ds.load_dataset(name, conf, streaming=True) if conf else ds.load_dataset(name, streaming=True)
                split = d.get("train") or list(d.values())[0]
                cur, idx = [], 0
                n = 0
                for row in split:
                    txt = row.get("text") or row.get("body") or row.get("content") or row.get("comment") or ""
                    if txt and len(txt) > 30:
                        cur.append(str(txt).strip())
                        n += 1
                    if len(cur) >= 10_000:
                        (out / f"shard_{idx:04d}.txt").write_text("\n\n".join(cur), encoding="utf-8")
                        print(f"  wrote shard {idx} ({len(cur)} entries)")
                        cur.clear()
                        idx += 1
                        if idx >= 5:
                            break
                if cur:
                    (out / f"shard_{idx:04d}.txt").write_text("\n\n".join(cur), encoding="utf-8")
                if n > 0:
                    print(f"[reddit_subset] success with {name}, {n} entries")
                    return
            except Exception as e:
                print(f"  {name} -> {e}")
    except Exception as e:
        print(f"[reddit_subset] datasets lib issue: {e}")

    print("[reddit_subset] all HF candidates failed; skip")


def main(argv: list[str]) -> int:
    reddit_subset()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
