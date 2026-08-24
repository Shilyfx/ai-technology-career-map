---
type: role
role_family: application-engineering
sample_count: 5
status: developing
snapshot_date: 2026-08-24
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
aliases:
  - LLM Application Engineer
  - AI Product Engineer
---

# AI Application Engineer

## 主要使命

把模型能力嵌入真实工作流，交付用户可用、可评、可控的 AI 产品。这个岗位通常比“训练更大模型”更关注任务定义、context、tool、全栈系统和用户反馈。

## 日常工作

- 快速原型与用户任务分析；
- API/SDK、structured output、RAG、tool use、Agent workflow；
- 后端/前端、认证、数据库、队列与集成；
- eval、trace、guardrail、成本与延迟；
- 与产品、设计、领域专家和安全团队迭代。

## 技能重点

**主深度**：Python/TypeScript、API、全栈或后端、RAG/Agent、eval、产品判断。

**理解层**：ML/LLM 原理、embedding、token/context、模型选择、fine-tuning 边界。

## 作品证据

一个“有任务集而不只是 UI”的项目：

- 30+ 真实任务；
- 来源与权限；
- 工具错误、模型错误、产品错误分开；
- trace、回归、预算、人工审批；
- 用户结果和失败案例。

## 常见误区

- 把框架教程当产品；
- 每个问题都上 Agent；
- 只调 prompt，不做 eval；
- 忽略普通软件工程、权限和数据；
- demo 成功一次就声称生产可用。

## 当前信号

OpenAI 的 API Agents PM 样本强调 SDK/API、开发者体验、可靠性和安全；AI Index 2026 也显示岗位技能从聊天工具词汇转向 agentic systems、workflow 与规模化执行。详见 [[2026-08-AI-Job-Market-Snapshot]]。

## Sample Basis

5 samples: OpenAI API Agents/SDK, Anthropic Computer Use, and Apple NLU/LLM; 4 employers are not implied by this role count.

## Main Deliverables

Reliable user workflow, API/tool integration, evals, permissions, latency and cost.

## Responsibility Clusters

Task framing; context/RAG; tool workflow; product integration; eval/observability.

## Skill Profile

| Skill | Required | Preferred | Responsibility | Sample N | Role Priority | Target Depth | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [[Python]] | yes |  | service and workflow code | 4 | Core | implement | high | Job Samples |
| [[HTTP-API]] | yes |  | integration contract | 3 | Core | implement | high | Job Samples |
| [[RAG]] |  | yes | grounded context | 2 | Common | implement | medium | Job Samples |
| [[Tool-Calling-Agent-Workflow]] | yes |  | agent actions | 3 | Core | implement | high | Job Samples |
| [[LLM-Evals]] | yes |  | quality loop | 3 | Core | use | medium | Job Samples |

## Non-skill Gates

Product judgment, privacy, permissions, user empathy and ownership of production incidents.

## Seniority/Subtrack Differences

Entry-level focuses on one workflow and tests; senior tracks own architecture, eval policy and reliability.

## Portfolio Evidence

30+ task set, API contract, failure taxonomy, trace, cost/latency report and rollback plan.

## Adjacent Roles

[[ML-and-AI-Engineer]]、[[AI-Product-Manager]]、[[AI-Solutions-Architect-and-FDE]]。

## Source Limitations

Sample is biased toward frontier-company, senior and US/Europe postings; validate local roles separately.

## Refresh

Refresh Job Samples every 30–60 days; revisit this profile after new family coverage.
