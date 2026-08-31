---
type: skill
skill_category: LLM-Applications
status: developing
stability: emerging
created: 2026-08-31
updated: 2026-09-01
review_after: 2026-10-31
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
prerequisites:
  - "[[LLM-API-and-Structured-Outputs]]"
  - "[[Tool-Calling-and-Action-Contracts]]"
recommended_foundations:
  - "[[Software-Design-and-Architecture]]"
related_concepts:
  - "[[Workflow-Automation-and-Business-Process-Design]]"
  - "[[Agent-Evals-and-Trace-Debugging]]"
sample_batch: enterprise-applied-ai-2026-08
---

# Agent Orchestration 与 State

## Skill Boundary

本卡关注 workflow 与 agent 的执行状态：loop、plan/act/observe、确定性/动态分支、stop/max steps、session/checkpoint/resume、长任务取消、恢复、partial completion、人工暂停/handoff、manager 与 tool-as-agent。默认 single agent first。

## 为什么岗位需要它

Notion、Glean、Salesforce 和 ServiceNow 的证据把代理从 demo 推到长会话生产系统；可靠性来自显式状态和恢复，而不是多代理数量。

## Role Demand

应用工程负责状态机与会话存储；平台工程负责并发、取消、租约与观测；FDE 需要将客户审批、handoff 和部分完成解释清楚。

## Job Evidence

[[Notion-Software-Engineer-AI-Workflows-2026-08]]、[[Glean-Software-Engineer-Agents-2026-08]] 的职责提到 async/recurring agent；[[ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08]] 现为完整来源，直接给出 state machine、checkpoint、resume、cancellation 与 tool invocation 证据。

## 前置 Skills

硬前置是 [[LLM-API-and-Structured-Outputs]] 与 [[Tool-Calling-and-Action-Contracts]]；推荐 [[Software-Design-and-Architecture]]。RAG 是并行能力，不是 Agent 硬依赖。

## 学习范围

workflow/agent 边界、plan/act/observe loop、状态 schema、确定性 branch 与模型 branch、终止条件/max steps、session id、checkpoint、resume、cancel、retry/recovery、partial result、human pause/handoff、single vs multi-agent。

## 核心知识

- 用状态转移图说明每一步输入、输出、owner 和副作用；状态必须可序列化、版本化。
- stop 条件同时包括成功、不可恢复错误、预算/步数上限和人工接管。
- 多代理只有在权限、上下文或并行性有清楚收益时才引入；否则增加协调和评估面。

## Practice

实现一个单代理订单异常流程：plan → tool call → observe → human approval → resume；支持 checkpoint、取消、超时、一次 retry、partial completion 和 handoff。再用一个确定性分支对照动态分支。

## Pass Evidence

提供状态图、可重放 session、checkpoint/resume 测试、max-step/stop 断言、取消与恢复 trace、人工暂停和 handoff 记录；证明重复 resume 不重复写入。

## 常见失败

无限 agent loop；把历史消息当状态；checkpoint 不含 schema version；取消后仍写副作用；多代理只是 prompt 分工；失败后丢失 partial completion。

## 不需要深挖到什么程度

不要求先实现分布式 actor 或多代理框架；单代理状态契约通过后再按证据增加并行 worker。

## Related Knowledge

[[Tool-Calling-and-Action-Contracts]]、[[Workflow-Automation-and-Business-Process-Design]]、[[Agent-Evals-and-Trace-Debugging]]

## Practice Boundary

通过线是可恢复状态机，不是“会调用一个 agent SDK”。

## Actual Evidence

用 [[Evidence-Card]]记录一次 cancel/resume 与一次 partial completion 修复。

## Sources

### Official / normative

- https://www.anthropic.com/engineering/building-effective-agents

### Job evidence

- [[Notion-Software-Engineer-AI-Workflows-2026-08]]
- [[Glean-Software-Engineer-Agents-2026-08]]
- [[ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08]]
