---
type: job-sample
company: Ramp
role_title: Software Engineer, Frontend, Ramp Revenue
role_family: ai-application-engineering
seniority: experienced
location: Not stated on page
region: US
source_url: https://jobs.ashbyhq.com/ramp/1540a41f-d88f-4c89-9b08-5b9fade1ee81
source_kind: official-job-posting
source_status: active
source_access: dynamic-partial
sample_batch: enterprise-applied-ai-2026-08
company_segment: fintech-platform
role_subtrack: product-application
snapshot_date: 2026-08-31
retrieved: 2026-09-01
status: developing
created: 2026-08-31
updated: 2026-09-01
review_after: 2026-10-15
related: []
evidence_audit_status: partial
---

# Ramp — Software Engineer, Frontend, Ramp Revenue

## Source Scope
官方职位 URL：[https://jobs.ashbyhq.com/ramp/1540a41f-d88f-4c89-9b08-5b9fade1ee81](https://jobs.ashbyhq.com/ramp/1540a41f-d88f-4c89-9b08-5b9fade1ee81)。审计日期：`2026-09-01`；状态：`active` / `source_access: dynamic-partial` / `evidence_audit_status: partial`。页面需动态渲染、重定向或部分可读；仅保留可复核的中/低置信事实。
每条证据只保留一个可回溯事实；未适配当前 Skill 的信号不强行归类。

## Role Summary
本卡以官方职位页面为证据边界；请优先阅读下方来源段落与 Evidence Trace。

## Responsibilities
- Shape APIs, workflows, and data contracts behind product experiences
- Design human-in-the-loop workflows with approvals and execution status
- Interfaces for asynchronous systems with partial results, errors, retries, and user intervention

## Explicit Requirements
- Deep frontend expertise in TypeScript and React

## Preferred/Nice-to-have
- Human-in-the-loop AI systems including evaluation
- Human-in-the-loop AI systems including review, approvals, tool execution, and recovery

## Skill Extraction
证据类型允许 `required`、`preferred`、`responsibility`、`inferred-prerequisite`。Alternative Group 表示 one-of 或 at-least-N 选择关系。

| Raw Evidence | Skill | Evidence Type | Requirement Strength | Alternative Group | Depth Signal | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| Deep frontend expertise in TypeScript and React | [[TypeScript-JavaScript]] | required | explicit | none | use | medium |
| Shape APIs, workflows, and data contracts behind product experiences | [[HTTP-API]] | responsibility | explicit | none | use | medium |
| Design human-in-the-loop workflows with approvals and execution status | [[Human-in-the-Loop-and-Agent-Guardrails]] | responsibility | explicit | none | use | medium |
| Interfaces for asynchronous systems with partial results, errors, retries, and user intervention | [[Agent-Orchestration-and-State]] | responsibility | explicit | none | use | medium |
| Human-in-the-loop AI systems including evaluation | [[Agent-Evals-and-Trace-Debugging]] | preferred | explicit | none | use | medium |
| Human-in-the-loop AI systems including review, approvals, tool execution, and recovery | [[Human-in-the-Loop-and-Agent-Guardrails]] | preferred | explicit | none | use | medium |

## Non-skill Gates
年限、客户沟通、领域经验、地点、授权与合规语境保留在岗位判断中，不自动归一化为 Skill。

## Role Mapping
- Primary [[AI-Application-Engineer]]

## Limitations
页面需动态渲染、重定向或部分可读；仅保留可复核的中/低置信事实。

## Evidence Trace
### Evidence 1
Source Section: What You Need
Source Fidelity: direct
Raw Evidence: Deep frontend expertise in TypeScript and React
Mapped Skill: [[TypeScript-JavaScript]]
Evidence Type: required
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: medium
Mapping Rationale: TypeScript is explicitly required.
Notes: quoted or lightly normalized from official What You Need section; mapping kept to TypeScript-JavaScript only.

### Evidence 2
Source Section: What You’ll Do
Source Fidelity: direct
Raw Evidence: Shape APIs, workflows, and data contracts behind product experiences
Mapped Skill: [[HTTP-API]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: medium
Mapping Rationale: API/data-contract work is explicit responsibility.
Notes: quoted or lightly normalized from official What You’ll Do section; mapping kept to HTTP-API only.

### Evidence 3
Source Section: What You’ll Do
Source Fidelity: direct
Raw Evidence: Design human-in-the-loop workflows with approvals and execution status
Mapped Skill: [[Human-in-the-Loop-and-Agent-Guardrails]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: medium
Mapping Rationale: Human review and approvals are explicit HITL work.
Notes: quoted or lightly normalized from official What You’ll Do section; mapping kept to Human-in-the-Loop-and-Agent-Guardrails only.

### Evidence 4
Source Section: What You Need
Source Fidelity: direct
Raw Evidence: Interfaces for asynchronous systems with partial results, errors, retries, and user intervention
Mapped Skill: [[Agent-Orchestration-and-State]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: medium
Mapping Rationale: Long-running async state and recovery are orchestration concerns.
Notes: quoted or lightly normalized from official What You Need section; mapping kept to Agent-Orchestration-and-State only.

### Evidence 5
Source Section: Nice to Haves
Source Fidelity: close-paraphrase
Raw Evidence: Human-in-the-loop AI systems including evaluation
Mapped Skill: [[Agent-Evals-and-Trace-Debugging]]
Evidence Type: preferred
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: medium
Mapping Rationale: Evaluation is explicitly preferred agent-quality experience.
Notes: paraphrased from official Nice to Haves section; mapping kept to Agent-Evals-and-Trace-Debugging only.

### Evidence 6
Source Section: Nice to Haves
Source Fidelity: close-paraphrase
Raw Evidence: Human-in-the-loop AI systems including review, approvals, tool execution, and recovery
Mapped Skill: [[Human-in-the-Loop-and-Agent-Guardrails]]
Evidence Type: preferred
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: medium
Mapping Rationale: Review and approvals are explicitly preferred HITL experience.
Notes: paraphrased from official Nice to Haves section; mapping kept to Human-in-the-Loop-and-Agent-Guardrails only.
