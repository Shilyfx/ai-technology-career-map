---
type: system
page_kind: job-skill-extraction-rules
status: reference
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-09-24
related:
  - "[[Job-Sample-Index]]"
  - "[[Role-Map]]"
  - "[[Skill-Index]]"
---

# Job-Skill Extraction Rules

## Source hierarchy

1. 公司官方具体职位页面；2. 官方 careers/search 页面；3. 官方 role description；4. 官方招聘 API。市场报告只能支持宏观信号，不能替代 Role-specific Job Sample。

## Capture and copyright

每个样本记录 company、title、location、region、seniority、source URL、posted/retrieved、source status 和 access limitation。只写结构化摘要与短引用，不复制完整 JD。

Applied AI 批次额外记录 `sample_batch`、`company_segment`、`role_subtrack`；这些字段用于控制样本边界和偏差，不代表市场频率。

## Explicit vs inferred

岗位明确写出的工具、职责和要求才计入 `required`、`preferred` 或 `responsibility`。学习上推断的 prerequisite 单独标为 `inferred prerequisite`，不进入 Job frequency。

Skill 页的 `Sources` 必须分开列出 Official / normative、Job evidence、Practice tutorial；教程能说明如何练习，不能证明岗位需求。

## Normalization

`Python 3 → Python`、`K8s → Kubernetes`、`Retrieval Augmented Generation → RAG`、`LLM evaluation / model evals → Evals`。CUDA、NCCL、Triton、MLIR 等保留为不同 Skill，不因都属于性能而过度合并。

## Alternatives and counting

`PyTorch or JAX` 是 alternative framework requirement，不计为两个必需 Skill。一个 Job 中同一归一化 Skill 只计一次；同 URL 不得出现在多个 Job Sample。

## Role priority and depth

`Core` 需要多个独立样本或跨雇主重复出现并直接支撑交付；`Common` 是重复出现但非所有团队必需；`Specialized` 属于 subtrack/senior；`Company-specific` 只属于单一栈；`Prerequisite` 是学习推断。深度参考职责动词与上下文：understand → recognize/explain，use → use，build/design → implement，scale/optimize/profile → optimize，research/invent → research；不确定写 `uncertain`。

## Bias and refresh

保留 region、seniority、employer、sample batch；N 小时写 `2 / 3 samples`，不伪装成市场百分比。active Job Sample 30–60 天复查，过期标 `source_status: expired`，不删除历史证据。

Applied AI 批次是企业应用/Agentic Engineering 定向抽样，不替代 frontier/model-builder 批次；不得用产品名、框架名或多智能体热度自动生成 Skill。
