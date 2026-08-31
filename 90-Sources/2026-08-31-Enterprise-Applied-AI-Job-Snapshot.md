---
type: snapshot
page_kind: enterprise-applied-ai-job-snapshot
status: reference
stability: current
snapshot_date: 2026-08-31
created: 2026-08-31
updated: 2026-08-31
review_after: 2026-10-15
sample_batch: enterprise-applied-ai-2026-08
related:
  - "[[Job-Sample-Index]]"
  - "[[Role-Skill-Matrix]]"
  - "[[AI-Agents-and-Tool-Use]]"
---

# Enterprise Applied AI / Agentic Engineering Job Snapshot — 2026-08-31

## Research question

企业 Applied AI、Agentic Engineering、FDE、Agent Platform 和 AI 产品岗位，要求学习者先掌握哪些可复用能力？

## Scope

本批是附件预审的 Priority A 样本：Atlassian、Notion、Salesforce、ServiceNow/Moveworks、Ramp、Glean、Zapier、Front、Warp，共 22 个指定官方 URL。它是定向证据层，不是开放市场普查；不替代上一批 frontier/model-builder 样本。

## Verification boundary

2026-08-31 对指定 URL 做了可访问性核对：多数 Ashby/Greenhouse/Atlassian/Salesforce URL 可解析；ServiceNow/Moveworks 返回 HTTP 403，Front 是动态 ATS，Atlassian 25246 只返回招聘页壳，Glean 4659412005 重定向错误页。受限或过期样本保留 `source_access`、`source_status` 和低置信度，不把不可见正文写成当前明确要求。

## Company mix and role families

| Segment | Companies | Samples | Typical subtracks |
| --- | --- | ---: | --- |
| Enterprise SaaS / knowledge | Atlassian, Notion, Salesforce, ServiceNow/Moveworks, Glean | 15 | application, agent platform, FDE, architecture, PM |
| Fintech platform | Ramp | 3 | applied AI, enterprise product, frontend/HITL |
| Automation / developer platform | Zapier, Front, Warp | 4 | internal automation, GTM AI, FDE/integration |

Regions are intentionally mixed: Global/legal-entity dependent, APAC/Japan, US/Global and US/Remote. Seniority is weighted to experienced, senior, staff and principal; junior and China-local coverage remain open gaps.

## Directional skill clusters

These are qualitative clusters from the selected sample set, not percentages or market frequency:

- **Extreme signal**：workflow / orchestration；integrations / API / connectors；
- **High signal**：evals / observability；business-process discovery / delivery；full-stack implementation；
- **High safety signal**：security、permissions、governance、privacy、HITL；
- **Medium-high**：state、async、recovery、tool contracts、structured outputs/schema；
- **Rising / specialized**：MCP；multi-agent / A2A；
- **Common by use case**：RAG、memory；不是所有 Agent 的统一前置。

## Explicit vs inferred

`explicit` 只表示页面或附件预审中直接出现的责任/要求；`inferred` 是为了建立学习前置或邻接 Skill 的解释性连接，不加入 required 频次。产品名（Rovo、Agentforce、Moveworks 等）保持在样本上下文，不升级为 Skill。

## Learning implications

应用路径应为：`Python OR TypeScript/JavaScript → HTTP/JSON/API → Prompt/Context + LLM API/Structured Outputs → Tool Calling → Workflow/Agent Orchestration → Agent Evals/Trace → Production Integration`。DSA 是推荐基础，不是应用岗位的硬门槛；RAG、MCP、多智能体和 Computer Use 按目标 Role 选择。

## Sample links

### Atlassian

[[Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08]] · [[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]] · [[Atlassian-Principal-Architecture-AI-Native-Workflows-2026-08]]

### Notion

[[Notion-Software-Engineer-AI-Workflows-2026-08]] · [[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]] · [[Notion-Forward-Deployed-Architect-Japan-2026-08]]

### Salesforce

[[Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08]] · [[Salesforce-Success-Architect-Agentforce-2026-08]] · [[Salesforce-Forward-Deployed-Engineer-Supply-Chain-2026-08]] · [[Salesforce-Product-Manager-Agent-Fabric-2026-08]]

### ServiceNow / Moveworks

[[ServiceNow-AI-Agent-Engineer-Moveworks-2026-08]] · [[ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08]] · [[ServiceNow-Staff-Agent-Eval-Platform-2026-08]] · [[ServiceNow-Senior-Staff-Agent-Development-2026-08]]

### Ramp

[[Ramp-Applied-AI-Engineer-2026-08]] · [[Ramp-Software-Engineer-Enterprise-Product-2026-08]] · [[Ramp-Software-Engineer-Frontend-Revenue-2026-08]]

### Glean / Zapier / Front / Warp

[[Glean-Software-Engineer-Agents-2026-08]] · [[Glean-Founding-Forward-Deployed-Engineer-2026-08]] · [[Zapier-Engineer-Applied-AI-2026-08]] · [[Front-AI-Engineer-GTM-Operations-2026-08]] · [[Warp-Forward-Deployed-Engineer-2026-08]]

## Limitations and next batch

No claim of global frequency, compensation, hiring probability or universal prerequisite. The batch is senior-heavy and enterprise-SaaS-heavy; next refresh should add junior/early-career, China/APAC local employers, SMB SaaS and more non-US FDE samples. Recheck active pages within 30–60 days.
