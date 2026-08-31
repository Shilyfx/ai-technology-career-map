#!/usr/bin/env python3
"""Write the nine Applied AI skill cards with distinct learning contracts."""
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]
UPDATED = "2026-08-31"

PAGES = {
"04-Skills/Programming/TypeScript-JavaScript.md": ("""---
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
---""", """# TypeScript / JavaScript

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

运行时（Node、浏览器）、类型系统、ES modules、npm、Promise/async-await、event loop、fetch/HTTP、JSON 与 schema validation、非 2xx、stream、超时、retry、日志、环境变量与 secret、单元/集成测试。

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
"""),
"04-Skills/LLM-Applications/LLM-API-and-Structured-Outputs.md": ("""---
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
  - "[[Software-Design-and-Architecture]]"
recommended_foundations:
  - "[[Python]]"
  - "[[TypeScript-JavaScript]]"
related_concepts:
  - "[[Prompt-and-Context-Engineering]]"
  - "[[Tool-Calling-and-Action-Contracts]]"
sample_batch: enterprise-applied-ai-2026-08
---""", """# LLM API 与结构化输出

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
"""),
"04-Skills/LLM-Applications/Tool-Calling-and-Action-Contracts.md": ("""---
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
  - "[[LLM-API-and-Structured-Outputs]]"
  - "[[Enterprise-Integrations-and-Connectors]]"
recommended_foundations:
  - "[[Security-Privacy-and-Access-Control]]"
related_concepts:
  - "[[Human-in-the-Loop-and-Agent-Guardrails]]"
  - "[[Agent-Orchestration-and-State]]"
sample_batch: enterprise-applied-ai-2026-08
---""", """# Tool Calling 与 Action Contracts

## Skill Boundary

本卡只解决“模型提出动作后，系统如何安全、可重放地执行”：tool/input/output schema、描述、读写与副作用、可逆性、超时/重试/幂等/重复执行、权限/审计、工具分类、结果归一化、不可用和 tool choice。它不负责代理循环本身。

## 为什么岗位需要它

Agentforce、Notion、Ramp、Warp 等岗位的价值在于把模型连接到真实系统；没有 action contract，tool calling 只是不可审计的字符串生成。

## Role Demand

应用工程需要定义 adapter 和执行器；FDE/PM 需要把“读、写、发信、删除、收费”等风险暴露给审批与权限系统。

## Job Evidence

[[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]、[[Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08]]、[[Warp-Forward-Deployed-Engineer-2026-08]] 的 responsibilities 明确提到 tool calls/actions；这些行没有被升级为 universally required。

## 前置 Skills

硬前置：[[LLM-API-and-Structured-Outputs]] 与 [[Enterprise-Integrations-and-Connectors]]；安全控制参考 [[Human-in-the-Loop-and-Agent-Guardrails]]。

## 学习范围

工具名称/描述、输入输出 schema、read/write taxonomy、side effect、reversible/irreversible、权限 scope、audit event、timeout、retry、idempotency key、duplicate suppression、tool unavailable、tool choice 与错误归一化。

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
"""),
"04-Skills/LLM-Applications/Agent-Orchestration-and-State.md": ("""---
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
  - "[[LLM-API-and-Structured-Outputs]]"
  - "[[Tool-Calling-and-Action-Contracts]]"
recommended_foundations:
  - "[[Software-Design-and-Architecture]]"
related_concepts:
  - "[[Workflow-Automation-and-Business-Process-Design]]"
  - "[[Agent-Evals-and-Trace-Debugging]]"
sample_batch: enterprise-applied-ai-2026-08
---""", """# Agent Orchestration 与 State

## Skill Boundary

本卡关注 workflow 与 agent 的执行状态：loop、plan/act/observe、确定性/动态分支、stop/max steps、session/checkpoint/resume、长任务取消、恢复、partial completion、人工暂停/handoff、manager 与 tool-as-agent。默认 single agent first。

## 为什么岗位需要它

Notion、Glean、Salesforce 和 ServiceNow 的证据把代理从 demo 推到长会话生产系统；可靠性来自显式状态和恢复，而不是多代理数量。

## Role Demand

应用工程负责状态机与会话存储；平台工程负责并发、取消、租约与观测；FDE 需要将客户审批、handoff 和部分完成解释清楚。

## Job Evidence

[[Notion-Software-Engineer-AI-Workflows-2026-08]]、[[Glean-Software-Engineer-Agents-2026-08]] 的职责提到 async/recurring agent；ServiceNow 403 样本只保留长会话/检查点等低置信责任线索，未标成 required。

## 前置 Skills

硬前置是 [[LLM-API-and-Structured-Outputs]] 与 [[Tool-Calling-and-Action-Contracts]]；推荐 [[Software-Design-and-Architecture]]。RAG 是并行能力，不是 Agent 硬依赖。

## 学习范围

workflow/agent 边界、plan/act/observe loop、状态 schema、确定性 branch 与模型 branch、终止条件/max steps、session id、checkpoint、resume、cancel、retry/recovery、partial result、human pause/handoff、single vs multi-agent。

## 核心知识

- 用状态转移图说明每一步输入、输出、owner 和副作用；状态必须可序列化、版本化。
- stop 条件同时包括成功、不可恢复错误、预算/步数上限和人工接管。
- 多代理只有在权限、上下文或并行性有清楚收益时才引入；否则增加协调和评估面。

## Practice

实现一个单代理订单异常流程：plan → tool call → observe → human approval → resume；支持 checkpoint、取消、超时、一次 retry、partial completion 和 handoff。再用一个确定性分支对照动态分支。

## Pass Evidence

提供状态图、可重放 session、checkpoint/resume 测试、max-step/stop 断言、取消与恢复 trace、人工暂停和 handoff 记录；证明重复 resume 不重复写入。

## 常见失败

无限 agent loop；把历史消息当状态；checkpoint 不含 schema version；取消后仍写副作用；多代理只是 prompt 分工；失败后丢失 partial completion。

## 不需要深挖到什么程度

不要求先实现分布式 actor 或多代理框架；单代理状态契约通过后再按证据增加并行 worker。

## Related Knowledge

[[Tool-Calling-and-Action-Contracts]]、[[Workflow-Automation-and-Business-Process-Design]]、[[Agent-Evals-and-Trace-Debugging]]

## Practice Boundary

通过线是可恢复状态机，不是“会调用一个 agent SDK”。

## Actual Evidence

用 [[Evidence-Card]]记录一次 cancel/resume 与一次 partial completion 修复。

## Sources

### Official / normative

- https://www.anthropic.com/engineering/building-effective-agents

### Job evidence

- [[Notion-Software-Engineer-AI-Workflows-2026-08]]
- [[Glean-Software-Engineer-Agents-2026-08]]
- [[ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08]]
"""),
"04-Skills/LLM-Applications/Workflow-Automation-and-Business-Process-Design.md": ("""---
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
---""", """# Workflow Automation 与 Business Process Design

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
"""),
"04-Skills/LLM-Applications/MCP-and-Agent-Interoperability.md": ("""---
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
---""", """# MCP 与 Agent Interoperability

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
"""),
"04-Skills/Product-Delivery/Enterprise-Integrations-and-Connectors.md": ("""---
type: skill
skill_category: Product-Delivery
status: developing
stability: current
created: 2026-08-31
updated: 2026-08-31
review_after: 2026-11-30
roles:
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[AI-Application-Engineer]]"
  - "[[AI-Product-Manager]]"
prerequisites:
  - "[[HTTP-API]]"
  - "[[Software-Design-and-Architecture]]"
recommended_foundations:
  - "[[Security-Privacy-and-Access-Control]]"
related_concepts:
  - "[[Tool-Calling-and-Action-Contracts]]"
  - "[[Workflow-Automation-and-Business-Process-Design]]"
sample_batch: enterprise-applied-ai-2026-08
---""", """# Enterprise Integrations 与 Connectors

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

REST/GraphQL 识别与使用、分页、429、OAuth/OIDC、service account、refresh、secret rotation、scope、版本、schema mapping、双向 sync、idempotency、签名校验、backoff、partial failure、ownership、audit、SSO/SCIM。

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

### Job evidence

- [[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]]
- [[Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08]]
- [[Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08]]
"""),
"04-Skills/Evals-Safety/Agent-Evals-and-Trace-Debugging.md": ("""---
type: skill
skill_category: Evals-Safety
status: developing
stability: current
created: 2026-08-31
updated: 2026-08-31
review_after: 2026-11-30
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
prerequisites:
  - "[[Agent-Orchestration-and-State]]"
  - "[[Tool-Calling-and-Action-Contracts]]"
recommended_foundations:
  - "[[LLM-Evals]]"
  - "[[Observability]]"
related_concepts:
  - "[[Human-in-the-Loop-and-Agent-Guardrails]]"
sample_batch: enterprise-applied-ai-2026-08
---""", """# Agent Evals 与 Trace Debugging

## Skill Boundary

本卡与 [[LLM-Evals]] 分工明确：LLM-Evals 主要评 response/model/retrieval quality；本卡评 task success、trajectory、tool selection/arguments、state transition、side effect、recovery、handoff、retry、latency、cost、intervention，并用 trace 做回归诊断。

## 为什么岗位需要它

Glean、Zapier、Atlassian 和 ServiceNow 证据把“构建评估/监控”作为职责；它不是默认的候选人必需频率，而是生产代理的反馈闭环。

## Role Demand

工程师设计任务集、trace schema、断言和 failure slice；FDE/PM 负责 rubric、人工校准、风险分层和上线回归。

## Job Evidence

[[Glean-Software-Engineer-Agents-2026-08]]、[[Zapier-Engineer-Applied-AI-2026-08]] 的 responsibilities 明确提到 eval feedback/monitoring；[[ServiceNow-Staff-Agent-Eval-Platform-2026-08]] 因 403 只作低置信责任线索。

## 前置 Skills

硬前置：[[Agent-Orchestration-and-State]] 与 [[Tool-Calling-and-Action-Contracts]]；推荐 [[LLM-Evals]]、[[Observability]]。

## 学习范围

任务成功、轨迹、工具选择/参数、状态转移、副作用、恢复、handoff、retry、latency、cost、intervention、trace schema、rubric、judge、人工校准、回归阈值。

## 核心知识

- 先定义任务成功条件，再选择 response、trajectory、side-effect 等断言；单一 LLM judge 不能覆盖全部。
- Trace 至少含 run/session、state、tool call/result、policy decision、latency、cost、human intervention 和 error。
- 失败切片要能重放；修复必须比较同一任务集，区分模型漂移、工具故障和状态 bug。

## Practice

构造 30 个真实任务，加入 5 个 tool failure 与 5 个 permission/adversarial case；采集完整 trace，分别评 task success、trajectory、tool args、state transition、side effect、recovery、latency、cost 和 intervention，设回归门槛。

## Pass Evidence

提交任务 manifest、trace schema、rubric/judge 说明、人工校准样例、失败切片、5+5 故障结果、修复前后差异和回归报告；能指出一条“response 好但 task 失败”的案例。

## 常见失败

只测最终文本；把 judge 分数当真值；没有真实状态/副作用；忽略工具参数与恢复；失败样本不可重放；把 latency/cost 当模型质量的替代品。

## 不需要深挖到什么程度

不要求先研究所有统计显著性或训练 judge；先让任务、trace、失败和回归可审计。

## Related Knowledge

[[LLM-Evals]]、[[Observability]]、[[Agent-Orchestration-and-State]]、[[Human-in-the-Loop-and-Agent-Guardrails]]

## Practice Boundary

通过线是代理任务级证据闭环，不是普通 benchmark 分数表。

## Actual Evidence

用 [[Evidence-Card]]保留一份失败切片和回归决定。

## Sources

### Job evidence

- [[Glean-Software-Engineer-Agents-2026-08]]
- [[Zapier-Engineer-Applied-AI-2026-08]]
- [[ServiceNow-Staff-Agent-Eval-Platform-2026-08]]
"""),
"04-Skills/Evals-Safety/Human-in-the-Loop-and-Agent-Guardrails.md": ("""---
type: skill
skill_category: Evals-Safety
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
  - "[[Tool-Calling-and-Action-Contracts]]"
  - "[[Security-Privacy-and-Access-Control]]"
recommended_foundations:
  - "[[Agent-Evals-and-Trace-Debugging]]"
related_concepts:
  - "[[Workflow-Automation-and-Business-Process-Design]]"
sample_batch: enterprise-applied-ai-2026-08
---""", """# Human-in-the-Loop 与 Agent Guardrails

## Skill Boundary

本卡处理风险分类和人机边界：approval、interrupt/resume、escalation、pre-tool guard、post-tool verification、rollback、audit、least privilege、policy vs prompt、sandbox。它不是“加一句安全 prompt”，也不是完整 eval 平台。

## 为什么岗位需要它

企业 Agent 会修改工单、退款、删除数据或发送外部邮件；Atlassian、Salesforce、Warp 等样本把合规、审批和安全交付放在职责/要求中。

## Role Demand

工程师实现策略执行点；FDE 与客户定义风险矩阵；PM 负责 policy、审计和人工运营，而不是把所有风险推给模型。

## Job Evidence

[[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]] 将 AI risk/privacy/GDPR 作为 requirement；[[Salesforce-Product-Manager-Agent-Fabric-2026-08]]、[[Warp-Forward-Deployed-Engineer-2026-08]] 的 approvals/permissions 属于职责或前置推断。

## 前置 Skills

硬前置：[[Tool-Calling-and-Action-Contracts]] 与 [[Security-Privacy-and-Access-Control]]；推荐 [[Agent-Evals-and-Trace-Debugging]]。

## 学习范围

风险等级、auto-allow/confirm/manual-only/deny、approval、interrupt/resume、escalation、pre-tool policy guard、post-tool verification、rollback、audit、least privilege、policy/prompt 分离、sandbox。

## 核心知识

- 用动作和影响分类风险，不用“模型自信度”替代权限；删除/退款/外发默认高风险。
- policy 在工具执行前强制生效，prompt 只是行为提示；执行后仍要验证状态并记录 audit。
- approval 必须可恢复、过期、绑定资源和参数；拒绝/超时要有安全 fallback。

## Practice

为 refund、delete、external email、modify ticket 建风险矩阵，分别落到 auto allow、confirm、manual only、deny；实现 pre-tool guard、审批 interrupt/resume、post-tool verify、rollback、审计和 sandbox fixture。

## Pass Evidence

提交四类动作的决策表、policy test、权限 scope、审批/拒绝/超时/篡改参数 trace、回滚结果和审计记录；证明绕过 prompt 仍无法绕过 policy。

## 常见失败

所有动作都 auto-allow；把 prompt 当 policy；审批后参数被替换；没有 post-tool verify；rollback 不可用；审计缺 actor/resource/policy version。

## 不需要深挖到什么程度

不要求先完成企业合规认证；先把四类动作做成可执行、可审计的风险边界。

## Related Knowledge

[[Tool-Calling-and-Action-Contracts]]、[[Agent-Evals-and-Trace-Debugging]]、[[Security-Privacy-and-Access-Control]]、[[Workflow-Automation-and-Business-Process-Design]]

## Practice Boundary

通过线是 policy-enforced action boundary；业务领域的法律解释仍需专业审查。

## Actual Evidence

用 [[Evidence-Card]]记录一次被 guard 拦截的高风险动作和一次成功回滚。

## Sources

### Job evidence

- [[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]]
- [[Salesforce-Product-Manager-Agent-Fabric-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]
"""),
}


def main() -> int:
    for rel, (fm, body) in PAGES.items():
        p = ROOT / rel
        p.write_text(fm.rstrip().removesuffix("---").rstrip() + "\n---\n\n" + textwrap.dedent(body).strip() + "\n", encoding="utf-8")
    print(f"deepened {len(PAGES)} skill cards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
