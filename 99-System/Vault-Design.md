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

## 主模型

`02-Jobs → 03-Roles → 04-Skills → 05-Knowledge → 06-Evidence`

Job Samples 是需求证据；Role Profiles 是责任和优先级解释；Skills 是可学习对象；Knowledge 是概念分类；Evidence 是个人实践结果。`90-Sources` 保留市场和技术来源，`99-System` 保留规则。

## 目录职责

| 目录 | 作用 |
| --- | --- |
| `00-Home` | Job-first 入口、Current State、Career/Technology MOC、路径 |
| `01-Inbox` | Job-Inbox、Terms-Inbox、Term-Radar |
| `02-Jobs` | Job Sample Index 和带时间批次的官方样本 |
| `03-Roles` | Role Map、Profiles、Matrix、Role Skill Paths |
| `04-Skills` | Skill Index、Assessment、可学习 Skill Notes |
| `05-Knowledge` | Foundations/Models/Applications/Systems/Safety 概念 taxonomy 和 Radar |
| `06-Evidence` | Skill/Role 关联的实验、项目、解释和复盘 |
| `90-Sources` | 来源导航、市场快照和原始链接边界 |
| `99-Templates` | Job Sample、Role、Skill、Evidence 等模板 |
| `99-System` | Schema、抽取规则、复查、QA 和变更日志 |

## 7 层技术模型

七层仍然保留，但只是 `05-Knowledge` 的概念分类，不是学习优先级：数据/软件 → 训练 → 模型 → 应用 → 系统 → 安全/评测 → 产品/责任。优先级由 Job→Role→Skill 决定。

## 更新优先级

1. 新职位进 [[Job-Inbox]]，验证后成为 Job Sample；
2. 从多个样本抽取 Role Skill Profile；
3. 只有可复用、可练习、跨 Role 的对象才提升为 Skill；
4. Skill 的技术背景放入 Knowledge 概念页；
5. Practice 完成后建立 Evidence，并回链 Role/Skill；
6. 到期按 [[Review-Rules]] 复核并运行 `scripts/check_vault.py`。
