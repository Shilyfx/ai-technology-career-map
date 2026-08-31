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
  - "[[LLM-API-and-Structured-Outputs]]"
  - "[[Software-Design-and-Architecture]]"
  - "[[Security-Privacy-and-Access-Control]]"
related_concepts:
  - "[[Agent-Orchestration-and-State]]"
  - "[[MCP-and-Agent-Interoperability]]"
  - "[[Human-in-the-Loop-and-Agent-Guardrails]]"
sample_batch: enterprise-applied-ai-2026-08
---

# Tool Calling and Action Contracts

## 为什么岗位需要它

把模型意图变成有 schema、权限、幂等、结果语义和审计的动作。

## Role Demand

注册工具、校验参数、执行授权、处理超时/重试/幂等、回传结构化结果并记录 trace。

## Job Evidence

- [[Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08]]
- [[Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08]]
- [[ServiceNow-Senior-Staff-Agent-Development-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]

链接回每张 Job Sample 的 `Skill Extraction`；`explicit` 与 `inferred` 分开，样本不代表市场频率。

## 在岗位中怎么使用

注册工具、校验参数、执行授权、处理超时/重试/幂等、回传结构化结果并记录 trace。

## Role-specific Target Depth

- Application / FDE：implement；Agent Platform：implement→optimize；PM / Solutions：explain→use。
- 目标深度随交付责任变化，不是全局门槛。

## 前置 Skills

[[LLM-API-and-Structured-Outputs]], [[Software-Design-and-Architecture]], [[Security-Privacy-and-Access-Control]]

## 学习范围

定义、边界、接口契约、失败模式、权限/成本/延迟和可观测性；优先覆盖一个可交付流程。

## 核心知识

把模型意图变成有 schema、权限、幂等、结果语义和审计的动作。 重点掌握 schema、状态、重试、幂等、审计、回滚和业务结果之间的关系。

## Practice

实现查询→草稿两工具 workflow，把写入动作设为人工批准并注入重复/超时。

## Pass Evidence

完成 Practice 后，提交可重放的任务集、测试结果、trace、失败分类和一项修复前后对比。

## 常见失败

把 prompt 或单一框架当作系统边界；忽略权限、超时、幂等、回滚、失败切片和人工接管；只展示 happy path。

## 不需要深挖到什么程度

不必先研究模型训练内部、所有厂商 SDK 或复杂多智能体；先能在受控任务中完成实现、测试、trace 和复盘。

## Related Knowledge

[[Agent-Orchestration-and-State]], [[MCP-and-Agent-Interoperability]], [[Human-in-the-Loop-and-Agent-Guardrails]]

## Actual Evidence

尚无用户能力结论；完成 Practice 后复制 [[Evidence-Card]]，记录问题、行动、结果、失败和判断，并回链本 Skill 与目标 Role。

## Sources

### Official / normative

- https://modelcontextprotocol.io/specification/2026-07-28/server/tools
- https://developers.openai.com/api/reference/cli/resources/responses/methods/create

### Job evidence

- [[Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08]]
- [[Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08]]
- [[ServiceNow-Senior-Staff-Agent-Development-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]

### Practice tutorial

- [[Agent-Hooks-Guide]]

官方规范定义边界，岗位页决定优先级，教程只提供练习路径；三类证据不混写。
