"""Data loading + tokenization for Glemton.

We tokenize sharded `.txt` corpora into packed `uint16` `.bin` files
(GPT-style flat layout) so the trainer can mmap them and sample windows
of `seq_len` tokens cheaply.

Each shard file is just a contiguous stream of token ids. The trainer
draws random offsets into it, slicing `seq_len + 1` tokens to form an
(input, target) pair where target is input shifted by 1.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterator

import numpy as np
import torch


def write_shard(token_ids: np.ndarray, out_path: str) -> None:
    assert token_ids.dtype == np.uint16, "Vocab fits in uint16; if you exceed 65535 tokens, change this."
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    token_ids.tofile(out_path)


def open_shard(path: str) -> np.ndarray:
    return np.memmap(path, dtype=np.uint16, mode="r")


class PackedDataset(torch.utils.data.IterableDataset):
    """Yields (input, target) pairs of shape (seq_len,) from a set of packed shards.

    Random shard + random offset each time. No epoch boundary.
    """

    def __init__(self, shard_dir: str, seq_len: int, seed: int = 0):
        super().__init__()
        self.shard_paths = sorted(str(p) for p in Path(shard_dir).glob("*.bin"))
        if not self.shard_paths:
            raise FileNotFoundError(f"No .bin shards found in {shard_dir}")
        self.seq_len = seq_len
        self.seed = seed

    def __iter__(self) -> Iterator[tuple[torch.Tensor, torch.Tensor]]:
        worker = torch.utils.data.get_worker_info()
        rng_seed = self.seed + (worker.id if worker else 0)
        rng = np.random.default_rng(rng_seed)
        shards = [open_shard(p) for p in self.shard_paths]
        sizes = np.array([len(s) for s in shards], dtype=np.int64)
        weights = sizes / sizes.sum()
        while True:
            i = rng.choice(len(shards), p=weights)
            arr = shards[i]
            max_offset = len(arr) - self.seq_len - 1
            if max_offset <= 0:
                continue
            off = int(rng.integers(0, max_offset))
            chunk = arr[off : off + self.seq_len + 1].astype(np.int64)
            x = torch.from_numpy(chunk[:-1])
            y = torch.from_numpy(chunk[1:])
            yield x, y


def make_dataloader(shard_dir: str, seq_len: int, batch_size: int, num_workers: int = 2):
    ds = PackedDataset(shard_dir, seq_len=seq_len)
    return torch.utils.data.DataLoader(
        ds,
        batch_size=batch_size,
        num_workers=num_workers,
        pin_memory=True,
        drop_last=True,
    )
