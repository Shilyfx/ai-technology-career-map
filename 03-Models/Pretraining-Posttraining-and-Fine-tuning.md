---
type: concept
domain: training
status: seed
stability: current
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Transformer-and-Foundation-Models]]"
  - "[[Training-Evaluation-and-Generalization]]"
---

# Pretraining, Post-training and Fine-tuning

## 训练阶段地图

```mermaid
flowchart LR
  P["Pretraining\n学习通用表征/预测"] --> S["SFT\n学习任务与指令格式"]
  S --> A["Preference / Alignment\n偏好、安全、行为"]
  A --> R["RL / Reasoning\n对可验证目标优化"]
  R --> D["Deployment feedback\n持续评测与更新"]
```

不同团队会合并、跳过或重复这些阶段；术语边界并不完全统一。

## 常见方法

| 方法 | 目的 | 关键约束 |
| --- | --- | --- |
| Continued pretraining | 适配领域分布或语言 | 数据质量、遗忘、成本 |
| SFT | 学习指令、格式、示例行为 | 示范数据覆盖与一致性 |
| PEFT / LoRA | 用少量可训练参数适配模型 | 能力边界、部署合并 |
| RLHF / RLAIF | 用人类或 AI 反馈优化偏好 | reward hacking、偏好代表性 |
| DPO 类方法 | 直接用偏好对优化策略 | 偏好数据与 reference 假设 |
| PPO / GRPO 类 RL | 对奖励或可验证结果优化 | 稳定性、奖励设计、计算成本 |
| Distillation | 把教师行为压缩到学生模型 | 能力损失、数据与许可 |

## 先问哪种改变最便宜

```text
提示/context 是否足够？
→ 检索或工具是否能补知识/行动？
→ 少量 SFT/PEFT 是否足够？
→ 才考虑更重的后训练或预训练
```

## 评测要求

- 冻结任务集与 baseline；
- 区分格式改善、知识改善和推理改善；
- 检查通用能力回退与安全副作用；
- 记录训练数据、seed、checkpoint、硬件、代码版本；
- 在真实推理配置下测成本、延迟与稳定性。

## 一手资料

- Ouyang et al., [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)
- Rafailov et al., [Direct Preference Optimization](https://arxiv.org/abs/2305.18290)
