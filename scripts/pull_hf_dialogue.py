"""Pull a few HuggingFace dialogue datasets that ship as native parquet
(no Python loader script, so they survive the datasets-4.x deprecation).

These are picked to be clean human dialogue, not synthetic assistant data:
- li2017dailydialog/daily_dialog — the canonical DailyDialog
- ConvAI2 conversations (community parquet)
- Wizard-of-Wikipedia conversations
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"


def _ensure(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p


def daily_dialog_parquet() -> int:
    import datasets as ds

    out = _ensure(RAW / "daily_dialog")
    # Community-maintained parquet mirror.
    for candidate in (
        "li2017dailydialog/daily_dialog",
        "roskoN/dailydialog",
        "VietAI/dailydialog-vi-text-only",  # has English text too
    ):
        try:
            print(f"[daily_dialog] trying {candidate}")
            d = ds.load_dataset(candidate, trust_remote_code=False, cache_dir=str(out))
            split = d.get("train") or list(d.values())[0]
            print(f"  loaded {len(split)} rows from {candidate}")
            lines: list[str] = []
            for row in split:
                turns = row.get("dialog") or row.get("dialogue") or row.get("text") or []
                if isinstance(turns, str):
                    lines.append(turns)
                    continue
                block = []
                for i, t in enumerate(turns):
                    speaker = "<user>" if i % 2 == 0 else "<reply>"
                    block.append(f"{speaker} {t.strip() if hasattr(t, 'strip') else t}")
                if block:
                    lines.append("\n".join(block))
            (out / "daily_dialog_train.txt").write_text("\n\n".join(lines), encoding="utf-8")
            print(f"  wrote {len(lines)} dialogues to disk")
            return 0
        except Exception as e:
            print(f"  {candidate}: {e}")
    print("[daily_dialog] all candidates failed")
    return 1


def empathetic_dialogues() -> int:
    import datasets as ds

    out = _ensure(RAW / "empathetic_dialogues")
    try:
        d = ds.load_dataset("facebook/empathetic_dialogues", cache_dir=str(out))
        print(f"[empathetic_dialogues] loaded splits: {list(d.keys())}")
        # Group by conv_id and serialize per-conv as <user>/<reply>
        from collections import defaultdict
        convs = defaultdict(list)
        for row in d.get("train", []):
            convs[row["conv_id"]].append(row)
        lines: list[str] = []
        for cid, rows in convs.items():
            rows.sort(key=lambda r: r["utterance_idx"])
            block = []
            for i, r in enumerate(rows):
                spk = "<user>" if i % 2 == 0 else "<reply>"
                block.append(f"{spk} {r['utterance']}")
            lines.append("\n".join(block))
        (out / "empathetic_dialogues_train.txt").write_text("\n\n".join(lines), encoding="utf-8")
        print(f"  wrote {len(lines)} conversations")
        return 0
    except Exception as e:
        print(f"[empathetic_dialogues] failed: {e}")
        return 1


def squad_qa() -> int:
    """SQuAD as Q-then-A dialogue pairs. Big and clean, CC-BY-SA."""
    import datasets as ds

    out = _ensure(RAW / "squad")
    try:
        d = ds.load_dataset("rajpurkar/squad", cache_dir=str(out))
        rows = d.get("train", [])
        print(f"[squad] {len(rows)} QA pairs")
        lines: list[str] = []
        for row in rows:
            q = row["question"].strip()
            ans = row["answers"]["text"][0] if row["answers"]["text"] else ""
            ctx = row.get("context", "")
            lines.append(
                f"<user> Here's some context:\n{ctx}\n\n{q}\n<reply> {ans}"
            )
        # write in shards of 50k pairs
        shard_size = 50_000
        for i in range(0, len(lines), shard_size):
            (out / f"squad_train_{i//shard_size:03d}.txt").write_text(
                "\n\n".join(lines[i : i + shard_size]), encoding="utf-8"
            )
            print(f"  wrote shard {i//shard_size}")
        return 0
    except Exception as e:
        print(f"[squad] failed: {e}")
        return 1


SOURCES = {
    "daily_dialog": daily_dialog_parquet,
    "empathetic_dialogues": empathetic_dialogues,
    "squad": squad_qa,
}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python scripts/pull_hf_dialogue.py <source|all>")
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
    return SOURCES[target]()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
