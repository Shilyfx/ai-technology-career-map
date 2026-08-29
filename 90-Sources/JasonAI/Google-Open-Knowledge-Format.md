---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "Google Open Knowledge Format 完整指南：面向 AI Agent 的开放知识格式 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/google-open-knowledge-format/"
source_url: "https://jasonai.me/download/Google-Open-Knowledge-Format-开放知识格式完整指南.md"
published: 2026-08-12
retrieved: 2026-08-29
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-25
related:
  - "[[JasonAI-Source-Index]]"
  - "[[Agent-Memory-and-Knowledge-Operations]]"
  - "[[RAG-and-Knowledge-Systems]]"
  - "[[Prompt-and-Context-Engineering]]"
  - "[[AI-Application-Engineer]]"
---

## Open Knowledge Format v0.2

Open Knowledge Format（OKF）是 Google 提出的一套开放知识格式规范。它使用最常见的 **Markdown + YAML Frontmatter** 保存知识，让同一套知识既能被人阅读，也能被 Codex、Claude Code 等 AI Agent，以及 Obsidian、Git、MCP、RAG 等不同系统消费。OKF 与 Karpathy 提出的 LLM Wiki 思想非常接近，但两者解决的问题不同：

> **LLM Wiki 更关注“Agent 如何持续维护知识”，OKF 更关注“这些知识应该按照什么格式保存和交换”。**

当每个人、每个团队都使用自己的 Markdown 结构时，Agent 需要先理解不同项目的目录、字段、链接和来源约定。OKF 的作用，就是给这些知识建立一套尽可能轻量、开放且统一的格式。

简单来说，它就是一套 Markdown + YAML 的格式规范。

---

## 基础结构：Knowledge Bundle、Concept 与渐进式披露

OKF 把一组相关知识文件称为 **Knowledge Bundle**，可以理解为“知识包”。一个 Knowledge Bundle 本质上就是一个目录树：

```markdown
knowledge/
├── index.md                          ← 整个知识包的导航目录
├── log.md                            ← 重要更新记录
│
├── concepts/
│   ├── index.md
│   ├── agent-memory.md
│   └── context-engineering.md
│
├── tools/
│   ├── index.md
│   ├── codex.md
│   └── claude-code.md
│
└── references/
    └── index.md
```

知识包中最基本的单位叫 **Concept**。虽然 Concept 直译是“概念”，实际可以理解为一个**知识条目**。

一个 Concept 就是一个 Markdown 文件，它可以描述任何知识：技术概念、研究笔记、软件服务、API、数据库表、业务流程、指标或公司 Policy。例如：

```markdown
knowledge/
└── concepts/
    └── agent-memory.md
```

这个文件的 Concept ID 就是：`concepts/agent-memory`。也就是说，**文件在 Knowledge Bundle 中的路径，本身就是它的 Concept ID。**

### YAML Frontmatter

每个普通 Concept 都必须是 Markdown 文件，并在顶部包含 YAML Frontmatter。
OKF v0.2 唯一始终强制要求的字段只有：

```yaml
---
type: Research Topic
---
```

`type` 表示这个文件描述的是什么类型的知识。
例如可以使用 `Research Topic`、`AI Tool`、`API Endpoint`、`Metric`、`Policy` 等。OKF 不规定固定的 type 列表，但同一个知识库应该尽量保持自己的类型命名一致。
实际使用时通常还会加入：

```yaml
---
type: Research Topic
title: Agent Memory
description: AI Agent 长期保存和重新利用知识的机制。
tags: [ai-agent, memory]
---
```

其中 `title` 是标题，`description` 是一句话摘要，`tags` 用于横向分类。`description` 对 Agent 尤其重要，因为 Agent 可以先读取元数据，判断文件是否与当前任务有关，再决定是否加载完整正文。

这就是 **Progressive Disclosure（渐进式披露）**：`index.md → title / description → 相关 Concept → 完整正文 → 继续沿链接读取`
目标不是把整个知识库一次性塞进 Context Window，而是按需逐层加载。

### index.md：知识导航

`index.md` 是 OKF 的保留文件，主要负责告诉人和 Agent：**这个目录里有什么知识？**
Bundle 根目录的 `index.md` 可以声明 OKF 版本：

```markdown
---
okf_version: "0.2"
---

# AI Agent

* [Agent Memory](concepts/agent-memory.md) - Agent 长期保存和重新利用知识的机制。
* [Context Engineering](concepts/context-engineering.md) - 控制 Agent 当前应该加载哪些上下文。

# Tools

* [Codex](tools/codex.md) - OpenAI 的 AI Agent。
* [Claude Code](tools/claude-code.md) - Anthropic 的命令行 AI Agent。
```

