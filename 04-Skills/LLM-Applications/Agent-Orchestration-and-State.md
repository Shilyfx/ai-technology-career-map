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
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[AI-Product-Manager]]"
prerequisites:
  - "[[Tool-Calling-and-Action-Contracts]]"
  - "[[Software-Design-and-Architecture]]"
  - "[[Databases-and-Data-Modeling]]"
related_concepts:
  - "[[Workflow-Automation-and-Business-Process-Design]]"
  - "[[Agent-Evals-and-Trace-Debugging]]"
  - "[[Human-in-the-Loop-and-Agent-Guardrails]]"
sample_batch: enterprise-applied-ai-2026-08
---

# Agent Orchestration and State

## 为什么岗位需要它

负责步骤、状态、终止和恢复，让 Agent 成为可运营的任务系统。

## Role Demand

用显式状态机、事件和 checkpoint 处理并发、取消、超时、恢复与人工 handoff；先 deterministic workflow。

## Job Evidence

- [[Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08]]
- [[Notion-Software-Engineer-AI-Workflows-2026-08]]
- [[ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08]]
- [[Glean-Software-Engineer-Agents-2026-08]]

链接回每张 Job Sample 的 `Skill Extraction`；`explicit` 与 `inferred` 分开，样本不代表市场频率。

## 在岗位中怎么使用

用显式状态机、事件和 checkpoint 处理并发、取消、超时、恢复与人工 handoff；先 deterministic workflow。

## Role-specific Target Depth

- Application / FDE：implement；Agent Platform：implement→optimize；PM / Solutions：explain→use。
- 目标深度随交付责任变化，不是全局门槛。

## 前置 Skills

[[Tool-Calling-and-Action-Contracts]], [[Software-Design-and-Architecture]], [[Databases-and-Data-Modeling]]

## 学习范围

定义、边界、接口契约、失败模式、权限/成本/延迟和可观测性；优先覆盖一个可交付流程。

## 核心知识

负责步骤、状态、终止和恢复，让 Agent 成为可运营的任务系统。 重点掌握 schema、状态、重试、幂等、审计、回滚和业务结果之间的关系。

## Practice

实现可暂停的审批 workflow：状态持久化、重启恢复、人工批准、最大步骤和预算。

## Pass Evidence

完成 Practice 后，提交可重放的任务集、测试结果、trace、失败分类和一项修复前后对比。

## 常见失败

把 prompt 或单一框架当作系统边界；忽略权限、超时、幂等、回滚、失败切片和人工接管；只展示 happy path。

## 不需要深挖到什么程度

不必先研究模型训练内部、所有厂商 SDK 或复杂多智能体；先能在受控任务中完成实现、测试、trace 和复盘。

## Related Knowledge

[[Workflow-Automation-and-Business-Process-Design]], [[Agent-Evals-and-Trace-Debugging]], [[Human-in-the-Loop-and-Agent-Guardrails]]

## Actual Evidence

尚无用户能力结论；完成 Practice 后复制 [[Evidence-Card]]，记录问题、行动、结果、失败和判断，并回链本 Skill 与目标 Role。

## Sources

### Official / normative

- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/agents/
- https://openai.github.io/openai-agents-python/running_agents/
- https://openai.github.io/openai-agents-python/multi_agent/
- https://openai.github.io/openai-agents-python/handoffs/

### Job evidence

- [[Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08]]
- [[Notion-Software-Engineer-AI-Workflows-2026-08]]
- [[ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08]]
- [[Glean-Software-Engineer-Agents-2026-08]]

### Practice tutorial

- [[Obsidian-CLI-AI-Agent-Automation]]

官方规范定义边界，岗位页决定优先级，教程只提供练习路径；三类证据不混写。
