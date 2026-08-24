---
type: radar
status: reference
snapshot_date: 2026-08-24
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
stability: current
related:
  - "[[AI-Technology-MOC]]"
  - "[[Term-Radar]]"
  - "[[2026-08-AI-Job-Market-Snapshot]]"
---

# Technology Radar — 2026-08

> Radar 表示学习与复查优先级，不表示技术优劣。稳定概念、当前技术和岗位信号分开维护。

## Changes since last radar

这是第一版基线，**没有 previous radar**。

### Added

- 建立 Core / Build / Deepen / Watch / Avoid 五档；
- 把评测、数据质量、软件工程和系统边界放在 Core；
- 增加 `review_after`，后续更新必须写出变化原因。

### Promoted / Demoted / Removed

- Promoted：无（首次基线）。
- Demoted：无（首次基线）。
- Removed：无；暂不把单一框架名列入主雷达。

### Why

第一版先固定判断标准：能否解释问题、能否构建、能否评测、能否承担失败。后续变化必须能回到来源、证据或岗位交付物。

## Core：应形成稳定心智模型

- 数据质量、切分、泄漏与评测设计；
- Python、SQL、软件工程、API 与 Linux；
- 训练/验证/测试、泛化、失败切片和可复现性；
- 权限、隐私、威胁模型、可观测性与回滚。

## Build：适合做项目

- RAG、检索质量、引用与知识库更新；
- 工具调用、Agent 工作流、状态管理与人工兜底；
- Evals、trace、成本/延迟监控与回归集；
- 推理服务、缓存、批处理和基础 MLOps。

## Deepen：按岗位投入

- Transformer、预训练、后训练、微调与对齐；
- 多模态、生成模型、具身系统；
- 分布式训练、量化、编译器、kernel 与硬件适配；
- 安全评测、红队、治理和政策落地。

## Watch：保留观察，不提前承诺

- 快速变化的 Agent 框架与模型编排层；
- 新型推理时扩展、世界模型和 VLA 产品化；
- 职位名称与“Prompt Engineer”等岗位标签的变化。

## Avoid：不作为独立能力目标

- 只会复制 prompt 模板；
- 只追榜单或厂商热度；
- 没有任务集和失败分析的 demo；
- 把单个公司的高级岗位要求当成通用入门门槛。

## 更新规则

复查时更新 `updated` 与 `review_after`，保留本节变化记录；相关术语先进入 [[Term-Radar]]，个人掌握程度写入 [[Evidence-Index]]，不要把雷达当成个人进度表。
