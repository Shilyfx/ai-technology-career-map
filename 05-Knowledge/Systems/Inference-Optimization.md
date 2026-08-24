---
type: concept
domain: systems
status: developing
stability: emerging
depth: optimize
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
related:
  - "[[AI-Infrastructure-and-MLOps]]"
  - "[[Transformer-and-Foundation-Models]]"
---

# Inference Optimization

## 目标不是单独追求速度

推理优化在质量、延迟、吞吐、显存、成本、可靠性和工程复杂度之间取舍。

```text
request
→ tokenize / preprocess
→ schedule and batch
→ model forward / decode
→ cache / tool / postprocess
→ response
```

## 核心指标

- time to first token（TTFT）；
- inter-token latency；
- requests/tokens per second；
- p50/p95/p99 latency；
- GPU memory 与 utilization；
- quality under optimization；
- cost per successful task。

## 常见技术

| 技术 | 主要收益 | 风险/代价 |
| --- | --- | --- |
| batching / continuous batching | 提高吞吐 | 排队与尾延迟 |
| KV Cache / paged attention | 减少重复计算 | 显存与调度复杂度 |
| quantization | 降显存和计算 | 精度/能力回退 |
| speculative decoding | 加速生成 | draft 模型与接受率 |
| tensor/pipeline parallel | 扩展到多设备 | 通信和气泡 |
| kernel fusion / Triton/CUDA | 提高硬件效率 | 维护与硬件绑定 |
| routing / caching | 降成本与延迟 | 一致性、新鲜度、隐私 |

## 能力深度

```text
使用服务框架
→ 解释指标和瓶颈
→ 配置与 profiling
→ 修改调度/内存/并行
→ 编写 kernel / compiler / runtime
```

不是所有 AI 工程师都要写 CUDA，但所有上线模型的人都应能测延迟、吞吐、成本和质量回退。

## 当前岗位证据

OpenAI Model Inference 岗位明确要求 PyTorch、NVIDIA GPU、NCCL、CUDA、InfiniBand/MPI/NVLink 与生产分布式系统；华为官方岗位样本还列出 KV Cache、量化、投机推理、vLLM/SGLang、算子融合与国产硬件适配。见 [[2026-08-AI-Job-Market-Snapshot]]。

## 官方入口

- [vLLM documentation](https://docs.vllm.ai/)
- [NVIDIA CUDA documentation](https://docs.nvidia.com/cuda/)
