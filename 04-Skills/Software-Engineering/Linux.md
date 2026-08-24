---
type: skill
skill_category: software-engineering
status: developing
stability: stable
created: 2026-08-24
updated: 2026-08-24
review_after: 2027-02-24
roles:
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[Research-Engineer]]"
  - "[[Data-and-AI-Engineer]]"
  - "[[AI-Application-Engineer]]"
prerequisites: []
related_concepts:
  - "[[AI-Infrastructure-and-MLOps]]"
  - "[[Math-Data-and-Software-Foundations]]"
---

# Linux

## 为什么岗位需要它

训练、推理、容器、数据管道和生产服务通常运行在 Linux；岗位要求往往以系统调试和运行责任出现。

## Role Demand

| Role | Priority | Target Depth | Job Evidence | Note |
| --- | --- | --- | --- | --- |
| Infra / Inference | Core | implement | [[OpenAI-Software-Engineer-Model-Inference-San-Francisco-2026-08]] | 生产系统 |
| Data / AI Engineer | Common | use | [[Huawei-AI-Bottom-Software-Shanghai-2026-08]] | 系统软件 |
| Research Engineer | Common | use | [[Anthropic-ML-Infrastructure-Engineer-Safeguards-San-Francisco-2026-08]] | 研究基础设施 |

## 在岗位中怎么使用

进程、文件、网络、权限、日志、资源、shell、服务与故障排查。

## Role-specific Target Depth

Infra 需要 implement/optimize；应用工程只需能部署和诊断自己的服务。

## 前置 Skills

[[Git]]。

## 学习范围

进程/线程、文件系统、网络、权限、systemd、容器边界和资源限制。

## 核心知识

CPU/内存/IO、信号、端口、日志和可观测性。

## Practice

部署一个服务，加入资源限制、日志、健康检查和故障恢复演练。

## Pass Evidence

能用命令解释一次 CPU、内存或网络异常，并给出可复查修复。

## 常见失败 / 误区

只会重启服务、不看资源状态；权限问题被误判成模型问题。

## 不需要深挖到什么程度

非 Infra 岗位不必写内核模块，但不能把 Linux 当不可见黑盒。

## Related Concepts

[[AI-Infrastructure-and-MLOps]]、[[Inference-Optimization]]。

## Actual Evidence

尚无用户能力结论；使用 [[Evidence-Card]] 创建实际记录。

## Sources

[[OpenAI-Software-Engineer-Model-Inference-San-Francisco-2026-08]]、[[Huawei-AI-Bottom-Software-Shanghai-2026-08]]。