子目录也可以继续设置自己的 `index.md`，形成分层导航。Concept 之间推荐使用普通 Markdown Link：

```markdown
Agent Memory 与 [Context Engineering](/concepts/context-engineering.md) 密切相关。
```

这样 Markdown 文件成为节点，Markdown Link 则自然形成知识之间的连接。

### log.md：更新记录
`log.md` 记录 Knowledge Bundle 或某个目录的重要变化：

```markdown
# Knowledge Update Log

## 2026-08-10

* **Creation**: 新增 [Agent Memory](concepts/agent-memory.md)。
* **Update**: 更新 [Context Engineering](concepts/context-engineering.md) 的来源资料。

## 2026-08-09

* **Initialization**: 创建初始知识包。
```

日期使用 `YYYY-MM-DD`，最新记录放在最上面。

---

## OKF v0.2 的五个核心机制

基础的 Markdown、YAML、`index.md` 和链接解决的是“如何建立统一知识格式”。但当大量知识开始由 Agent 自动生成和维护以后，还需要回答五个更重要的问题：

| 机制 | 中文理解 | 核心字段 | 解决的问题 |
|---|---|---|---|
| Provenance | 来源追踪 | `sources` + Citation | 这条知识从哪里来？ |
| Trust | 可信度 | `generated`、`verified` | 谁生成的？谁验证过？ |
| Freshness | 时效性 | `stale_after` | 现在是否可能已经过时？ |
| Lifecycle | 生命周期 | `status` | 是草稿、正式版本还是已废弃？ |
| Attestation | 计算过程验证 | `runtime`、`parameters`、`executor`、`attester` | 结果是否按照规定方法计算？ |

### Provenance：来源追踪

Provenance 解决的是：**这条知识依据了什么资料？**
核心字段是 `sources`：

```yaml
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format v0.2 Specification
```

`resource` 指向原始资料，`id` 则给这个 Source 一个稳定标识。
如果还需要说明**正文中的某一句话具体来自哪个 Source**，可以使用 Citation，也就是 Markdown 脚注：

```markdown
OKF 中，文件路径就是知识条目的 Concept ID。[^okf-spec]

[^okf-spec]: Open Knowledge Format v0.2 Specification
```

这里的 `[^okf-spec]` 对应 YAML 中的：`sources[].id: okf-spec`。
因此可以形成：**结论 → Citation → Source → 原始资料**。
Source 还可以记录 `author`、`usage_count`、`last_modified` 等信息，为 Consumer 判断来源可靠性提供客观信号。

### Trust：生成与验证

知道来源之后，还需要知道：**这条知识是谁生成的？有没有真正被验证？**
核心字段是：

```yaml
generated:
  by: research-agent/1.0
  at: "2026-08-10T10:00:00+08:00"

verified:
  - by: human:jason
    at: "2026-08-10T11:00:00+08:00"
```

`generated` 表示当前内容由谁生成，以及最后一次发生有意义修改的时间。
`verified` 表示谁真正对照 Source 或真实资源检查过内容。

常见 Actor 表示方式：
- `research-agent/1.0`：Agent 或工具
- `human:jason`：人工审核
- `process:schema-check`：自动化程序

Consumer 可以根据 `verified` 推导：没有验证 → `unverified`，只有机器验证 → `machine-confirmed`，存在 `human:*` → `human-reviewed`。
因此 OKF 不需要直接写 `trust: high` 之类的主观评分。

### Freshness：时效性

Freshness 解决的是：**这条知识以前是正确的，现在还值得继续使用吗？**

核心字段：

```yaml
stale_after: "2026-12-31"
```

它表示：从这个日期开始，这条知识应该重新检查。
几个容易混淆的时间字段：

| 字段 | 含义 |
|---|---|
| `sources[].last_modified` | 原始 Source 最后修改时间 |
| `generated.at` | 当前 Concept 最后发生有意义修改的时间 |
| `stale_after` | 从什么时候开始应该重新检查 |

### Lifecycle：生命周期

Lifecycle 回答：**这条知识现在处于什么状态？**
核心字段：

```yaml
status: stable
```

标准状态有三个：
- `draft`：草稿，尚未准备好正式使用
- `stable`：当前正式版本
- `deprecated`：已经废弃，但为了历史记录和旧链接继续保留

Freshness 与 Lifecycle 是两个不同维度。例如：

```yaml
status: stable
stale_after: "2026-12-31"
```

意思是：**它现在仍然是正式版本，但到年底以后需要重新检查。**

### Attestation：计算过程验证

