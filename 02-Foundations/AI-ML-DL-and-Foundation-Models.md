---
type: concept
domain: foundations
status: validated
stability: stable
depth: explain
created: 2026-08-24
updated: 2026-08-24
aliases:
  - AI ML DL 与基础模型
related:
  - "[[AI-Technology-MOC]]"
  - "[[Transformer-and-Foundation-Models]]"
---

# AI, ML, DL and Foundation Models

## 一句话关系

```text
Artificial Intelligence
└─ Machine Learning
   └─ Deep Learning
      └─ Foundation Models（常用深度学习在大规模数据上训练）
         └─ LLM / VLM / 生成模型等具体家族
```

## 分清四个层级

| 概念               | 核心问题                  | 例子                        |
| ---------------- | --------------------- | ------------------------- |
| AI               | 如何让系统完成通常需要智能的任务      | 规划、识别、生成、决策               |
| ML               | 如何从数据或反馈中学习规律         | 分类、回归、排序                  |
| DL               | 如何用多层神经网络学习表征         | CNN、Transformer、Diffusion |
| Foundation Model | 如何训练可适配许多下游任务的大规模通用模型 | LLM、VLM                   |

LLM 是“以语言序列为核心输入/输出的基础模型家族”，不是 AI 的同义词。生成式 AI 也不只包含文本，还包括图像、音频、视频、3D 和多模态生成。

## 你真正需要理解的边界

- 规则系统也可以属于 AI，但不属于 ML；
- ML 不一定使用神经网络；
- DL 不一定是生成模型；
- Foundation Model 可以通过 prompting、retrieval、fine-tuning 或工具调用适配任务；
- “模型能力”与“完整产品能力”之间还有数据、应用、系统、安全和产品多层工程。

## 最小验证

把以下名词分别放入正确层级，并说明可能跨层的位置：推荐系统、决策树、Transformer、ChatGPT、RAG、自动驾驶、OCR、Agent。

## 下一步

- 原理：[[Training-Evaluation-and-Generalization]]
- 模型：[[Transformer-and-Foundation-Models]]
- 应用：[[RAG-and-Knowledge-Systems]]、[[AI-Agents-and-Tool-Use]]
