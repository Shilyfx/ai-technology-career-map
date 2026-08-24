---
type: concept
domain: applications
status: seed
stability: emerging
created: 2026-08-24
updated: 2026-08-24
aliases:
  - AI Agent
  - Agentic AI
related:
  - "[[RAG-and-Knowledge-Systems]]"
  - "[[Evals-and-Observability]]"
  - "[[AI-Safety-Security-and-Governance]]"
---

# AI Agents and Tool Use

## 最小定义

Agent 是一个围绕目标反复执行“观察—决定—行动—检查”的系统。模型可以参与决策，但完整 Agent 还需要状态、工具、权限、终止条件、错误处理和评测。

```mermaid
flowchart LR
  O["observe"] --> P["plan / decide"]
  P --> T["tool / action"]
  T --> V["validate"]
  V -->|继续| O
  V -->|完成/升级| H["finish or human handoff"]
```

## Workflow 与 Agent

- **Workflow**：路径主要由代码或人预先定义；
- **Agent**：模型在运行时决定部分步骤或工具；
- 两者可以混合。可预测任务通常先用 workflow，再只把不确定决策交给模型。

## 必备控制面

- 工具 schema 与输入验证；
- 最小权限、secret 隔离、sandbox；
- 状态与可恢复 checkpoint；
- retry、timeout、幂等、预算与速率限制；
- 人工审批和高风险动作确认；
- trace、任务级 eval 与终止条件。

## 热门名词的位置

| 名词 | 位置 |
| --- | --- |
| Function calling / tool use | 让模型选择结构化动作 |
| Context engineering | 构建模型当前可见的信息与约束 |
| Memory | 跨步骤或跨会话保存状态/知识 |
| MCP | 连接模型应用与外部工具/上下文的协议层 |
| Multi-agent | 多个角色/控制循环分工，不天然更可靠 |
| Computer use | 通过 UI 感知与操作软件，攻击面更大 |

## 当前岗位信号如何解读

AI Index 2026 显示 2025 年美国岗位中 Agentic AI、AI agents、Agentic systems 和 LangGraph 等词快速增长。可取的结论是企业开始招聘“协调并运行任务系统”的能力；不可取的结论是某个框架会成为永久标准。见 [[2026-08-AI-Job-Market-Snapshot]]。

## 最小实践

实现一个只使用 2–3 个工具的任务系统，并准备：20 个任务、5 个对抗输入、最大步骤数、预算、错误注入、人工审批点与任务成功率。先证明单 Agent/Workflow 可控，再考虑多 Agent。

## 一手资料

- Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [Model Context Protocol documentation](https://modelcontextprotocol.io/)
