---
type: concept
domain: data-systems
status: validated
stability: stable
depth: use
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[RAG-and-Knowledge-Systems]]"
  - "[[Data-and-AI-Engineer]]"
  - "[[AI-Safety-Security-and-Governance]]"
  - "[[Databases-and-Data-Modeling]]"
  - "[[Security-Privacy-and-Access-Control]]"
---

# Data Engineering and Governance

## AI 系统的数据不只在训练前出现

```text
raw source
→ ingestion
→ validation
→ transformation
→ training / retrieval / evaluation
→ feedback and monitoring
→ retention / deletion / audit
```

## 工程问题

- batch 与 streaming ingestion；
- schema、data contract、quality test；
- ETL/ELT、orchestration、lineage；
- lake/warehouse/vector index；
- feature、embedding、label 与 eval dataset；
- 权限、加密、PII、retention、deletion；
- 数据/模型版本可追溯。

## AI 特有风险

- 训练数据与评测集污染；
- 用户反馈直接回流导致攻击或偏差放大；
- 文档权限未传播到 RAG 索引；
- embedding 和日志泄露敏感信息；
- 数据许可、作者权与地域要求不明确；
- synthetic data 让错误模式循环放大。

## 最小数据契约

```text
owner:
source:
schema:
allowed_use:
quality_checks:
split_or_scope:
version:
lineage:
retention:
access_control:
known_biases:
```

## 最小实践

为一个 RAG 或训练数据集建立契约、质量检查、版本、权限继承与删除测试；证明一条源文档撤权后不会继续被检索。
