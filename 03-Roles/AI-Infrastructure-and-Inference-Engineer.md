---
type: role
role_family: ai-infrastructure
sample_count: 8
status: developing
snapshot_date: 2026-08-24
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

8 samples across OpenAI, Anthropic and Huawei inference/runtime/performance postings.

## Evidence Basis

Based on 8 Job Samples in [[Job-Sample-Index]]; employers, regions and seniority are summarized in this profile. Confidence is high for repeated explicit signals and medium for partial or inferred signals.

## Main Deliverables

High-throughput, low-tail-latency, observable and recoverable training/inference platform.

## Responsibility Clusters

Runtime/kernels; distributed execution; serving/capacity; profiling; reliability/cost.

## Skill Profile

| Skill | Required | Preferred | Responsibility | Sample N | Role Priority | Target Depth | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [[Linux]] | yes |  | systems operation | 3 | Prerequisite | use | high | Job Samples |
| [[Distributed-Systems]] | yes |  | cluster execution | 8 | Core | implement | high | Job Samples |
| [[CUDA-GPU-Basics]] | yes |  | accelerator performance | 6 | Core | optimize | high | Job Samples |
| [[Model-Serving]] | yes |  | production inference | 6 | Core | implement | high | Job Samples |
| [[Observability]] | yes |  | SLO and profiling | 5 | Common | implement | medium | Job Samples |
| [[Agent-Orchestration-and-State]] | specialized |  | runtime state/checkpoint | 1 | Specialized | implement→optimize | medium | [[ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08]] |
| [[Tool-Calling-and-Action-Contracts]] | specialized |  | action execution boundary | 2 | Specialized | implement | medium | [[ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08]] |
| [[Agent-Evals-and-Trace-Debugging]] | specialized |  | trajectory/eval platform | 2 | Specialized | implement→optimize | medium | [[ServiceNow-Staff-Agent-Eval-Platform-2026-08]] |
| [[MCP-and-Agent-Interoperability]] | preferred |  | protocol adapters | 2 | Specialized | use→implement | medium | [[Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08]] |

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
