---
type: skill
skill_category: Evals Safety
status: developing
stability: current
created: 2026-08-31
updated: 2026-08-31
review_after: 2026-11-30
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[AI-Safety-Evals-and-Governance]]"
  - "[[AI-Product-Manager]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
prerequisites:
  - "[[Statistics-and-Experiment-Design]]"
  - "[[LLM-API-and-Structured-Outputs]]"
  - "[[Observability]]"
related_concepts:
  - "[[Human-in-the-Loop-and-Agent-Guardrails]]"
  - "[[Agent-Orchestration-and-State]]"
sample_batch: enterprise-applied-ai-2026-08
---

# Agent Evals and Trace Debugging

## 为什么岗位需要它

让团队知道 Agent 是否完成任务、哪里失败、是否退化，以及修复应落在哪里。

## Role Demand

建立任务集、轨迹 schema、规则/模型/人工评分、切片、trace 查询、回归门和成本/延迟诊断。

## Job Evidence

- [[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]]
- [[ServiceNow-Staff-Agent-Eval-Platform-2026-08]]
- [[Glean-Software-Engineer-Agents-2026-08]]
- [[Zapier-Engineer-Applied-AI-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]

链接回每张 Job Sample 的 `Skill Extraction`；`explicit` 与 `inferred` 分开，样本不代表市场频率。

## 在岗位中怎么使用

建立任务集、轨迹 schema、规则/模型/人工评分、切片、trace 查询、回归门和成本/延迟诊断。

## Role-specific Target Depth

- Application / FDE：implement；Agent Platform：implement→optimize；PM / Solutions：explain→use。
- 目标深度随交付责任变化，不是全局门槛。

## 前置 Skills

[[Statistics-and-Experiment-Design]], [[LLM-API-and-Structured-Outputs]], [[Observability]]

## 学习范围

定义、边界、接口契约、失败模式、权限/成本/延迟和可观测性；优先覆盖一个可交付流程。

## 核心知识

让团队知道 Agent 是否完成任务、哪里失败、是否退化，以及修复应落在哪里。 重点掌握 schema、状态、重试、幂等、审计、回滚和业务结果之间的关系。

## Practice

为 30 个任务 + 5 个对抗任务实现 runner，记录每步 tool/model/latency/cost 并回归修复。

## Pass Evidence

完成 Practice 后，提交可重放的任务集、测试结果、trace、失败分类和一项修复前后对比。

## 常见失败

把 prompt 或单一框架当作系统边界；忽略权限、超时、幂等、回滚、失败切片和人工接管；只展示 happy path。

## 不需要深挖到什么程度

不必先研究模型训练内部、所有厂商 SDK 或复杂多智能体；先能在受控任务中完成实现、测试、trace 和复盘。

## Related Knowledge

[[Human-in-the-Loop-and-Agent-Guardrails]], [[Agent-Orchestration-and-State]]

## Actual Evidence

尚无用户能力结论；完成 Practice 后复制 [[Evidence-Card]]，记录问题、行动、结果、失败和判断，并回链本 Skill 与目标 Role。

## Sources

### Official / normative

- https://openai.github.io/openai-agents-python/testing/
- https://openai.github.io/openai-agents-python/zh/tracing/
- https://openai.github.io/openai-agents-python/running_agents/

### Job evidence

- [[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]]
- [[ServiceNow-Staff-Agent-Eval-Platform-2026-08]]
- [[Glean-Software-Engineer-Agents-2026-08]]
- [[Zapier-Engineer-Applied-AI-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]

### Practice tutorial

- [[Agent-Hooks-Guide]]

官方规范定义边界，岗位页决定优先级，教程只提供练习路径；三类证据不混写。
