---
type: skill
skill_category: Programming
status: developing
stability: current
created: 2026-08-31
updated: 2026-08-31
review_after: 2026-11-30
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
prerequisites:
  - "[[Software-Design-and-Architecture]]"
recommended_foundations:
  - "[[Data-Structures-and-Algorithms]]"
related_concepts:
  - "[[HTTP-API]]"
  - "[[LLM-API-and-Structured-Outputs]]"
sample_batch: enterprise-applied-ai-2026-08
---

# TypeScript / JavaScript

## Skill Boundary

本卡覆盖能在 Node 或浏览器中交付可靠的异步 API/LLM 客户端：类型、模块、Promise、HTTP、JSON Schema、流式输出、错误和测试。React 只在目标是全栈 UI 时作为可选延伸；本卡不把 React 当作语言前置。

## 为什么岗位需要它

Notion、Ramp、Atlassian、Glean、Zapier 等样本把 TypeScript/JavaScript 与 API、异步工作流或产品交付绑定；Atlassian 明确将 Python、TypeScript、Go 写成语言选项，不能解读成三者同时必需。

## Role Demand

应用工程/FDE 需要实现 Node 服务、SDK、MCP adapter 和审批 UI；平台岗位更关心事件循环、超时和流式 backpressure。PM 只需读懂接口和故障边界。

## Job Evidence

[[Notion-Software-Engineer-AI-Workflows-2026-08]]、[[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]、[[Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08]]、[[Ramp-Software-Engineer-Frontend-Revenue-2026-08]] 的 `Skill Extraction` 提供 Batch B 证据；每条证据保留 Requirements/Responsibilities 来源段。

## 前置 Skills

硬前置是 [[Software-Design-and-Architecture]]；[[Data-Structures-and-Algorithms]] 是推荐基础而非 Applied AI 语言学习的硬门槛。

## 学习范围

运行时（Node、浏览器）、类型系统、ES modules、npm、Promise/async-await、event loop、fetch/HTTP、JSON 与 schema validation、非 2xx、stream、超时、retry、日志、环境变量与 secret、单元/集成 tests。

## 核心知识

- 用 `unknown`、判别联合和窄化承接不可信 JSON；不要用 `any` 掩盖 schema 漂移。
- 以 `AbortController` 实现超时，以指数退避区分可重试 429/5xx 与不可重试 4xx；重试必须带 request id 和幂等策略。
- 解释 microtask、event loop 与并发 Promise 的关系；流式响应要处理半包、取消和背压。
- 使用 `.env`/系统 secret 注入，不把 key 写入仓库；测试替换真实 provider。

## Practice

完成一个 TypeScript LLM/API client：`async/await` 调用、AbortController 超时、429/5xx 指数重试、非 2xx 错误分类、结构化响应 JSON Schema 校验、流式 token 聚合、脱敏日志和环境 secret；为成功、HTTP、schema、timeout、retry 写测试。

## Pass Evidence

审阅者必须能在测试和 trace 中定位：Promise/async 失败、schema 失败、HTTP 失败、timeout、retry、日志字段和测试断言；README 可从零运行且没有真实 key。React 仅在提交 UI 时检查组件状态，不作为基础通过条件。

## 常见失败

把 TypeScript 类型当运行时验证；并发请求没有取消；所有错误都重试；流式半包导致 JSON 损坏；把 key 放进前端 bundle；只测 happy path。

## 不需要深挖到什么程度

不要求先掌握编译器实现或 React 全生态；能解释本项目的 runtime、边界和失败重放即可。

## Related Knowledge

[[HTTP-API]]、[[LLM-API-and-Structured-Outputs]]、[[Tool-Calling-and-Action-Contracts]]、[[Software-Design-and-Architecture]]

## Practice Boundary

本卡的完成线是可靠客户端与测试，不是训练模型或构建完整代理编排器。

## Actual Evidence

完成 Practice 后用 [[Evidence-Card]] 记录一次失败重放、修复和回归结果，并回链目标 Role。

## Sources

### Official / normative

- https://developer.mozilla.org/en-US/docs/Web/JavaScript
- https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick

### Job evidence

- [[Notion-Software-Engineer-AI-Workflows-2026-08]]
- [[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]
- [[Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08]]

### Practice tutorial

- [[Obsidian-CLI-AI-Agent-Automation]]
