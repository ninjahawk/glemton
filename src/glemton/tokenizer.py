"""Train and load the Glemton BPE tokenizer.

A 32k vocabulary trained from scratch on the Glemton dialogue corpus.
Special tokens include turn markers — `<user>` and `<reply>` — so the
turn-taking convention is baked into the tokenizer (and therefore the
pretraining objective) rather than being a downstream prompt-template trick.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from tokenizers import Tokenizer, decoders, models, pre_tokenizers, processors, trainers


SPECIAL_TOKENS = [
    "<pad>",
    "<bos>",
    "<eos>",
    "<unk>",
    "<user>",
    "<reply>",
    "<sep>",
]


def build_trainer(vocab_size: int = 32000) -> trainers.BpeTrainer:
    return trainers.BpeTrainer(
        vocab_size=vocab_size,
        special_tokens=SPECIAL_TOKENS,
        min_frequency=2,
        show_progress=True,
        initial_alphabet=pre_tokenizers.ByteLevel.alphabet(),
    )


def build_tokenizer() -> Tokenizer:
    tok = Tokenizer(models.BPE(unk_token="<unk>"))
    tok.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
    tok.decoder = decoders.ByteLevel()
    return tok


def train_from_files(files: Iterable[str], out_path: str, vocab_size: int = 32000) -> None:
    tok = build_tokenizer()
    trainer = build_trainer(vocab_size=vocab_size)
    tok.train(list(files), trainer)
    bos_id = tok.token_to_id("<bos>")
    eos_id = tok.token_to_id("<eos>")
    tok.post_processor = processors.TemplateProcessing(
        single="<bos> $A <eos>",
        pair="<bos> $A <eos> $B:1 <eos>:1",
        special_tokens=[("<bos>", bos_id), ("<eos>", eos_id)],
    )
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    tok.save(out_path)


def load(path: str) -> Tokenizer:
    return Tokenizer.from_file(path)
