"""Run the sycophancy probe against a Glemton checkpoint end-to-end.

Reads tests/probes/sycophancy_probes.txt, generates one response per prompt,
counts assistant-tone markers, writes a JSON report under logs/.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from glemton.generate import generate_text, load_checkpoint
from glemton.tokenizer import load as load_tokenizer
from glemton.eval_sycophancy import load_probes, score_responses


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--ckpt", default="checkpoints/glemton-debug-10m/final.pt")
    p.add_argument("--tokenizer", default="data/tokenizer/glemton-bpe-32k.json")
    p.add_argument("--probes", default="tests/probes/sycophancy_probes.txt")
    p.add_argument("--out", default="logs/sycophancy_eval.json")
    p.add_argument("--max-new-tokens", type=int, default=80)
    p.add_argument("--temperature", type=float, default=0.8)
    args = p.parse_args()

    print(f"loading model from {args.ckpt}")
    model, cfg = load_checkpoint(args.ckpt)
    tok = load_tokenizer(args.tokenizer)

    probes = load_probes(args.probes)
    print(f"running {len(probes)} probes")

    responses: list[str] = []
    for i, prompt in enumerate(probes):
        wrapped = f"<user> {prompt}\n<reply>"
        resp = generate_text(
            model, tok, wrapped,
            max_new_tokens=args.max_new_tokens,
            temperature=args.temperature,
        )
        next_user = resp.find("<user>")
        if next_user > 0:
            resp = resp[:next_user]
        resp = resp.strip()
        responses.append(resp)
        print(f"  [{i+1}/{len(probes)}] {prompt[:60]!r} -> {resp[:80]!r}")

    out = score_responses(probes, responses)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"\nresult: {out['total_markers']} markers across {out['responses']} responses "
          f"({out['markers_per_100']:.1f} per 100)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
