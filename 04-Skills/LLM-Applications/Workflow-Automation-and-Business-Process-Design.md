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
  - "[[Software-Design-and-Architecture]]"
  - "[[Technical-Communication]]"
related_concepts:
  - "[[Agent-Orchestration-and-State]]"
  - "[[Enterprise-Integrations-and-Connectors]]"
  - "[[Human-in-the-Loop-and-Agent-Guardrails]]"
sample_batch: enterprise-applied-ai-2026-08
---

# Workflow Automation and Business Process Design

## 为什么岗位需要它

把业务目标、例外和审批点翻译成可观察、可重放、可交付的流程。

## Role Demand

做流程 discovery、触发器、步骤、数据契约、例外、SLA、人工节点和业务指标；只把不确定环节交给模型。

## Job Evidence

- [[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]
- [[Salesforce-Forward-Deployed-Engineer-Supply-Chain-2026-08]]
- [[Zapier-Engineer-Applied-AI-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]

链接回每张 Job Sample 的 `Skill Extraction`；`explicit` 与 `inferred` 分开，样本不代表市场频率。

## 在岗位中怎么使用

做流程 discovery、触发器、步骤、数据契约、例外、SLA、人工节点和业务指标；只把不确定环节交给模型。

## Role-specific Target Depth

- Application / FDE：implement；Agent Platform：implement→optimize；PM / Solutions：explain→use。
- 目标深度随交付责任变化，不是全局门槛。

## 前置 Skills

[[HTTP-API]], [[Software-Design-and-Architecture]], [[Technical-Communication]]

## 学习范围

定义、边界、接口契约、失败模式、权限/成本/延迟和可观测性；优先覆盖一个可交付流程。

## 核心知识

把业务目标、例外和审批点翻译成可观察、可重放、可交付的流程。 重点掌握 schema、状态、重试、幂等、审计、回滚和业务结果之间的关系。

## Practice

自动化 RSS/工单→分类→草稿→人工批准→写回，含去重、重试上限和审计。

## Pass Evidence

完成 Practice 后，提交可重放的任务集、测试结果、trace、失败分类和一项修复前后对比。

## 常见失败

把 prompt 或单一框架当作系统边界；忽略权限、超时、幂等、回滚、失败切片和人工接管；只展示 happy path。

## 不需要深挖到什么程度

不必先研究模型训练内部、所有厂商 SDK 或复杂多智能体；先能在受控任务中完成实现、测试、trace 和复盘。

## Related Knowledge

[[Agent-Orchestration-and-State]], [[Enterprise-Integrations-and-Connectors]], [[Human-in-the-Loop-and-Agent-Guardrails]]

## Actual Evidence

尚无用户能力结论；完成 Practice 后复制 [[Evidence-Card]]，记录问题、行动、结果、失败和判断，并回链本 Skill 与目标 Role。

## Sources

### Official / normative

- https://www.anthropic.com/engineering/building-effective-agents

### Job evidence

- [[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]
- [[Salesforce-Forward-Deployed-Engineer-Supply-Chain-2026-08]]
- [[Zapier-Engineer-Applied-AI-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]

### Practice tutorial

- [[Claude-Code-n8n-Workflow]]

官方规范定义边界，岗位页决定优先级，教程只提供练习路径；三类证据不混写。
