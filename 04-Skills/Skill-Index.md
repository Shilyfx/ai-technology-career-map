---
type: moc
domain: skills
page_kind: skill-index
status: reference
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-09-24
related:
  - "[[Role-Map]]"
  - "[[Role-Skill-Matrix]]"
  - "[[Role-Skill-Assessment]]"
---

# Skill Index

> Skill 是岗位学习对象，不是技术热词清单。每项 Skill 都应能回到 Role Profile 和 Job Sample，并有 Practice 与 Pass Evidence。

| Category | Skill | Main Roles | Status | Stability |
| --- | --- | --- | --- | --- |
| Programming | [[Python]] / [[SQL]] / [[Git]] | Research, ML, Application, Data | validated | stable |
| Software Engineering | [[Linux]] / [[Testing]] / [[HTTP-API]] / [[Docker-Containers]] | All technical roles | developing | stable |
| Data | [[Data-Quality-and-Lineage]] | Data, ML, Application | developing | current |
| ML Foundations | [[ML-Experimentation]] / [[Model-Evaluation]] / [[Transformer-LLM-Fundamentals]] | Research, ML, Evals | developing | stable |
| Model Training | [[PyTorch]] / [[Distributed-Training]] | Research, ML, Infra | developing | current |
| LLM Applications | [[RAG]] / [[Tool-Calling-Agent-Workflow]] | Application, FDE, PM | developing | current |
| Infra / Inference | [[Model-Serving]] / [[Distributed-Systems]] / [[CUDA-GPU-Basics]] / [[Observability]] | Infra, Research, ML | developing | current |
| Evals / Safety | [[LLM-Evals]] / [[AI-Safety-Measurement]] | Evals, Safety, PM | developing | current |
| Product / Delivery | [[API-Product-Delivery]] / [[Technical-Communication]] | Application, PM, FDE | developing | stable |

## Promotion rule

只有满足至少两项才优先独立成页：真实 Job Sample 明确要求、被两个以上 Role 使用、可独立学习、有清晰 Practice/Pass Evidence、是关键 prerequisite，或已在多个现有页面反复出现。Framework 不自动成为 Skill。

## Dependency examples

```text
Python → HTTP-API → RAG → Tool-Calling-Agent-Workflow → LLM-Evals
Python → SQL → Data-Quality-and-Lineage → ML-Experimentation
Linux → Docker-Containers → Distributed-Systems → Model-Serving
```

同一 Skill 可对不同 Role 设定不同 Target Depth；不要在 Skill frontmatter 设置全局 `depth`。
