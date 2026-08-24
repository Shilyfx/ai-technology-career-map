---
type: skill
skill_category: infra-inference
status: developing
stability: stable
created: 2026-08-24
updated: 2026-08-24
review_after: 2027-02-24
roles:
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[AI-Application-Engineer]]"
  - "[[AI-Safety-Evals-and-Governance]]"
prerequisites:
  - "[[Linux]]"
  - "[[HTTP-API]]"
  - "[[Testing]]"
related_concepts:
  - "[[Evals-and-Observability]]"
---

# Observability

## 为什么岗位需要它
没有日志、指标、trace 和质量信号，生产 AI 的失败无法定位或复盘。

## Role Demand
Infra 为 Core；应用/Evals 为 Common。证据见 [[Anthropic-Performance-Engineer-Inference-Systems-San-Francisco-2026-08]]。

## 在岗位中怎么使用
记录延迟、吞吐、成本、错误、工具轨迹、数据版本和质量回归。

## Role-specific Target Depth
Infra implement；应用 use/implement；PM 读指标并追问边界。

## 前置 Skills
[[Linux]]、[[HTTP-API]]、[[Testing]]。

## 学习范围
structured logs、metrics、traces、alerts、SLO、容量和隐私。

## 核心知识
信号选择、采样、关联 ID、告警阈值和数据脱敏。

## Practice
为一个 agent/API 服务建立端到端 trace、p95 和失败分类。

## Pass Evidence
能从一次请求还原工具、模型、数据和延迟链路。

## 常见失败 / 误区
只记字符串日志；指标无行动；泄漏 prompt、用户数据或密钥。

## 不需要深挖到什么程度
先能定位真实故障，再按服务规模学习 tracing 平台细节。

## Related Concepts
[[Evals-and-Observability]]、[[Model-Serving]]。

## Actual Evidence
尚无用户能力结论；使用 [[Evidence-Card]]。

## Sources
[[Anthropic-Performance-Engineer-Inference-Systems-San-Francisco-2026-08]]、[[OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08]]。
