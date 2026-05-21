"""Run the long-conversation consistency probe against a Glemton checkpoint.

For each gap in {5, 10, 25, 50, 75}, builds N synthetic conversations with
a fact planted at turn 2 and recall queried at turn (2+gap). Reports recall
accuracy by gap.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from glemton.eval_long_conversation import (
    evaluate,
    grade_response,
    make_probe_suite,
    serialize_probe,
)
from glemton.generate import generate_text, load_checkpoint
from glemton.tokenizer import load as load_tokenizer


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--ckpt", default="checkpoints/glemton-debug-10m/final.pt")
    p.add_argument("--tokenizer", default="data/tokenizer/glemton-bpe-32k.json")
    p.add_argument("--out", default="logs/long_conversation_eval.json")
    p.add_argument("--max-new-tokens", type=int, default=40)
    p.add_argument("--temperature", type=float, default=0.7)
    p.add_argument("--seed", type=int, default=0)
    args = p.parse_args()

    print(f"loading model from {args.ckpt}")
    model, cfg = load_checkpoint(args.ckpt)
    tok = load_tokenizer(args.tokenizer)
    print(f"loaded {model.num_parameters()/1e6:.1f}M params; max_seq_len={model.cfg.max_seq_len}")

    probes = make_probe_suite(seed=args.seed)
    print(f"running {len(probes)} probes (gaps 5,10,25,50,75 x 3 each)")

    def gen_fn(ctx: str) -> str:
        # Append a <reply> turn marker so the model knows to respond.
        prompt = ctx + "\n<reply>"
        out = generate_text(
            model, tok, prompt,
            max_new_tokens=args.max_new_tokens,
            temperature=args.temperature,
        )
        n = out.find("<user>")
        return (out[:n] if n > 0 else out).strip()

    result = evaluate(gen_fn, probes)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(result, indent=2), encoding="utf-8")
    print("\nrecall accuracy by gap:")
    for gap, acc in result["summary_accuracy_by_gap"].items():
        print(f"  gap={gap:3d}: {acc*100:5.1f}% ({sum(1 for r in result['results'] if r['gap'] == gap and r['recalled'])}/{sum(1 for r in result['results'] if r['gap'] == gap)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
