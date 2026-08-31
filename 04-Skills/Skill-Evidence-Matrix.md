---
type: matrix
domain: skills
page_kind: skill-evidence-matrix
status: reference
created: 2026-08-24
updated: 2026-08-31
review_after: 2026-09-24
related:
  - "[[Skill-Index]]"
  - "[[Role-Skill-Matrix]]"
  - "[[Job-Sample-Index]]"
---

# Skill Evidence Matrix

> Batch B（Enterprise Applied AI / Agentic Delivery）计数直接由 22 张 Job Sample 的 `Skill Extraction` 表推导；同一岗位对同一 Skill 只计一次。`responsibility` 频率不等于候选人 `required` 频率，`preferred` 也不会升级为 required。

## Batch B — derived counts

| Skill | Role | Required | Preferred | Responsibility | Inferred | Sample N | Confidence |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [[TypeScript-JavaScript]] | Application / FDE / Platform | 9 | 0 | 0 | 1 | 10 | high/medium |
| [[Python]] | Application / Platform | 4 | 0 | 0 | 3 | 7 | high/low |
| [[LLM-API-and-Structured-Outputs]] | Application / FDE / PM | 4 | 1 | 3 | 4 | 12 | high/medium/low |
| [[Tool-Calling-and-Action-Contracts]] | Application / FDE / Platform | 0 | 2 | 6 | 1 | 9 | high/medium/low |
| [[Agent-Orchestration-and-State]] | Application / Platform / FDE | 0 | 1 | 10 | 2 | 11 | high/medium/low |
| [[Workflow-Automation-and-Business-Process-Design]] | Application / FDE / PM | 0 | 1 | 13 | 1 | 15 | high/medium/low |
| [[MCP-and-Agent-Interoperability]] | Platform / FDE / Application | 0 | 1 | 6 | 0 | 6 | high/medium |
| [[Enterprise-Integrations-and-Connectors]] | FDE / Application / PM | 11 | 0 | 5 | 8 | 21 | high/medium/low |
| [[Agent-Evals-and-Trace-Debugging]] | Application / Platform / FDE | 1 | 3 | 9 | 2 | 14 | high/medium/low |
| [[Human-in-the-Loop-and-Agent-Guardrails]] | Application / FDE / PM | 2 | 1 | 5 | 4 | 12 | high/medium/low |
| [[RAG]] | Application / FDE | 0 | 1 | 0 | 2 | 3 | medium/low |

`Alternative Group`（例如 `language-1`）表示 one-of；Python、TypeScript、Go 等选项不作为同时要求相加。由于当前 Skill 词表没有独立 Go 卡片，Go 保留在 Raw Evidence 与组说明中。

## Batch A — legacy view

Batch A（Frontier/Model/Infra）仍使用旧的 `explicit/inferred` 历史抽取格式，保留在各旧 Job Sample 中，不与 Batch B 的四类证据计数混算。Batch A 更偏模型、基础设施和研究岗位；Batch B 更偏企业 Applied AI、FDE 与 Agentic Delivery。两批都不是市场普查。

## Reading rule

矩阵只提供可复算的分母和分类入口；具体 Raw Evidence、Source Section、来源访问状态和 Evidence Trace 必须回到对应 Job Sample。页面过期/403 的行只保留低置信历史线索。

## Prerequisite layer

[[Prerequisite-Foundation-Map]] 是学习顺序的综合层，不把 DSA、RAG 或某门语言误写成所有 Agent 岗位的硬前置。完成 Practice 后再用 [[Evidence-Index]] 形成个人能力证据。
