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
