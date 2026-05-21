"""Tokenize processed text shards into packed `uint16` .bin files.

Reads data/processed/**/*.txt, tokenizes each doc with the trained BPE,
concatenates ids with <eos> as separator, writes uint16 arrays into
data/tokenized/<source>/shard_NNNNN.bin.

The trainer mmaps these directly.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str]) -> int:
    sys.path.insert(0, str(ROOT / "src"))
    from glemton.tokenizer import load

    tok_path = ROOT / "data" / "tokenizer" / "glemton-bpe-32k.json"
    if not tok_path.exists():
        print(f"[pack_shards] missing tokenizer at {tok_path}; train it first")
        return 1
    tok = load(str(tok_path))
    eos_id = tok.token_to_id("<eos>")
    if eos_id is None or eos_id > 65535:
        print("[pack_shards] vocab > 65535; uint16 packing not possible")
        return 1

    src_root = ROOT / "data" / "processed"
    dst_root = ROOT / "data" / "tokenized"
    if not src_root.exists():
        print(f"[pack_shards] no processed/ dir at {src_root}")
        return 1

    shards = sorted(src_root.rglob("*.txt"))
    print(f"[pack_shards] packing {len(shards)} input shards")
    for shard in shards:
        rel = shard.relative_to(src_root)
        dst = dst_root / rel.parent / shard.with_suffix(".bin").name
        if dst.exists():
            continue
        text = shard.read_text(encoding="utf-8", errors="ignore")
        # Encode docs (separated by blank lines) and join with <eos>.
        docs = [d for d in text.split("\n\n") if d.strip()]
        ids: list[int] = []
        for d in docs:
            enc = tok.encode(d).ids
            ids.extend(enc)
            ids.append(eos_id)
        arr = np.array(ids, dtype=np.uint16)
        dst.parent.mkdir(parents=True, exist_ok=True)
        arr.tofile(dst)
        print(f"  {shard} -> {dst} ({len(arr):,} tokens)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
