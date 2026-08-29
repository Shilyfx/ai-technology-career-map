---
type: skill
skill_category: ml-foundations
status: developing
stability: stable
evidence_mode: prerequisite-synthesis
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-28
roles:
  - "[[Research-Scientist]]"
  - "[[Research-Engineer]]"
  - "[[ML-and-AI-Engineer]]"
  - "[[AI-Safety-Evals-and-Governance]]"
  - "[[AI-Product-Manager]]"
  - "[[Data-and-AI-Engineer]]"
prerequisites:
  - "[[Python]]"
related_concepts:
  - "[[Training-Evaluation-and-Generalization]]"
  - "[[Evals-and-Observability]]"
---

# Statistics and Experiment Design

## 为什么岗位需要它

岗位交付不是“跑过一次就更好”，而是要判断改动是否带来真实改善、对哪些切片有效、结果有多大不确定性，以及成本和风险是否值得。

## Role Demand

Research、ML、Evals/Safety 需要 implement；Data 和 Application 需要 use；PM 需要 explain 指标、实验和决策边界。

## Job Evidence

当前样本将统计、实验和测量分散在 [[ML-Experimentation]]、[[Model-Evaluation]]、[[LLM-Evals]] 与 [[AI-Safety-Measurement]] 中，没有单独的“统计学”标签。本页是学习前置层，不把综合判断写成新的 explicit Job Sample 计数。

## 在岗位中怎么使用

定义问题和指标、选择对照、固定切分、处理随机性，报告置信区间/效应量，分析切片和误差，并决定是否继续、回滚或扩大实验。

## Role-specific Target Depth

Research/ML/Evals 需要 implement；Application 需要 use；PM 需要 explain/decide；Safety 还要理解误报、漏报和阈值选择。

## 前置 Skills

[[Python]]。

## 学习范围

概率基础、抽样、均值/方差、置信区间、假设检验、效应量、功效、A/B、分层切片、相关与因果、标注一致性。

## 核心知识

样本数和测量误差决定结论强度；平均分可能掩盖灾难切片；统计显著不等于业务重要；相关性不等于因果。

## Practice

为一个 RAG 或 Agent 改动设计 baseline/ablation，至少 30 条任务、3 个切片、置信区间和失败分类，比较质量、延迟、成本与安全指标。

## Pass Evidence

能复跑分析并回答：比较对象是什么、指标测量什么、结果不确定性多大、哪些样本不能外推，以及下一步动作是什么。

## 常见失败

挑最好的一次运行；只报 p-value；混用数据切分；忽略多重比较、标注偏差和回归到均值。

## 不需要深挖到什么程度

非研究岗位先掌握实验设计、切片和不确定性表达；只有测量科学或研究方向才继续深入理论推导。

## Related Knowledge

[[ML-Experimentation]]、[[Model-Evaluation]]、[[LLM-Evals]]、[[AI-Safety-Measurement]]。

## Actual Evidence

尚无用户能力结论；完成一次完整对照实验后使用 [[Evidence-Card]] 记录。

## Sources

[[ML-Experimentation]]、[[Model-Evaluation]]、[[LLM-Evals]]、[[AI-Safety-Measurement]]、[[NotebookLM-Advanced-Tips]]。

