"""Generate STATUS.md from the training log - text only, no GPU.

Parses logs/glemton_350m_v1_preview.log for the latest training state,
lists checkpoints, estimates ETA, and flags crashes. Called periodically
by weekend_run.ps1 and committed to git so progress is visible on a phone.
"""
from __future__ import annotations

import re
import time
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "logs" / "glemton_350m_v1_preview.log"
CKPT_DIR = ROOT / "checkpoints" / "glemton-350m"
TARGET_TOKENS = 3_000_000_000
STATUS = ROOT / "STATUS.md"

STEP_RE = re.compile(
    r"\[train\] step=(\d+) tokens=([\d.]+)M loss=([\d.]+) lr=([\d.eE+-]+) tok/s=(\d+)"
)
CRASH_RE = re.compile(r"Traceback|RuntimeError|CUDA error|OOM|Killed|FAILED", re.I)


def _read_text_any(path: Path) -> str:
    """Decode a log file regardless of encoding.

    PowerShell's Tee-Object writes UTF-16 LE; a plain redirect may write
    UTF-8. Sniff the BOM (and fall back to a null-byte heuristic for
    BOM-less UTF-16) so STATUS.md parsing never silently sees zero steps.
    """
    raw = path.read_bytes()
    if raw.startswith(b"\xff\xfe"):
        return raw.decode("utf-16-le", errors="replace")
    if raw.startswith(b"\xfe\xff"):
        return raw.decode("utf-16-be", errors="replace")
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw.decode("utf-8-sig", errors="replace")
    if raw[:400].count(0) > 40:  # BOM-less UTF-16
        return raw.decode("utf-16-le", errors="replace")
    return raw.decode("utf-8", errors="replace")


def tail(path: Path, n: int) -> list[str]:
    if not path.exists():
        return []
    return _read_text_any(path).splitlines()[-n:]


def main() -> None:
    recent = tail(LOG, 400)
    steps = [STEP_RE.search(l) for l in recent]
    steps = [m for m in steps if m]

    if steps:
        last = steps[-1]
        step = int(last.group(1))
        tokens_m = float(last.group(2))
        loss = float(last.group(3))
        tok_s = int(last.group(5))
        losses = [float(m.group(3)) for m in steps[-30:]]
        avg_loss = sum(losses) / len(losses)
    else:
        step = 0
        tokens_m = 0.0
        loss = avg_loss = float("nan")
        tok_s = 0

    pct = 100.0 * tokens_m * 1e6 / TARGET_TOKENS
    if tok_s > 0:
        remain_tokens = TARGET_TOKENS - tokens_m * 1e6
        eta_secs = remain_tokens / tok_s
        eta_str = str(timedelta(seconds=int(eta_secs)))
        done_at = (datetime.now() + timedelta(seconds=eta_secs)).strftime("%a %Y-%m-%d %H:%M")
    else:
        eta_str = "unknown"
        done_at = "unknown"

    crashed = any(CRASH_RE.search(l) for l in recent[-60:])
    final_done = (CKPT_DIR / "final.pt").exists()
    if final_done:
        state = "COMPLETE - final.pt saved"
    elif crashed:
        state = "CRASH DETECTED - wrapper should be auto-resuming"
    elif steps:
        state = "TRAINING"
    else:
        state = "NOT STARTED / no log lines yet"

    ckpts = sorted(CKPT_DIR.glob("step_*.pt")) if CKPT_DIR.exists() else []
    ckpt_lines = "\n".join(f"- `{c.name}`" for c in ckpts) or "- (none yet)"

    loss_curve = " -> ".join(f"{float(m.group(3)):.2f}" for m in steps[::max(1, len(steps) // 12)][-12:])

    md = f"""# Glemton 350M v1.0-preview - training status

_Auto-generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} local. Updated every ~10 min by `weekend_run.ps1`._

## State: {state}

| Metric | Value |
|---|---|
| Tokens seen | {tokens_m:.0f}M / 3000M ({pct:.1f}%) |
| Step | {step} |
| Latest loss | {loss:.4f} |
| Avg loss (last 30 logged) | {avg_loss:.4f} |
| Throughput | {tok_s:,} tok/s |
| ETA to 3B tokens | {eta_str} |
| Projected finish | {done_at} |

## Loss trajectory (sampled)
{loss_curve}

## Checkpoints on disk
{ckpt_lines}

## Recent log tail
```
{chr(10).join(recent[-12:])}
```
"""
    STATUS.write_text(md, encoding="utf-8")
    print(f"[gen_status] wrote {STATUS} - state={state} tokens={tokens_m:.0f}M")


if __name__ == "__main__":
    main()
