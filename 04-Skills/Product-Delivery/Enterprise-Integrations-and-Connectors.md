---
type: skill
skill_category: Product Delivery
status: developing
stability: current
created: 2026-08-31
updated: 2026-08-31
review_after: 2026-11-30
roles:
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[AI-Application-Engineer]]"
  - "[[AI-Product-Manager]]"
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
prerequisites:
  - "[[HTTP-API]]"
  - "[[Databases-and-Data-Modeling]]"
  - "[[Security-Privacy-and-Access-Control]]"
related_concepts:
  - "[[Workflow-Automation-and-Business-Process-Design]]"
  - "[[MCP-and-Agent-Interoperability]]"
sample_batch: enterprise-applied-ai-2026-08
---

# Enterprise Integrations and Connectors

## 为什么岗位需要它

决定 AI 能否进入真实企业系统：身份、数据、API、事件、权限、schema 和运营边界。

## Role Demand

做 discovery、REST/GraphQL/event/webhook connector，处理 OAuth/SAML/OIDC/SCIM、限流、映射、同步、审计和回滚。

## Job Evidence

- [[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]]
- [[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]
- [[Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08]]
- [[Front-AI-Engineer-GTM-Operations-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]

链接回每张 Job Sample 的 `Skill Extraction`；`explicit` 与 `inferred` 分开，样本不代表市场频率。

## 在岗位中怎么使用

做 discovery、REST/GraphQL/event/webhook connector，处理 OAuth/SAML/OIDC/SCIM、限流、映射、同步、审计和回滚。

## Role-specific Target Depth

- Application / FDE：implement；Agent Platform：implement→optimize；PM / Solutions：explain→use。
- 目标深度随交付责任变化，不是全局门槛。

## 前置 Skills

[[HTTP-API]], [[Databases-and-Data-Modeling]], [[Security-Privacy-and-Access-Control]]

## 学习范围

定义、边界、接口契约、失败模式、权限/成本/延迟和可观测性；优先覆盖一个可交付流程。

## 核心知识

决定 AI 能否进入真实企业系统：身份、数据、API、事件、权限、schema 和运营边界。 重点掌握 schema、状态、重试、幂等、审计、回滚和业务结果之间的关系。

## Practice

为 CRM/工单模拟器做双向 connector：schema mapping、增量同步、权限矩阵、失败重放和审计。

## Pass Evidence

完成 Practice 后，提交可重放的任务集、测试结果、trace、失败分类和一项修复前后对比。

## 常见失败

把 prompt 或单一框架当作系统边界；忽略权限、超时、幂等、回滚、失败切片和人工接管；只展示 happy path。

## 不需要深挖到什么程度

不必先研究模型训练内部、所有厂商 SDK 或复杂多智能体；先能在受控任务中完成实现、测试、trace 和复盘。

## Related Knowledge

[[Workflow-Automation-and-Business-Process-Design]], [[MCP-and-Agent-Interoperability]]

## Actual Evidence

尚无用户能力结论；完成 Practice 后复制 [[Evidence-Card]]，记录问题、行动、结果、失败和判断，并回链本 Skill 与目标 Role。

## Sources

### Official / normative

- https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture

### Job evidence

- [[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]]
- [[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]
- [[Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08]]
- [[Front-AI-Engineer-GTM-Operations-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]

### Practice tutorial

- [[Notion-MCP-Beginner]]

官方规范定义边界，岗位页决定优先级，教程只提供练习路径；三类证据不混写。