Attestation 主要用于数据库、BI、财务指标等重要计算场景。它解决的是：**Agent 给出的数字，是否真的按照经过批准的方法计算出来？**
例如公司规定 Revenue 必须使用固定 SQL，就可以建立一种特殊 Concept：

````markdown
---
type: Attested Computation
title: Revenue for Fiscal Year

runtime: bigquery

parameters:
  - name: year
    type: integer
    required: true

executor:
  resource: /references/run-bigquery.md
  receipt: [job_id, executed_sql, result]

attester:
  resource: /references/revenue-check.py
---

# Computation

```sql
SELECT SUM(net_amount)
FROM finance.orders
WHERE fiscal_year = @year
```
````

`runtime` 表示执行环境；
`parameters` 表示 Agent 可以提供的参数；
`executor` 定义如何执行，并返回实际执行记录，也就是 Receipt（执行凭证）；
`attester` 是确定性检查程序，用来检查 Receipt，并判断实际执行是否符合批准的计算约束。

Agent 可以提供：`year = 2026`。但不应该擅自修改 SQL。
这种机制主要用于财务数据、利润率、业务指标等高要求场景，普通个人知识笔记通常不需要。

---

## 完整 OKF v0.2 Concept 模板

下面是一份为了展示字段关系而设计的**完整模板**。

它使用 `Attested Computation` 作为类型，因此能够同时展示普通 Concept 字段和计算验证字段。实际使用时不需要机械填写所有字段，没有明确用途的字段应该直接省略。

````markdown
---
# 唯一始终强制要求的字段
type: Attested Computation

# 推荐字段
title: Example Concept
description: 用一句话说明这条知识是什么，以及为什么值得读取。
resource: https://example.com/canonical-resource
tags: [example, research]

# ===== 生命周期与时效性 =====
# draft | stable | deprecated
status: stable
# 从这个日期开始应重新检查
stale_after: "2026-12-31"

# ===== 内容生成信息 =====
generated:
  by: research-agent/1.0
  at: "2026-08-10T10:00:00+08:00"

# ===== 验证信息 =====
verified:
  - by: process:auto-check
    at: "2026-08-10T10:30:00+08:00"

  - by: human:jason
    at: "2026-08-10T11:00:00+08:00"

# ===== 来源追踪 =====
sources:
  - id: official-docs
    resource: https://example.com/docs
    title: Official Documentation
    author: process:official-docs
    usage_count: 1200
    last_modified: "2026-08-01"

  - id: internal-policy
    resource: /references/internal-policy.md
    title: Internal Policy
    last_modified: "2026-07-20"

# usage_count 所对应的统计时间窗口
usage_window:
  from: "2026-07-01"
  to: "2026-07-31"

# ===== Attested Computation =====

# 执行环境
runtime: bigquery

# Agent 可以提供的参数
parameters:
  - name: year
    type: integer
    required: true

# 如果计算代码保存在独立文件中，可以使用 computation 指向它
# computation: /references/computations/revenue.sql

# 如何执行
executor:
  resource: /references/executors/run-bigquery.md
  receipt:
    - job_id
    - executed_sql
    - result

# 如何验证执行结果
attester:
  resource: /references/attesters/revenue-check.py
---

# Definition

这里保存真正的知识正文。

某一个需要来源支持的结论。[^official-docs]

# Relationships

参见 [Another Concept](/concepts/another-concept.md)。

# Computation

```sql
SELECT SUM(net_amount)
FROM finance.orders
WHERE fiscal_year = @year
```

[^official-docs]: Official Documentation
````

对于普通个人知识笔记，通常没有必要使用 Attested Computation。

一个更实际的普通 Concept 基线通常只需要：

```yaml
---
type: Research Topic
title: Agent Memory
description: AI Agent 长期保存和重新利用知识的机制。
tags: [ai-agent, memory]

generated:
  by: research-agent/1.0
  at: "2026-08-10T10:00:00+08:00"

sources:
  - id: official-docs
    resource: https://example.com/docs
    title: Official Documentation
---
```

真正重要的知识，再根据需求加入 `verified`、`status` 和 `stale_after`。

---

## 实际使用场景

### Obsidian 个人知识库

不需要把整个 Obsidian Vault 全部强制改造成 OKF。

Daily Note、Inbox、Canvas、模板和临时草稿可以继续使用原来的结构，只把真正需要被 Agent 长期复用的知识整理成独立 Knowledge Bundle。

