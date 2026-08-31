---
type: skill
skill_category: product-delivery
status: developing
stability: stable
created: 2026-08-24
updated: 2026-08-24
review_after: 2027-02-24
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Product-Manager]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
prerequisites:
  - "[[HTTP-API]]"
  - "[[Testing]]"
  - "[[Software-Design-and-Architecture]]"
related_concepts:
  - "[[AI-Product-Engineering]]"
---

# API Product Delivery

## 为什么岗位需要它
模型能力必须通过清晰契约、版本、权限和开发者体验变成可用产品。

## Role Demand
Application/PM/FDE 为 Core；研究岗位是接口意识。证据见 [[OpenAI-Software-Engineer-API-SDK-Seattle-2026-08]]。

## Job Evidence

[[OpenAI-Software-Engineer-API-SDK-Seattle-2026-08]]、[[OpenAI-Product-Manager-API-Agents-San-Francisco-2026-08]] 的 `Skill Extraction` 是本 Skill 的 Job Evidence；只把明确要求作为 required 证据，职责推断保留为 inferred。

## 在岗位中怎么使用
定义 API/SDK、错误、限流、计费、兼容性、文档、评测和发布流程。

## Role-specific Target Depth
应用 implement；PM decide/prioritize；FDE use/implement。

## 前置 Skills
[[HTTP-API]]、[[Testing]]、[[Software-Design-and-Architecture]]。

## 学习范围
契约、版本、认证、权限、可靠性、成本、文档和用户反馈。

## 核心知识
向后兼容、可观测性、失败语义和安全默认值。

## Practice
设计一个带版本、鉴权、错误 schema、限流和示例的 API。

## Pass Evidence
新用户能按文档完成调用，失败时能定位并安全重试。

## 常见失败
只设计 happy path；把模型 prompt 暴露成稳定契约；无弃用策略。

## 不需要深挖到什么程度
PM 不必亲自实现 SDK，但要能审查契约与风险。

## Related Knowledge
[[AI-Product-Engineering]]、[[Tool-Calling-and-Action-Contracts]]。

## Actual Evidence
尚无用户能力结论；用 [[Evidence-Card]] 记录。

## Sources
[[OpenAI-Software-Engineer-API-SDK-Seattle-2026-08]]、[[OpenAI-Product-Manager-API-Agents-San-Francisco-2026-08]]。
