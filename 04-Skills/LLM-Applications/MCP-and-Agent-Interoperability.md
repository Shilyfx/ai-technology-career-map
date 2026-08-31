---
type: skill
skill_category: LLM-Applications
status: developing
stability: emerging
created: 2026-08-31
updated: 2026-08-31
review_after: 2026-10-31
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
prerequisites:
  - "[[Tool-Calling-and-Action-Contracts]]"
  - "[[Enterprise-Integrations-and-Connectors]]"
recommended_foundations:
  - "[[HTTP-API]]"
related_concepts:
  - "[[Agent-Orchestration-and-State]]"
sample_batch: enterprise-applied-ai-2026-08
---

# MCP 与 Agent Interoperability

## Skill Boundary

本卡覆盖 MCP Host/Client/Server、JSON-RPC、initialize/capability negotiation、tools/resources/prompts、stdio/Streamable HTTP、authorization/OAuth、notifications、versioning、local/remote 与 trust boundary。MCP ≠ Tool Calling ≠ Agent ≠ RAG。

## 为什么岗位需要它

Atlassian、Notion、Front、Warp 的岗位将 MCP 作为企业连接和 agent interoperability 责任；它是一层协议与信任边界，不是“多一个工具函数”。

## Role Demand

工程师要能实现或接入 server/client、协商能力、鉴权和取消；FDE 要能解释本地/远程部署与数据边界；PM 只需定义兼容性和治理要求。

## Job Evidence

[[Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08]]、[[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]、[[Front-AI-Engineer-GTM-Operations-2026-08]]、[[Warp-Forward-Deployed-Engineer-2026-08]] 的 responsibilities 提到 MCP；证据矩阵将其与 required 分开。

## 前置 Skills

硬前置：[[Tool-Calling-and-Action-Contracts]] 与 [[Enterprise-Integrations-and-Connectors]]；推荐 [[HTTP-API]]。不要求先会 Agent 或 RAG。

## 学习范围

Host/Client/Server 拓扑、JSON-RPC request/response/error、initialize、capability negotiation、tools/resources/prompts、stdio、Streamable HTTP、OAuth/授权、notifications/versioning、local/remote trust boundary。

## 核心知识

- Host 控制用户体验和权限，Client 管理连接，Server 暴露能力；不要把三者混成一个“agent”。
- initialize 前不能假设能力；版本和通知要显式记录；远程 HTTP 需认证、来源和租约。
- 工具仍需 action contract；MCP 只规定互操作层，不替你做模型决策、状态机或检索。

## Practice

实现一个本地 stdio server 与 Streamable HTTP client，暴露一个 read resource、一个工具和一个 prompt；完成 initialize/capability negotiation、OAuth scope、版本不兼容、notification、取消和本地/远程 trust boundary 测试。

## Pass Evidence

提交协议交互日志：initialize、能力、调用、错误、通知、取消和版本；审阅者能标出 Host/Client/Server、权限 scope、数据流向以及 MCP/Tool/Agent/RAG 四者边界。

## 常见失败

把 MCP 当模型函数调用；跳过 initialize；远程 server 无 OAuth；把 resource 当可信数据；版本不兼容静默降级；local server 继承过宽文件权限。

## 不需要深挖到什么程度

不要求实现完整生态或 A2A；先完成一个最小 server/client 和 trust-boundary review。

## Related Knowledge

[[Tool-Calling-and-Action-Contracts]]、[[Enterprise-Integrations-and-Connectors]]、[[Agent-Orchestration-and-State]]

## Practice Boundary

通过线是协议与权限交互；Agent loop、RAG 质量和业务流程另行验证。

## Actual Evidence

用 [[Evidence-Card]]记录一次 capability mismatch 或 OAuth scope 错误的修复。

## Sources

### Official / normative

- https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
- https://modelcontextprotocol.io/specification/2026-07-28/server/tools
- https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization
- https://a2a-protocol.org/v0.3.0/specification/

### Job evidence

- [[Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08]]
- [[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]
