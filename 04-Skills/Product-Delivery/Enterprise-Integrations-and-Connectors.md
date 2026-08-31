---
type: skill
skill_category: Product-Delivery
status: developing
stability: current
created: 2026-08-31
updated: 2026-09-01
review_after: 2026-11-30
roles:
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[AI-Application-Engineer]]"
  - "[[AI-Product-Manager]]"
prerequisites:
  - "[[HTTP-API]]"
recommended_foundations:
  - "[[Security-Privacy-and-Access-Control]]"
  - "[[Software-Design-and-Architecture]]"
related_concepts:
  - "[[Tool-Calling-and-Action-Contracts]]"
  - "[[Workflow-Automation-and-Business-Process-Design]]"
sample_batch: enterprise-applied-ai-2026-08
---

# Enterprise Integrations 与 Connectors

## Skill Boundary

本卡超出 HTTP 基础，覆盖 REST/GraphQL、webhook、分页、限流、OAuth/OIDC/service account、token refresh、secret storage、scope、API version/schema mapping、sync/idempotency/signature/retry/backoff、partial failure、data ownership、audit、SSO/SCIM。HTTP API 只负责协议基础。

## 为什么岗位需要它

FDE 和应用工程的核心交付是把 CRM、工单、数据仓库和身份系统可靠接入；企业客户真正关心权限、数据归属、可恢复性和升级路径。

## Role Demand

FDE 负责 discovery、field mapping 和客户授权；工程师实现 connector、sync、重试和审计；PM 负责 API 生命周期、SLA 和数据 ownership。

## Job Evidence

[[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]]、[[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]、[[Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08]] 和 [[Warp-Forward-Deployed-Engineer-2026-08]] 明确要求或承担企业集成；矩阵按 required/responsibility 区分。

## 前置 Skills

硬前置：[[HTTP-API]]；推荐 [[Security-Privacy-and-Access-Control]]。不要求先学 MCP 或 Agent。

## 学习范围

REST/GraphQL 识别与使用、分页/pagination、429、OAuth/OIDC、service account、refresh、secret rotation、scope、版本、schema mapping、双向 sync、idempotency、签名校验、backoff、partial failure、ownership、audit、SSO/SCIM。

## 核心知识

- 先画系统边界、数据 owner 和授权链，再写 connector；OAuth scope 比“能调通”更重要。
- 同步要有 cursor、幂等键、冲突策略和 dead-letter/人工修复；webhook 要验签与防重放。
- API 版本和 schema mapping 需要 contract test；secret 只能进入用户/部署环境，不能进日志。

## Practice

实现一个 CRM→工单 connector：OAuth 登录/刷新、分页 sync、webhook 验签、schema mapping、429 backoff、idempotency、partial failure、dead-letter、审计和 token rotation；补一个 GraphQL read path。

## Pass Evidence

提供 data-flow/ownership 图、scope 清单、contract tests、重放 fixture、重复 webhook、429、token 过期、字段缺失、部分失败和回滚 trace；证明 secret 不出现在代码/日志。

## 常见失败

只测试 200；把 access token 当永久 key；分页丢数据；webhook 重放；schema 变更静默破坏；失败时整批回滚造成数据丢失；没有 owner 和审计。

## 不需要深挖到什么程度

不要求支持所有 SaaS；一个 connector 的完整生命周期足以证明能力。

## Related Knowledge

[[HTTP-API]]、[[Tool-Calling-and-Action-Contracts]]、[[Human-in-the-Loop-and-Agent-Guardrails]]、[[Security-Privacy-and-Access-Control]]

## Practice Boundary

通过线是可靠、可审计的企业连接器；LLM schema 与代理 loop 由相邻 Skills 负责。

## Actual Evidence

以 [[Evidence-Card]]记录一次 token refresh 或 partial failure 的修复与回放。

## Sources

### Official / normative

- [OAuth 2.0 Authorization Framework (RFC 6749)](https://datatracker.ietf.org/doc/html/rfc6749)
- [OAuth 2.0 Bearer Token Usage (RFC 6750)](https://datatracker.ietf.org/doc/html/rfc6750)
- [OAuth PKCE (RFC 7636)](https://datatracker.ietf.org/doc/html/rfc7636)
- [GitHub webhook signature validation](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries)

### Job evidence

- [[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]]
- [[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]
- [[Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08]]

### Practice

- [[JasonAI-Source-Index]]：连接器、API、Webhook 与 Obsidian 自动化实操入口。