```markdown
My-Obsidian-Vault/
├── README.md                         ← Vault 自身说明
├── AGENTS.md                         ← Codex / Claude Code 的操作规则
│
├── inbox/                            ← 尚未整理的信息
├── daily/                            ← Daily Notes
│
├── sources/                          ← 原始文章、论文、GitHub、视频转录
│   ├── articles/
│   ├── papers/
│   └── github/
│
└── knowledge/                        ← OKF Knowledge Bundle
    ├── index.md
    ├── log.md
    │
    ├── concepts/
    │   ├── index.md
    │   ├── ai-agent/
    │   └── knowledge-management/
    │
    ├── tools/
    │   ├── index.md
    │   ├── codex.md
    │   └── claude-code.md
    │
    └── references/
```

推荐流程：

**原始资料 → Agent 研究 → 更新或创建 Concept → 添加 Source / Citation → 更新 index.md → 更新 log.md → Git 保存历史**

其中原始资料继续作为 Source of Truth，OKF 保存的是经过整理、关联和综合后的长期知识。

### 软件项目与 Agent 文档

代码仓库可以建立独立 `.okf/`：

```markdown
my-project/
├── AGENTS.md                         ← Agent 行为规范
├── README.md
├── src/
├── tests/
│
└── .okf/                             ← Agent 长期项目知识
    ├── index.md
    ├── log.md
    ├── architecture/
    ├── services/
    ├── decisions/
    ├── APIs/
    └── runbooks/
```

OKF 不应该重新复制一遍源代码。
更适合保存的是：架构为什么这样设计、历史决策、重要业务约束、模块关系、API 的业务含义、不能破坏的规则以及故障处理流程。
代码仍然是实现层面的 Source of Truth，OKF 是 Agent 可以长期读取的语义和背景知识。

### API 与业务约定

OKF 也不应该取代 OpenAPI。OpenAPI 继续负责参数、Schema、Response、Status Code 等正式接口定义；OKF 保存的是 OpenAPI 很难表达的业务语义和上下文。

```markdown
project/
├── openapi/
│   └── api.yaml                      ← API 正式 Schema / Source of Truth
│
└── .okf/
    ├── index.md
    ├── APIs/
    │   ├── authentication.md         ← 认证架构和业务约定
    │   └── create-order.md           ← Endpoint 的业务语义和限制
    │
    └── policies/
        └── order-creation.md         ← 正式业务规则
```

例如 API Concept 可以直接指向真实 OpenAPI：

```yaml
---
type: API Endpoint
title: Create Order
description: 创建新的 Customer Order，并返回唯一订单 ID。
resource: ../../openapi/api.yaml#/paths/~1orders/post

sources:
  - id: openapi
    resource: ../../openapi/api.yaml
    title: Production OpenAPI Specification

  - id: order-policy
    resource: /policies/order-creation.md
    title: Order Creation Policy
---
```

正文只保存调用顺序、业务限制、幂等规则、与其他 Endpoint 的关系等真正需要 Agent 理解的上下文。
数据库 Schema、业务指标和企业 Policy 也可以采用相同思路；其中需要严格保证计算方式的指标，再进一步使用 Attested Computation。

---

## 使用建议与注意事项

实际采用 OKF v0.2 时，不要为了“符合规范”而机械填写所有字段。

可以按照需求逐步增加：

- **最小实现：** `type`
- **实际可读知识：** `type + title + description`
- **可追溯知识：** `generated + sources + Citation`
- **长期可信知识：** `verified + status + stale_after`
- **重要业务计算：** `Attested Computation + executor + receipt + attester`

另外需要注意几个原则：
1. **OKF 是格式，不是知识管理软件。** 它不能替代 Obsidian、Git、RAG、MCP 或数据库，而是可以和这些系统组合使用。
2. **不要重复真正的 Source of Truth。** 源代码、数据库 Schema、OpenAPI、官方文档仍然应该保持为原始事实来源。OKF 更适合保存这些资产背后的语义、关系和长期知识。
3. **警惕知识 Drift。** 原始系统已经变化，但 OKF 文档没有同步更新，就会产生“文档和真实系统不一致”的问题。重要知识应该结合 `stale_after`、自动检查、Git Diff 和人工 Review。
4. **不要一开始过度工程化。** 对个人知识库而言，`type`、`title`、`description`、`sources` 已经能够获得很大价值；只有真正重要的内容才需要逐步增加验证和生命周期机制。

OKF v0.2 真正重要的并不是 YAML 本身，而是它建立了一套面向 Agent 的知识约定：

> **知识应该能够被定位、被导航、被追溯来源、被判断可信度、被判断是否过期，并且能够脱离某一个 Agent 或平台长期存在。**

这也是 OKF 可以与 Obsidian、Git、Codex、Claude Code、MCP、RAG、数据库和其他 Agent 系统组合使用的核心原因。

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
