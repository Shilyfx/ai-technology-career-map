# Vault maintenance rules

## 入口与状态

- 首次导航读 `00-Home/Start-Here.md`；每日只读写 `00-Home/Current-State.md`。
- `Current-State` 是唯一的动态状态权威：只能有一个 `current` 和一个 `next`。其他页面只描述路线、事实或候选项，不得复制“当前/下一步”。其余事项放 `Later` 或 `Parking Lot`。
- 新名词先进入 `01-Inbox/Terms-Inbox.md`；不要因为出现一个术语就创建空白概念页。

## 元数据

- 所有正式 Markdown 页面使用统一 frontmatter，详见 `99-System/Metadata-Schema.md`。
- `status` 只表示笔记成熟度：`seed | developing | validated | reference | deprecated`。不要用 `active/current/next/learning/done/todo` 代替它。
- `stability` 表示内容变化速度：`stable | current | emerging`；快变页面必须有 `review_after`，市场/雷达页面必须有 `snapshot_date`。
- 日期至少维护 `created` 与 `updated`；来源或快照另外记录 `published`、`retrieved` 或 `snapshot_date`。

## 内容边界

- 把稳定概念、当前技术、岗位市场信号和个人证据分开写。
- 只有当名词需要独立解释、会被多个页面引用或已经有实践证据时，才新建 Concept 笔记。
- 每个概念至少回答：是什么、解决什么、依赖什么、何时不用、如何验证；不要批量制造薄概念页。
- 市场信号只能支持“岗位样本中出现了什么”，不能直接把它写成稳定技术定义或普遍门槛。

## 学习与证据

- `00-Home/Learning-Path.md` 的每个主要 Stage 使用 Learning Unit：Goal、Prerequisites、Concepts、Practice、Pass Evidence、Next。
- 完成学习阶段必须有 `09-Evidence/` 中的证据；阅读记录不等于通过。
- Evidence 卡片必须闭环：问题 → 行动 → 结果 → 失败 → 判断 → 对应技能 → 下一缺口，并链接回岗位或学习路径。
- 公共仓库不提交个人私密能力差距、凭证、内部数据或未经脱敏的项目材料。

## 时效与来源

- 岗位与市场数据优先使用招聘方职位页、官方报告和原始统计来源，写明地域、样本范围和限制。
- 变化快的技术页用 `review_after`；过期内容按 `99-System/Review-Rules.md` 标为待复核或 `deprecated`，不要静默删除证据。
- 不把单个公司的高级岗位要求写成初学者门槛；删除失效岗位链接时保留标题、抓取日期和提炼出的技能证据。

## 提交前质检

- 运行 `python scripts/check_vault.py`，修复所有 Errors；Warnings 必须有明确理由。
- 检查双向链接、重复笔记名、枚举、日期、快变页面的复查机制和证据回链。
- README 必须使用标准 Markdown 链接，不能依赖 Obsidian 双向链接才能在 GitHub 阅读。

## 写作风格

- 默认简体中文，保留必要英文术语与别名。
- 先给心智模型，再给细节；先讲依赖，再讲框架名。
- 避免“万能”“必学”“彻底取代”等无边界表述。
- 学习建议必须带可验证产出，而不只是“看课程”。
