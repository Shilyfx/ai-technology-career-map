---
type: concept
domain: ml-foundations
status: seed
stability: stable
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Math-Data-and-Software-Foundations]]"
  - "[[Evals-and-Observability]]"
---

# Training, Evaluation and Generalization

## 核心闭环

```mermaid
flowchart LR
  Q["问题与假设"] --> D["数据与 split"]
  D --> B["baseline"]
  B --> T["训练"]
  T --> E["评测"]
  E --> F["失败切片"]
  F --> R["保留 / 放弃 / 下一步"]
```

训练的目标不是“让训练集分数变高”，而是学习在目标分布上有用的规律。评测负责判断这一点是否成立。

## 必须分开的集合

- **Train**：用于更新参数；
- **Validation**：选择超参数、阈值或 checkpoint；
- **Test**：冻结决策后评估泛化；
- **Production/shifted slice**：检查真实分布、长尾与漂移。

数据泄漏、重复样本、患者/用户级切分错误、使用 Test 调参，都会让结果看似更好但证据失效。

## 常见训练概念

| 概念 | 作用 | 常见误区 |
| --- | --- | --- |
| loss | 提供优化信号 | 与业务指标完全等价 |
| optimizer | 更新参数 | 更复杂一定更好 |
| batch | 一次估计梯度的数据 | 只影响速度，不影响训练动态 |
| epoch/step | 训练进度单位 | 不同配置可直接按 epoch 比较 |
| regularization | 限制过拟合 | 能修复错误 split |
| checkpoint | 保存模型状态 | 文件存在就证明训练有效 |

## 评测至少有四层

1. **执行有效性**：代码、数据、checkpoint、seed 是否正确；
2. **总体指标**：accuracy、F1、AUC、Dice、loss 等；
3. **切片与失败样本**：哪些人群、场景、长度、质量条件失败；
4. **决策价值**：相对 baseline 的收益是否覆盖成本与风险。

## 最小验证

给一个实验写出：假设、baseline、唯一变化、split 来源、主要指标、两个 failure slice、停止规则和 keep/drop/next 决策。
