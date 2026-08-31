---
type: moc
domain: skills
page_kind: skill-index
status: reference
created: 2026-08-24
updated: 2026-08-31
review_after: 2026-09-24
related:
  - "[[Role-Map]]"
  - "[[Role-Skill-Matrix]]"
  - "[[Role-Skill-Assessment]]"
  - "[[Skill-Evidence-Matrix]]"
  - "[[Prerequisite-Foundation-Map]]"
---

# Skill Index

> Skill 是岗位学习对象，不是技术热词清单。每项 Skill 都应能回到 Role Profile 和 Job Sample，并有 Practice 与 Pass Evidence。

学习闭环：`Role Requirement → Skill Note → Practice → Pass Evidence`。证据汇总见 [[Skill-Evidence-Matrix]]；具体来源必须回到 Job Sample 的 `Evidence Trace`。

| Category | Skill | Main Roles | Status | Stability |
| --- | --- | --- | --- | --- |
| Programming | [[Python]] / [[TypeScript-JavaScript]] / [[SQL]] / [[Git]] | Research, ML, Application, Data, FDE | validated/developing | stable |
| Software Engineering | [[Linux]] / [[Testing]] / [[HTTP-API]] / [[Docker-Containers]] | All technical roles | developing | stable |
| Data | [[Data-Quality-and-Lineage]] | Data, ML, Application | developing | current |
| ML Foundations | [[ML-Experimentation]] / [[Model-Evaluation]] / [[Transformer-LLM-Fundamentals]] | Research, ML, Evals | developing | stable |
| Model Training | [[PyTorch]] / [[Distributed-Training]] | Research, ML, Infra | developing | current |
| LLM Applications | [[Prompt-and-Context-Engineering]] / [[LLM-API-and-Structured-Outputs]] / [[Tool-Calling-and-Action-Contracts]] / [[Agent-Orchestration-and-State]] / [[Workflow-Automation-and-Business-Process-Design]] / [[MCP-and-Agent-Interoperability]] / [[RAG]] | Application, FDE, PM, Agent Platform | developing | current |
| Legacy bridge | [[Tool-Calling-Agent-Workflow]] | 旧链接迁移入口 | reference | current |
| Infra / Inference | [[Model-Serving]] / [[Distributed-Systems]] / [[CUDA-GPU-Basics]] / [[Observability]] | Infra, Research, ML | developing | current |
| Evals / Safety | [[LLM-Evals]] / [[Agent-Evals-and-Trace-Debugging]] / [[Human-in-the-Loop-and-Agent-Guardrails]] / [[AI-Safety-Measurement]] | Evals, Safety, Application, FDE, PM | developing | current |
| Product / Delivery | [[API-Product-Delivery]] / [[Enterprise-Integrations-and-Connectors]] / [[Technical-Communication]] | Application, PM, FDE | developing | current/stable |

## Learning prerequisite layer

这些页面是为了回答“正式岗位 Skill 之前先学什么”。它们是可独立练习的通用能力，但其中标记 `evidence_mode: prerequisite-synthesis` 的页面并不增加 Job Sample 的 explicit 频次；岗位要求仍回到 [[Role-Skill-Matrix]] 和具体 Job Sample。

| Foundation | Feeds into | Main roles | Suggested depth |
| --- | --- | --- | --- |
| [[Data-Structures-and-Algorithms]] | [[Python]]、[[TypeScript-JavaScript]]、[[SQL]]、[[Testing]]、[[Distributed-Systems]] | Research / ML / Application / Data / Infra | implement |
| [[Statistics-and-Experiment-Design]] | [[ML-Experimentation]]、[[Model-Evaluation]]、[[LLM-Evals]] | Research / ML / Evals / PM | use → implement |
| [[Databases-and-Data-Modeling]] | [[SQL]]、[[Data-Quality-and-Lineage]]、[[RAG]] | Data / ML / Application / FDE | use → implement |
| [[Software-Design-and-Architecture]] | [[HTTP-API]]、[[LLM-API-and-Structured-Outputs]]、[[Tool-Calling-and-Action-Contracts]]、[[Model-Serving]] | Application / Data / ML / Infra / FDE | use → implement |
| [[Security-Privacy-and-Access-Control]] | [[Tool-Calling-and-Action-Contracts]]、[[MCP-and-Agent-Interoperability]]、[[RAG]]、[[AI-Safety-Measurement]] | All technical roles + PM | explain → implement |
| [[Prompt-and-Context-Engineering]] | [[RAG]]、[[LLM-API-and-Structured-Outputs]]、[[Tool-Calling-and-Action-Contracts]]、[[LLM-Evals]] | Application / PM / FDE / Safety | use → implement |

## Promotion rule

只有满足至少两项才优先独立成页：真实 Job Sample 明确要求、被两个以上 Role 使用、可独立学习、有清晰 Practice/Pass Evidence、是关键 prerequisite，或已在多个现有页面反复出现。Framework 不自动成为 Skill。

## Dependency examples

```text
Data-Structures-and-Algorithms → Python OR TypeScript-JavaScript → HTTP-API → Software-Design-and-Architecture
Prompt-and-Context-Engineering + LLM-API-and-Structured-Outputs → Tool-Calling-and-Action-Contracts → Workflow-Automation-and-Business-Process-Design / Agent-Orchestration-and-State → Agent-Evals-and-Trace-Debugging
Python → SQL → Databases-and-Data-Modeling → Data-Quality-and-Lineage → ML-Experimentation
Linux → Docker-Containers → Distributed-Systems → Model-Serving
HTTP-API → Security-Privacy-and-Access-Control
```

同一 Skill 可对不同 Role 设定不同 Target Depth；不要在 Skill frontmatter 设置全局 `depth`。
