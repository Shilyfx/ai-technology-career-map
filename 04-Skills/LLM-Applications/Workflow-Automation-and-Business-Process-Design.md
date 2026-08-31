---
type: skill
skill_category: LLM-Applications
status: developing
stability: current
created: 2026-08-31
updated: 2026-08-31
review_after: 2026-11-30
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[AI-Product-Manager]]"
prerequisites:
  - "[[HTTP-API]]"
  - "[[Enterprise-Integrations-and-Connectors]]"
recommended_foundations:
  - "[[Agent-Orchestration-and-State]]"
related_concepts:
  - "[[Human-in-the-Loop-and-Agent-Guardrails]]"
  - "[[Tool-Calling-and-Action-Contracts]]"
sample_batch: enterprise-applied-ai-2026-08
---

# Workflow Automation 与 Business Process Design

## Skill Boundary

本卡将业务过程翻译成可交付 workflow：as-is/to-be、trigger、step、branch、owner、SLA、approval、exception、compensation、retry、webhook/cron/queue/event、automation boundary、agentic vs deterministic、manual fallback 和业务指标。n8n/Zapier/Make/Workato 只是示例。

## 为什么岗位需要它

Atlassian、Salesforce、Zapier、Warp、Ramp 样本的共同交付物是“把企业流程跑起来”，而不是单独一个模型调用。

## Role Demand

FDE 负责 discovery 和流程建模；应用工程负责连接与执行；PM 负责 SLA、审批和 business metric。先确定 deterministic boundary，再放 agent。

## Job Evidence

[[Salesforce-Forward-Deployed-Engineer-Supply-Chain-2026-08]]、[[Zapier-Engineer-Applied-AI-2026-08]]、[[Warp-Forward-Deployed-Engineer-2026-08]] 将 workflow/automation 标为 responsibilities；这不等于所有候选人都必须熟悉某个编排产品。

## 前置 Skills

硬前置：[[HTTP-API]] 与 [[Enterprise-Integrations-and-Connectors]]；推荐了解 [[Agent-Orchestration-and-State]]，不要求先学 MCP。

## 学习范围

流程地图、触发器、步骤、分支、owner、SLA、审批、异常、补偿、retry/backoff、webhook/cron/queue/event、agent boundary、manual fallback、指标与回滚。

## 核心知识

- 每个 step 要有输入/输出、owner、超时和失败去向；不可逆步骤前置审批。
- 事件驱动适合解耦与重放；cron 适合轮询但要防重复；webhook 要校验签名。
- 用业务指标（处理时长、自动化率、错误率、人工升级率）而非 agent 次数评价流程。

## Practice

选一个“客户工单→分类→补充信息→更新系统→通知”的流程，画 as-is/to-be，分别实现 deterministic 与 agentic 分支；加入 approval、SLA、webhook、queue、retry、compensation、manual fallback 和业务指标。

## Pass Evidence

提交流程图、step contract、异常/补偿矩阵、重放 fixture、SLA/指标 dashboard 截图或 JSON、人工 fallback 演练；明确哪些步骤禁止 agent 自主决定。

## 常见失败

先选工具后理解流程；把所有 branch 交给模型；没有 owner/SLA；重试造成重复通知；没有补偿；只量 token 不量业务结果。

## 不需要深挖到什么程度

不要求掌握所有自动化平台；能用一个平台或自写 worker 证明边界和失败处理即可。

## Related Knowledge

[[Enterprise-Integrations-and-Connectors]]、[[Agent-Orchestration-and-State]]、[[Human-in-the-Loop-and-Agent-Guardrails]]

## Practice Boundary

通过线是可解释的业务流程设计；模型编排和工具安全由相邻 Skills 负责。

## Actual Evidence

用 [[Evidence-Card]]记录一条流程的 before/after 业务指标和一次补偿演练。

## Sources

### Job evidence

- [[Salesforce-Forward-Deployed-Engineer-Supply-Chain-2026-08]]
- [[Zapier-Engineer-Applied-AI-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]
