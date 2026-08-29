---
type: concept
domain: foundations
status: validated
stability: stable
depth: use
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Learning-Path]]"
  - "[[Role-Skill-Matrix]]"
  - "[[Data-Structures-and-Algorithms]]"
  - "[[Statistics-and-Experiment-Design]]"
  - "[[Databases-and-Data-Modeling]]"
---

# Math, Data and Software Foundations

> AI 岗位的共同底座不是“会写 prompt”，而是能把数据、模型和软件连接成可验证系统。

## 数学：学到能支持判断

| 区域 | 最低目标 | 深挖岗位 |
| --- | --- | --- |
| 线性代数 | 理解向量、矩阵、投影、相似度、张量 shape | 研究、模型、性能优化 |
| 概率统计 | 理解分布、期望、方差、抽样、置信与偏差 | 研究、评测、产品实验 |
| 微积分与优化 | 理解梯度、链式法则、学习率与局部优化 | 研究、训练 |
| 数值计算 | 理解精度、稳定性、溢出与近似 | Infra、推理、训练 |

不要求所有岗位先完成数学课程。要求是：遇到 loss、metric、sampling 或 quantization 时，能回到相关数学而不是只背 API。

## 数据：从“文件”升级为“证据”

```text
source → schema → cleaning → labeling → split → version → lineage → quality checks
```

最低能力：Python、SQL、表格/JSON/Parquet、缺失与异常处理、数据切分、去重、权限与 PII 意识。

## 软件工程：从 notebook 升级为系统

- Git 与可审查变更；
- 模块边界、配置、依赖管理；
- 单元测试、集成测试、回归测试；
- API、并发、队列、缓存、数据库基础；
- Linux、容器、日志、错误处理；
- 性能 profiling 与容量意识。

## 为什么岗位数据强调这些能力

Stanford AI Index 2026 的美国 AI 岗位统计中，高频专业技能不仅有 Python 和计算机科学，还包括 scalability、automation、workflow management、data analysis、SQL、project management 和 AWS。详见 [[2026-08-AI-Job-Market-Snapshot]]。

## 最小实践

选择一个小数据集，交付：

1. 带参数的数据处理脚本；
2. schema 与数据质量检查；
3. 固定 split manifest；
4. README、环境与一条可重复运行命令；
5. 至少一个失败测试。
