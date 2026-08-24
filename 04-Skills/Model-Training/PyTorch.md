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
  - "[[Python]]"
  - "[[Transformer-LLM-Fundamentals]]"
related_concepts:
  - "[[Pretraining-Posttraining-and-Fine-tuning]]"
---

# PyTorch

## 为什么岗位需要它
它是多份训练、研究和推理岗位中的实现载体；真正需要的是张量、autograd、性能和调试能力。

## Role Demand
Research/ML 为 Core；Infra 按 runtime 方向 Specialized。证据见 [[OpenAI-Software-Engineer-Model-Inference-San-Francisco-2026-08]]。

## Job Evidence

[[OpenAI-Software-Engineer-Model-Inference-San-Francisco-2026-08]]、[[Apple-Machine-Learning-Engineer-Video-Cupertino-2026-06]] 的 `Skill Extraction` 是本 Skill 的 Job Evidence；只把明确要求作为 required 证据，职责推断保留为 inferred。

## 在岗位中怎么使用
写模型、数据 loader、训练循环、checkpoint、profiling 和评测代码。

## Role-specific Target Depth
ML/研究 implement；应用通常 recognize/use；infra 需理解执行和性能边界。

## 前置 Skills
[[Python]]、[[Transformer-LLM-Fundamentals]]。

## 学习范围
tensors、autograd、modules、data、mixed precision、checkpoint 和 profiler。

## 核心知识
形状、设备、梯度、数值稳定性和内存。

## Practice
实现一个小模型训练、验证、checkpoint 恢复和 profiler 报告。

## Pass Evidence
能解释一次 shape/device/gradient 错误并提供测试防回归。

## 常见失败
只会复制 notebook；忽略 device、seed、数据泄漏和显存。

## 不需要深挖到什么程度
应用岗位不因 SDK 依赖就学习 kernel；按目标岗位加深。

## Related Knowledge
[[Pretraining-Posttraining-and-Fine-tuning]]、[[Distributed-Training]]。

## Actual Evidence
尚无用户能力结论；用 [[Evidence-Card]] 记录。

## Sources
[[OpenAI-Software-Engineer-Model-Inference-San-Francisco-2026-08]]、[[Apple-Machine-Learning-Engineer-Video-Cupertino-2026-06]]。
