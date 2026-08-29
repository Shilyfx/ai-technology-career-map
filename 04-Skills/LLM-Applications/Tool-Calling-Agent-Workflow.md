---
type: skill
skill_category: llm-applications
status: developing
stability: current
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Product-Manager]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
prerequisites:
  - "[[HTTP-API]]"
  - "[[RAG]]"
  - "[[Software-Design-and-Architecture]]"
  - "[[Prompt-and-Context-Engineering]]"
  - "[[Security-Privacy-and-Access-Control]]"
related_concepts:
  - "[[AI-Agents-and-Tool-Use]]"
---

# Tool Calling and Agent Workflow

## 为什么岗位需要它
Agent 的价值来自可控地调用工具、处理状态和完成任务，而不是只生成文本。

## Role Demand
应用为 Core；PM/FDE 为 Common；研究按环境和 eval 加深。证据见 [[OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08]]。

## Job Evidence

[[OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08]]、[[Anthropic-Research-Engineer-Computer-Use-San-Francisco-2026-08]] 的 `Skill Extraction` 是本 Skill 的 Job Evidence；只把明确要求作为 required 证据，职责推断保留为 inferred。

## 在岗位中怎么使用
定义工具 schema、权限、状态、重试、超时、人工接管和审计。

## Role-specific Target Depth
应用 implement；PM explain 产品边界；FDE use/implement 场景集成。

## 前置 Skills
[[HTTP-API]]、[[RAG]]、[[Software-Design-and-Architecture]]、[[Prompt-and-Context-Engineering]]、[[Security-Privacy-and-Access-Control]]。

## 学习范围
tool schema、planner/executor、状态机、错误处理、安全和回归评测。

## 核心知识
可逆操作、最小权限、幂等、轨迹记录和失败恢复。

## Practice
构建一个有两个工具、权限检查、重试与人工确认的 agent。

## Pass Evidence
能展示成功、工具失败、越权和超时四条可复盘轨迹。

## 常见失败
把 agent 当 prompt；工具无 schema/权限；忽略副作用和幂等。

## 不需要深挖到什么程度
先掌握可靠工作流，不必为简单任务引入复杂多 agent 编排。

## Related Knowledge
[[AI-Agents-and-Tool-Use]]、[[LLM-Evals]]。

## Actual Evidence
尚无用户能力结论；关联 [[Evidence-Card]]。

## Sources
[[OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08]]、[[Anthropic-Research-Engineer-Computer-Use-San-Francisco-2026-08]]、[[Agent-Hooks-Guide]]、[[Obsidian-MCP-Automation]]、[[n8n-Obsidian-RSS-Automation]]。
