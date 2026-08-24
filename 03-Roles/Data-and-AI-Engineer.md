---
type: role
role_family: data-engineering
sample_count: 3
status: developing
snapshot_date: 2026-08-24
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
---

# Data and AI Engineer

## 主要使命

构建训练、检索、评测和产品都能信任的数据系统。AI 项目失败常不是模型不够强，而是数据来源、schema、权限、更新、标签或反馈闭环不可信。

## 日常工作

- ingestion、ETL/ELT、batch/streaming；
- warehouse/lake、vector/embedding pipeline；
- schema、data contracts、quality、lineage；
- 训练集、标签、反馈与 eval dataset；
- 权限、PII、retention、deletion 与审计；
- pipeline orchestration、监控、成本与恢复。

## 技能重点

SQL、Python、数据建模、数据库、分布式计算、workflow orchestration、云、测试、数据治理；理解 ML 数据切分、feature/label、embedding、RAG 权限传播和模型反馈风险。

## 作品证据

构建一个可追溯数据流，并证明：

- schema 变化会被检测；
- 重复、空值、异常和泄漏有检查；
- 每个训练/评测产物能回溯源版本；
- 撤权/删除能传播到索引和下游；
- pipeline 失败可恢复且不会静默产出错误数据。

## 相邻岗位

[[ML-and-AI-Engineer]]、[[AI-Application-Engineer]]、[[AI-Infrastructure-and-Inference-Engineer]]。

## Sample Basis
3 samples: Apple data curation, Anthropic RL data, and data-intensive safeguards infrastructure.

## Evidence Basis

Based on 3 Job Samples in [[Job-Sample-Index]]; employers, regions and seniority are summarized in this profile. Confidence is high for repeated explicit signals and medium for partial or inferred signals.

## Main Deliverables
Traceable ingestion, curated datasets, quality gates, access controls and recoverable pipelines.

## Responsibility Clusters
Data modeling; quality/lineage; ML dataset and feedback; privacy; orchestration and reliability.

## Skill Profile
| Skill | Required | Preferred | Responsibility | Sample N | Role Priority | Target Depth | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [[Python]] | yes |  | pipeline code | 3 | Core | implement | high | Job Samples |
| [[SQL]] | yes |  | querying and quality | 2 | Core | implement | high | Job Samples |
| [[Data-Quality-and-Lineage]] | yes |  | trust and traceability | 3 | Core | implement | high | Job Samples |
| [[Testing]] |  | yes | correctness gates | 2 | Common | implement | medium | Job Samples |
| [[Distributed-Systems]] |  | yes | scale and recovery | 2 | Common | use | medium | Job Samples |

## Non-skill Gates
Privacy, data stewardship, cross-team contracts and silent-failure intolerance.

## Seniority/Subtrack Differences
Analytics data work emphasizes SQL; ML data work emphasizes labeling, splits, lineage and feedback.

## Portfolio Evidence
Schema change test, quality report, source lineage, deletion propagation and recovery run.

## Adjacent Roles
[[ML-and-AI-Engineer]]、[[AI-Application-Engineer]]、[[AI-Infrastructure-and-Inference-Engineer]]。

## Source Limitations
Batch is light on entry-level and warehouse-specific postings; framework names are not core skills.

## Refresh
Refresh data-tool signals every 60–90 days and stable data fundamentals every 180–365 days。
