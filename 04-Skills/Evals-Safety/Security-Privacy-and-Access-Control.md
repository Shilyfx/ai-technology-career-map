---
type: skill
skill_category: evals-safety
status: developing
stability: current
evidence_mode: prerequisite-synthesis
created: 2026-08-29
updated: 2026-08-29
review_after: 2026-11-29
roles:
  - "[[AI-Application-Engineer]]"
  - "[[Data-and-AI-Engineer]]"
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[AI-Safety-Evals-and-Governance]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[AI-Product-Manager]]"
prerequisites:
  - "[[HTTP-API]]"
related_concepts:
  - "[[AI-Safety-Security-and-Governance]]"
  - "[[Data-Engineering-and-Governance]]"
  - "[[AI-Agents-and-Tool-Use]]"
---

# Security, Privacy and Access Control

## 为什么岗位需要它

Agent、RAG、数据管道和模型服务都会接触真实数据与有副作用的工具。权限、隐私、密钥和审计是系统能否上线的前置条件，不是上线后再补的插件。

## Role Demand

Application/Data/Infra/Solutions 需要把权限和数据边界实现到系统；Safety/PM 需要定义风险、门槛、责任和升级路径。

## Job Evidence

当前样本把 safeguards、数据治理、API 认证、可靠性和模型评测分散在多个 Skill 中；本页是从这些交付物提炼的 cross-cutting prerequisite，不增加一个没有直接抽取的“安全岗位频次”。

## 在岗位中怎么使用

做 threat model、身份和资源授权、最小权限、secret 隔离、PII/retention/deletion、审计、sandbox、prompt injection 与工具越权测试。

## Role-specific Target Depth

Application/Infra/Data/FDE 需要 implement；Safety 需要 implement/optimize 风险测量；PM 需要 explain/decide；所有角色都要能识别升级条件。

## 前置 Skills

[[HTTP-API]]。

## 学习范围

认证与授权、RBAC/ABAC、密钥管理、信任边界、输入验证、注入、日志脱敏、数据生命周期、供应链和事故响应。

## 核心知识

Prompt 不是权限；Hook 不是沙箱；RAG 召回必须继承权限；日志和记忆也属于数据资产；安全控制必须能测试、审计和撤销。

## Practice

为一个带 Agent 工具的学习助手写 threat model，实施只读/写入分级、敏感目录保护、密钥外置、越权测试和审计日志，再演练撤销权限。

## Pass Evidence

能展示一次允许、一次拒绝、一次注入攻击和一次撤权后的行为，并说明日志中哪些字段被脱敏、谁可以审计。

## 常见失败

把 API key 放进前端或笔记；用自然语言承诺代替授权；日志记录完整敏感内容；默认给 Agent 写权限；没有删除和回滚。

## 不需要深挖到什么程度

普通应用先掌握身份、数据边界和工具安全；高风险领域再深入密码学、合规和红队专业方法。

## Related Knowledge

[[AI-Safety-Measurement]]、[[LLM-Evals]]、[[Data-Quality-and-Lineage]]、[[Tool-Calling-Agent-Workflow]]、[[Model-Serving]]。

## Actual Evidence

尚无用户能力结论；完成 threat model 和攻击/防守演练后使用 [[Evidence-Card]] 记录。

## Sources

[[Agent-Hooks-Guide]]、[[Obsidian-MCP-Automation]]、[[Obsidian-MCP-Beginner]]、[[AI-Safety-Security-and-Governance]]。

