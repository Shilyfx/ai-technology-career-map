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
  - "[[LLM-API-and-Structured-Outputs]]"
recommended_foundations:
  - "[[HTTP-API]]"
  - "[[Enterprise-Integrations-and-Connectors]]"
  - "[[Security-Privacy-and-Access-Control]]"
related_concepts:
  - "[[Human-in-the-Loop-and-Agent-Guardrails]]"
  - "[[Agent-Orchestration-and-State]]"
sample_batch: enterprise-applied-ai-2026-08
---

# Tool Calling 与 Action Contracts

## Skill Boundary

本卡只解决“模型提出动作后，系统如何安全、可重放地执行”：tool/input/output schema、描述、读写与副作用、可逆性、超时/重试/幂等/重复执行、权限/审计、工具分类、结果归一化、不可用和 tool choice。它不负责代理循环本身。

## 为什么岗位需要它

Agentforce、Notion、Ramp、Warp 等岗位的价值在于把模型连接到真实系统；没有 action contract，tool calling 只是不可审计的字符串生成。

## Role Demand

应用工程需要定义 adapter 和执行器；FDE/PM 需要把“读、写、发信、删除、收费”等风险暴露给审批与权限系统。

## Job Evidence

[[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]、[[Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08]]、[[Warp-Forward-Deployed-Engineer-2026-08]] 的 responsibilities 明确提到 tool calls/actions；这些行没有被升级为 universally required。

## 前置 Skills

硬前置：[[LLM-API-and-Structured-Outputs]]；[[HTTP-API]]、[[Enterprise-Integrations-and-Connectors]] 和 [[Security-Privacy-and-Access-Control]] 是推荐基础，安全控制参考 [[Human-in-the-Loop-and-Agent-Guardrails]]。

## 学习范围

工具名称/描述、输入输出 schema、read/write taxonomy、side effect、reversible/irreversible、permission scope、audit event、timeout、retry、idempotency key、duplicate suppression、tool unavailable、tool choice 与错误归一化。

## 核心知识

- 描述要告诉模型何时不能用工具；执行器仍必须在服务端校验，不信任模型参数。
- 每个写工具都有幂等键、权限检查、预览/确认和结果校验；删除/外发等不可逆动作默认升级。
- 把 provider-specific tool result 归一化为 `success | retryable_error | permanent_error | needs_approval`。

## Practice

实现 `read_ticket`、`update_ticket`、`send_external_email` 三个工具：schema、权限、审计、timeout、一次安全 retry、幂等和重复请求 fixture；模拟工具不可用、模型选错工具、参数缺失以及审批后 resume。

## Pass Evidence

审阅者检查每个工具的 read/write/side-effect 标签、权限 scope、audit id、幂等键、重复执行结果、timeout/retry、不可用分支、参数校验和审批前后 trace；不可逆工具没有 silent auto-run。

## 常见失败

把工具描述当权限；重试写操作造成双扣；没有 timeout；把 provider 错误原样泄露；把 tool unavailable 当空结果；缺少结果 schema 与审计。

## 不需要深挖到什么程度

不要求实现所有 MCP server 或多代理；先交付一个受限工具集和可重放 contract。

## Related Knowledge

[[LLM-API-and-Structured-Outputs]]、[[Enterprise-Integrations-and-Connectors]]、[[Human-in-the-Loop-and-Agent-Guardrails]]

## Practice Boundary

通过线是动作契约与安全执行器；loop、checkpoint 和业务流程由其他 Skills 负责。

## Actual Evidence

以 [[Evidence-Card]] 记录一次重复写操作被幂等键拦截的 trace。

## Sources

### Official / normative

- https://platform.openai.com/docs/guides/function-calling

### Job evidence

- [[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]
- [[Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]
