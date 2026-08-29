---
type: skill
skill_category: ml-foundations
status: developing
stability: stable
created: 2026-08-24
updated: 2026-08-24
review_after: 2027-02-24
roles:
  - "[[Research Engineer]]"
  - "[[ML-and-AI-Engineer]]"
  - "[[AI-Safety-Evals-and-Governance]]"
prerequisites:
  - "[[ML-Experimentation]]"
  - "[[Statistics-and-Experiment-Design]]"
related_concepts:
  - "[[Evals-and-Observability]]"
---

# Model Evaluation

## 为什么岗位需要它
没有与任务和风险匹配的评测，训练或产品改动无法形成可靠决策。

## Role Demand
Research、ML、Safety/Evals 为 Core；应用和 PM 需要解释评测结果。证据见 [[Apple-Machine-Learning-Engineer-Eval-Insights-London-2026-06]]。

## Job Evidence

[[Anthropic-Research-Engineer-Model-Evaluations-San-Francisco-2026-08]]、[[Apple-Machine-Learning-Engineer-Eval-Insights-London-2026-06]] 的 `Skill Extraction` 是本 Skill 的 Job Evidence；只把明确要求作为 required 证据，职责推断保留为 inferred。

## 在岗位中怎么使用
设计任务集、指标、对照、切片、人工审查和回归门禁。

## Role-specific Target Depth
Evals/研究需要 implement；应用需要 use；PM 需要 explain 限制。

## 前置 Skills
[[ML-Experimentation]]、[[Statistics-and-Experiment-Design]]。

## 学习范围
离线/在线评测、分类/生成指标、基准偏差、回归和人评协议。

## 核心知识
测量有效性、可靠性、覆盖、切片和 metric gaming。

## Practice
为一个 RAG 或 agent 系统建 20 条任务的回归评测集。

## Pass Evidence
能说明每个指标测量什么、遗漏什么，以及一次失败的定位路径。

## 常见失败
只看单一平均分；把 benchmark 当真实用户；忽略标注和 judge 偏差。

## 不需要深挖到什么程度
先能做任务对齐和回归门禁，再决定是否深入统计测量理论。

## Related Knowledge
[[LLM-Evals]]、[[AI-Safety-Measurement]]。

## Actual Evidence
尚无用户能力结论；使用 [[Evidence-Card]] 记录。

## Sources
[[Anthropic-Research-Engineer-Model-Evaluations-San-Francisco-2026-08]]、[[Apple-Machine-Learning-Engineer-Eval-Insights-London-2026-06]]。
