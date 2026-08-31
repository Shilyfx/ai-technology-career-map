---
type: role
role_family: application-engineering
sample_count: 14
status: developing
snapshot_date: 2026-08-31
created: 2026-08-24
updated: 2026-09-01
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

14 curated samples (11 Batch B application/agent-product cards + 3 Batch A API/application cards); employers span Atlassian, Notion, Glean, Salesforce, ServiceNow/Moveworks, Ramp, Zapier, Front and OpenAI. Batch B locations cover Global/US/APAC; seniority is mostly senior/staff, with product-application and agent-platform subtracks.

## Main Deliverables

可靠的用户 workflow、LLM/API/tool contracts、可恢复状态、权限和企业连接器、可重放 eval/trace、产品指标与上线回滚。

## Responsibility Clusters

任务 framing；LLM I/O 与 context；actions；workflow/state；integrations；eval/observability；HITL/guardrails；全栈交付。

## Skill Profile

| Skill | Required N | Preferred N | Responsibility N | Inferred N | Sample N | Priority | Target Depth | Confidence |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| [[TypeScript-JavaScript]] | 4 | 0 | 0 | 0 | 4 | Core | use→implement | high/medium |
| [[Python]] | 4 | 0 | 0 | 2 | 6 | Core | use→implement | low/medium |
| [[LLM-API-and-Structured-Outputs]] | 1 | 0 | 2 | 0 | 3 | Core | use→implement | high/medium |
| [[Tool-Calling-and-Action-Contracts]] | 0 | 0 | 0 | 0 | 0 | Common | explain/use | context |
| [[Agent-Orchestration-and-State]] | 1 | 1 | 7 | 0 | 7 | Common | explain/use | high/medium |
| [[Workflow-Automation-and-Business-Process-Design]] | 1 | 1 | 3 | 1 | 5 | Common | explain/use | low/medium |
| [[MCP-and-Agent-Interoperability]] | 0 | 1 | 3 | 0 | 3 | Specialized | use→implement | high/medium |
| [[Enterprise-Integrations-and-Connectors]] | 0 | 2 | 2 | 0 | 3 | Common | explain/use | high/medium |
| [[Agent-Evals-and-Trace-Debugging]] | 0 | 2 | 1 | 0 | 3 | Common | explain/use | high/medium |
| [[Human-in-the-Loop-and-Agent-Guardrails]] | 0 | 1 | 2 | 1 | 3 | Common | explain/use | low/medium |

Evidence strength is based on Batch B row classifications; `responsibility` and `preferred` are not counted as required.
## Non-skill Gates

产品判断、需求澄清、隐私/权限、用户沟通、领域知识、生产 ownership 和 incident response。

## Seniority/Subtrack Differences

初级先交付一个 deterministic workflow 与测试；中级负责 tool/state/integration；高级负责平台边界、评测政策、成本/SLO 和跨团队结果。MCP、multi-agent、Computer Use 只在 subtrack 或项目证据支持时加深。

## Portfolio Evidence

作品 A：30+ 任务的结构化抽取/API；B：有 checkpoint、tool permissions、HITL 的 workflow；C：企业 connector + eval/trace + 成本/延迟和回滚报告。每个作品都要有失败样本与业务结果，不只展示 UI。

## Adjacent Roles

[[AI-Solutions-Architect-and-FDE]]、[[AI-Infrastructure-and-Inference-Engineer]]、[[AI-Product-Manager]]、[[AI-Safety-Evals-and-Governance]]。

## Source Limitations

样本偏中高级、企业 SaaS、US/APAC 和动态 ATS；不代表 junior、中国本地或 SMB 市场。Source Fidelity 审计将完整、动态、重定向和历史来源分开，受限页面保留在 Job Sample 的 `source_access`，不扩写不可见正文。

## Refresh

Applied AI Job Samples 每 30–60 天复查；稳定的软件工程基础按 180–365 天复查。

## Learning prerequisites

推荐顺序：[[Python]] **或** [[TypeScript-JavaScript]] → [[HTTP-API]] → [[Prompt-and-Context-Engineering]] + [[LLM-API-and-Structured-Outputs]]。[[Workflow-Automation-and-Business-Process-Design]] 可并行进入；明确需要模型动作时再学 [[Tool-Calling-and-Action-Contracts]] → [[Agent-Orchestration-and-State]] → [[Agent-Evals-and-Trace-Debugging]]。[[Enterprise-Integrations-and-Connectors]] 是生产分支，不是所有 Tool Calling 的硬前置；[[RAG]]、[[MCP-and-Agent-Interoperability]] 和 [[Human-in-the-Loop-and-Agent-Guardrails]] 按项目进入。[[Data-Structures-and-Algorithms]] 与 [[Software-Design-and-Architecture]] 是推荐基础而非硬门槛。
