# Vault maintenance rules

## Job-first invariant

1. 默认导航必须遵循 `Job Sample → Role → Skill → Practice → Evidence`；
2. Technology MOC、Radar 和 Knowledge taxonomy 是参考，不得替代 Job/Role/Skill 优先级；
3. Job Sample 只保留官方来源的短摘录和明确/推断分离，不复制完整 JD；
4. Role Profile 的优先级必须有 Sample Basis、Sample N、Confidence 和限制；
5. Skill 是可复用、可练习、可验证的学习对象；框架名不自动升级为 Skill；
6. 同一 Job 内同一 Skill 只计一次，替代项不重复计数，统一名称后再汇总；
7. Skill 不设全局 depth，深度写在 Role Skill Profile；
8. Evidence 只能证明个人实践，Job Sample 只能证明岗位需求；
9. `00-Home/Current-State.md` 是唯一动态状态页，目标是 Target Role / Current Skill / Next Skill；
10. 新岗位先入 `01-Inbox/Job-Inbox.md`，新名词先入 `01-Inbox/Terms-Inbox.md`。

## 目录与链接

主模型为 `02-Jobs → 03-Roles → 04-Skills → 05-Knowledge → 06-Evidence`。七层模型只作 Knowledge taxonomy。README 使用标准 Markdown 链接；Obsidian 页面可用 wikilink。

## 元数据与时效

正式页面必须有 `type/status/created/updated`。允许的 type、Job Sample、Role、Skill 和 Evidence 合约见 `99-System/Metadata-Schema.md`。`status` 不是工作流状态；快变内容使用 `review_after`。

岗位样本 30–60 天复核，Role 60–90 天，当前工具和 Skill 60–90 天，稳定概念 180–365 天。过期样本保留证据并标 `source_status: expired`。

## Evidence

Evidence 闭环为 `problem → action → result → failure → judgment → skill → gap`，必须回链 Role/Skill；不得提交密钥、私有能力差距、内部数据或未经脱敏材料。

## 提交前质检

运行 `python scripts/check_vault.py`，修复所有 Errors；Warnings 要有明确理由。QA 检查：frontmatter、日期、重复 source_url、明确路径链接、Canvas JSON、Job/Role/Skill 合约、Current-State 单例、前置循环、Evidence 和密钥扫描。
