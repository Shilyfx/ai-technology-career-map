---
type: job-sample
company: ServiceNow / Moveworks
role_title: Senior Staff Software Engineer, Agentic Systems
role_family: ai-infrastructure
seniority: staff
location: Mountain View, California
region: US
source_url: https://careers.servicenow.com/jobs/744000145848949/senior-staff-software-engineer-agentic-systems-moveworks/
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

# ServiceNow / Moveworks — Senior Staff Software Engineer, Agentic Systems

## Source Scope
官方职位 URL：[https://careers.servicenow.com/jobs/744000145848949/senior-staff-software-engineer-agentic-systems-moveworks/](https://careers.servicenow.com/jobs/744000145848949/senior-staff-software-engineer-agentic-systems-moveworks/)。审计日期：`2026-09-01`；状态：`active` / `source_access: full` / `evidence_audit_status: verified`。官方页面完整可读；证据按源段落逐事实记录。
每条证据只保留一个可回溯事实；未适配当前 Skill 的信号不强行归类。

## Role Summary
本卡以官方职位页面为证据边界；请优先阅读下方来源段落与 Evidence Trace。

## Responsibilities
- A state machine manages long-running agent sessions across planning, execution, and user interaction
- Distributed session management uses DynamoDB leases, heartbeats, crash recovery, and checkpointing
- Event-driven message pipelines use SQS, Kafka, and gRPC/Socket.IO
- Structured concurrency uses Python asyncio TaskGroups and cancellation
- OpenTelemetry instrumentation and distributed trace context propagation

## Explicit Requirements
- Deep experience in distributed systems, concurrency, event-driven architectures, databases, observability, or gRPC/protobuf
- Strong in Python or Go

## Preferred/Nice-to-have
- 当前来源未确认 preferred 项。

## Skill Extraction
证据类型允许 `required`、`preferred`、`responsibility`、`inferred-prerequisite`。Alternative Group 表示 one-of 或 at-least-N 选择关系。

| Raw Evidence | Skill | Evidence Type | Requirement Strength | Alternative Group | Depth Signal | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| A state machine manages long-running agent sessions across planning, execution, and user interaction | [[Agent-Orchestration-and-State]] | responsibility | explicit | none | use | high |
| Distributed session management uses DynamoDB leases, heartbeats, crash recovery, and checkpointing | [[Agent-Orchestration-and-State]] | responsibility | explicit | none | use | high |
| Event-driven message pipelines use SQS, Kafka, and gRPC/Socket.IO | [[Distributed-Systems]] | responsibility | explicit | none | use | high |
| Structured concurrency uses Python asyncio TaskGroups and cancellation | [[Python]] | responsibility | explicit | none | use | high |
| OpenTelemetry instrumentation and distributed trace context propagation | [[Observability]] | responsibility | explicit | none | use | high |
| Deep experience in distributed systems, concurrency, event-driven architectures, databases, observability, or gRPC/protobuf | [[Distributed-Systems]] | required | explicit | areas-3-of-6 | use | high |
| Deep experience in distributed systems, concurrency, event-driven architectures, databases, observability, or gRPC/protobuf | [[Observability]] | required | explicit | areas-3-of-6 | use | high |
| Strong in Python or Go | [[Python]] | required | explicit | language-2 | use | high |

## Non-skill Gates
年限、客户沟通、领域经验、地点、授权与合规语境保留在岗位判断中，不自动归一化为 Skill。

## Role Mapping
- Primary [[AI-Infrastructure-and-Inference-Engineer]]

## Limitations
官方页面完整可读；证据按源段落逐事实记录。

## Evidence Trace
### Evidence 1
Source Section: What you get to do in this role
Source Fidelity: direct
Raw Evidence: A state machine manages long-running agent sessions across planning, execution, and user interaction
Mapped Skill: [[Agent-Orchestration-and-State]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: high
Mapping Rationale: The source explicitly describes an agent orchestration state machine.
Notes: quoted or lightly normalized from official What you get to do in this role section; mapping kept to Agent-Orchestration-and-State only.

### Evidence 2
Source Section: What you get to do in this role
Source Fidelity: direct
Raw Evidence: Distributed session management uses DynamoDB leases, heartbeats, crash recovery, and checkpointing
Mapped Skill: [[Agent-Orchestration-and-State]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: high
Mapping Rationale: Checkpointed session state is explicit orchestration responsibility.
Notes: quoted or lightly normalized from official What you get to do in this role section; mapping kept to Agent-Orchestration-and-State only.

### Evidence 3
Source Section: What you get to do in this role
Source Fidelity: direct
Raw Evidence: Event-driven message pipelines use SQS, Kafka, and gRPC/Socket.IO
Mapped Skill: [[Distributed-Systems]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: high
Mapping Rationale: Queues and streaming are explicit distributed-systems work.
Notes: quoted or lightly normalized from official What you get to do in this role section; mapping kept to Distributed-Systems only.

### Evidence 4
Source Section: What you get to do in this role
Source Fidelity: direct
Raw Evidence: Structured concurrency uses Python asyncio TaskGroups and cancellation
Mapped Skill: [[Python]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: high
Mapping Rationale: Python asyncio is explicit implementation responsibility; the source also names Go.
Notes: quoted or lightly normalized from official What you get to do in this role section; mapping kept to Python only.

### Evidence 5
Source Section: What you get to do in this role
Source Fidelity: direct
Raw Evidence: OpenTelemetry instrumentation and distributed trace context propagation
Mapped Skill: [[Observability]]
Evidence Type: responsibility
Requirement Strength: explicit
Alternative Group: none
Depth Signal: use
Confidence: high
Mapping Rationale: OpenTelemetry and tracing are explicit observability signals.
Notes: quoted or lightly normalized from official What you get to do in this role section; mapping kept to Observability only.

### Evidence 6
Source Section: Qualifications
Source Fidelity: direct
Raw Evidence: Deep experience in distributed systems, concurrency, event-driven architectures, databases, observability, or gRPC/protobuf
Mapped Skill: [[Distributed-Systems]]
Evidence Type: required
Requirement Strength: explicit
Alternative Group: areas-3-of-6
Depth Signal: use
Confidence: high
Mapping Rationale: Distributed systems is one of six areas from which the source requires at least three.
Notes: quoted or lightly normalized from official Qualifications section; mapping kept to Distributed-Systems only. Alternative group is not summed.

### Evidence 7
Source Section: Qualifications
Source Fidelity: direct
Raw Evidence: Deep experience in distributed systems, concurrency, event-driven architectures, databases, observability, or gRPC/protobuf
Mapped Skill: [[Observability]]
Evidence Type: required
Requirement Strength: explicit
Alternative Group: areas-3-of-6
Depth Signal: use
Confidence: high
Mapping Rationale: Observability is one of six explicit qualification areas.
Notes: quoted or lightly normalized from official Qualifications section; mapping kept to Observability only. Alternative group is not summed.

### Evidence 8
Source Section: Required
Source Fidelity: direct
Raw Evidence: Strong in Python or Go
Mapped Skill: [[Python]]
Evidence Type: required
Requirement Strength: explicit
Alternative Group: language-2
Depth Signal: use
Confidence: high
Mapping Rationale: Python is one member of the explicit language alternative.
Notes: quoted or lightly normalized from official Required section; mapping kept to Python only. Alternative group is not summed.
