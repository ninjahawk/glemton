# WAKE_UP — live status handoff

**Updated:** 2026-05-24 ~15:30
**Read this first.** It is the current state of the project. CLAUDE.md is the
stable rules; this file is what is actually happening right now.

---

## STATE: v1.0-preview run COMPLETE. final.pt saved 2026-05-24 15:17.

One clean run start to finish (Thu 2026-05-21 20:32 → Sun 2026-05-24 15:17,
~66h GPU). **3000M tokens at 12,484 tok/s, attempt 1, zero crashes, zero
resumes.** Final loss 2.0–2.3. Checkpoints kept: 500M, 1000M, 1500M, 2000M
milestones + 2500/2600/2700/2800/2900/3000 newest, plus `final.pt`.

### Eval results (run 2026-05-24)

**Sycophancy probe: 0 markers / 39 responses (0.0 per 100).** The headline
claim from CLAUDE.md holds — zero "great question", "I'd be happy to", "as
an AI", "I understand your concern" across the full probe set. Many responses
are empty (~13/39 produced nothing after `<reply>` — instruction-following is
weak as expected), but when the model does speak it speaks in casual spoken
register, not chatbot-speak. Report: `logs/sycophancy_eval_v1preview.json`.

**Long-conversation recall: 0/15, every gap (5/10/25/50/75).** Total failure —
honest. This was the predicted outcome documented in CLAUDE.md: OPUS is
2-line subtitle pairs with no preserved scene context, so the model has no
mechanism to learn long-range recall from this corpus. The fix is corpus
expansion (scene-grouped OPUS, Ubuntu Dialogue, SE threads), not more tokens
on this corpus. Report: `logs/long_conversation_eval_v1preview.json`.

**Qualitative sample:** Outputs are clearly movie-subtitle register — short
casual lines, even `[CELL PHONE RINGS]` stage directions creep in. The
literary prompts (Elizabeth/the old man) trigger Gutenberg-leaning prose.
No SQuAD-template capture, no EOS-collapse. The corpus fix worked.

### Defensible claims — honest status
1. **No corporate-chatbot tone:** ✅ Sycophancy 0.0/100, sample outputs confirm.
2. **Long-conversation consistency:** ❌ Not supported by this corpus. v2.0 task.
3. **Local-first:** Architectural — 365M params, RTX 5070, GGUF-quantizable.
   Not eval-tested here.

### Open from CLAUDE.md
- "Sober ninjahawk decides on commit attribution + naming" — release-time call.
- Long-conversation claim needs corpus work before any public v1.0 release;
  what's done is genuinely "1.0-preview", not v1.0.

The scheduled task `Glemton-WeekendTrain` is **State: Ready** (idle, GPU free).
It will not relaunch unless manually started or a logon trigger fires; with
training complete and `final.pt` present, the wrapper would exit immediately
even if it did.

---

## What this session did (2026-05-21)

The previous overnight 350M run (`glemton-350m`, 500M-token target) was found
**collapsed into SQuAD Q&A templates** and unsalvageable. Full diagnosis below.
This session diagnosed it, rebuilt the corpus mix, validated the fix on a
scaffold model, and prepared an unattended weekend training run.

### Root cause of the dead 350M run
SQuAD was the **only corpus in that run's mix that contained `<user>/<reply>`
turn markers**. Gutenberg books and Common Pile are raw prose with no markers.
So every time the model saw a `<user>` token it was inside a SQuAD question.
It learned `<user> → factual question`. All 8 checkpoints of that run show one
of: SQuAD-template capture, EOS-collapse (empty output), or empty-on-marker.
Archived at `checkpoints/glemton-350m-squad-poisoned-archive/` (one ckpt kept
as the documented lesson).

### The fix — corpus composition, not just weighting
OPUS OpenSubtitles got tokenized in the background during the crash:
**1.98 B tokens of real `<user>/<reply>`-formatted spoken dialogue.** That plus
Hacker News (2.6 M, also marker-formatted) means the model now sees `<user>`
markers overwhelmingly in genuine conversation, not Q&A.

Tokenized corpus inventory:
| Source | Tokens | Marker-formatted? |
|---|---|---|
| opus_subtitles | 1.98 B | yes (`<user>/<reply>`) |
| common_pile | 499 M | no (raw prose) |
| gutenberg_books | 12.5 M | no (raw prose) |
| hacker_news | 2.6 M | yes |
| squad | 2.2 M | yes — DROPPED, it poisoned the last run |

~2.5 B unique tokens total.

