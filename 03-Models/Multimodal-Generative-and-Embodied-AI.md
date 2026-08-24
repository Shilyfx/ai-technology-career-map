---
type: concept
domain: models
status: seed
stability: emerging
created: 2026-08-24
updated: 2026-08-24
aliases:
  - 多模态 生成式与具身 AI
related:
  - "[[Transformer-and-Foundation-Models]]"
  - "[[Technology-Radar-2026-08]]"
---

# Multimodal, Generative and Embodied AI

## 三个不要混用的概念

| 概念 | 核心 | 代表任务 |
| --- | --- | --- |
| Generative AI | 学习并生成数据分布中的样本 | 文本、图像、音频、视频生成 |
| Multimodal AI | 联合理解或生成多种模态 | 图文问答、语音交互、视频理解 |
| Embodied AI | 在物理或模拟环境中感知、规划并行动 | 机器人操作、导航、控制 |

## 常见模型家族

- **LLM**：语言序列建模；
- **VLM**：视觉与语言的联合表征、理解或生成；
- **Diffusion model**：通过逐步去噪学习生成过程；
- **Speech model**：ASR、TTS、speech-to-speech；
- **World model**：学习环境动态以支持预测与规划；
- **VLA**：把视觉、语言与动作连接起来。

## 系统难点

多模态不是简单拼接输入。需要处理时间同步、坐标/patch、模态缺失、对齐数据、输出评测与模态间冲突。具身系统还要面对实时性、安全、sim2real、硬件限制和不可逆行动。

## 岗位映射

- 算法研究：跨模态对齐、生成目标、表示学习；
- Research Engineer：训练管线、数据规模、评测与分布式系统；
- Infra/Inference：高吞吐、多模态缓存、kernel 与设备适配；
- Robotics：C++、控制、传感器、仿真与系统安全；
- Product：用户交互、模态选择、失败兜底与成本。

中国官方岗位样本中，华为把多模态训练、跨模态对齐、Diffusion/DiT、分布式训练和推理优化放在同一复杂系统链路中，说明该方向通常要求算法与系统协同，而不是只会调用视觉语言 API。见 [[2026-08-AI-Job-Market-Snapshot]]。
