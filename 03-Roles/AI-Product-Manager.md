---
type: role
role_family: product
sample_count: 3
status: developing
snapshot_date: 2026-08-31
created: 2026-08-24
updated: 2026-09-01
review_after: 2026-11-24
aliases:
  - AI PM
  - Applied AI Product Manager
  - Agent Platform Product Manager
---

# AI Product Manager

## 主要使命

选择正确问题，把不确定模型能力转成用户价值，并在质量、速度、成本、安全与业务结果之间做取舍。

## 技能重点

- 用户研究、workflow 与机会识别；
- AI/ML/LLM 能力边界与技术判断；
- 指标树、统计、实验和 failure taxonomy；
- API/平台/开发者体验或行业产品理解；
- safety、privacy、policy 与上线风险；
- 路线图、跨团队协作和清晰沟通。

不一定要以写生产代码为主，但需要足够技术深度与研究/工程团队讨论模型、数据、eval、API 和系统约束。

## Sample Observations

本批两个 OpenAI PM Job Samples 分别显示 API/agent 产品路线图与安全测量/统计协作；它们支持产品责任簇的方向性判断，不代表所有 AI PM 的统一要求。

Applied AI 批次新增 [[Salesforce-Product-Manager-Agent-Fabric-2026-08]]：产品责任扩展到 Discover/Govern/Orchestrate/Observe 控制面、API/MCP、policy、observability、治理和 enterprise outcomes。

## 作品证据

- 用户任务与证据，而不是功能愿望；
- 一页能力契约和失败预算；
- 指标树：模型→系统→行为→业务→风险；
- 明确 build/buy/model choice 与 human-in-the-loop；
- 上线、回滚和停止条件。

来源：[OpenAI PM, API Agents](https://openai.com/careers/product-manager-api-agents-san-francisco/)、[OpenAI PM, Safety Measurement](https://openai.com/careers/product-manager-safety-measurement-san-francisco/)、[Google DeepMind Careers](https://deepmind.google/careers/)

## Sample Basis

3 directional senior PM samples: Salesforce Agent Fabric (Batch B) plus OpenAI API Agents and Safety Measurement (Batch A). Employers/regions are Salesforce US/global and OpenAI San Francisco; subtracks are agent platform, API platform and safety measurement. This is not a census.

## Evidence Basis

Based on 3 Job Samples in [[Job-Sample-Index]]; employers, regions and seniority are summarized in this profile. Confidence is high for repeated explicit signals and medium for partial or inferred signals.

## Main Deliverables

Problem framing, roadmap, success criteria, risk controls and cross-functional delivery.

## Responsibility Clusters

User/workflow discovery; technical product judgment; metrics/evals; safety; stakeholder alignment.

## Skill Profile

| Skill | Required N | Preferred N | Responsibility N | Inferred N | Sample N | Priority | Target Depth | Confidence |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| [[TypeScript-JavaScript]] | 0 | 0 | 0 | 0 | 0 | Prerequisite | explain/use | context |
| [[Python]] | 0 | 0 | 0 | 0 | 0 | Prerequisite | explain/use | context |
| [[LLM-API-and-Structured-Outputs]] | 0 | 0 | 0 | 0 | 0 | Common | explain/use | context |
| [[Tool-Calling-and-Action-Contracts]] | 0 | 0 | 0 | 0 | 0 | Common | explain/use | context |
| [[Agent-Orchestration-and-State]] | 0 | 0 | 1 | 0 | 1 | Common | explain/use | high/medium |
| [[Workflow-Automation-and-Business-Process-Design]] | 0 | 0 | 0 | 0 | 0 | Common | explain/use | context |
| [[MCP-and-Agent-Interoperability]] | 0 | 0 | 1 | 0 | 1 | Specialized | use→implement | high/medium |
| [[Enterprise-Integrations-and-Connectors]] | 0 | 0 | 0 | 0 | 0 | Common | explain/use | context |
| [[Agent-Evals-and-Trace-Debugging]] | 0 | 0 | 0 | 0 | 0 | Common | explain/use | context |
| [[Human-in-the-Loop-and-Agent-Guardrails]] | 0 | 0 | 0 | 0 | 0 | Common | explain/use | context |

Evidence strength is based on Batch B row classifications; `responsibility` and `preferred` are not counted as required.
## Non-skill Gates

Product judgment, prioritization, empathy, executive communication and accountability.

## Seniority/Subtrack Differences

API PM owns developer platform; Agent Platform PM owns registry, governance, orchestration and observation; safety PM owns measurement and risk. All require technical fluency, not identical coding depth.

## Portfolio Evidence

PRD, metric tree, eval plan, risk register, launch/rollback criteria and post-launch decision.

## Adjacent Roles

[[AI-Application-Engineer]]、[[AI-Safety-Evals-and-Governance]]、[[AI-Solutions-Architect-and-FDE]]。

## Source Limitations

Two senior US postings plus one redirected Salesforce Agent Fabric sample are directional; the partial source does not represent all AI PM hiring.

## Refresh

Refresh every 30–60 days while API and safety product scope changes quickly.

## Learning prerequisites

PM 不必先成为生产工程师，但应先完成 [[Technical-Communication]]、[[Statistics-and-Experiment-Design]] 和 [[Prompt-and-Context-Engineering]] 的 explain/use 练习，再进入 [[LLM-API-and-Structured-Outputs]]、[[Workflow-Automation-and-Business-Process-Design]]、[[Agent-Evals-and-Trace-Debugging]] 与 [[Human-in-the-Loop-and-Agent-Guardrails]]；涉及平台互操作时理解 [[MCP-and-Agent-Interoperability]]，涉及真实用户数据时补 [[Security-Privacy-and-Access-Control]]。
