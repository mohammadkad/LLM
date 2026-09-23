# LLM Architectures: From the Beginning to Now

## Pre-Transformer Era (Foundations)

| Architecture | Year | Notes |
|---|---|---|
| RNNs | 1980s–2014 | Step-by-step sequence processing; struggled with long-range dependencies |
| LSTM | 1997 | Gated RNN variant, handled longer dependencies |
| GRU | 2014 | Simplified gated RNN variant |
| Seq2Seq + Attention | 2014–2015 | Bahdanau/Luong attention; direct ancestor of the Transformer |

## The Transformer Breakthrough

| Architecture | Year | Notes |
|---|---|---|
| **Transformer** | 2017 | "Attention Is All You Need" — dropped recurrence for self-attention, enabled parallelization |

## Early Transformer LLMs (2018–2019)

| Architecture | Year | Type | Notes |
|---|---|---|---|
| BERT | 2018 | Encoder-only | Bidirectional, masked language modeling; dominated NLU |
| GPT-1 / GPT-2 | 2018–2019 | Decoder-only | Autoregressive next-token prediction |
| T5 | 2019 | Encoder-decoder | Framed all NLP tasks as text-to-text |

## Scaling Era (2020–2022)

| Architecture | Year | Notes |
|---|---|---|
| GPT-3 | 2020 | 175B, decoder-only, strong few-shot/in-context learning |
| Switch Transformer | 2021 | Early large-scale sparse Mixture-of-Experts (MoE) |
| PaLM | 2022 | Large dense decoder-only, scaling law benchmarks |
| Chinchilla | 2022 | Reshaped scaling philosophy (compute-optimal data:param ratio) |

## Instruction-Tuning & Alignment Era (2022–2023)

| Architecture | Year | Notes |
|---|---|---|
| InstructGPT / ChatGPT | 2022 | Decoder-only + RLHF (training change, not architectural) |
| LLaMA | 2023 | Efficient open-weight dense decoder-only; sparked open ecosystem |
| GPT-4 | 2023 | Reportedly MoE (unconfirmed); added multimodal input |
| Mixtral | 2023 | Popularized sparse MoE in open-weight models |

## Long-Context & Efficiency Innovations (2023–2024)

| Architecture / Technique | Year | Notes |
|---|---|---|
| Mamba (state-space models) | 2023 | Attention alternative; linear-time, strong on long context |
| GQA / sliding-window attention / FlashAttention | 2023–2024 | Efficiency mechanisms widely adopted, not standalone architectures |

## Reasoning-Model Era (2024–2025)

| Architecture | Year | Notes |
|---|---|---|
| OpenAI o1 / o3 | 2024–2025 | Decoder-only + extended chain-of-thought at inference time |
| DeepSeek V3 / R1 | 2024–2025 | Large sparse MoE, efficient training, open-weight reasoning variants |
| Claude 3/4, Gemini 1.5–2.x | 2024–2025 | Long-context, natively multimodal, increasingly MoE (per outside reporting) |

## Current Frontier (2026)

| Architecture | Notes |
|---|---|
| Hybrid dense-MoE / multi-tier MoE routing | Reported in GPT-5.5/5.6, newer Claude generations |
| Hybrid Mamba-Transformer | e.g., NVIDIA Nemotron 3 — state-space efficiency + transformer expressiveness |
| Subquadratic / sparse attention | Targets O(n²) bottleneck for multi-million-token contexts |
| Unified routing systems | e.g., GPT-5 routing queries to fast vs. deep sub-models |

---

