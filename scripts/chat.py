"""Interactive chat REPL against a Glemton checkpoint.

Tracks the full conversation, building up the `<user>:/<reply>:` history
each turn so the model sees the running dialogue.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from glemton.generate import load_checkpoint, generate_text
from glemton.tokenizer import load as load_tokenizer


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ckpt", default="checkpoints/glemton-debug-10m/final.pt")
    p.add_argument("--tokenizer", default="data/tokenizer/glemton-bpe-32k.json")
    p.add_argument("--max-new-tokens", type=int, default=128)
    p.add_argument("--temperature", type=float, default=0.8)
    args = p.parse_args()

    print(f"loading model from {args.ckpt}")
    model, cfg = load_checkpoint(args.ckpt)
    tok = load_tokenizer(args.tokenizer)
    print(f"loaded {model.num_parameters()/1e6:.1f}M params on {next(model.parameters()).device}")
    print("type your message and press enter. ctrl-c to quit.\n")

    history: list[str] = []
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            continue
        history.append(f"<user> {line}")
        history.append("<reply>")
        prompt = "\n".join(history)
        out = generate_text(
            model, tok, prompt,
            max_new_tokens=args.max_new_tokens,
            temperature=args.temperature,
        )
        # Strip anything past the next user turn the model may have hallucinated.
        next_user = out.find("<user>")
        reply = out[:next_user] if next_user > 0 else out
        reply = reply.strip()
        print(reply)
        history[-1] = f"<reply> {reply}"


if __name__ == "__main__":
    main()
