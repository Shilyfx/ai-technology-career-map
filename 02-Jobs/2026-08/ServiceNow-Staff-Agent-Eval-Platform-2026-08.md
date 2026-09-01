---
type: job-sample
company: ServiceNow / Moveworks
role_title: Staff Software Engineer, Agent Eval Platform
role_family: ai-infrastructure
seniority: staff
location: Not stated on page
region: US/Global
source_url: https://careers.servicenow.com/jobs/744000145843394/staff-software-engineer-agent-eval-platform/
source_kind: official-job-posting
source_status: active
source_access: full
sample_batch: enterprise-applied-ai-2026-08
company_segment: enterprise-saas
role_subtrack: agent-platform
snapshot_date: 2026-08-31
retrieved: 2026-09-01
status: developing
created: 2026-08-31
updated: 2026-09-01
review_after: 2026-10-15
related: []
evidence_audit_status: verified
---

# ServiceNow / Moveworks — Staff Software Engineer, Agent Eval Platform

## Source Scope
官方职位 URL：[https://careers.servicenow.com/jobs/744000145843394/staff-software-engineer-agent-eval-platform/](https://careers.servicenow.com/jobs/744000145843394/staff-software-engineer-agent-eval-platform/)。审计日期：`2026-09-01`；状态：`active` / `source_access: full` / `evidence_audit_status: verified`。官方页面完整可读；证据按源段落逐事实记录。
每条证据只保留一个可回溯事实；未适配当前 Skill 的信号不强行归类。

## Role Summary
本卡以官方职位页面为证据边界；请优先阅读下方来源段落与 Evidence Trace。

## Responsibilities
- Build the judgement layer: rubrics, judges, calibration against human labels, and trajectory scoring
- Execute scenarios, collect traces/final state, validate, score, and tear down
- Scheduling, retries, high-concurrency execution, run isolation, and versioned reports
- OpenTelemetry-native observability and a span data model for agent trajectories
- Calibration against human labels
- Contract-testing mocks against real API schemas in CI

## Explicit Requirements
- Deep experience in distributed systems, orchestration, observability, concurrency, data pipelines, or gRPC/protobuf
- Strong in Python or Go

## Preferred/Nice-to-have
- 当前来源未确认 preferred 项。

## Skill Extraction
证据类型允许 `required`、`preferred`、`responsibility`、`inferred-prerequisite`。Alternative Group 表示 one-of 或 at-least-N 选择关系。

| Raw Evidence | Skill | Evidence Type | Requirement Strength | Alternative Group | Depth Signal | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| Build the judgement layer: rubrics, judges, calibration against human labels, and trajectory scoring | [[Agent-Evals-and-Trace-Debugging]] | responsibility | explicit | none | use | high |
| Execute scenarios, collect traces/final state, validate, score, and tear down | [[Agent-Evals-and-Trace-Debugging]] | responsibility | explicit | none | use | high |
| Scheduling, retries, high-concurrency execution, run isolation, and versioned reports | [[Agent-Evals-and-Trace-Debugging]] | responsibility | explicit | none | use | high |
| OpenTelemetry-native observability and a span data model for agent trajectories | [[Observability]] | responsibility | explicit | none | use | high |
| Calibration against human labels | [[Agent-Evals-and-Trace-Debugging]] | responsibility | explicit | none | use | high |
| Contract-testing mocks against real API schemas in CI | [[Testing]] | responsibility | explicit | none | use | high |
| Deep experience in distributed systems, orchestration, observability, concurrency, data pipelines, or gRPC/protobuf | [[Distributed-Systems]] | required | explicit | areas-3-of-6 | use | high |
| Deep experience in distributed systems, orchestration, observability, concurrency, data pipelines, or gRPC/protobuf | [[Observability]] | required | explicit | areas-3-of-6 | use | high |
| Strong in Python or Go | [[Python]] | required | explicit | language-1 | use | high |

## Non-skill Gates
年限、客户沟通、领域经验、地点、授权与合规语境保留在岗位判断中，不自动归一化为 Skill。

## Role Mapping
- Primary [[AI-Infrastructure-and-Inference-Engineer]]

## Limitations
官方页面完整可读；证据按源段落逐事实记录。

## Evidence Trace
### Evidence 1
Source Section: The Role
Source Fidelity: close-paraphrase
Raw Evidence: Build the judgement layer: rubrics, judges, calibration against human labels, and trajectory scoring
Mapped Skill: [[Agent-Evals-and-Trace-Debugging]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: high
Mapping Rationale: Judges, rubrics, calibration, and trajectory scoring are explicit agent-evaluation signals.
Notes: paraphrased from official The Role section; mapping kept to Agent-Evals-and-Trace-Debugging only.

### Evidence 2
Source Section: Eval orchestration at scale
Source Fidelity: close-paraphrase
Raw Evidence: Execute scenarios, collect traces/final state, validate, score, and tear down
Mapped Skill: [[Agent-Evals-and-Trace-Debugging]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: high
Mapping Rationale: The source explicitly describes an end-to-end evaluation harness.
Notes: paraphrased from official Eval orchestration at scale section; mapping kept to Agent-Evals-and-Trace-Debugging only.

### Evidence 3
Source Section: Eval orchestration at scale
Source Fidelity: close-paraphrase
Raw Evidence: Scheduling, retries, high-concurrency execution, run isolation, and versioned reports
Mapped Skill: [[Agent-Evals-and-Trace-Debugging]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: high
Mapping Rationale: These are evaluation-harness runtime concerns in the eval orchestration section, not business workflow automation.
Notes: paraphrased from official Eval orchestration at scale section; mapping kept to Agent-Evals-and-Trace-Debugging only.

### Evidence 4
Source Section: Agent observability and tracing
Source Fidelity: direct
Raw Evidence: OpenTelemetry-native observability and a span data model for agent trajectories
Mapped Skill: [[Observability]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: high
Mapping Rationale: OpenTelemetry, spans, and trajectory traces are explicit observability work.
Notes: quoted or lightly normalized from official Agent observability and tracing section; mapping kept to Observability only.

### Evidence 5
Source Section: The Role
Source Fidelity: direct
Raw Evidence: Calibration against human labels
Mapped Skill: [[Agent-Evals-and-Trace-Debugging]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: high
Mapping Rationale: Human labels calibrate evaluator ground truth; the source does not describe runtime approval or authorization.
Notes: quoted or lightly normalized from official The Role section; mapping kept to Agent-Evals-and-Trace-Debugging only.

### Evidence 6
Source Section: Stateful simulation
Source Fidelity: direct
Raw Evidence: Contract-testing mocks against real API schemas in CI
Mapped Skill: [[Testing]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: high
Mapping Rationale: Contract testing is explicitly named.
Notes: quoted or lightly normalized from official Stateful simulation section; mapping kept to Testing only.

### Evidence 7
Source Section: Qualifications
Source Fidelity: direct
Raw Evidence: Deep experience in distributed systems, orchestration, observability, concurrency, data pipelines, or gRPC/protobuf
Mapped Skill: [[Distributed-Systems]]
Evidence Type: required
Requirement Strength: explicit
Alternative Group: areas-3-of-6
Depth Signal: use
Confidence: high
Mapping Rationale: Distributed systems is one of six explicit qualification areas.
Notes: quoted or lightly normalized from official Qualifications section; mapping kept to Distributed-Systems only. Alternative group is not summed.

### Evidence 8
Source Section: Qualifications
Source Fidelity: direct
Raw Evidence: Deep experience in distributed systems, orchestration, observability, concurrency, data pipelines, or gRPC/protobuf
Mapped Skill: [[Observability]]
Evidence Type: required
Requirement Strength: explicit
Alternative Group: areas-3-of-6
Depth Signal: use
Confidence: high
Mapping Rationale: Observability is one of six explicit qualification areas.
Notes: quoted or lightly normalized from official Qualifications section; mapping kept to Observability only. Alternative group is not summed.

### Evidence 9
Source Section: Required
Source Fidelity: direct
Raw Evidence: Strong in Python or Go
Mapped Skill: [[Python]]
Evidence Type: required
Requirement Strength: explicit
Alternative Group: language-1
Depth Signal: use
Confidence: high
Mapping Rationale: Python is one member of the explicit language alternative.
Notes: quoted or lightly normalized from official Required section; mapping kept to Python only. Alternative group is not summed.
