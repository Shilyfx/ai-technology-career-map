---
type: role
role_family: application-engineering
sample_count: 14
status: developing
snapshot_date: 2026-08-31
created: 2026-08-24
updated: 2026-08-31
review_after: 2026-11-30
aliases:
  - LLM Application Engineer
  - Applied AI Engineer
  - AI Product Engineer
  - AI Agent Engineer
  - AI Workflow Engineer
---

# AI Application Engineer

## 主要使命

把模型能力嵌入真实工作流，交付可用、可评、可控并产生业务结果的 AI 产品。应用岗位的主问题是任务、接口、状态、权限和运营，不是单纯训练更大模型。

## 日常工作

用户任务与流程 discovery；Python 或 TypeScript/JavaScript 服务；LLM API 与 structured output；tool calling；workflow/agent orchestration；全栈 UX；数据库和企业集成；eval、trace、guardrail、成本与延迟。

## Sample Basis

14 个应用/Agent 样本：Notion、Salesforce、ServiceNow/Moveworks、Ramp、Glean、Zapier、Front、Atlassian 与上一批 frontier samples。详见 [[Job-Sample-Index]] 和 [[2026-08-31-Enterprise-Applied-AI-Job-Snapshot]]。本计数用于本 Vault 的定向学习，不是市场普查。

## Main Deliverables

可靠的用户 workflow、LLM/API/tool contracts、可恢复状态、权限和企业连接器、可重放 eval/trace、产品指标与上线回滚。

## Responsibility Clusters

任务 framing；LLM I/O 与 context；actions；workflow/state；integrations；eval/observability；HITL/guardrails；全栈交付。

## Skill Profile

| Skill | Required | Preferred | Responsibility | Sample N | Role Priority | Target Depth | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [[Python]] **或** [[TypeScript-JavaScript]] | yes (choose one) |  | service/full-stack code | 10+ | Core | implement | high | Batch A+B |
| [[HTTP-API]] | yes |  | API contract | 8+ | Core | implement | high | Batch A+B |
| [[Prompt-and-Context-Engineering]] | yes |  | context/task design | 7+ | Core | use→implement | high | Batch A+B |
| [[LLM-API-and-Structured-Outputs]] | yes |  | model I/O contract | 10 | Core | implement | high | Batch B |
| [[Tool-Calling-and-Action-Contracts]] | yes |  | safe actions | 12 | Core | implement | high | Batch B |
| [[Workflow-Automation-and-Business-Process-Design]] | yes |  | workflow delivery | 14 | Core | implement | high | Batch B |
| [[Agent-Orchestration-and-State]] | common |  | state/recovery | 7 | Common | implement | medium-high | Batch B |
| [[Agent-Evals-and-Trace-Debugging]] | yes |  | quality/ops loop | 10 | Core | implement | high | Batch B |
| [[Enterprise-Integrations-and-Connectors]] | common |  | production integration | 9 | Common | implement | high | Batch B |
| [[Human-in-the-Loop-and-Agent-Guardrails]] | common |  | approvals/risk | 8 | Common | implement | medium-high | Batch B |
| [[MCP-and-Agent-Interoperability]] |  | preferred | protocol adapters | 5 | Specialized | use→implement | medium | Batch B |
| [[RAG]] |  | preferred | grounded context | use case | Common | implement | medium | Batch A+B |

## Non-skill Gates

产品判断、需求澄清、隐私/权限、用户沟通、领域知识、生产 ownership 和 incident response。

## Seniority/Subtrack Differences

初级先交付一个 deterministic workflow 与测试；中级负责 tool/state/integration；高级负责平台边界、评测政策、成本/SLO 和跨团队结果。MCP、multi-agent、Computer Use 只在 subtrack 或项目证据支持时加深。

## Portfolio Evidence

作品 A：30+ 任务的结构化抽取/API；B：有 checkpoint、tool permissions、HITL 的 workflow；C：企业 connector + eval/trace + 成本/延迟和回滚报告。每个作品都要有失败样本与业务结果，不只展示 UI。

## Adjacent Roles

[[AI-Solutions-Architect-and-FDE]]、[[AI-Infrastructure-and-Inference-Engineer]]、[[AI-Product-Manager]]、[[AI-Safety-Evals-and-Governance]]。

## Source Limitations

样本偏中高级、企业 SaaS、US/APAC 和动态 ATS；不代表 junior、中国本地或 SMB 市场。受限页面保留在 Job Sample 的 `source_access`，不扩写不可见正文。

## Refresh

Applied AI Job Samples 每 30–60 天复查；稳定的软件工程基础按 180–365 天复查。

## Learning prerequisites

推荐顺序：[[Python]] **或** [[TypeScript-JavaScript]] → [[HTTP-API]] → [[Prompt-and-Context-Engineering]] + [[LLM-API-and-Structured-Outputs]] → [[Tool-Calling-and-Action-Contracts]] → [[Workflow-Automation-and-Business-Process-Design]] / [[Agent-Orchestration-and-State]] → [[Agent-Evals-and-Trace-Debugging]] → [[Enterprise-Integrations-and-Connectors]]。[[Data-Structures-and-Algorithms]] 是推荐基础而非硬门槛；[[RAG]]、[[MCP-and-Agent-Interoperability]] 和 [[Human-in-the-Loop-and-Agent-Guardrails]] 按项目进入。
