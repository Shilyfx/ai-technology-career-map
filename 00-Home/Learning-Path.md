---
type: path
status: active
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Start-Here]]"
  - "[[AI-Technology-MOC]]"
  - "[[Career-MOC]]"
---

# Learning Path

> 这条路线按依赖组织，不按热点组织。已有基础时先做产出验证，可以跳过整段阅读。

## Stage 0 — 定位：先分层

阅读：[[AI-ML-DL-and-Foundation-Models]]、[[AI-Technology-MOC]]、[[Role-Map]]。

**通过证据**：能把 10 个陌生名词放入“数据/训练/模型/应用/系统/安全/产品”之一，并解释为什么。

## Stage 1 — 共同底座

```text
Python + SQL + Git + Linux
→ 数据处理与可复现脚本
→ 线性代数、概率统计、优化直觉
→ 软件测试与 API
```

阅读：[[Math-Data-and-Software-Foundations]]。

**通过证据**：从原始数据生成可复现训练/分析输入；脚本有参数、日志、测试和版本记录。

## Stage 2 — 机器学习闭环

```text
问题定义 → 数据切分 → baseline → 训练 → 指标 → 失败样本 → 决策
```

阅读：[[Training-Evaluation-and-Generalization]]。

**通过证据**：完成一个基线，能解释数据泄漏、过拟合、阈值和错误切片，而不只报告一个总分。

## Stage 3 — 基础模型时代的核心概念

阅读：[[Transformer-and-Foundation-Models]]、[[Pretraining-Posttraining-and-Fine-tuning]]、[[Multimodal-Generative-and-Embodied-AI]]。

**通过证据**：能从 token/embedding 到 attention、训练目标、推理输出解释一次端到端模型调用，并说明能力来自哪里、限制在哪里。

## Stage 4 — 构建可靠 AI 应用

```text
用户任务 → context / retrieval → model → tools → validation → feedback
```

阅读：[[RAG-and-Knowledge-Systems]]、[[AI-Agents-and-Tool-Use]]、[[Evals-and-Observability]]、[[AI-Product-Engineering]]。

**通过证据**：做一个有固定任务集、可追踪来源、失败分类、成本/延迟记录的应用。是否用了 Agent 框架不影响通过。

## Stage 5 — 生产系统与风险

阅读：[[AI-Infrastructure-and-MLOps]]、[[Inference-Optimization]]、[[Data-Engineering-and-Governance]]、[[AI-Safety-Security-and-Governance]]。

**通过证据**：能说明系统的 SLO、回滚、权限、数据边界、攻击面、成本上限和模型更新策略。

## Stage 6 — 岗位专修与作品集

从 [[Career-MOC]] 选择一条主路径：

| 路径 | 代表作品 |
| --- | --- |
| 研究 | 可复现实验、消融、论文式报告 |
| 研究工程 | 规模化训练/评测工具与性能证据 |
| 应用工程 | 真实任务集上的可靠 AI 工作流 |
| 基础设施 | 吞吐、延迟、利用率、稳定性改进 |
| 产品 | 用户问题、指标、实验、风险与路线图 |
| 解决方案/FDE | 从业务约束到上线结果的完整交付 |
| 安全/评测 | 威胁模型、评测集、失效分析与控制闭环 |

**通过证据**：作品能让面试者看见你的判断过程、失败处理和权衡，而不只是最终 demo。

## 不建议的顺序

- 先背几十个框架名，再补基础；
- 把 prompt 模板数量当作能力深度；
- 只做聊天界面，不建立评测任务集；
- 只追最高 benchmark，不检查数据与执行有效性；
- 同时学研究、应用、Infra、产品所有路径到同一深度。
