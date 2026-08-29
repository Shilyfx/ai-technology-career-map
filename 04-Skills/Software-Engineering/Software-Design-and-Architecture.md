---
type: skill
skill_category: software-engineering
status: developing
stability: stable
evidence_mode: prerequisite-synthesis
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-28
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[Data-and-AI-Engineer]]"
  - "[[ML-and-AI-Engineer]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[AI-Product-Manager]]"
prerequisites:
  - "[[Python]]"
  - "[[HTTP-API]]"
related_concepts:
  - "[[AI-Product-Engineering]]"
  - "[[AI-Agents-and-Tool-Use]]"
---

# Software Design and Architecture

## 为什么岗位需要它

AI 功能最终要成为可维护的系统：边界、状态、依赖、失败、权限、版本、数据和团队协作都需要设计。只会写 demo 不能承担生产交付。

## Role Demand

Application、Infra、Data、ML 和 Solutions/FDE 需要 use/implement；PM 需要 explain 取舍、风险和交付边界。

## Job Evidence

岗位样本把 API、分布式系统、模型服务、数据质量和测试分别计数；它们共同构成软件设计能力的输入，但没有把架构作为独立标签。本页是跨 Skill 的学习前置层，不新增招聘频次。

## 在岗位中怎么使用

拆分模块和服务、定义接口与状态、选择同步/异步边界、设计重试/幂等/回滚，写 ADR 并用测试和观测验证设计。

## Role-specific Target Depth

Application/FDE 需要 implement；Infra/Data/ML 需要 implement/use 规模与恢复设计；PM 需要 explain build/buy 与风险。

## 前置 Skills

[[Python]]、[[HTTP-API]]。

## 学习范围

模块化、接口契约、状态机、事件流、队列、缓存、错误模型、版本、部署、依赖、容量和可观测性。

## 核心知识

先写不变量和失败路径；局部优化不能破坏权限和可恢复性；架构是约束下的取舍，不是组件清单。

## Practice

设计一个“文档摄入 → RAG → Agent 工具调用 → 评测”的小系统，画组件图，写 API/schema、失败矩阵、权限边界和回滚方案。

## Pass Evidence

能在一次故障注入后说明影响范围、恢复路径和为何选择该边界；新成员可按 ADR 和测试运行系统。

## 常见失败

先选框架再找问题；所有逻辑塞进一个 prompt；没有超时和幂等；把日志当可观测性；无法解释成本。

## 不需要深挖到什么程度

先掌握一个端到端系统的边界和失败处理；不必为了入门先设计全球分布式平台。

## Related Knowledge

[[HTTP-API]]、[[Testing]]、[[Tool-Calling-Agent-Workflow]]、[[Model-Serving]]、[[Distributed-Systems]]、[[API-Product-Delivery]]。

## Actual Evidence

尚无用户能力结论；完成架构 Practice 后使用 [[Evidence-Card]] 记录。

## Sources

[[AI-Agents-and-Tool-Use]]、[[Obsidian-CLI-AI-Agent-Automation]]、[[Obsidian-MCP-Automation]]、[[n8n-Obsidian-RSS-Automation]]。

