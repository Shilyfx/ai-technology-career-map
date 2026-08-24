---
type: skill
skill_category: llm-applications
status: developing
stability: current
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Product-Manager]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
prerequisites:
  - "[[Python]]"
  - "[[Transformer-LLM-Fundamentals]]"
related_concepts:
  - "[[RAG-and-Knowledge-Systems]]"
---

# Retrieval-Augmented Generation

## 为什么岗位需要它
当答案依赖私有、更新或可追溯知识时，检索是比盲目提示更可控的路径。

## Role Demand
应用/FDE 为 Core；PM 需 explain；研究按 eval 或 retrieval 方向加深。证据见 [[Apple-Machine-Learning-Engineer-LLM-Cupertino-2026-02]]。

## 在岗位中怎么使用
切分、索引、召回、重排、上下文拼接、引用和回归评测。

## Role-specific Target Depth
应用 implement；FDE use/implement；PM explain 成本和失败模式。

## 前置 Skills
[[Python]]、[[Transformer-LLM-Fundamentals]]。

## 学习范围
embedding、向量检索、混合检索、reranking、grounding 和 freshness。

## 核心知识
召回率、上下文噪声、权限过滤、引用和数据更新。

## Practice
做一个带引用和离线评测的最小 RAG，并记录召回失败。

## Pass Evidence
能区分检索失败、上下文失败、生成失败和评测失败。

## 常见失败 / 误区
把向量库当知识库；不做权限过滤；只用最终答案分数。

## 不需要深挖到什么程度
普通应用先掌握可解释的检索闭环，不必先实现 embedding 模型。

## Related Concepts
[[RAG-and-Knowledge-Systems]]、[[LLM-Evals]]。

## Actual Evidence
尚无用户能力结论；用 [[Evidence-Card]] 记录。

## Sources
[[Apple-Machine-Learning-Engineer-LLM-Cupertino-2026-02]]、[[OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08]]。
