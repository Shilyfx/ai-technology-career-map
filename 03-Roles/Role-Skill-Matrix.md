---
type: matrix
status: reference
snapshot_date: 2026-08-31
created: 2026-08-24
updated: 2026-08-31
review_after: 2026-11-30
related:
  - "[[Role-Map]]"
  - "[[Job-Sample-Index]]"
  - "[[Skill-Index]]"
  - "[[Skill-Evidence-Matrix]]"
---

# Role–Skill Matrix

> H/M/L 是基于 Role Profile 和 Job Sample 的编辑性总结；原始要求、explicit/inferred 和访问限制必须回到具体 Job Sample。本表按 Applied AI 交付边界重排，不把 RAG 或多智能体设为通用门槛。

| Role | Language / SW | LLM I/O & Context | Agent / Workflow | Integration / MCP | Evals / Ops | Model / Training | Infra | Delivery |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Research Scientist | H | M | L–M | L | M–H | H | M | M |
| Research Engineer | H | M | M | L | H | H | H | M |
| ML / AI Engineer | H | M | M | M | H | H | M | M |
| AI Application Engineer | H | H | H | H | H | M | M | H |
| Agent Runtime / Agent Platform | H | H | H | H | H | M | H | M |
| AI Solutions Architect / FDE | M | H | H | H | H | L–M | M–H | H |
| AI Product Manager | M | H | H | M–H | H | M | L–M | H |
| Safety / Evals / Governance | M | M | M | M | H | M–H | M | H |
| Data / AI Engineer | H | M | M | H | H | M | M | M |

## Evidence-count view

`Evidence Count` 写成 `explicit / inferred`，统计不同 Job Sample 的 `Skill Extraction` 行，不是关键词出现次数；inferred 不计入 required frequency。Applied 批次受限或过期页面仍保留为低置信度上下文。

| Skill | Main roles | Priority | Evidence Count | Confidence |
| --- | --- | --- | --- | --- |
| [[Python]] | Application / ML / Infra | Core | 14 / 4 | High |
| [[TypeScript-JavaScript]] | Application / FDE / Platform | Core option | 7 / 6 | High |
| [[HTTP-API]] | Application / FDE / PM | Core | 10 / 2 | High |
| [[LLM-API-and-Structured-Outputs]] | Application / FDE / PM | Core | 9 / 8 | High |
| [[Tool-Calling-and-Action-Contracts]] | Application / FDE / Platform | Core | 10 / 5 | High |
| [[Agent-Orchestration-and-State]] | Application / Platform / FDE | Core | 7 / 4 | High |
| [[Workflow-Automation-and-Business-Process-Design]] | Application / FDE / PM | Core | 12 / 4 | High |
| [[Enterprise-Integrations-and-Connectors]] | FDE / Application / PM | Core | 11 / 5 | High |
| [[MCP-and-Agent-Interoperability]] | Platform / FDE / Application | Specialized | 7 / 4 | Medium-high |
| [[Agent-Evals-and-Trace-Debugging]] | Application / Platform / Safety | Core | 10 / 6 | High |
| [[Human-in-the-Loop-and-Agent-Guardrails]] | Application / FDE / Safety / PM | Core | 8 / 7 | High |
| [[RAG]] | Application / FDE | Common by use case | 1 / 1 | Medium |
| [[Model-Serving]] | Infra / FDE | Core | 6 / 3 | High |
| [[Observability]] | Infra / Application | Common | 4 / 4 | High |
| [[LLM-Evals]] | Evals / Application | Core | 7 / 2 | High |

## Interpretation

先用目标 Role 的 Skill Profile 决定深度，再沿 [[Role-Skill-Paths]] 排序。[[Data-Structures-and-Algorithms]] 是多数工程方向的推荐基础，但不是 AI Application 的 hard block；[[RAG]] 是并行能力；MCP、multi-agent/A2A、Computer Use 由具体职责决定。

学习前置层见 [[Prerequisite-Foundation-Map]]。标记 `evidence_mode: prerequisite-synthesis` 的页面不增加 Job Sample explicit 频次。
