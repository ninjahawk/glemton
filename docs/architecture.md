# Architecture

Glemton v1.0 is a dense decoder-only transformer in the Llama-3 family. The choice is deliberately boring at the architecture level so that the unusual ideas (corpus, no-instruction-tuning, turn-marker pretraining) carry the project rather than ambitious architectural bets that the Blackwell toolchain in 2026-05 doesn't yet support cleanly.

## Headline numbers

| | v1.0 (target) | actual at config build |
|---|---|---|
| Parameters | ~350 M | **365 M** |
| Vocab | 32 000 | 32 000 |
| `d_model` | 1024 | 1024 |
| Layers | 30 | 30 |
| Heads / KV heads | 16 / 4 (GQA) | 16 / 4 |
| FFN dim | 2752 (SwiGLU) | 2752 |
| Max sequence length | 32 768 | 32 768 |
| Tokenizer | 32 k BPE trained from scratch | pending |

The +4% drift from the 350 M target is acceptable; it's still a "small" model by 2026 standards and well within the 12 GB VRAM envelope.

## Component-level choices

### Normalization — RMSNorm
Lighter than LayerNorm, no bias, no centering. Standard in every modern open LM since Llama 1.

### Position encoding — RoPE with θ = 1 000 000
Standard rotary embeddings on Q/K. The high θ is the Llama-3 long-context trick: it stretches the positional frequency spectrum so the model can extrapolate beyond its pretraining context window without being explicitly trained at every position. We pretrain at 2048 (cheap) and rely on RoPE to extend usable context out to 32 k for the long-conversation eval. This is well-documented to work for moderate extrapolation; we'll measure where Glemton's effective context degrades and document it in `docs/evals.md`.

### Attention — GQA, sliding-window with periodic global layers
- **GQA** (Grouped-Query Attention) with 4 KV heads vs 16 Q heads — 4× compression of the KV cache at minimal quality cost, big inference-memory win for long conversations.
- **Sliding-window 4096** at most layers, with every 6th layer doing **full attention**. This is the Llama-3 pattern. Lets the model handle 32 k context without paying quadratic cost at every layer, while preserving global-coherence channels.
- Implemented via `torch.nn.functional.scaled_dot_product_attention` for v1.0. **FlashAttention-3 sliding-window kernels** are deferred until we confirm a Blackwell-compatible build; on the 5070 with FA-3 we expect ~2× throughput.

### FFN — SwiGLU
Three projections — gate, up, down — with SiLU on gate, multiplied by up. Standard. Ratio chosen so total FFN params per layer land ~2.7× `d_model`, matching the Llama-3 SwiGLU ratio.

### Embedding tying
Input and output projections share weights. Saves ~33 M params at 32 k vocab — meaningful on a 350 M model.

### Turn convention baked into the tokenizer
The tokenizer special-token vocabulary includes:
```
<pad> <bos> <eos> <unk> <user> <reply> <sep>
```
Every training document is structured as a stream of `<user> ... <reply> ...` blocks, so the model learns the turn-marker pattern as a pretraining objective rather than as a downstream chat template trick. This is the closest thing we have to a "novel architectural choice" — the format is the inductive bias.

## What we explicitly chose NOT to do at v1.0

- **Mamba-2 / RWKV / hybrid SSM**: stronger fit for the long-conversation claim, but custom CUDA kernels need updated Blackwell (sm_120) support and the toolchain was patchy as of 2026-05. Re-evaluate for v2.0 once sm_120 kernels stabilize.
- **FlashAttention-3 sliding-window kernels at v1.0**: deferred until we verify a Blackwell build; falling back to PyTorch's `scaled_dot_product_attention` for the initial pretrain.
- **Mixture of experts**: would help capacity-per-parameter, but adds routing complexity that doesn't survive a 350 M scale.
- **Multi-token prediction / speculative decoding heads**: nice for inference, irrelevant for the headline claims.

## Sanity checks already passed

- `src/glemton/model.py` builds and runs a forward pass on CPU for both `debug-10m.yaml` (12.3 M params, sane init loss ≈ 9.9 vs `log(32000) ≈ 10.37`) and `glemton-350m.yaml` (365 M params).
- PyTorch 2.12 nightly cu128 sees the RTX 5070 with capability `(12, 0)` and `bf16_supported == True`.
