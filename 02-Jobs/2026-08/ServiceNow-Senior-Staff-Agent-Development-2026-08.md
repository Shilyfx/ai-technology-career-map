---
type: job-sample
company: ServiceNow / Moveworks
role_title: Senior Staff Software Engineer, Agent Development
role_family: ai-application-engineering
seniority: staff
location: Not stated on page
region: US/Global
source_url: https://careers.servicenow.com/jobs/744000145302723/senior-staff-software-engineer-agent-development/
source_kind: official-job-posting
source_status: active
source_access: limited-http-403
sample_batch: enterprise-applied-ai-2026-08
company_segment: enterprise-saas
role_subtrack: product-application
snapshot_date: 2026-08-31
retrieved: 2026-08-31
status: developing
created: 2026-08-31
updated: 2026-08-31
review_after: 2026-10-15
related: []
---

# ServiceNow / Moveworks — Senior Staff Software Engineer, Agent Development

## Source Scope
官方职位 URL：[https://careers.servicenow.com/jobs/744000145302723/senior-staff-software-engineer-agent-development/](https://careers.servicenow.com/jobs/744000145302723/senior-staff-software-engineer-agent-development/)。2026-08-31 访问记录：`active` / `limited-http-403`。当前页面访问受限或动态渲染；低/中置信度线索不升级为高置信必需项。
本卡只保留短证据与学习映射，不复制完整 JD。

## Role Summary
页面返回 403；历史信号聚焦生产代理、多代理规划、记忆和恢复。

## Responsibilities
- Responsibilities: multi-agent planning, tool calling, memory and recovery
- Responsibilities: produce structured outputs in production agents
- Responsibilities: evaluate agent trajectories and failures

## Explicit Requirements
- 当前可复核要求有限；不要把职责或历史摘要当作 required。

## Preferred/Nice-to-have
- 未从当前来源确认 preferred 项。

## Skill Extraction
证据类型只允许 `required`、`preferred`、`responsibility`、`inferred-prerequisite`；`required`/`preferred` 来自官方资格段，`responsibility` 来自职责段，`inferred-prerequisite` 仅用于学习前置推断。Alternative Group 中的成员是 one-of，不同时计入要求。

| Raw Evidence | Skill | Evidence Type | Requirement Strength | Alternative Group | Depth Signal | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| Historical/limited signal: Python or Go backend development | [[Python]] | inferred-prerequisite | inferred | — | use | low |
| Historical/limited signal: distributed systems and async/concurrency | [[Agent-Orchestration-and-State]] | inferred-prerequisite | inferred | — | use | low |
| Responsibilities: multi-agent planning, tool calling, memory and recovery | [[Agent-Orchestration-and-State]] | responsibility | explicit | — | implement | low |
| Responsibilities: produce structured outputs in production agents | [[LLM-API-and-Structured-Outputs]] | responsibility | explicit | — | implement | low |
| Responsibilities: evaluate agent trajectories and failures | [[Agent-Evals-and-Trace-Debugging]] | responsibility | explicit | — | implement | low |
| Inferred prerequisite: Redis/DynamoDB/gRPC-style service integration | [[Enterprise-Integrations-and-Connectors]] | inferred-prerequisite | inferred | — | use | low |

## Non-skill Gates
年限、客户沟通、领域经验、地点、授权与合规语境保留在岗位判断中，不自动归一化为 Skill。

## Role Mapping
- Primary [[AI-Application-Engineer]]

## Limitations
当前页面访问受限或动态渲染；低/中置信度线索不升级为高置信必需项。

## Evidence Trace
### Evidence 1
Source Section: Historical summary (403)
Raw Evidence: Historical/limited signal: Python or Go backend development
Mapped Skill: [[Python]]
Evidence Type: inferred-prerequisite
Requirement Strength: inferred
Alternative Group: none
Depth Signal: use
Confidence: low
Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction
Notes: 短证据与映射保持一一对应；不把摘要复制成多条假证据。

### Evidence 2
Source Section: Historical summary (403)
Raw Evidence: Historical/limited signal: distributed systems and async/concurrency
Mapped Skill: [[Agent-Orchestration-and-State]]
Evidence Type: inferred-prerequisite
Requirement Strength: inferred
Alternative Group: none
Depth Signal: use
Confidence: low
Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction
Notes: 短证据与映射保持一一对应；不把摘要复制成多条假证据。

### Evidence 3
Source Section: Responsibilities
Raw Evidence: Responsibilities: multi-agent planning, tool calling, memory and recovery
Mapped Skill: [[Agent-Orchestration-and-State]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: implement
Confidence: low
Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction
Notes: 短证据与映射保持一一对应；不把摘要复制成多条假证据。

### Evidence 4
Source Section: Responsibilities
Raw Evidence: Responsibilities: produce structured outputs in production agents
Mapped Skill: [[LLM-API-and-Structured-Outputs]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: implement
Confidence: low
Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction
Notes: 短证据与映射保持一一对应；不把摘要复制成多条假证据。

### Evidence 5
Source Section: Responsibilities
Raw Evidence: Responsibilities: evaluate agent trajectories and failures
Mapped Skill: [[Agent-Evals-and-Trace-Debugging]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: implement
Confidence: low
Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction
Notes: 短证据与映射保持一一对应；不把摘要复制成多条假证据。

### Evidence 6
Source Section: Learning prerequisite inference
Raw Evidence: Inferred prerequisite: Redis/DynamoDB/gRPC-style service integration
Mapped Skill: [[Enterprise-Integrations-and-Connectors]]
Evidence Type: inferred-prerequisite
Requirement Strength: inferred
Alternative Group: none
Depth Signal: use
Confidence: low
Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction
Notes: 短证据与映射保持一一对应；不把摘要复制成多条假证据。
