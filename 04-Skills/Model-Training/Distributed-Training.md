---
type: skill
skill_category: model-training
status: developing
stability: current
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
roles:
  - "[[Research Engineer]]"
  - "[[ML-and-AI-Engineer]]"
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
prerequisites:
  - "[[PyTorch]]"
  - "[[Distributed-Systems]]"
related_concepts:
  - "[[AI-Infrastructure-and-MLOps]]"
---

# Distributed Training

## 为什么岗位需要它
前沿训练、推理和数据管线都受多卡通信、容错、吞吐和成本约束。

## Role Demand
Research/Infra 为 Core；ML 为 Common，其他角色只需理解成本。证据见 [[Apple-Machine-Learning-Engineer-SIML-Cupertino-2026-07]]。

## 在岗位中怎么使用
选择并行策略、同步/异步边界、checkpoint、通信和故障恢复。

## Role-specific Target Depth
Infra/研究 optimize；ML implement/use；PM/FDE explain。

## 前置 Skills
[[PyTorch]]、[[Distributed-Systems]]。

## 学习范围
data/model parallel、collective、梯度同步、网络、容错和资源调度。

## 核心知识
通信成本、扩展效率、数值一致性和恢复语义。

## Practice
让小模型在两张卡或模拟 rank 上运行并记录吞吐/失败恢复。

## Pass Evidence
能用数据解释增加设备后为何变快或变慢。

## 常见失败 / 误区
只加 GPU 不看通信；把单卡结果直接外推；没有恢复测试。

## 不需要深挖到什么程度
非 Infra 岗位先会读并发配置和故障日志，不必先写通信库。

## Related Concepts
[[AI-Infrastructure-and-MLOps]]、[[CUDA-GPU-Basics]]。

## Actual Evidence
尚无用户能力结论；关联 [[Evidence-Card]]。

## Sources
[[Apple-Machine-Learning-Engineer-SIML-Cupertino-2026-07]]、[[Huawei-Algorithm-Expert-Multimodal-Beijing-2026-08]]。
