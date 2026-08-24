---
type: radar
page_kind: technology-radar
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

- AI / ML / DL / Foundation Model 的边界，以及数据、训练、模型、应用、系统和安全的层次；
- 数据质量、切分、泄漏、训练/验证/测试、泛化与失败切片；
- token / tokenizer、embedding、attention 与 Transformer 的基本机制；
- 训练与推理的区别，SFT / PEFT 的基本目的和边界；
- 评测设计、可复现性、软件工程、Python、SQL、API 与 Linux；
- 权限、隐私、威胁模型、可观测性与回滚。

## Build：适合做项目

- RAG、检索质量、引用与知识库更新；
- 工具调用、Agent 工作流、状态管理与人工兜底；
- Evals、trace、成本/延迟监控与回归集；
- 推理服务、缓存、批处理和基础 MLOps。

## Deepen：按岗位投入

- Transformer 实现、预训练系统、进阶后训练、RL / reasoning 与 MoE；
- 分布式训练、CUDA / NCCL、kernel / compiler、量化内部机制与硬件适配；
- serving 优化、KV cache、批处理与容量建模；
- 机制可解释性、进阶多模态 / 机器人，以及安全评测、红队和治理落地。

## Topic × depth

同一主题可以同时出现在多个深度：Core 只要求稳定的解释与边界判断，Build 要求能在受控任务中使用，Deepen 才要求实现、优化或研究。Radar 因此按“主题 × 所需深度”维护，而不是把一个主题整体贴成必学或暂不相关。

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
