---
type: skill
skill_category: Evals-Safety
status: developing
stability: current
created: 2026-08-31
updated: 2026-09-01
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
---

# Agent Evals 与 Trace Debugging

## Skill Boundary

本卡与 [[LLM-Evals]] 分工明确：LLM-Evals 主要评 response/model/retrieval quality；本卡评 task success、trajectory、tool selection/arguments、state transition、side effect、recovery、handoff、retry、latency、cost、intervention，并用 trace 做回归诊断。

## 为什么岗位需要它

Glean、Zapier、Atlassian 和 ServiceNow 证据把“构建评估/监控”作为职责；它不是默认的候选人必需频率，而是生产代理的反馈闭环。

## Role Demand

工程师设计任务集、trace schema、断言和 failure slice；FDE/PM 负责 rubric、人工校准、风险分层和上线回归。

## Job Evidence

[[Glean-Software-Engineer-Agents-2026-08]]、[[Zapier-Engineer-Applied-AI-2026-08]] 的 responsibilities 明确提到 eval feedback/monitoring；[[ServiceNow-Staff-Agent-Eval-Platform-2026-08]] 现为完整可读来源，直接给出 judges、rubrics、trajectory 与 calibration 证据。

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

### Official / normative

- [OpenAI Agents SDK testing](https://openai.github.io/openai-agents-python/testing/)
- [OpenAI Agents SDK tracing](https://openai.github.io/openai-agents-python/tracing/)

### Job evidence

- [[Glean-Software-Engineer-Agents-2026-08]]
- [[Zapier-Engineer-Applied-AI-2026-08]]
- [[ServiceNow-Staff-Agent-Eval-Platform-2026-08]]

### Practice

- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
