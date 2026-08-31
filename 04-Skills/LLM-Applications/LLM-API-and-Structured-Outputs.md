---
type: skill
skill_category: LLM Applications
status: developing
stability: current
created: 2026-08-31
updated: 2026-08-31
review_after: 2026-11-30
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[AI-Product-Manager]]"
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
prerequisites:
  - "[[HTTP-API]]"
  - "[[Prompt-and-Context-Engineering]]"
  - "[[Software-Design-and-Architecture]]"
related_concepts:
  - "[[Tool-Calling-and-Action-Contracts]]"
  - "[[Agent-Evals-and-Trace-Debugging]]"
sample_batch: enterprise-applied-ai-2026-08
---

# LLM API and Structured Outputs

## 为什么岗位需要它

让模型输出成为可验证的 API 数据，而不是散文；是应用、FDE、平台和 PM 的接口层。

## Role Demand

设计请求/响应、JSON Schema、校验、拒答、重试和版本化，并记录模型、prompt、schema、成本和延迟。

## Job Evidence

- [[Notion-Software-Engineer-AI-Workflows-2026-08]]
- [[Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]

链接回每张 Job Sample 的 `Skill Extraction`；`explicit` 与 `inferred` 分开，样本不代表市场频率。

## 在岗位中怎么使用

设计请求/响应、JSON Schema、校验、拒答、重试和版本化，并记录模型、prompt、schema、成本和延迟。

## Role-specific Target Depth

- Application / FDE：implement；Agent Platform：implement→optimize；PM / Solutions：explain→use。
- 目标深度随交付责任变化，不是全局门槛。

## 前置 Skills

[[HTTP-API]], [[Prompt-and-Context-Engineering]], [[Software-Design-and-Architecture]]

## 学习范围

定义、边界、接口契约、失败模式、权限/成本/延迟和可观测性；优先覆盖一个可交付流程。

## 核心知识

让模型输出成为可验证的 API 数据，而不是散文；是应用、FDE、平台和 PM 的接口层。 重点掌握 schema、状态、重试、幂等、审计、回滚和业务结果之间的关系。

## Practice

做发票/工单抽取 API：固定 schema、拒答样例、字段校验、版本化回归集和人工复核队列。

## Pass Evidence

完成 Practice 后，提交可重放的任务集、测试结果、trace、失败分类和一项修复前后对比。

## 常见失败

把 prompt 或单一框架当作系统边界；忽略权限、超时、幂等、回滚、失败切片和人工接管；只展示 happy path。

## 不需要深挖到什么程度

不必先研究模型训练内部、所有厂商 SDK 或复杂多智能体；先能在受控任务中完成实现、测试、trace 和复盘。

## Related Knowledge

[[Tool-Calling-and-Action-Contracts]], [[Agent-Evals-and-Trace-Debugging]]

## Actual Evidence

尚无用户能力结论；完成 Practice 后复制 [[Evidence-Card]]，记录问题、行动、结果、失败和判断，并回链本 Skill 与目标 Role。

## Sources

### Official / normative

- https://developers.openai.com/api/reference/cli/resources/responses/methods/create
- https://developers.openai.com/api/docs/guides/latest-model

### Job evidence

- [[Notion-Software-Engineer-AI-Workflows-2026-08]]
- [[Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]

### Practice tutorial

- [[YAML-Frontmatter-AI-Prompts]]

官方规范定义边界，岗位页决定优先级，教程只提供练习路径；三类证据不混写。
