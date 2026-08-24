---
type: skill
skill_category: evals-safety
status: developing
stability: current
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
roles:
  - "[[AI-Safety-Evals-and-Governance]]"
  - "[[Research Engineer]]"
  - "[[AI-Application-Engineer]]"
prerequisites:
  - "[[Model-Evaluation]]"
  - "[[RAG]]"
related_concepts:
  - "[[Evals-and-Observability]]"
---

# LLM Evals

## 为什么岗位需要它
LLM 输出开放且不稳定，必须用任务集、judge、人工审查和安全切片建立回归信号。

## Role Demand
Evals/Safety 为 Core；应用为 Common；PM 需理解决策边界。证据见 [[OpenAI-Research-Engineer-Frontier-Evals-San-Francisco-2026-08]]。

## Job Evidence

[[OpenAI-Research-Engineer-Frontier-Evals-San-Francisco-2026-08]]、[[Apple-Machine-Learning-Engineer-Eval-Insights-London-2026-06]] 的 `Skill Extraction` 是本 Skill 的 Job Evidence；只把明确要求作为 required 证据，职责推断保留为 inferred。

## 在岗位中怎么使用
构造 eval set、rubric、LLM-as-judge、回归门禁和失败样本分析。

## Role-specific Target Depth
Evals implement/optimize；应用 implement/use；PM explain。

## 前置 Skills
[[Model-Evaluation]]、[[RAG]]。

## 学习范围
能力、安全、agent、judge calibration、偏差、覆盖和持续评测。

## 核心知识
任务有效性、分层指标、人工协议和自动评测的局限。

## Practice
为工具 agent 建一套包含越权、幻觉、超时和成功率的评测。

## Pass Evidence
能证明一次模型升级改善了目标切片且未损害 guardrail。

## 常见失败
把 judge 当真值；样本泄漏；只报告平均分，不报告灾难失败。

## 不需要深挖到什么程度
普通应用先会写可复现回归集；安全岗位再深入测量和红队方法。

## Related Knowledge
[[Evals-and-Observability]]、[[AI-Safety-Measurement]]。

## Actual Evidence
尚无用户能力结论；通过 [[Evidence-Card]] 记录。

## Sources
[[OpenAI-Research-Engineer-Frontier-Evals-San-Francisco-2026-08]]、[[Apple-Machine-Learning-Engineer-Eval-Insights-London-2026-06]]。
