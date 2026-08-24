---
type: role
role_family: ai-infrastructure
sample_count: 8
status: developing
snapshot_date: 2026-08-24
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
aliases:
  - AI Infra Engineer
  - Inference Engineer
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

## 当前岗位证据

OpenAI Model Inference 样本列出 PyTorch、GPU、CUDA、NCCL、InfiniBand/MPI/NVLink 与生产分布式系统。华为样本进一步列出 vLLM/SGLang、量化、KV Cache、投机推理、算子融合、MLIR/LLVM/TVM/Triton 与国产硬件适配。

来源：[OpenAI Model Inference](https://openai.com/careers/software-engineer-model-inference-san-francisco/)、[华为 AI 大模型架构师](https://career.huawei.com/reccampportal/portal5/social-recruitment-detail.html?dataSource=1&jobId=28183)、[华为 AI 底层软件岗位](https://career.huawei.com/reccampportal/portal5/social-recruitment-detail.html?dataSource=1&jobId=32189)

## Sample Basis

8 samples across OpenAI, Anthropic and Huawei inference/runtime/performance postings.

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

## Non-skill Gates

On-call ownership, numerical correctness, hardware trade-offs and incident communication.

## Seniority/Subtrack Differences

Serving roles emphasize SLO/capacity; kernel roles emphasize low-level optimization; architect roles add delivery.

## Portfolio Evidence

Profile trace, load test, capacity model, failure injection, rollback and measured optimization.

## Adjacent Roles

[[Research-Engineer]]、[[ML-and-AI-Engineer]]、[[AI-Solutions-Architect-and-FDE]]。

## Source Limitations

Samples overrepresent frontier labs and senior specialists; hardware stacks differ by employer.

## Refresh

Review tools and hardware signals every 30–60 days; stable distributed concepts every 180–365 days.
