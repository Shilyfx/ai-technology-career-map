---
type: path
page_kind: role-learning-paths
status: reference
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
related:
  - "[[Learning-Path]]"
  - "[[Job-Skill-Matrix]]"
---

# Role-Based Learning Paths

> Stage 0–2 是共同基础，Stage 3 建立基础模型时代的共同素养；之后按岗位分支。Stage 4/5 是可选专修层，不是所有人都必须完成的统一前置课。

## 研究 / Research Scientist

```text
ML/DL + math
→ Transformer / training
→ paper reproduction
→ research question + controlled experiment
→ one specialization
```

必做：统计、严谨 eval、论文阅读、复现、baseline、消融与科研写作。

作品：一份可复现实验报告，包含反证或失败分析。

Recommended branch point: Stage 2 → Stage 3 深入 → Research。

## 研究工程 / Research Engineer

```text
software + PyTorch
→ experiment systems
→ distributed training / profiling
→ research implementation
→ specialization at scale
```

必做：测试、数据/配置/checkpoint、multi-GPU、profiling、恢复与可复现。

作品：将研究实验可靠地扩展，并给性能和正确性证据。

Recommended branch point: Stage 2 → Stage 3 → training / systems。

## ML / AI Engineer

```text
data + ML/DL
→ training / evaluation
→ deployment and monitoring
→ reliability / performance
→ one model or product specialization
```

必做：数据与实验闭环、模型训练、评测、部署、监控、回归和成本意识。

作品：一份端到端模型生命周期项目，明确数据、训练、评测、部署和失败处理。

Recommended branch point: Stage 2 → Stage 3 → selected Stage 4 + Stage 5。

## Data / AI Engineer

```text
SQL + data systems
→ data contracts / quality
→ feature or embedding pipeline
→ serving / governance
→ domain delivery
```

必做：数据契约、质量、lineage、权限、SQL、管道可靠性和 AI 使用边界。

作品：可追溯、可信、可服务的数据流，包含质量门禁、权限和回滚说明。

Recommended branch point: Stage 1 → Stage 2 → Stage 4 data / AI systems + selected Stage 5。

## 应用工程 / AI Application Engineer

```text
backend/full-stack
→ model API + structured output
→ RAG
→ eval + trace
→ workflow / controlled agent
```

必做：TypeScript/Python、API、数据库、RAG、eval、权限、安全、成本。

作品：真实任务集上的产品，而不是一次性聊天 demo。

Recommended branch point: Stage 3 → Stage 4 → selected Stage 5。

## Infra / Inference

```text
Linux + systems
→ containers / observability
→ GPU runtime
→ distributed / serving
→ compiler or kernel (optional depth)
```

必做：系统设计、网络/存储、PyTorch runtime、profiling、SLO、容量与事故恢复。

作品：可量化地改进 latency/throughput/utilization/reliability 中至少一项。

Recommended branch point: Stage 2/3 → Stage 5 systems / inference。

## 产品 / AI PM

```text
user research + product sense
→ AI capability literacy
→ metrics and experiment
→ safety/cost trade-offs
→ API/platform or domain depth
```

必做：任务分解、能力契约、指标、数据解释、风险、技术沟通。

作品：端到端决策 case，包含“不做什么”和回滚条件。

Recommended branch point: Stage 2 + Stage 3 explain-level → product specialization。

## Solutions Architect / FDE

```text
software + cloud
→ domain workflow
→ prototype
→ architecture + integration
→ delivery + adoption
```

必做：系统架构、数据/安全、项目交付、行业沟通、培训、反馈回流。

作品：完整行业案例，含假设/约束/架构/eval/部署/adoption。

Recommended branch point: Stage 3 → Stage 4 → selected Stage 5。

## Safety / Evals / Governance

```text
ML + statistics + security literacy
→ risk taxonomy
→ evaluation design
→ red team / mitigation
→ production measurement / governance
```

必做：威胁建模、测试集、scoring、coverage、残余风险、政策/工程控制。

作品：一个系统的 eval 和 risk-control package，不只是一份政策总结。

Recommended branch point: Stage 2 → Stage 3 literacy → eval / safety specialization。

## 每条路径的最小每周节奏

| 时间 | 产出 |
| --- | --- |
| 2–3 小时 | 读一个概念并写自己的系统图/反例 |
| 3–5 小时 | 构建或改进一小块可运行系统 |
| 1 小时 | 写 failure log 与下一步假设 |
| 每两周 | 把一段工作整理成可展示证据 |

不要把“看了多少课程”当作主要进度条。
