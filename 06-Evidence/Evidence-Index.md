---
type: moc
domain: evidence
page_kind: evidence-index
status: reference
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Learning-Path]]"
  - "[[Career-MOC]]"
  - "[[Evidence-Card]]"
  - "[[Skill-Index]]"
---

# Evidence Index

> 本仓库不伪造个人能力证据。每条记录必须回链一个 Skill 和 Role，公开 Job Sample 只证明岗位需求，不证明个人能力。

## Evidence 类型

| type | 用途 | 最小产出 |
| --- | --- | --- |
| `lab` | 可复现实验、基线、消融、评测 | 命令、版本、结果、失败切片 |
| `project` | 面向用户或业务的交付 | 任务集、架构、成本/延迟、回滚 |
| `evidence` | 概念边界和最小验证 | 图、例子、验证问题、限制 |
| `review` | 决策复盘 | 问题、行动、失败、判断、缺口 |

## 通过标准

`problem → action → result → failure → judgment → skill → gap`

同时标记 `role_targets` 和 `skills`。没有失败、限制或判断的截图只能算参考材料。

## 开始记录

复制 [[Evidence-Card]] 到 `Labs/`、`Projects/`、`Explanations/` 或 `Reviews/`，补齐目标 Role、Skill、Practice 和可复现证据。
