"""Train the 32k BPE tokenizer on the processed dialogue corpus.

Pulls all `.txt` shards under data/processed/ as the training input,
writes the resulting tokenizer JSON to data/tokenizer/glemton-bpe-32k.json.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str]) -> int:
    sys.path.insert(0, str(ROOT / "src"))
    from glemton.tokenizer import train_from_files

    vocab_size = 32000
    if len(argv) >= 2:
        vocab_size = int(argv[1])

    files = sorted(str(p) for p in (ROOT / "data" / "processed").rglob("*.txt"))
    if not files:
        print("[train_tokenizer] no training files under data/processed/; run prepare_corpus.py first")
        return 1
    print(f"[train_tokenizer] training on {len(files)} files, vocab_size={vocab_size}")
    out_path = ROOT / "data" / "tokenizer" / "glemton-bpe-32k.json"
    train_from_files(files, str(out_path), vocab_size=vocab_size)
    print(f"[train_tokenizer] wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
