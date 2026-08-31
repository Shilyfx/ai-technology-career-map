---
type: path
page_kind: role-learning-paths
status: reference
created: 2026-08-24
updated: 2026-09-01
review_after: 2026-11-30
related:
  - "[[Learning-Path]]"
  - "[[Role-Map]]"
  - "[[Skill-Index]]"
  - "[[2026-08-31-Enterprise-Applied-AI-Job-Snapshot]]"
---

# Role Skill Paths

> 路径从 Role 交付物出发；DSA 是推荐基础，不是 Applied AI Application 的硬门槛。语言选择为 Python **或** TypeScript/JavaScript，不要求两者同时精通。

## Applied AI Application / Agent Workflow

```text
Python OR TypeScript/JavaScript
→ HTTP/JSON/API
→ Prompt/Context + LLM API/Structured Outputs
→ Tool Calling (when actions are needed)
↘ Workflow Automation (can start early/in parallel)
→ Agent Orchestration
→ Agent Evals / Trace
→ Production Integration (branch)
```

入口：[[Python]] **或** [[TypeScript-JavaScript]] → [[HTTP-API]] → [[Prompt-and-Context-Engineering]] + [[LLM-API-and-Structured-Outputs]]。[[Workflow-Automation-and-Business-Process-Design]] 可并行；需要模型动作时再进入 [[Tool-Calling-and-Action-Contracts]] → [[Agent-Orchestration-and-State]] → [[Agent-Evals-and-Trace-Debugging]]。[[Enterprise-Integrations-and-Connectors]] 是生产集成分支，不是所有 Tool Calling 的硬前置；[[Data-Structures-and-Algorithms]] 与 [[Software-Design-and-Architecture]] 为推荐基础；[[RAG]]、[[MCP-and-Agent-Interoperability]]、[[Human-in-the-Loop-and-Agent-Guardrails]] 按项目选修或加深。

### Applied subtracks

- AI Product/Application Engineer：全栈、LLM I/O、工具契约、评测与用户结果；
- Agent/Workflow Engineer：状态、事件、恢复、异步、业务流程；
- Internal AI Automation Engineer：连接器、权限、审计、成本和可运营流程；
- Full-stack AI Product Engineer：TypeScript/React、审批 UX、后端契约和 trace。

## Solutions / FDE / Architect

[[Technical-Communication]] + [[HTTP-API]] → [[Software-Design-and-Architecture]]；[[Workflow-Automation-and-Business-Process-Design]] 可并行 → [[Enterprise-Integrations-and-Connectors]]（生产分支） + [[LLM-API-and-Structured-Outputs]] → [[Tool-Calling-and-Action-Contracts]] → [[Human-in-the-Loop-and-Agent-Guardrails]] → [[Agent-Evals-and-Trace-Debugging]]。需要跨客户端/工具生态时加入 [[MCP-and-Agent-Interoperability]]。

## Agent Runtime / Agent Platform（Infra specialized）

[[Data-Structures-and-Algorithms]] → [[Linux]] → [[Testing]] → [[Software-Design-and-Architecture]] → [[Distributed-Systems]] → [[Agent-Orchestration-and-State]] → [[Tool-Calling-and-Action-Contracts]] → [[Agent-Evals-and-Trace-Debugging]] → [[Observability]] → [[MCP-and-Agent-Interoperability]]。GPU/serving 路径仍保留：[[CUDA-GPU-Basics]] → [[Model-Serving]]。

## AI Product Manager

[[Technical-Communication]] → [[Prompt-and-Context-Engineering]] → [[LLM-API-and-Structured-Outputs]] → [[Workflow-Automation-and-Business-Process-Design]] → [[Agent-Evals-and-Trace-Debugging]] + [[Human-in-the-Loop-and-Agent-Guardrails]] → [[API-Product-Delivery]]。涉及平台互操作时理解 [[MCP-and-Agent-Interoperability]]；不要求先成为生产工程师。

## Research / ML / Data / Safety

- Research / ML：[[Data-Structures-and-Algorithms]] → [[Python]] → [[Statistics-and-Experiment-Design]] → [[ML-Experimentation]] → [[Model-Evaluation]] → [[PyTorch]] → [[Distributed-Training]]；
- Data / AI Engineer：[[Python]] + [[SQL]] → [[Databases-and-Data-Modeling]] → [[Data-Quality-and-Lineage]] → [[Testing]] → [[Distributed-Systems]]；
- Safety / Evals：[[Statistics-and-Experiment-Design]] → [[Model-Evaluation]] → [[LLM-Evals]] → [[Agent-Evals-and-Trace-Debugging]] → [[Human-in-the-Loop-and-Agent-Guardrails]] → [[Security-Privacy-and-Access-Control]]。

## 选择规则

先选一个真实工作流和目标 Role，再决定 RAG、Memory、MCP、Multi-agent/A2A 或 Computer Use 是否必要。优先 deterministic workflow；只有在任务不确定性和评测证据支持时才增加自主循环。
