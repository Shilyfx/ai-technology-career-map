---
type: matrix
status: reference
snapshot_date: 2026-08-24
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-09-24
related:
  - "[[Role-Map]]"
  - "[[Job-Sample-Index]]"
  - "[[Skill-Index]]"
  - "[[Skill-Evidence-Matrix]]"
---

# Role–Skill Matrix

> H/M/L 是基于 Role Profile 和 Job Sample 的编辑性总结；原始要求、explicit/inferred 和 source limitations 必须回到具体 Job Sample。

| Role | Python | Data/SQL | ML/Training | RAG/Agent | Infra/Serving | Evals/Safety | Product/Delivery |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Research Scientist | H | M | H | L–M | M | M–H | M |
| Research Engineer | H | M | H | M | H | H | M |
| ML / AI Engineer | H | M–H | H | M | M | H | M |
| AI Application Engineer | H | M | M | H | M | H | H |
| AI Infra / Inference | M | M | M–H | L | H | H | M |
| Data / AI Engineer | H | H | M | M | M | H | M |
| AI Product Manager | M | M | M | M | L | H | H |
| Solutions Architect / FDE | M | M | M | H | H | H | H |
| Safety / Evals / Governance | M | M–H | M–H | M | M | H | H |

## Interpretation

先用目标 Role 的 Skill Profile 决定深度；不要把矩阵中的 H 当成统一课程表，也不要因为一个框架名称出现就创建独立 Skill。

## Evidence-count view

`Evidence Count` 写成 `explicit / inferred`，统计的是不同 Job Sample 的 Skill Extraction 行，不是关键词出现次数；inferred 不计入 required frequency。Confidence 是基于来源可见度、样本重复度和抽取限制的编辑判断。

| Skill | Role | Priority | Evidence Count | Confidence |
| --- | --- | --- | --- | --- |
| [[Python]] | Research / ML / Application | Core | 14 / 4 | High |
| [[SQL]] | Data / ML | Core | 1 / 1 | Medium |
| [[Git]] | All engineering | Common | 0 / 1 | Medium |
| [[Linux]] | Infra | Prerequisite | 1 / 0 | Medium |
| [[Testing]] | Research / Application / Safety | Core | 2 / 5 | High |
| [[HTTP-API]] | Application / PM | Core | 2 / 0 | High |
| [[Docker-Containers]] | Application / ML | Common | 1 / 1 | Medium |
| [[Data-Quality-and-Lineage]] | Data / ML | Core | 2 / 1 | High |
| [[ML-Experimentation]] | Research / ML / Evals | Core | 7 / 3 | High |
| [[Model-Evaluation]] | Research / Evals | Core | 6 / 4 | High |
| [[Transformer-LLM-Fundamentals]] | ML / Research | Common | 3 / 2 | Medium |
| [[PyTorch]] | ML / Research | Core | 2 / 5 | Medium |
| [[Distributed-Training]] | Research / Infra | Specialized | 2 / 3 | Medium |
| [[RAG]] | Application / FDE | Common | 1 / 1 | Medium |
| [[Tool-Calling-Agent-Workflow]] | Application / PM | Core | 5 / 0 | High |
| [[Model-Serving]] | Infra / FDE | Core | 6 / 3 | High |
| [[Distributed-Systems]] | Infra / Research | Core | 9 / 3 | High |
| [[CUDA-GPU-Basics]] | Infra / Research | Specialized | 7 / 2 | High |
| [[Observability]] | Infra / Application | Common | 4 / 4 | High |
| [[LLM-Evals]] | Evals / Application | Core | 7 / 2 | High |
| [[AI-Safety-Measurement]] | Safety / PM | Core | 3 / 1 | High |
| [[API-Product-Delivery]] | PM / Application | Core | 2 / 2 | Medium |
| [[Technical-Communication]] | PM / FDE | Core | 4 / 3 | High |
