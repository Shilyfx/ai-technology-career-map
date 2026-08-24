---
type: skill
skill_category: software-engineering
status: developing
stability: stable
created: 2026-08-24
updated: 2026-08-24
review_after: 2027-02-24
roles:
  - "[[Research-Engineer]]"
  - "[[ML-and-AI-Engineer]]"
  - "[[AI-Application-Engineer]]"
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[AI-Safety-Evals-and-Governance]]"
prerequisites:
  - "[[Python]]"
related_concepts:
  - "[[Training-Evaluation-and-Generalization]]"
  - "[[Evals-and-Observability]]"
---

# Testing

## 为什么岗位需要它

AI 系统的变化来自代码、数据、模型和配置；测试是把回归、错误输入和不确定性变成可见证据的共同能力。

## Role Demand

| Role | Priority | Target Depth | Job Evidence | Note |
| --- | --- | --- | --- | --- |
| Research Engineer | Core | implement | [[OpenAI-Research-Engineer-Frontier-Evals-San-Francisco-2026-08]] | 可靠实验 |
| Application Engineer | Core | implement | [[OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08]] | 生产 primitives |
| Safety / Evals | Core | implement | [[Anthropic-Research-Engineer-Model-Evaluations-San-Francisco-2026-08]] | regression gate |

## 在岗位中怎么使用

单元、集成、数据契约、回归、golden set、故障注入和发布门禁。

## Role-specific Target Depth

研究与应用至少能实现测试；Safety 还要衡量覆盖、误报、漏报和稳定性。

## 前置 Skills

[[Python]]。

## 学习范围

测试层次、夹具、mock、确定性、数据/模型回归和失败诊断。

## 核心知识

测试不是证明模型正确，而是约束已知失败并揭示变化。

## Practice

为一个 API 或评测 pipeline 建立 happy path、边界、错误输入和回归集。

## Pass Evidence

测试可独立运行；至少一次故意引入的回归被捕获且记录原因。

## 常见失败 / 误区

只测总分、只测 happy path、把 flaky test 当真实退化。

## 不需要深挖到什么程度

不要求每个岗位实现完整测试框架；要求能把关键风险转为检查。

## Related Concepts

[[Evals-and-Observability]]、[[Training-Evaluation-and-Generalization]]。

## Actual Evidence

尚无用户能力结论；使用 [[Evidence-Card]] 创建实际记录。

## Sources

[[OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08]]。
