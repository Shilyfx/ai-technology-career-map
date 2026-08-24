---
type: skill
skill_category: infra-inference
status: developing
stability: stable
created: 2026-08-24
updated: 2026-08-24
review_after: 2027-02-24
roles:
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[Research Engineer]]"
  - "[[Data-and-AI-Engineer]]"
prerequisites:
  - "[[Linux]]"
  - "[[Testing]]"
related_concepts:
  - "[[AI-Infrastructure-and-MLOps]]"
---

# Distributed Systems

## 为什么岗位需要它
AI 训练、数据和服务都要在节点失败、网络延迟和资源有限时继续正确运行。

## Role Demand
Infra/Research 为 Core；Data 为 Common；应用按规模选择。证据见 [[OpenAI-Software-Engineer-GPT-Infrastructure-San-Francisco-2026-08]]。

## Job Evidence

[[OpenAI-Software-Engineer-GPT-Infrastructure-San-Francisco-2026-08]]、[[Anthropic-Performance-Engineer-Inference-Systems-San-Francisco-2026-08]] 的 `Skill Extraction` 是本 Skill 的 Job Evidence；只把明确要求作为 required 证据，职责推断保留为 inferred。

## 在岗位中怎么使用
拆分服务、定义一致性、重试、幂等、队列、限流和故障恢复。

## Role-specific Target Depth
Infra implement/optimize；Data use/implement；PM/FDE explain。

## 前置 Skills
[[Linux]]、[[Testing]]。

## 学习范围
RPC、队列、状态、复制、超时、重试、调度、可观测性。

## 核心知识
部分失败、背压、容量、恢复和一致性取舍。

## Practice
设计一个有超时、重试、幂等和故障注入的推理服务。

## Pass Evidence
能画出失败路径并证明重试不会重复副作用。

## 常见失败
无限重试；只看 happy path；把更多节点当作自动高可用。

## 不需要深挖到什么程度
应用岗位先会识别分布式边界，不需立刻实现共识算法。

## Related Knowledge
[[AI-Infrastructure-and-MLOps]]、[[Model-Serving]]。

## Actual Evidence
尚无用户能力结论；关联 [[Evidence-Card]]。

## Sources
[[OpenAI-Software-Engineer-GPT-Infrastructure-San-Francisco-2026-08]]、[[Anthropic-Performance-Engineer-Inference-Systems-San-Francisco-2026-08]]。
