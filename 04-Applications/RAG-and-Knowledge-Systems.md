---
type: concept
domain: applications
status: seed
stability: current
created: 2026-08-24
updated: 2026-08-24
aliases:
  - RAG
  - 检索增强生成
related:
  - "[[AI-Agents-and-Tool-Use]]"
  - "[[Evals-and-Observability]]"
  - "[[Data-Engineering-and-Governance]]"
---

# RAG and Knowledge Systems

## RAG 是什么

Retrieval-Augmented Generation 在生成前检索外部证据，把模型参数之外的知识送入上下文。它主要解决知识可更新、可追溯和领域信息访问问题，不自动解决推理错误或来源错误。

```mermaid
flowchart LR
  U["用户问题"] --> Q["query understanding"]
  Q --> R["retrieval"]
  R --> RR["reranking / filtering"]
  RR --> C["context construction"]
  C --> G["generation"]
  G --> V["citation / validation"]
```

## 关键组件

- 文档解析、chunking、metadata 与权限；
- sparse / dense / hybrid retrieval；
- embedding 与 vector database；
- reranker 与 query rewriting；
- context budget、去重与排序；
- 引用、答案拒绝、freshness 与缓存。

## 典型失败

| 层 | 失败 |
| --- | --- |
| 数据 | 文档过期、权限错误、解析丢失 |
| 检索 | 没召回、召回噪声、查询歧义 |
| 上下文 | 证据被截断、顺序偏差、互相冲突 |
| 生成 | 忽略证据、混合来源、无依据扩写 |
| 产品 | 用户无法判断可信度、无反馈闭环 |

## 评测拆分

不要只评最终答案。分别测 retrieval recall/precision、reranking、context relevance、faithfulness、answer usefulness、citation correctness、latency 和 cost。

## 何时不用 RAG

- 知识很小且规则可精确编码；
- 任务不依赖外部知识；
- 权限或来源无法可靠管理；
- 需要结构化计算，应该调用数据库/API/工具；
- 数据极少且可直接放入固定 context。

## 最小实践

用 30–50 个真实问题建立 golden set，记录每题应命中的来源、不可回答条件与失败类型，再比较“无检索 / 简单检索 / hybrid + rerank”。

## 一手资料

- Lewis et al., [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
