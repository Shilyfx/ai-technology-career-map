---
type: concept
domain: models
status: seed
stability: stable
created: 2026-08-24
updated: 2026-08-24
aliases:
  - Transformer
related:
  - "[[AI-ML-DL-and-Foundation-Models]]"
  - "[[Pretraining-Posttraining-and-Fine-tuning]]"
---

# Transformer and Foundation Models

## Transformer 解决什么

Transformer 用 attention 在序列元素之间建立依赖，并通过并行张量计算高效训练。它成为语言和多模态基础模型的重要骨架，但“Transformer”不自动意味着大模型、生成能力或聊天能力。

```text
raw input
→ tokenizer / patch / acoustic encoder
→ embeddings + position information
→ repeated attention + feed-forward blocks
→ task head / decoder
→ probabilities or generated tokens
```

## 五个关键名词

- **Token**：模型处理的离散单元，不等同于单词；
- **Embedding**：把离散对象映射到连续向量；
- **Attention**：根据 query-key 关系聚合 value；
- **Context window**：单次计算可直接处理的上下文范围；
- **Autoregressive generation**：根据已有 token 逐步预测下一个 token。

## Foundation Model 的能力从哪里来

```text
architecture
+ data distribution
+ training objective
+ scale and compute
+ post-training
+ inference strategy
+ tools / retrieval / system context
= observed behavior
```

因此不能把一次产品表现全部归因于“模型参数更多”。

## 相关结构

- **Encoder-only**：偏理解与表征；
- **Decoder-only**：偏自回归生成；
- **Encoder-decoder**：输入输出映射；
- **MoE**：每个 token 只激活部分专家，以扩展容量；
- **Multimodal Transformer**：对齐或联合处理多种模态。

## 何时不必自己训练 Transformer

当任务可通过现成模型、检索、规则、轻量适配或传统 ML 达成时，从头训练通常不是第一选择。先建立 baseline、数据和评测。

## 最小验证

手绘一次模型调用链，并在每个箭头标出 shape、数据类型、可训练/不可训练部分与可能的失败点。

## 一手资料

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
