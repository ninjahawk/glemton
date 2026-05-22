"""Quick qualitative sampling of a checkpoint - detect template collapse fast.

Usage:
    python scripts/sample_ckpt.py path/to/checkpoint.pt
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from glemton.generate import load_checkpoint, generate_text
from glemton.tokenizer import load as load_tokenizer

PROMPTS = [
    "<user> Hello, how are you?\n<reply>",
    "<user> What is your favorite book?\n<reply>",
    "<user> Tell me about a time you were sad.\n<reply>",
    "<user> Did you see the news today?\n<reply>",
    "<user> I had a rough day at work.\n<reply>",
    "The old man sat by the fire and remembered",
    "Elizabeth turned to her sister and said,",
]


def main():
    ckpt = sys.argv[1] if len(sys.argv) > 1 else "checkpoints/glemton-scaffold-validate-opus/final.pt"
    tok = load_tokenizer("data/tokenizer/glemton-bpe-32k.json")
    print(f"\n========== {ckpt} ==========")
    model, cfg = load_checkpoint(ckpt)
    for pr in PROMPTS:
        out = generate_text(model, tok, pr, max_new_tokens=80, temperature=0.8)
        print(f"\nPROMPT: {pr!r}")
        print(f"OUTPUT: {out.strip()[:400]}")


if __name__ == "__main__":
    main()
