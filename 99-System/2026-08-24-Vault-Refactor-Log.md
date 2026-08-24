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

## Verification record

- `scripts/check_vault.py` 是本次提交前的唯一自动质检入口；
- 手工复核 README 链接、Current-State 单例、雷达变化段和现有 Canvas 是否包含动态状态；
- 本记录只描述结构变化，不把 QA 结果写死；最终结果以提交时的 QA 输出为准。
