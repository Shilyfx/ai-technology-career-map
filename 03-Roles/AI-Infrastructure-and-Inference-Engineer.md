---
type: role
role_family: ai-infrastructure
sample_count: 10
status: developing
snapshot_date: 2026-08-31
created: 2026-08-24
updated: 2026-08-31
review_after: 2026-11-24
aliases:
  - AI Infra Engineer
  - Inference Engineer
  - Agent Runtime Engineer
  - Agent Platform Engineer
---

# AI Infrastructure and Inference Engineer

## 主要使命

让训练与推理在真实硬件和规模上高效、稳定、可观察、可恢复。成功通常由利用率、吞吐、尾延迟、故障率、开发速度和成本衡量。

## 技能栈分层

```text
Linux / network / storage / distributed systems
→ containers / orchestration / observability
→ GPU/NPU + PyTorch runtime
→ parallelism / scheduling / memory
→ CUDA/NCCL/Triton/compiler/kernel（深度方向）
```

## 典型工作

- 训练集群、作业调度、checkpoint 与容错；
- 模型服务、batching、KV Cache、路由与缓存；
- profiling、kernel、通信、显存和拓扑优化；
- SLO、容量、事故响应、成本治理；
- 与模型团队做算法—系统协同。

## 作品证据

- 一份真实 profile 与瓶颈假设；
- 前后对比：p95、throughput、memory、utilization、quality；
- 故障注入、恢复和回滚；
- 解释优化为何成立、在哪些负载下失效。

## Sample Observations

本批 OpenAI、Anthropic 和 Huawei Job Samples 共同出现 PyTorch/GPU、分布式系统、推理性能和硬件适配；vLLM/SGLang、量化、KV Cache、编译器等是部分样本的专项信号，不是统一入门要求。

来源：[OpenAI Model Inference](https://openai.com/careers/software-engineer-model-inference-san-francisco/)、[华为 AI 大模型架构师](https://career.huawei.com/reccampportal/portal5/social-recruitment-detail.html?dataSource=1&jobId=28183)、[华为 AI 底层软件岗位](https://career.huawei.com/reccampportal/portal5/social-recruitment-detail.html?dataSource=1&jobId=32189)

## Sample Basis

10 curated platform/runtime samples (8 Batch A frontier/model/infra cards + 2 Batch B ServiceNow Agent Platform cards). Employers are OpenAI, Anthropic, Huawei and ServiceNow/Moveworks; regions are US, Switzerland/Europe and China. Seniority is senior/staff; subtracks are inference, GPU/runtime, safeguards and agent-platform.

## Evidence Basis

Based on 8 Job Samples in [[Job-Sample-Index]]; employers, regions and seniority are summarized in this profile. Confidence is high for repeated explicit signals and medium for partial or inferred signals.

## Main Deliverables

High-throughput, low-tail-latency, observable and recoverable training/inference platform.

## Responsibility Clusters

Runtime/kernels; distributed execution; serving/capacity; profiling; reliability/cost.

## Skill Profile

| Skill | Required N | Preferred N | Responsibility N | Inferred N | Sample N | Priority | Target Depth | Confidence |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| [[TypeScript-JavaScript]] | 0 | 0 | 0 | 0 | 0 | Prerequisite | explain/use | context |
| [[Python]] | 0 | 0 | 0 | 1 | 1 | Prerequisite | explain/use | low/medium |
| [[LLM-API-and-Structured-Outputs]] | 0 | 0 | 0 | 0 | 0 | Common | explain/use | context |
| [[Tool-Calling-and-Action-Contracts]] | 0 | 0 | 2 | 0 | 2 | Specialized | use→implement | low/medium |
| [[Agent-Orchestration-and-State]] | 0 | 0 | 1 | 1 | 1 | Specialized | use→implement | low/medium |
| [[Workflow-Automation-and-Business-Process-Design]] | 0 | 0 | 1 | 0 | 1 | Specialized | use→implement | low/medium |
| [[MCP-and-Agent-Interoperability]] | 0 | 0 | 0 | 0 | 0 | Specialized | use→implement | context |
| [[Enterprise-Integrations-and-Connectors]] | 0 | 0 | 0 | 2 | 2 | Common | explain/use | low/medium |
| [[Agent-Evals-and-Trace-Debugging]] | 0 | 0 | 2 | 1 | 2 | Specialized | use→implement | low/medium |
| [[Human-in-the-Loop-and-Agent-Guardrails]] | 0 | 0 | 1 | 0 | 1 | Common | explain/use | low/medium |

Evidence strength is based on Batch B row classifications; `responsibility` and `preferred` are not counted as required.
## Non-skill Gates

On-call ownership, numerical correctness, hardware trade-offs and incident communication.

## Seniority/Subtrack Differences

Serving roles emphasize SLO/capacity; kernel roles emphasize low-level optimization; **Agent Runtime / Agent Platform** roles add state machines, tool boundaries, async recovery, eval traces and protocol adapters. This is a specialized applied-AI branch, not a replacement for GPU/serving fundamentals.

## Portfolio Evidence

Profile trace, load test, capacity model, failure injection, rollback and measured optimization.

## Adjacent Roles

[[Research-Engineer]]、[[ML-and-AI-Engineer]]、[[AI-Solutions-Architect-and-FDE]]。

## Source Limitations

Samples overrepresent frontier labs and senior specialists; hardware stacks differ by employer.

## Refresh

Review tools and hardware signals every 30–60 days; stable distributed concepts every 180–365 days.

## Learning prerequisites

先补 [[Data-Structures-and-Algorithms]]、[[Linux]]、[[Testing]] 和 [[Software-Design-and-Architecture]]，再进入 [[Distributed-Systems]]、[[CUDA-GPU-Basics]]、[[Model-Serving]] 与 [[Observability]]。若目标是 Agent Runtime / Agent Platform，再进入 [[Agent-Orchestration-and-State]] → [[Tool-Calling-and-Action-Contracts]] → [[Agent-Evals-and-Trace-Debugging]] → [[MCP-and-Agent-Interoperability]]；生产环境同时练习 [[Security-Privacy-and-Access-Control]]。
