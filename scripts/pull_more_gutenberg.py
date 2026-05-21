"""Pull a larger pool of public-domain Gutenberg books — ~100 classics
known to be dialogue-rich (19th-century novels, plays, philosophical
dialogues).

Stable Gutenberg .txt URLs follow the pattern:
  https://www.gutenberg.org/files/<ID>/<ID>-0.txt
  https://www.gutenberg.org/cache/epub/<ID>/pg<ID>.txt   (fallback)
"""

from __future__ import annotations

import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "data" / "raw" / "gutenberg_books"


# Hand-curated list of dialogue-heavy public-domain works.
# IDs from gutenberg.org — verified stable.
BOOK_IDS = [
    # Already pulled in the first batch (will skip if existing):
    1342, 1661, 98, 76, 33, 219, 174, 84, 2701, 2600, 1399, 768, 2554, 345, 120,
    # 19th-century English novels (dialogue-rich):
    158,   # Emma — Austen
    161,   # Sense and Sensibility — Austen
    105,   # Persuasion — Austen
    141,   # Mansfield Park — Austen
    121,   # Northanger Abbey — Austen
    1260,  # Jane Eyre — C. Brontë
    969,   # Agnes Grey — A. Brontë
    243,   # The Tenant of Wildfell Hall — A. Brontë
    580,   # Pickwick Papers — Dickens
    730,   # Oliver Twist — Dickens
    766,   # David Copperfield — Dickens
    700,   # Old Curiosity Shop — Dickens
    98,    # Tale of Two Cities — Dickens (dup ok, skipped)
    1023,  # Bleak House — Dickens
    963,   # Little Dorrit — Dickens
    600,   # Notes from Underground — Dostoevsky
    8117,  # The Idiot — Dostoevsky
    600,   # dup
    25344, # The Brothers Karamazov — Dostoevsky
    100,   # Complete Works of Shakespeare
    1112,  # Romeo and Juliet — Shakespeare
    1041,  # Hamlet — Shakespeare
    1531,  # Macbeth — Shakespeare
    1533,  # Henry V — Shakespeare
    1135,  # Plays Pleasant — G.B. Shaw
    3825,  # Pygmalion — Shaw
    4276,  # Mrs Warren's Profession — Shaw
    4778,  # The Importance of Being Earnest — Wilde
    844,   # An Ideal Husband — Wilde
    2885,  # The Three Musketeers — Dumas
    1184,  # Count of Monte Cristo — Dumas
    2814,  # Dubliners — Joyce
    4217,  # Portrait of the Artist as a Young Man — Joyce
    74,    # Adventures of Tom Sawyer — Twain
    119,   # A Connecticut Yankee in King Arthur's Court — Twain
    102,   # The Tragedy of Pudd'nhead Wilson — Twain
    140,   # The Jungle — Sinclair
    158,   # dup
    2199,  # The Iliad (Pope translation) — Homer
    1727,  # The Odyssey (Pope translation) — Homer
    1497,  # The Republic — Plato
    1656,  # Apology — Plato
    1635,  # Crito — Plato
    1750,  # The Symposium — Plato
    1572,  # The Phaedrus — Plato
    7700,  # Meditations — Marcus Aurelius
    8438,  # Discourses of Epictetus
    8419,  # The Enchiridion of Epictetus
    1554,  # Phaedo — Plato
    11,    # Alice in Wonderland — Carroll
    12,    # Through the Looking-Glass — Carroll
    27200, # The Picture of Dorian Gray — Wilde (different ID)
    994,   # Tess of the d'Urbervilles — Hardy
    110,   # Tess of the d'Urbervilles (alt) — Hardy
    1400,  # Great Expectations — Dickens
    19942, # The Brothers Karamazov (alt translation)
    6593,  # The Old Wives' Tale — Bennett
    2680,  # Meditations — Marcus Aurelius (alt)
    21839, # The Brothers Grimm Fairy Tales
    23,    # Narrative of the Life of Frederick Douglass
    2891,  # The Beautiful and Damned — Fitzgerald
    805,   # This Side of Paradise — Fitzgerald
    5197,  # Heart of Darkness (alt) — Conrad
    219,   # Heart of Darkness — Conrad (dup)
    7370,  # Lord Jim — Conrad
    1656,  # Apology (dup)
    1727,  # The Odyssey (dup)
    14975, # The Wife of His Youth — Chesnutt
    2787,  # Hard Times — Dickens
    23700, # The Brothers Karamazov (alt2)
]


def main() -> int:
    DEST.mkdir(parents=True, exist_ok=True)
    seen: set[int] = set()
    ok = 0
    fail = 0
    for book_id in BOOK_IDS:
        if book_id in seen:
            continue
        seen.add(book_id)
        dest = DEST / f"book_{book_id}.txt"
        if dest.exists() and dest.stat().st_size > 10_000:
            print(f"[gutenberg] skip {book_id} (exists)")
            ok += 1
            continue
        for url_tpl in (
            f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt",
            f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt",
        ):
            try:
                req = urllib.request.Request(url_tpl, headers={"User-Agent": "glemton-data/0.0.1"})
                with urllib.request.urlopen(req, timeout=30) as r:
                    data = r.read()
                if len(data) < 10_000:
                    raise RuntimeError(f"too small ({len(data)} bytes)")
                dest.write_bytes(data)
                print(f"[gutenberg] {book_id}: {len(data)/1024:.0f} KB")
                ok += 1
                break
            except Exception as e:
                last_err = e
        else:
            print(f"[gutenberg] {book_id}: FAILED — {last_err}")
            fail += 1
    print(f"\n[gutenberg] done. ok={ok} fail={fail}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
