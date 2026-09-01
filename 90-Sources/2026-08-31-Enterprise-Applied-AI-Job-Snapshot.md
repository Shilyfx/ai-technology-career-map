---
type: snapshot
page_kind: enterprise-applied-ai-job-snapshot
status: reference
stability: current
snapshot_date: 2026-08-31
created: 2026-08-31
updated: 2026-09-01
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

2026-09-01 对 22 个指定 URL 逐一重开并记录来源边界：Atlassian A1/A2、ServiceNow M1/M3/M4、Glean G1、Warp 为完整可读；Ashby（Notion/Ramp/Front/Zapier）为动态部分可读；Salesforce 已重定向至新官方域、只保留部分可复核摘要；A3、G2 已失效；M2 返回 404。2026-09-01 追加 metadata sweep：Warp=New York、Zapier=NAMER/EMEA Remote、ServiceNow M1=Bangalore、M4/M3=Mountain View。受限或历史样本保留 `source_access`、`source_status` 和审计状态，不把不可见正文写成当前明确要求。

## Company mix and role families

| Segment | Companies | Samples | Typical subtracks |
| --- | --- | ---: | --- |
| Enterprise SaaS / knowledge | Atlassian, Notion, Salesforce, ServiceNow/Moveworks, Glean | 15 | application, agent platform, FDE, architecture, PM |
| Fintech platform | Ramp | 3 | applied AI, enterprise product, frontend/HITL |
| Automation / developer platform | Zapier, Front, Warp | 4 | internal automation, GTM AI, FDE/integration |

Regions are intentionally mixed: Global/legal-entity dependent, Japan/APAC, Bangalore India/APAC, NAMER/EMEA Remote, New York/Mountain View US and US/Remote. Seniority is weighted to experienced, senior, staff and principal; junior and China-local coverage remain open gaps.

## Directional skill clusters

These are qualitative clusters from the selected sample set, not percentages or market frequency:

- **Extreme signal**：workflow / orchestration；integrations / API / connectors；
- **High signal**：evals / observability；business-process discovery / delivery；full-stack implementation；
- **High safety signal**：security、permissions、governance、privacy、HITL；
- **Medium-high**：state、async、recovery、tool contracts、structured outputs/schema；
- **Rising / specialized**：MCP；multi-agent / A2A；
- **Common by use case**：RAG、memory；不是所有 Agent 的统一前置。

## Evidence rebuild totals

| Evidence Type | Rows | Interpretation |
| --- | ---: | --- |
| `required` | 35 | 仅来自 Requirements/Qualifications 类段落；`Required One-of` 另行计数，不相加 |
| `preferred` | 26 | Preferred/Nice-to-have；永不升级为 required |
| `responsibility` | 65 | What you’ll do/Responsibilities/Role context；职责频率 ≠ 候选人必备技能频率 |
| `inferred-prerequisite` | 7 | 仅用于历史/动态来源的学习前置；不代表招聘门槛 |

`Alternative Group`（如 `language-1`、`areas-3-of-6`）是 one-of 或 at-least-N；Python、TypeScript、Go 等成员不能作为同时要求相加。`Source Fidelity` 只允许 `direct`、`close-paraphrase`、`inferred`；`inferred-prerequisite` 不得标为 direct。产品名（Rovo、Agentforce、Moveworks 等）保持在样本上下文，不升级为 Skill。

## Source Fidelity Audit Table

| Company | Role | Access | Audit Status | Direct Evidence Rows | Paraphrase Rows | Inferred Rows | Main Limit |
| --- | --- | --- | --- | ---: | ---: | ---: | --- |
| Atlassian | Senior Engineering Manager, Agentic AI Integrations | full | verified | 9 | 4 | 0 | none observed |
| Atlassian | Senior Principal Forward Deployed Engineer | full | verified | 5 | 4 | 0 | none observed |
| Atlassian | Principal Architecture, AI-native workflows | page-shell-only | historical | 0 | 0 | 2 | page shell or redirect error |
| Notion | Software Engineer, AI Workflows | dynamic-partial | partial | 2 | 1 | 0 | dynamic ATS/JS shell |
| Notion | Forward Deployed Engineer, GTM Japan | dynamic-partial | partial | 8 | 4 | 0 | dynamic ATS/JS shell |
| Notion | Forward Deployed Architect, Japan | dynamic-partial | partial | 4 | 1 | 0 | dynamic ATS/JS shell |
| Glean | Software Engineer, Agents | full | verified | 4 | 3 | 0 | none observed |
| Glean | Founding Forward Deployed Engineer | page-shell-only | historical | 0 | 0 | 2 | page shell or redirect error |
| Salesforce | Forward Deployed Engineer | partial | partial | 0 | 4 | 0 | redirected official page |
| Salesforce | Forward Deployed Engineer, Agentforce for Supply Chain | partial | partial | 0 | 3 | 0 | redirected official page |
| Salesforce | Success Architect, Agentforce Data Cloud | partial | partial | 0 | 3 | 0 | redirected official page |
| Salesforce | Product Manager, Agent Fabric | partial | partial | 0 | 4 | 0 | redirected official page |
| ServiceNow / Moveworks | AI Agent Engineer | full | verified | 7 | 4 | 0 | none observed |
| ServiceNow / Moveworks | Senior Staff Software Engineer, Agent Development | blocked | historical | 0 | 0 | 2 | URL unavailable |
| ServiceNow / Moveworks | Senior Staff Software Engineer, Agentic Systems | full | verified | 8 | 0 | 0 | none observed |
| ServiceNow / Moveworks | Staff Software Engineer, Agent Eval Platform | full | verified | 6 | 3 | 0 | none observed |
| Ramp | Applied AI Engineer | dynamic-partial | partial | 4 | 1 | 0 | dynamic ATS/JS shell |
| Ramp | Software Engineer, Enterprise Product | dynamic-partial | partial | 2 | 1 | 0 | dynamic ATS/JS shell |
| Ramp | Software Engineer, Frontend, Ramp Revenue | dynamic-partial | partial | 4 | 2 | 0 | dynamic ATS/JS shell |
| Zapier | Engineer, Applied AI | dynamic-partial | partial | 2 | 4 | 0 | dynamic ATS/JS shell |
| Front | AI Engineer, GTM / Operations | dynamic-partial | partial | 1 | 3 | 1 | dynamic ATS/JS shell |
| Warp | Forward Deployed Engineer | full | verified | 8 | 4 | 0 | none observed |

Required、Preferred、Responsibility、Inferred 的频数只描述本批证据行；它们不等同于市场比例或招聘概率。完整逐行计数见 [[Skill-Evidence-Matrix]]。

最终证据修正与矩阵冻结记录见 [[2026-09-01-Final-Evidence-Corrections-Matrix-Freeze-Report]]。

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
