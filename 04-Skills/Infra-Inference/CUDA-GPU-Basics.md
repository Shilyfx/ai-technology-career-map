---
type: skill
skill_category: infra-inference
status: developing
stability: current
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
roles:
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[Research Engineer]]"
  - "[[ML-and-AI-Engineer]]"
prerequisites:
  - "[[Linux]]"
  - "[[PyTorch]]"
related_concepts:
  - "[[Inference-Optimization]]"
---

# CUDA and GPU Basics

## 为什么岗位需要它
GPU 内存、kernel、通信和利用率决定训练/推理的性能与成本上限。

## Role Demand
Infra 为 Core；研究/ML 按性能方向 Specialized。证据见 [[OpenAI-Software-Engineer-Inference-Performance-San-Francisco-2026-08]]。

## 在岗位中怎么使用
读 profiler、定位 kernel/内存/通信瓶颈，并在正确性测试后优化。

## Role-specific Target Depth
Infra optimize；研究/ML use；PM/FDE 只需 explain 成本约束。

## 前置 Skills
[[Linux]]、[[PyTorch]]。

## 学习范围
device/memory、kernel、streams、同步、NCCL、profiling 和低精度。

## 核心知识
计算/内存带宽、显存、同步和数值误差。

## Practice
对一个张量算子做 profiler 前后对比并写出瓶颈假设。

## Pass Evidence
能用 trace 和显存/吞吐数据验证优化是否真实。

## 常见失败 / 误区
只看 GPU 利用率；忽略数据/通信；优化后不测数值一致性。

## 不需要深挖到什么程度
普通应用无需先写 CUDA kernel；岗位需要时从 profiling 开始。

## Related Concepts
[[Inference-Optimization]]、[[Distributed-Training]]。

## Actual Evidence
尚无用户能力结论；记录在 [[Evidence-Card]]。

## Sources
[[OpenAI-Software-Engineer-Inference-Performance-San-Francisco-2026-08]]、[[Huawei-AI-Bottom-Software-Shanghai-2026-08]]。
