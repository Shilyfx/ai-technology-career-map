---
type: skill
skill_category: programming
status: developing
stability: stable
created: 2026-08-24
updated: 2026-08-24
review_after: 2027-02-24
roles:
  - "[[Data-and-AI-Engineer]]"
  - "[[ML-and-AI-Engineer]]"
  - "[[AI-Application-Engineer]]"
prerequisites:
  - "[[Data-Structures-and-Algorithms]]"
related_concepts:
  - "[[Math-Data-and-Software-Foundations]]"
  - "[[Data-Engineering-and-Governance]]"
---

# SQL

## 为什么岗位需要它

数据、评测、产品指标和可观测性都需要可复查的查询；它是 AI 岗位常见但容易被模型热度遮蔽的基础 Skill。

## Role Demand

| Role | Priority | Target Depth | Job Evidence | Note |
| --- | --- | --- | --- | --- |
| Data / AI Engineer | Core | implement | [[Apple-Machine-Learning-Engineer-Data-Curation-Cupertino-2026-06]] | 数据应用与管道 |
| ML / AI Engineer | Common | use | [[Apple-Machine-Learning-Engineer-Search-Cupertino-2026-06]] | 大数据处理偏好 |
| Infra / Evals | Common | use | [[Anthropic-Performance-Engineer-Inference-Systems-San-Francisco-2026-08]] | telemetry 分析 |

## Job Evidence

[[Apple-Machine-Learning-Engineer-Data-Curation-Cupertino-2026-06]] 的 `Skill Extraction` 是本 Skill 的 Job Evidence；只把明确要求作为 required 证据，职责推断保留为 inferred。

## 在岗位中怎么使用

建模、连接、聚合、质量检查、实验切片和指标追踪。

## Role-specific Target Depth

Data 工程需要 implement；PM/研究协作通常只需 explain/use。

## 前置 Skills

[[Python]]。

## 学习范围

关系模型、JOIN、窗口、聚合、索引、质量检查和查询性能。

## 核心知识

NULL、重复、时间窗口、分层抽样、数据血缘与权限边界。

## Practice

为一份评测数据建立 schema、质量查询、切片报表和变更说明。

## Pass Evidence

提交查询、样例数据、质量结果和一个能解释指标变化的切片。

## 常见失败

重复 JOIN、时间泄漏、把 NULL 当 0、无权限地复制敏感数据。

## 不需要深挖到什么程度

非 Data 岗位不必把数据库内核当主线；必须能读写与验证任务相关的数据。

## Related Knowledge

[[Data-Engineering-and-Governance]]、[[Training-Evaluation-and-Generalization]]。

## Actual Evidence

尚无用户能力结论；使用 [[Evidence-Card]] 创建实际记录。

## Sources

[[Apple-Machine-Learning-Engineer-Data-Curation-Cupertino-2026-06]]。
