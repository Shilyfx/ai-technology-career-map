---
type: skill
skill_category: data
status: developing
stability: stable
evidence_mode: prerequisite-synthesis
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-28
roles:
  - "[[Data-and-AI-Engineer]]"
  - "[[ML-and-AI-Engineer]]"
  - "[[AI-Application-Engineer]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
prerequisites:
  - "[[SQL]]"
related_concepts:
  - "[[Data-Engineering-and-Governance]]"
  - "[[RAG-and-Knowledge-Systems]]"
---

# Databases and Data Modeling

## 为什么岗位需要它

训练集、评测集、用户状态、日志和检索索引都需要明确的数据模型。没有 schema、主键、生命周期和访问边界，模型输出再好也无法可靠迭代。

## Role Demand

Data/AI 为 Core prerequisite；ML/Application/FDE 需要 use；复杂产品还要能在关系库、对象存储、搜索/向量索引之间做边界判断。

## Job Evidence

现有样本分别记录 SQL、Data Quality、RAG 和分布式系统；没有单独把“数据库建模”作为标签。本页用于补齐学习前置，不增加 Job Sample 的 explicit 频次。

## 在岗位中怎么使用

设计实体和关系、事件表、版本表、状态表、数据契约、索引和迁移；让训练/评测/反馈数据可追溯、可删除、可重放。

## Role-specific Target Depth

Data 需要 implement；ML/Application 需要 use/implement 与任务相关的模型；PM/FDE 需要 explain 数据边界和成本。

## 前置 Skills

[[SQL]]。

## 学习范围

关系模型、主键/外键、范式与反范式、事务、一致性、索引、分区、时间序列、事件建模、对象存储、向量索引和 schema migration。

## 核心知识

检索结果必须能回到原文版本；删除和撤权要传播到下游；embedding 不是数据库模型的替代品；查询性能要和成本、freshness 一起看。

## Practice

为一个带 RAG 的学习助手设计 documents/chunks/embeddings/feedback/evals 五张逻辑表，写 schema、质量查询、版本迁移和删除传播演练。

## Pass Evidence

能展示一次 schema 变更、一次重复/孤儿记录检测、一次按来源回溯，以及一次撤权或删除后的索引清理。

## 常见失败

把 JSON dump 当 schema；没有唯一键；混淆文档版本和 embedding 版本；删除主表却遗留索引和缓存。

## 不需要深挖到什么程度

应用岗位先掌握建模、查询和生命周期；不需要一开始研究数据库内核或自建向量数据库。

## Related Knowledge

[[SQL]]、[[Data-Quality-and-Lineage]]、[[RAG]]、[[Distributed-Systems]]。

## Actual Evidence

尚无用户能力结论；完成 schema 与迁移 Practice 后使用 [[Evidence-Card]] 记录。

## Sources

[[Data-Quality-and-Lineage]]、[[RAG-and-Knowledge-Systems]]、[[Obsidian-Copilot-RAG]]、[[n8n-Obsidian-RSS-Automation]]。

