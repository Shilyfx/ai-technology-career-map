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
  - "[[Python]]"
  - "[[Data-Quality-and-Lineage]]"
related_concepts:
  - "[[Training-Evaluation-and-Generalization]]"
---

# ML Experimentation

## 为什么岗位需要它
岗位样本反复要求用可复现、可比较的实验把模型变化转成可信结论。

## Role Demand
Research/ML/Evals 为 Core；产品和应用以理解指标为边界。证据见 [[OpenAI-Research-Engineer-Frontier-Evals-San-Francisco-2026-08]]。

## Job Evidence

[[OpenAI-Research-Engineer-Frontier-Evals-San-Francisco-2026-08]]、[[Apple-Machine-Learning-Engineer-Eval-Insights-London-2026-06]] 的 `Skill Extraction` 是本 Skill 的 Job Evidence；只把明确要求作为 required 证据，职责推断保留为 inferred。

## 在岗位中怎么使用
固定数据切分、seed、配置、baseline、指标、日志和失败解释。

## Role-specific Target Depth
研究岗位 implement/optimize；应用岗位 use；PM explain。

## 前置 Skills
[[Python]]、[[Data-Quality-and-Lineage]]。

## 学习范围
假设、对照、消融、置信区间、可重复性、误差分析和资源预算。

## 核心知识
实验设计、数据泄漏、随机性、统计显著性和可复现记录。

## Practice
对一个模型改动做 baseline、消融和失败样本报告。

## Pass Evidence
第三方可复跑命令并得到相同结论，且知道结论边界。

## 常见失败
只报最好一次；混用 split；把相关性当因果；忽略成本和失败率。

## 不需要深挖到什么程度
非研究岗位先做到可审计和可比较，不必立即研究高级统计理论。

## Related Knowledge
[[Training-Evaluation-and-Generalization]]、[[Model-Evaluation]]。

## Actual Evidence
尚无用户能力结论；请关联具体 [[Evidence-Card]]。

## Sources
[[OpenAI-Research-Engineer-Frontier-Evals-San-Francisco-2026-08]]、[[Apple-Machine-Learning-Engineer-Eval-Insights-London-2026-06]]。
