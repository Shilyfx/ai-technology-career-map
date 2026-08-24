---
type: system
page_kind: vault-design
status: reference
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Metadata-Schema]]"
  - "[[Review-Rules]]"
  - "[[Current-State]]"
---

# Vault Design

## 目录职责

| 目录 | 作用 |
| --- | --- |
| `00-Home` | 首次入口、唯一当前状态、技术/术语雷达、路线与 MOC |
| `01-Inbox` | 真实陌生名词和待分类材料 |
| `02-Foundations` | 数据、数学、软件、ML 闭环 |
| `03-Models` | 模型、训练与多模态能力 |
| `04-Applications` | RAG、Agent、eval、产品工程 |
| `05-Systems` | 数据系统、MLOps、Infra、推理 |
| `06-Safety` | 安全、安全工程、治理 |
| `07-Careers` | 岗位、技能矩阵和角色边界 |
| `08-Paths` | 基于岗位的专修路线 |
| `09-Evidence` | 实验、项目、解释和复盘证据；只建立有真实内容的子目录 |
| `90-Sources` | 可替换的市场快照与来源 |
| `99-Templates` | 新术语、技术、岗位和 Evidence 卡片模板 |
| `99-System` | Schema、复查规则、QA 和设计日志 |

## 7 层技术模型

1. 问题、数据与软件底座；
2. 训练、评测与泛化；
3. 模型与基础模型；
4. 应用、RAG 与 Agent；
5. 数据系统、MLOps、推理与基础设施；
6. 安全、治理与风险；
7. 产品、岗位交付物与业务结果。

## 链接原则

- `Start-Here` 负责首次导航，`Current-State` 负责唯一动态状态；
- 入口页指向 5–10 个高价值页面；
- 概念页链接前置、后续与相邻概念；
- 市场快照不承担稳定定义；
- 工具/框架名优先放在所属概念页，除非确实需要独立比较；
- Evidence 必须回链学习阶段或岗位，避免“做过但无法解释”；
- 避免为了图谱好看而建立虚假关系。

## 学习路线模型

`Learning-Path` 不是所有人都要走完的单一直线课程：Stage 0–2 是共享基础，Stage 3 建立基础模型时代的共同素养，之后按岗位分支。Stage 4 应用系统和 Stage 5 生产/系统/风险是可选专修层，Stage 6 用于岗位专修与作品集。

## 更新优先级

1. 新问题先写入 Inbox；
2. 影响多个页面的定义先更新 Concept；
3. 当前技术或岗位变化只更新 Radar/Snapshot；
4. 被多个页面重复引用或有实践证据的条目再升级为独立笔记；
5. 到 `review_after` 时按 `Review-Rules` 复查，并运行 `scripts/check_vault.py`。
