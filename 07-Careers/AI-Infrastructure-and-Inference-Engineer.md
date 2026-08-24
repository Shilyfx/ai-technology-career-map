---
type: role
role_family: ai-infrastructure
status: seed
snapshot_date: 2026-08-24
created: 2026-08-24
updated: 2026-08-24
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
