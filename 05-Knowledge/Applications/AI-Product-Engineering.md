---
type: concept
domain: product
status: developing
stability: current
depth: use
created: 2026-08-24
updated: 2026-08-31
review_after: 2026-11-24
related:
  - "[[AI-Product-Manager]]"
  - "[[AI-Application-Engineer]]"
  - "[[Evals-and-Observability]]"
  - "[[Software-Design-and-Architecture]]"
  - "[[Prompt-and-Context-Engineering]]"
  - "[[Security-Privacy-and-Access-Control]]"
  - "[[Workflow-Automation-and-Business-Process-Design]]"
  - "[[Agent-Evals-and-Trace-Debugging]]"
---

# AI Product Engineering

## AI 产品不是“给现有页面加聊天框”

AI 产品工程把概率模型嵌入真实用户工作流，并设计反馈、权限、失败兜底和持续改进。

```text
user job
→ decision or workflow bottleneck
→ AI capability contract
→ prototype
→ task eval
→ production controls
→ adoption and outcome
```

## 能力契约

在开发前写清：

- 输入来自哪里，是否可信；
- 输出用于建议、草稿还是自动行动；
- 允许哪些错误，不允许哪些错误；
- 何时拒答、何时询问、何时升级给人；
- 延迟、成本、隐私与合规边界；
- 如何测用户结果，而不只测“回答看起来不错”。

## 常见设计模式

- Copilot：人主导，模型提供建议；
- Autocomplete/transform：局部、高频、可撤销；
- Search/RAG：来源可查；
- Workflow automation：固定步骤 + 局部模型判断；
- Agent：在受控边界内动态选择行动；
- Human review queue：高风险或低置信度升级。

Applied AI 岗位把上述模式落到可交付的技能链：[[LLM-API-and-Structured-Outputs]] → [[Tool-Calling-and-Action-Contracts]] → [[Workflow-Automation-and-Business-Process-Design]] / [[Agent-Orchestration-and-State]] → [[Agent-Evals-and-Trace-Debugging]] → [[Enterprise-Integrations-and-Connectors]]。[[RAG]]、[[MCP-and-Agent-Interoperability]] 和 [[Human-in-the-Loop-and-Agent-Guardrails]] 按任务和风险进入。

## 产品指标

| 层 | 例子 |
| --- | --- |
| 模型 | task accuracy、faithfulness |
| 系统 | latency、availability、cost |
| 行为 | adoption、completion、override |
| 业务 | 周期时间、质量、收入、风险降低 |
| 风险 | harmful rate、leakage、escalation miss |

## 最小实践

不要只做 demo。写一个一页 PRD，附 20 个真实任务、失败预算、人工兜底、指标树和上线后回滚条件。
