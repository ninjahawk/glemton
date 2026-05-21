"""Run the 10M-param scaffold-validation training.

Wrapper around `glemton.train.train` that points at configs/debug-10m.yaml.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    sys.path.insert(0, str(ROOT / "src"))
    from glemton.train import train

    cfg = ROOT / "configs" / "debug-10m.yaml"
    train(str(cfg))
    return 0


if __name__ == "__main__":
    sys.exit(main())
