---
type: skill
skill_category: data
status: developing
stability: current
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
roles:
  - "[[Data-and-AI-Engineer]]"
  - "[[ML-and-AI-Engineer]]"
  - "[[AI-Application-Engineer]]"
prerequisites:
  - "[[Python]]"
  - "[[SQL]]"
  - "[[Databases-and-Data-Modeling]]"
related_concepts:
  - "[[Data-Engineering-and-Governance]]"
---

# Data Quality and Lineage

## 为什么岗位需要它
模型和产品结果首先受数据正确性、覆盖、版本和来源影响。

## Role Demand
Data/ML 是 Core；应用岗位是 Common prerequisite。[[Apple-Machine-Learning-Engineer-Data-Curation-Cupertino-2026-06]] 和 [[Anthropic-Software-Engineer-RL-Data-San-Francisco-2026-08]] 提供样本。

## Job Evidence

[[Apple-Machine-Learning-Engineer-Data-Curation-Cupertino-2026-06]]、[[Anthropic-Software-Engineer-RL-Data-San-Francisco-2026-08]] 的 `Skill Extraction` 是本 Skill 的 Job Evidence；只把明确要求作为 required 证据，职责推断保留为 inferred。

## 在岗位中怎么使用
定义 schema、质量检查、血缘、过滤规则和可回溯版本。

## Role-specific Target Depth
Data 需要 implement；ML 需要 use/implement；PM 只需 explain 质量风险。

## 前置 Skills
[[Python]]、[[SQL]]、[[Databases-and-Data-Modeling]]。

## 学习范围
schema、缺失/重复/漂移、采样、标注、lineage、数据契约。

## 核心知识
数据质量维度、可追溯元数据、train/serve skew 和隐私边界。

## Practice
为一组训练样本写 schema、质量报告和可重跑过滤管线。

## Pass Evidence
能定位一条异常记录的来源、影响和修复版本。

## 常见失败
只看数量不看覆盖；清洗后丢失来源；把数据漂移误认为模型退化。

## 不需要深挖到什么程度
非数据岗位不必先掌握整套数据平台；先能读质量报告并做正确决策。

## Related Knowledge
[[Data-Engineering-and-Governance]]、[[ML-Experimentation]]。

## Actual Evidence
尚无用户能力结论；通过 [[Evidence-Card]] 记录实际项目。

## Sources
[[Apple-Machine-Learning-Engineer-Data-Curation-Cupertino-2026-06]]、[[Anthropic-Software-Engineer-RL-Data-San-Francisco-2026-08]]。
