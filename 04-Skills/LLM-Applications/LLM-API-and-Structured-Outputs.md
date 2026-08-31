---
type: skill
skill_category: LLM-Applications
status: developing
stability: current
created: 2026-08-31
updated: 2026-09-01
review_after: 2026-11-30
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[AI-Product-Manager]]"
prerequisites:
  - "[[HTTP-API]]"
recommended_foundations:
  - "[[Python]]"
  - "[[TypeScript-JavaScript]]"
  - "[[Software-Design-and-Architecture]]"
related_concepts:
  - "[[Prompt-and-Context-Engineering]]"
  - "[[Tool-Calling-and-Action-Contracts]]"
sample_batch: enterprise-applied-ai-2026-08
---

# LLM API 与结构化输出

## Skill Boundary

本卡把模型调用当作可观测的接口契约：请求/响应、模型选择边界、stream、token/latency/cost、限流、重试、provider 错误、结构化输出与 refusal/fallback。它不等同于 prompt 技巧、RAG 或 tool calling。

## 为什么岗位需要它

Applied AI/FDE 岗位要把模型接入产品和客户系统；结构化输出是下游代码可以验证的 interface contract，而不是“模型大概返回 JSON”。

## Role Demand

工程师需能比较模型能力、上下文和成本，处理流式/非流式两条路径；PM/FDE 需能定义 schema、SLO、预算和降级条件。

## Job Evidence

[[Notion-Software-Engineer-AI-Workflows-2026-08]]、[[Ramp-Applied-AI-Engineer-2026-08]]、[[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]] 与 [[Warp-Forward-Deployed-Engineer-2026-08]] 的 evidence rows 将“生产 LLM/结构化抽取”与职责分别标为 required 或 responsibility。

## 前置 Skills

硬前置：[[HTTP-API]]；推荐先会 [[Python]] 或 [[TypeScript-JavaScript]]。不要求先学 RAG 或 Agent。

## 学习范围

请求参数、provider/model 选择边界、流式事件、输入输出 token、延迟分位数、成本估算、429/5xx、退避与 request id、JSON Schema 的 enum/nullable/optional、schema version、fallback、refusal、截断和 invalid output。

## 核心知识

- 把“模型答得好”拆成可测的接口：schema 版本、必填字段、枚举、可空与缺省值。
- 预算同时记录 token、请求数、p50/p95 latency 和 provider 错误率；只在安全条件下自动 retry。
- 流式路径不能假设每个 chunk 是完整 JSON；最终聚合后再验证，并保存拒答原因。
- fallback 可以换模型、走人工或返回可解释的 `unknown`，不能静默伪造字段。

## Practice

实现一个 provider-neutral client：同一任务支持 stream/non-stream，输出 JSON Schema（含 enum、nullable、optional 和 `schema_version`），记录 token/cost/latency，处理 rate limit、provider error、timeout、refusal、invalid output，并按策略 fallback。

## Pass Evidence

提交一份契约测试：有效输出、枚举越界、缺字段、null、版本不兼容、拒答、截断、429、5xx、超时各有 fixture；trace 能回放模型选择、token、延迟、成本、重试和最终 fallback。

## 常见失败

把 JSON mode 当 schema validation；把 nullable 当 optional；无限重试 4xx；流式首 token 延迟未计入；成本只看单次而不看分位数；provider refusal 被当作空成功。

## 不需要深挖到什么程度

不要求推导 Transformer 或训练 loss；只需能根据任务、SLO、预算和风险选择调用策略。

## Related Knowledge

[[HTTP-API]]、[[Prompt-and-Context-Engineering]]、[[Tool-Calling-and-Action-Contracts]]、[[Agent-Evals-and-Trace-Debugging]]

## Practice Boundary

通过线是稳定的模型接口契约；tool schema、代理状态和业务审批分别由相邻 Skills 承担。

## Actual Evidence

用 [[Evidence-Card]] 保存一次 schema 失败和一次成本/延迟优化前后对比。

## Sources

### Official / normative

- https://platform.openai.com/docs/guides/structured-outputs
- https://platform.openai.com/docs/guides/text?api-mode=responses

### Job evidence

- [[Notion-Software-Engineer-AI-Workflows-2026-08]]
- [[Ramp-Applied-AI-Engineer-2026-08]]
- [[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]]
