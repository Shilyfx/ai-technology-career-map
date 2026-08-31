---
type: job-sample
company: Atlassian
role_title: Senior Engineering Manager, Agentic AI Integrations
role_family: ai-application-engineering
seniority: senior
location: Global (legal-entity dependent)
region: Global
source_url: https://www.atlassian.com/company/careers/details/26357
source_kind: official-job-posting
source_status: active
source_access: full
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

# Atlassian — Senior Engineering Manager, Agentic AI Integrations

## Source Scope
官方职位 URL：[https://www.atlassian.com/company/careers/details/26357](https://www.atlassian.com/company/careers/details/26357)。2026-08-31 访问记录：`active` / `full`。当前官方页面可访问；短证据按 Requirements/Preferred/Responsibilities 原段落分类。
本卡只保留短证据与学习映射，不复制完整 JD。

## Role Summary
管理企业 Agentic AI 集成，重点是多代理基础组件、互操作协议与可观测可靠性。

## Responsibilities
- Responsibilities: foundational components for multi-agent systems
- Responsibilities: adopt MCP/A2A and connect enterprise agents
- Responsibilities: reliability, cost and latency for a 4-9s service

## Explicit Requirements
- Requirements: Python, TypeScript, or Go
- Requirements: Python, TypeScript, or Go

## Preferred/Nice-to-have
- Preferred: observability, vector databases and secure model communication
- Preferred: MCP architecture and A2A protocol familiarity

## Skill Extraction
证据类型只允许 `required`、`preferred`、`responsibility`、`inferred-prerequisite`；`required`/`preferred` 来自官方资格段，`responsibility` 来自职责段，`inferred-prerequisite` 仅用于学习前置推断。Alternative Group 中的成员是 one-of，不同时计入要求。

| Raw Evidence | Skill | Evidence Type | Requirement Strength | Alternative Group | Depth Signal | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| Requirements: Python, TypeScript, or Go | [[Python]] | required | explicit | language-1 | implement | high |
| Requirements: Python, TypeScript, or Go | [[TypeScript-JavaScript]] | required | explicit | language-1 | implement | high |
| Responsibilities: foundational components for multi-agent systems | [[Agent-Orchestration-and-State]] | responsibility | explicit | — | implement | high |
| Responsibilities: adopt MCP/A2A and connect enterprise agents | [[MCP-and-Agent-Interoperability]] | responsibility | explicit | — | implement | high |
| Responsibilities: reliability, cost and latency for a 4-9s service | [[Enterprise-Integrations-and-Connectors]] | responsibility | explicit | — | implement | high |
| Preferred: observability, vector databases and secure model communication | [[Agent-Evals-and-Trace-Debugging]] | preferred | explicit | — | use | high |
| Preferred: MCP architecture and A2A protocol familiarity | [[Tool-Calling-and-Action-Contracts]] | preferred | explicit | — | use | high |

## Non-skill Gates
年限、客户沟通、领域经验、地点、授权与合规语境保留在岗位判断中，不自动归一化为 Skill。

## Role Mapping
- Primary [[AI-Application-Engineer]]

## Limitations
当前官方页面可访问；短证据按 Requirements/Preferred/Responsibilities 原段落分类。

## Evidence Trace
### Evidence 1
Source Section: Requirements
Raw Evidence: Requirements: Python, TypeScript, or Go
Mapped Skill: [[Python]]
Evidence Type: required
Requirement Strength: explicit
Alternative Group: language-1
Depth Signal: implement
Confidence: high
Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction
Notes: one-of language alternative; do not count all three

### Evidence 2
Source Section: Requirements
Raw Evidence: Requirements: Python, TypeScript, or Go
Mapped Skill: [[TypeScript-JavaScript]]
Evidence Type: required
Requirement Strength: explicit
Alternative Group: language-1
Depth Signal: implement
Confidence: high
Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction
Notes: one-of language alternative; do not count all three

### Evidence 3
Source Section: Responsibilities
Raw Evidence: Responsibilities: foundational components for multi-agent systems
Mapped Skill: [[Agent-Orchestration-and-State]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: implement
Confidence: high
Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction
Notes: 短证据与映射保持一一对应；不把摘要复制成多条假证据。

### Evidence 4
Source Section: Responsibilities
Raw Evidence: Responsibilities: adopt MCP/A2A and connect enterprise agents
Mapped Skill: [[MCP-and-Agent-Interoperability]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: implement
Confidence: high
Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction
Notes: 短证据与映射保持一一对应；不把摘要复制成多条假证据。

### Evidence 5
Source Section: Responsibilities
Raw Evidence: Responsibilities: reliability, cost and latency for a 4-9s service
Mapped Skill: [[Enterprise-Integrations-and-Connectors]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: implement
Confidence: high
Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction
Notes: 短证据与映射保持一一对应；不把摘要复制成多条假证据。

### Evidence 6
Source Section: Preferred
Raw Evidence: Preferred: observability, vector databases and secure model communication
Mapped Skill: [[Agent-Evals-and-Trace-Debugging]]
Evidence Type: preferred
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: high
Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction
Notes: preferred signal, not a hard gate

### Evidence 7
Source Section: Preferred
Raw Evidence: Preferred: MCP architecture and A2A protocol familiarity
Mapped Skill: [[Tool-Calling-and-Action-Contracts]]
Evidence Type: preferred
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: high
Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction
Notes: tool contracts are a related foundation
