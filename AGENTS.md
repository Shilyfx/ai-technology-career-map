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

## Applied AI / Agentic Engineering rules

- 不把 RAG 视为所有 Agent 的通用前置；按任务决定是否进入 RAG 分支。
- 不把产品名或框架名直接升级为 Skill；Skill 必须可复用、可练习、可验证。
- 不把 multi-agent / A2A 当默认架构；先证明 deterministic workflow 或单 Agent 的收益。
- 优先确定性 workflow，再把不确定决策局部交给 Agent；工具副作用必须有显式权限、幂等、恢复和人工接管思路。
- MCP 是角色/环境相关能力，不是所有学习者的通用必修。
- Job Sample 决定优先级，官方规范定义边界，教程只决定练习方式；三类证据分开记录。
- Applied AI 企业样本用于补足 Application/FDE/Agent Platform，不用 frontier/model-builder 岗位替代它们。
- `responsibility` 不等于候选人 `required`；职责频率不能直接当作技能必需频率。
- `preferred`/Nice-to-have 永远不计入 required；`inferred-prerequisite` 只服务学习顺序。
- Python、TypeScript、Go 等 `Alternative Group` 是 one-of，不得把替代项相加为同时要求。
- `source_access`、`source_status` 与 confidence 必须一致：limited/blocked/403/过期不能给高置信 required。
- 每个 Skill 行必须回到具体 Raw Evidence/Source Section；不能把同一份摘要复制成每个 Skill 的假证据。
- Job Evidence 变化后必须重新计算 Skill Evidence Matrix 和 Role priority，不能沿用旧的手写频次。
- Source Fidelity 审计必须逐条打开官方 `source_url`，并写入 `source_status`、`source_access`、`retrieved`、`updated` 与 `evidence_audit_status`；不要把旧的 `limited-http-403` 留在已可读页面。
- Batch B 的 Raw Evidence 要贴近官方 wording；禁止把不相关要求合并成 synthetic sentence。每条 Evidence Trace 都要有 Source Fidelity 与语义具体的 Mapping Rationale。
- observability/debugging/metrics/tracing 不映射 Agent Evals，除非原文明确出现 quality/eval/trajectory/benchmark/judge/regression；MCP/A2A 不映射 Tool Calling，除非另有明确 tool/action/execution 信号。
- Preferred 中明确的 RAG/retrieval/grounding 保持 preferred，不得降为 inferred；现有 taxonomy 不得强迫映射，允许使用已有非 Applied Skill 或留空不计。

## 目录与链接

主模型为 `02-Jobs → 03-Roles → 04-Skills → 05-Knowledge → 06-Evidence`。七层模型只作 Knowledge taxonomy。README 使用标准 Markdown 链接；Obsidian 页面可用 wikilink。

## 元数据与时效

正式页面必须有 `type/status/created/updated`。允许的 type、Job Sample、Role、Skill 和 Evidence 合约见 `99-System/Metadata-Schema.md`。`status` 不是工作流状态；快变内容使用 `review_after`。

岗位样本 30–60 天复核，Role 60–90 天，当前工具和 Skill 60–90 天，稳定概念 180–365 天。过期样本保留证据并标 `source_status: expired`。

## Evidence

Evidence 闭环为 `problem → action → result → failure → judgment → skill → gap`，必须回链 Role/Skill；不得提交密钥、私有能力差距、内部数据或未经脱敏材料。

## 提交前质检

运行 `python scripts/check_vault.py`，修复所有 Errors；Warnings 要有明确理由。QA 检查：frontmatter、日期、重复 source_url、明确路径链接、Canvas JSON、Job/Role/Skill 合约、Current-State 单例、前置循环、Evidence 和密钥扫描。
