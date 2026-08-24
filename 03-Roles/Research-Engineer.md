---
type: role
role_family: research-engineering
sample_count: 8
status: developing
snapshot_date: 2026-08-24
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
---

# Research Engineer

## 主要使命

把研究想法变成正确、高性能、可扩展的实验系统，并用工程反馈推动研究。它不是“论文少一点的软件工程师”，而是理论与实现之间的桥。

OpenAI 当前通用岗位强调强编程、无 bug 的 ML 代码和大型分布式系统；DeepMind 同样把工程、数学、研究、前沿模型优化与分布式计算基础设施并列。

## 日常工作

- 实现新模型、loss、训练策略和 eval；
- 数据/训练/评测管线与实验工具；
- 分布式训练、性能 profiling、故障恢复；
- 复现论文、定位数值或数据问题；
- 与 Scientist 共同形成研究结论和论文。

## 技能重点

**主深度**：Python、PyTorch/JAX、ML/DL、实验设计、分布式系统、性能与可靠性。

**按方向加深**：CUDA/NCCL、RL、multimodal、data systems、model evals、interpretability。

## 作品证据

- 把单卡/小规模 baseline 扩展到多卡或大数据；
- correctness test、determinism/seed 说明、checkpoint 恢复；
- 吞吐、显存、利用率、失败率前后对比；
- 工程改动如何影响研究问题的清晰解释。

## 常见误区

- 只追性能，不验证结果是否科学有效；
- 只有 notebook，没有测试与恢复；
- 只复述论文，不能定位实现偏差；
- 误以为必须有 PhD；更决定性的证据是研究工程能力，但具体岗位仍可能有学历偏好。

来源：[OpenAI Research Engineer](https://openai.com/careers/research-engineer-san-francisco/)、[Google DeepMind Careers](https://deepmind.google/careers/)

## Sample Basis
8 samples across OpenAI, Anthropic and Huawei research/training/post-training/multimodal roles.

## Main Deliverables
Correct, scalable experiments that connect research hypotheses to measured model behavior.

## Responsibility Clusters
Research implementation; data/training; evals; distributed/performance; scientific communication.

## Skill Profile
| Skill | Required | Preferred | Responsibility | Sample N | Role Priority | Target Depth | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [[Python]] | yes |  | experiment implementation | 8 | Core | implement | high | Job Samples |
| [[ML-Experimentation]] | yes |  | reproducible research | 8 | Core | implement | high | Job Samples |
| [[Model-Evaluation]] | yes |  | scientific conclusion | 6 | Core | implement | high | Job Samples |
| [[PyTorch]] |  | yes | model training | 5 | Common | implement | medium | Job Samples |
| [[Distributed-Training]] |  | yes | scale | 5 | Specialized | optimize | medium | Job Samples |

## Non-skill Gates
Research taste, reproducibility, scientific honesty, communication and persistence through negative results.

## Seniority/Subtrack Differences
Pretraining/post-training tracks emphasize training systems; eval tracks emphasize measurement; algorithm tracks emphasize hypotheses.

## Portfolio Evidence
Reproduction, controlled change, ablation, failure analysis, resource report and rerunnable code.

## Adjacent Roles
[[Research-Scientist]]、[[ML-and-AI-Engineer]]、[[AI-Infrastructure-and-Inference-Engineer]]。

## Source Limitations
Frontier lab and senior bias; some Anthropic pages were only partially visible during capture.

## Refresh
Refresh job evidence every 30–60 days and core research practices every 180–365 days。
