---
type: system
page_kind: refactor-log
status: reference
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Vault-Design]]"
  - "[[Metadata-Schema]]"
  - "[[Review-Rules]]"
---

# Vault Refactor Log — 2026-08-24

## Scope

把第一版 AI 技术与职业地图从“可读的页面集合”升级为可持续维护的 Obsidian/GitHub 知识系统。

## Changes

- 增加唯一动态状态页 `00-Home/Current-State.md`，并将首次导航与每日状态分离；
- 统一元数据枚举、日期、`depth`、`review_after` 和快照字段；
- 将 Terms Inbox 收敛为真实待处理项，增加独立 Term Radar；
- 为 Learning Path 补齐 Learning Unit 和 Evidence 通过条件；
- 增加 Evidence Index、Evidence Card、复查规则和无依赖 Vault QA；
- README 改为 GitHub 可读的标准链接，并说明目录职责与时效边界；
- 保留公开仓库边界：不新增个人私密技能差距、密钥或虚构项目证据。

## Second-pass consistency fixes

- 将 Stage 0 固定练习集与真实 Terms Inbox 分离，并把 Pass Evidence 定义为唯一来源；
- 将职业路线改为 Stage 0–2 共同基础、Stage 3 共同素养后分支，明确 Stage 4/5 的专修性质；
- 按主题 × 深度重新整理 Technology Radar，避免 Core 与 Stage 3 的冲突；
- 修正 `page_kind`、Evidence Index、来源索引和模板的语义契约，区分模板与实际 Evidence；
- 强化无依赖 QA：复查到期、别名冲突、前置元数据链接、页面契约、证据正文和多格式密钥扫描。

## Job-first architecture refactor

- 建立 `02-Jobs/2026-08` 官方 Job Sample 批次，覆盖 OpenAI、Anthropic、Apple、Huawei 四家雇主与研究、ML、应用、Infra、Data、PM、Safety、Solutions 家族；
- 将原技术目录收敛到 `05-Knowledge`，职业内容迁移到 `03-Roles`，学习对象落到 `04-Skills`，证据迁移到 `06-Evidence`；
- 新增 Job Sample、Role Profile、Skill Card、Extraction Rules，并把 Start Here、Current State、Career MOC、Learning Path 改为 Job → Role → Skill → Practice → Evidence；
- 角色页增加 Sample Basis、Skill Profile、非技能门槛、来源限制和刷新周期；Skill 页采用 Role-specific Target Depth，不设置全局深度；
- 两个 Canvas 分别保留知识参考图和新的 Job Samples→Roles→Skills→Practice/Evidence 图；
- 分支 `refactor/job-first-skill-map` 只做架构重构，完成后仅推送该分支，不合并 `main`。

## Verification record

- `scripts/check_vault.py` 是本次提交前的唯一自动质检入口；
- 手工复核 README 链接、Current-State 单例、雷达变化段和现有 Canvas 是否包含动态状态；
- 本记录只描述结构变化，不把 QA 结果写死；最终结果以提交时的 QA 输出为准。
