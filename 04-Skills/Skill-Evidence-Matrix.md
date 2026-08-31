---
type: matrix
domain: skills
page_kind: skill-evidence-matrix
status: reference
created: 2026-08-24
updated: 2026-09-01
review_after: 2026-10-01
related:
  - "[[Skill-Index]]"
  - "[[Role-Skill-Matrix]]"
  - "[[Job-Sample-Index]]"
---

# Skill Evidence Matrix

> Batch B（Enterprise Applied AI / Agentic Delivery）计数由 22 张 Job Sample 的 `Skill Extraction` 表推导；每个单元格是证据行计数，`Sample N` 是去重后的职位数。`Required One-of` 单独列出，避免把 Python/TypeScript/Go 等替代项相加。

## Batch B — source-quality derived counts

| Skill | Required Direct | Required One-of | Preferred | Responsibility | Inferred | High/Medium Source N | Low/Historical N | Sample N |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [[Agent-Evals-and-Trace-Debugging]] | 0 | 0 | 3 | 4 | 1 | 6 | 1 | 7 |
| [[Agent-Orchestration-and-State]] | 1 | 0 | 4 | 11 | 0 | 12 | 0 | 12 |
| [[Databases-and-Data-Modeling]] | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 2 |
| [[Distributed-Systems]] | 2 | 2 | 0 | 1 | 1 | 4 | 1 | 5 |
| [[Docker-Containers]] | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| [[Enterprise-Integrations-and-Connectors]] | 2 | 0 | 2 | 4 | 1 | 7 | 1 | 8 |
| [[HTTP-API]] | 2 | 1 | 2 | 3 | 0 | 7 | 0 | 7 |
| [[Human-in-the-Loop-and-Agent-Guardrails]] | 0 | 0 | 1 | 4 | 1 | 4 | 1 | 5 |
| [[LLM-API-and-Structured-Outputs]] | 1 | 0 | 0 | 3 | 0 | 4 | 0 | 4 |
| [[Linux]] | 1 | 0 | 1 | 0 | 0 | 2 | 0 | 2 |
| [[MCP-and-Agent-Interoperability]] | 0 | 0 | 3 | 5 | 0 | 6 | 0 | 6 |
| [[Model-Serving]] | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| [[Observability]] | 1 | 2 | 0 | 10 | 0 | 10 | 0 | 10 |
| [[Prompt-and-Context-Engineering]] | 0 | 0 | 2 | 1 | 0 | 3 | 0 | 3 |
| [[Python]] | 0 | 8 | 0 | 1 | 2 | 9 | 1 | 10 |
| [[RAG]] | 0 | 0 | 2 | 1 | 0 | 3 | 0 | 3 |
| [[Security-Privacy-and-Access-Control]] | 0 | 0 | 2 | 5 | 0 | 6 | 0 | 6 |
| [[Software-Design-and-Architecture]] | 2 | 0 | 0 | 1 | 0 | 3 | 0 | 3 |
| [[Testing]] | 1 | 0 | 0 | 1 | 0 | 2 | 0 | 2 |
| [[Tool-Calling-and-Action-Contracts]] | 0 | 0 | 1 | 1 | 0 | 2 | 0 | 2 |
| [[TypeScript-JavaScript]] | 1 | 5 | 0 | 0 | 0 | 6 | 0 | 6 |
| [[Workflow-Automation-and-Business-Process-Design]] | 1 | 1 | 2 | 9 | 1 | 11 | 1 | 12 |

`Alternative Group`（例如 `language-1`、`areas-3-of-6`）保留原始选择关系。`High/Medium Source N` 与 `Low/Historical N` 按职位去重，不能解释成市场频率；历史/不可用页面仅保留低置信学习线索。

## Batch A — legacy view

Batch A（Frontier/Model/Infra）仍使用旧的 `explicit/inferred` 历史抽取格式，保留在各旧 Job Sample 中，不与 Batch B 的四类证据计数混算。两批都不是市场普查。

## Reading rule

矩阵只提供可复算的分母和分类入口；具体 Raw Evidence、Source Section、Source Fidelity、来源访问状态和 Evidence Trace 必须回到对应 Job Sample。`responsibility`、`preferred` 不会升级为 `required`。

## Prerequisite layer

[[Prerequisite-Foundation-Map]] 是学习顺序综合层，不把 DSA、RAG 或某门语言误写成所有 Agent 岗位的硬前置。完成 Practice 后再用 [[Evidence-Index]] 形成个人能力证据。
