"""Sample side-by-side from several checkpoints to compare quality drift."""
from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from glemton.generate import load_checkpoint, generate_text
from glemton.tokenizer import load as load_tokenizer

CKPTS = [
    "checkpoints/glemton-350m/step_15259_tokens_250M.pt",
    "checkpoints/glemton-350m/step_18311_tokens_300M.pt",
    "checkpoints/glemton-350m/step_21363_tokens_350M.pt",
    "checkpoints/glemton-350m/step_24415_tokens_400M.pt",
]
PROMPTS = [
    "<user> Hello, how are you?\n<reply>",
    "<user> What is your favorite book?\n<reply>",
    "<user> Tell me about a time you were sad.\n<reply>",
    "The old man sat by the fire and remembered",
    "Elizabeth turned to her sister and said,",
]

def main():
    tok = load_tokenizer("data/tokenizer/glemton-bpe-32k.json")
    for ck in CKPTS:
        print(f"\n========== {ck} ==========")
        model, cfg = load_checkpoint(ck)
        for pr in PROMPTS:
            out = generate_text(model, tok, pr, max_new_tokens=80, temperature=0.8)
            print(f"\nPROMPT: {pr!r}")
            print(f"OUTPUT: {out.strip()[:400]}")
        del model
        import torch; torch.cuda.empty_cache()

if __name__ == "__main__":
    main()
