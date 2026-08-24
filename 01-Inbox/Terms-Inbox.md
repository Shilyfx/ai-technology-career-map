---
type: inbox
status: active
created: 2026-08-24
updated: 2026-08-24
aliases:
  - 术语收集箱
---

# Terms Inbox

> 陌生名词先放这里。收集箱的目标是归类与决定深度，不是囤积链接。

## 待处理

| 名词 | 在哪里听到 | 初步层级 | 我需要做什么 | 状态 |
| --- | --- | --- | --- | --- |
| 示例：KV Cache | 岗位 JD | 系统/推理 | 能解释用途与内存权衡 | example |
|  |  |  |  | inbox |

## 四步处理法

1. **归层**：数据、训练、模型、应用、系统、安全、产品；
2. **去营销**：把“它很先进”改写成“它解决 X 约束”；
3. **查依赖**：如果解释需要三个陌生词，先补最近的前置；
4. **定深度**：recognize / explain / use / implement / optimize / research。

## 常见术语雷达

### 基础与训练

AI、ML、DL、supervised learning、self-supervised learning、loss、optimizer、backpropagation、batch、epoch、checkpoint、overfitting、generalization、data leakage、transfer learning、fine-tuning、PEFT、LoRA、SFT、RLHF、RLAIF、DPO、PPO、GRPO、synthetic data、distillation。

### 基础模型与多模态

Transformer、token、tokenizer、embedding、attention、context window、foundation model、LLM、MoE、reasoning model、test-time compute、VLM、diffusion、multimodal、world model、VLA、embodied AI。

### 应用与 Agent

prompt engineering、context engineering、structured output、function calling、tool use、RAG、vector database、hybrid search、reranker、chunking、Agent、workflow、planner、memory、human-in-the-loop、MCP、A2A、multi-agent、computer use。

### 评测、安全与治理

benchmark、eval、golden set、LLM-as-a-judge、hallucination、grounding、guardrail、red teaming、prompt injection、jailbreak、model card、AI RMF、AI governance、alignment、interpretability、mechanistic interpretability。

### 系统与基础设施

GPU、NPU、CUDA、NCCL、distributed training、data parallel、tensor parallel、pipeline parallel、inference、serving、batching、KV Cache、quantization、speculative decoding、vLLM、SGLang、Triton、MLflow、Kubernetes、observability、latency、throughput、SLO、rollback。

## 已归档到主线

- 上位概念：[[AI-ML-DL-and-Foundation-Models]]
- Transformer：[[Transformer-and-Foundation-Models]]
- 后训练：[[Pretraining-Posttraining-and-Fine-tuning]]
- RAG：[[RAG-and-Knowledge-Systems]]
- Agent：[[AI-Agents-and-Tool-Use]]
- Evals：[[Evals-and-Observability]]
- Infra：[[AI-Infrastructure-and-MLOps]]、[[Inference-Optimization]]
