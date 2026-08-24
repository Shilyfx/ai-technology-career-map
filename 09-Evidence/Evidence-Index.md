---
type: evidence
page_kind: evidence-index
status: reference
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Learning-Path]]"
  - "[[Career-MOC]]"
  - "[[Evidence-Card]]"
---

# Evidence Index

> 本仓库目前不伪造个人能力证据。这里先定义入口和判定标准；真实实验、项目、解释或复盘完成后，再建立独立 Evidence 卡片。

## Evidence 类型

| Folder / type | 用途 | 最小产出 |
| --- | --- | --- |
| `lab` | 可复现实验、基线、消融、评测 | 命令、数据/模型版本、结果、失败切片 |
| `project` | 面向用户或业务的完整交付 | 任务集、架构、成本/延迟、回滚或兜底 |
| `evidence` / `explanation` | 解释一个概念并证明边界 | 图、最小例子、验证问题和限制 |
| `review` | 复盘一次决策 | 问题、行动、失败、判断和下一缺口 |

## 通过标准

每条证据都必须闭环：

`problem → action → result → failure → judgment → skill → gap`

并至少回链一个 [[Learning-Path]] Stage 或 [[Role-Map]] 岗位。没有失败、限制或判断的截图/链接只能作为参考材料，不能作为阶段通过证据。

## 开始记录

复制 [[Evidence-Card]] 到合适的子目录（`Labs/`、`Projects/`、`Explanations/` 或 `Reviews/`），补齐 frontmatter 和正文。涉及私有项目时只提交脱敏摘要、公开链接或可复现实验说明。