### Scaffold validation — PASSED
Trained a 50M model on 100M tokens of the new mix
(`configs/scaffold-validate-opus.yaml`). Output is conversational, movie-subtitle
register, **zero sycophancy markers, zero SQuAD templates, no EOS-collapse**.
All three pathologies of the dead run are gone. Checkpoint kept at
`checkpoints/glemton-scaffold-validate-opus/final.pt`.

### Two failed launch attempts (lessons)
1. The 500M `glemton-350m` run died earlier from an OS kill — data-prep jobs
   (pack_shards/OPUS prep) were running concurrently and exhausted host RAM.
   **Lesson: never run heavy CPU/IO jobs while GPU training is active.**
2. A relaunch via `Start-Process ... -Minimized` from inside the Claude Code
   harness died instantly with `forrtl: error (200): window-CLOSE event` —
   the process stayed console-tied and got killed when the launching tool
   call ended. **Lesson: a process launched through the harness is NOT
   detached. Use Windows Task Scheduler for genuine session-independence.**

---

## THE PLAN — v1.0-preview run

**Goal:** train the 350M model to 3 B tokens on the OPUS-dominant corpus,
fully decoupled from Claude Code, with phone-visible status updates.

**Config:** `configs/glemton-350m.yaml` — already set to 3 B tokens,
checkpoint every 100 M, OPUS-dominant `source_weights` (opus 1.0, common_pile
0.3, gutenberg_books 2.0, hacker_news 1.0, squad 0.0).

**Why 3 B and not more:** 3 B is the practical ceiling for ~2.5 B unique
tokens. Past that the model memorizes rather than generalizes. A true v1.0 at
10–15 B tokens needs the corpus expanded FIRST (see "after the trip" below).

**Runtime:** ~67 h at ~12.4 k tok/s.

### Decoupled execution — BUILT AND RUNNING
`scripts/weekend_run.ps1` runs as the Scheduled Task `Glemton-WeekendTrain`
(per-user, "run only when logged on" → no admin/UAC; AtLogOn trigger so it
resumes after a reboot; no execution time limit; runs on battery). The Task
Scheduler service owns the process — no console, immune to terminal close.
The wrapper resumes from the latest checkpoint on crash, writes `STATUS.md`,
git-pushes it every ~10 min, and prunes old checkpoints. Claude Code is now a
pure read-only observer.

Done this session: hardened `weekend_run.ps1`
(`FOR_DISABLE_CONSOLE_CTRL_HANDLER=1` + wrapper log); fixed `gen_status.py` to
parse the UTF-16 training log (it was stuck at NOT STARTED); registered and
started the task; preflight-verified the model steps cleanly (loss 10.6→8.2,
no nan); confirmed STATUS.md populates.

### ninjahawk's part (still needed)
- **Pause Windows Update** (Settings → Windows Update → Pause). Do NOT let
  Claude registry-hack this.
- Keep the PC **on, plugged in, and logged in** for the whole trip — the task
  is "run only when logged on"; a logoff stops it (a reboot+login restarts it).
- Optional: enable Remote Control for phone steering.

### NEXT ACTION for a fresh terminal
Nothing to launch. **Monitor only.** Check `STATUS.md` for progress. If state
shows CRASH, the wrapper auto-resumes — confirm via `logs/weekend_run_wrapper.log`.
First checkpoint lands at 100M tokens (~2.2h in).

---

## Host state (already done this session)
- Disk: 26 GB free (cleaned up dead checkpoint dirs)
- Sleep + hibernate disabled on AC power
- 7 commits pushed to `origin/master`

## After the trip — path to a true v1.0
3 B-token run = "Glemton 1.0-preview". For a genuinely better v1.0:
1. Expand corpus to ~5–10 B unique tokens: unpack
   `data/raw/gutenberg_dialogue/source.tar.gz`, unpack the Stack Exchange
   `.7z` archives, pull more SE dumps + DailyDialog/EmpatheticDialogues via
   HF parquet, more curated public-domain dialogue.
2. Then a 10–15 B-token run (~7–12 days GPU).
3. **Honest caveat:** the "long-conversation consistency" claim in CLAUDE.md
   is NOT supported by the current corpus — OPUS is 2-line subtitle pairs
   with no preserved scene context. Fixing it needs scene-grouped OPUS or
   genuinely multi-turn corpora (Ubuntu Dialogue, SE threads), not more
   tokens. Address this during corpus expansion.

## Expected model quality (honest)
350M params at 3 B tokens, conversational corpus only. It will sound like a
casual movie character — short, punchy, contemporary spoken English, zero
corporate-chatbot tone. It will NOT be factually accurate, will NOT reason,
will NOT follow instructions well. The defensible claim is tone/register +
zero sycophancy, not capability. Do not claim MMLU-style wins.
