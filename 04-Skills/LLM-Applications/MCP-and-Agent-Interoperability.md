---
type: skill
skill_category: LLM Applications
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
  - "[[Tool-Calling-and-Action-Contracts]]"
  - "[[Enterprise-Integrations-and-Connectors]]"
  - "[[Security-Privacy-and-Access-Control]]"
related_concepts:
  - "[[Agent-Orchestration-and-State]]"
  - "[[Human-in-the-Loop-and-Agent-Guardrails]]"
sample_batch: enterprise-applied-ai-2026-08
---

# MCP and Agent Interoperability

## 为什么岗位需要它

在需要跨客户端、服务器和工具生态时掌握协议边界；不是所有岗位默认必修。

## Role Demand

实现 MCP server/client，理解 discovery、tools/list/tools/call、transport、授权、版本和审计。

## Job Evidence

- [[Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08]]
- [[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]
- [[Notion-Forward-Deployed-Architect-Japan-2026-08]]
- [[Front-AI-Engineer-GTM-Operations-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]

链接回每张 Job Sample 的 `Skill Extraction`；`explicit` 与 `inferred` 分开，样本不代表市场频率。

## 在岗位中怎么使用

实现 MCP server/client，理解 discovery、tools/list/tools/call、transport、授权、版本和审计。

## Role-specific Target Depth

- Application / FDE：implement；Agent Platform：implement→optimize；PM / Solutions：explain→use。
- 目标深度随交付责任变化，不是全局门槛。

## 前置 Skills

[[Tool-Calling-and-Action-Contracts]], [[Enterprise-Integrations-and-Connectors]], [[Security-Privacy-and-Access-Control]]

## 学习范围

定义、边界、接口契约、失败模式、权限/成本/延迟和可观测性；优先覆盖一个可交付流程。

## 核心知识

在需要跨客户端、服务器和工具生态时掌握协议边界；不是所有岗位默认必修。 重点掌握 schema、状态、重试、幂等、审计、回滚和业务结果之间的关系。

## Practice

给 Obsidian 或测试数据库做只读 server，再增加需批准的写工具并做契约测试。

## Pass Evidence

完成 Practice 后，提交可重放的任务集、测试结果、trace、失败分类和一项修复前后对比。

## 常见失败

把 prompt 或单一框架当作系统边界；忽略权限、超时、幂等、回滚、失败切片和人工接管；只展示 happy path。

## 不需要深挖到什么程度

不必先研究模型训练内部、所有厂商 SDK 或复杂多智能体；先能在受控任务中完成实现、测试、trace 和复盘。

## Related Knowledge

[[Agent-Orchestration-and-State]], [[Human-in-the-Loop-and-Agent-Guardrails]]

## Actual Evidence

尚无用户能力结论；完成 Practice 后复制 [[Evidence-Card]]，记录问题、行动、结果、失败和判断，并回链本 Skill 与目标 Role。

## Sources

### Official / normative

- https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
- https://modelcontextprotocol.io/specification/2026-07-28/server/tools
- https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization
- https://a2a-protocol.org/v0.3.0/specification/

### Job evidence

- [[Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08]]
- [[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]
- [[Notion-Forward-Deployed-Architect-Japan-2026-08]]
- [[Front-AI-Engineer-GTM-Operations-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]

### Practice tutorial

- [[Obsidian-MCP-Beginner]]

官方规范定义边界，岗位页决定优先级，教程只提供练习路径；三类证据不混写。
