---
type: skill
skill_category: infra-inference
status: developing
stability: current
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
roles:
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[AI-Application-Engineer]]"
prerequisites:
  - "[[HTTP-API]]"
  - "[[Docker-Containers]]"
  - "[[PyTorch]]"
  - "[[Software-Design-and-Architecture]]"
related_concepts:
  - "[[Inference-Optimization]]"
---

# Model Serving

## 为什么岗位需要它
模型只有在稳定、可观测、可扩展的服务中才产生产品价值。

## Role Demand
Infra 为 Core；应用/FDE 为 Common。证据见 [[Huawei-AI-Architect-Training-Inference-Beijing-2026-08]]。

## Job Evidence

[[OpenAI-Software-Engineer-Model-Inference-San-Francisco-2026-08]]、[[Huawei-AI-Architect-Training-Inference-Beijing-2026-08]] 的 `Skill Extraction` 是本 Skill 的 Job Evidence；只把明确要求作为 required 证据，职责推断保留为 inferred。

## 在岗位中怎么使用
打包模型、管理批处理/流式请求、版本、容量、回滚和安全边界。

## Role-specific Target Depth
Infra implement/optimize；应用 use/implement；PM explain 延迟和成本。

## 前置 Skills
[[HTTP-API]]、[[Docker-Containers]]、[[PyTorch]]、[[Software-Design-and-Architecture]]。

## 学习范围
模型加载、batching、并发、GPU memory、路由、版本和健康检查。

## 核心知识
延迟/吞吐、容量、冷启动、故障隔离和可回滚发布。

## Practice
把一个模型封装成带健康检查、指标、超时和版本回滚的服务。

## Pass Evidence
能用压测数据解释 p95 延迟、吞吐和资源成本。

## 常见失败
只测平均延迟；无超时/限流；模型版本和数据版本不可追踪。

## 不需要深挖到什么程度
应用岗位先掌握服务契约和故障边界，不必马上优化 kernel。

## Related Knowledge
[[Inference-Optimization]]、[[Observability]]。

## Actual Evidence
尚无用户能力结论；使用 [[Evidence-Card]]。

## Sources
[[OpenAI-Software-Engineer-Model-Inference-San-Francisco-2026-08]]、[[Huawei-AI-Architect-Training-Inference-Beijing-2026-08]]。
